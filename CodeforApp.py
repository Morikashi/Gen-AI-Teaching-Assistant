from crewai import Agent, Task, Crew, Process 
import os
import gradio as gr
from b2sdk.v1 import InMemoryAccountInfo, B2Api
import requests
import google.generativeai as genai
from pytube import YouTube
import tempfile

GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=GOOGLE_API_KEY)

os.environ["OPENAI_API_BASE"] = 'https://api.groq.com/openai/v1'
os.environ["OPENAI_MODEL_NAME"] = 'llama3-70b-8192'
os.environ["OPENAI_API_KEY"] = os.getenv('Token')

API_key_baseten = os.getenv('Baseten')
model_id_whisper = os.getenv('Baseten_Model')
application_key_id_blackblaze = os.getenv('application_key_id_blackblaze')
application_key_blackblaze = os.getenv('application_key_blackblaze')
bucket_name = os.getenv('bucket_name')

def main():
    with gr.Blocks() as demo:
        with gr.Row():
            with gr.Column(scale=3):
                audio_input = gr.Audio(sources=["upload"], type="filepath", interactive=True, label="Please upload your audio lesson",format="mp3")
                print(audio_input)
                youtube_input = gr.Textbox(placeholder="Enter YouTube URL here...", lines=1, label="Enter YouTube link")
        
        with gr.Row():
            with gr.Column(scale=1):
                notes_output = gr.Textbox(lines=4, placeholder="Notes Output")
                quiz_output = gr.Textbox(lines=4, placeholder="Quiz Output")
        
        with gr.Row():
            with gr.Column(scale=1):
                #audio_player = gr.Audio(interactive=False)
                video_output = gr.HTML()
        
        with gr.Row():
            text_button = gr.Button("Send")
        
        text_button.click(process_input, [audio_input, youtube_input], [notes_output, quiz_output, audio_input, video_output])
        youtube_input.change(embed_youtube_video, [youtube_input], video_output)
    
    demo.launch()

def process_input(audio_file, youtube_link):
    if audio_file is not None:
        with open(audio_file, 'rb') as file_data:
            notes, quiz = upload_to_b2(file_data)
        return notes, quiz, audio_file, None
    elif youtube_link:
        notes, quiz = process_youtube_link(youtube_link)
        return notes, quiz, None, youtube_link
    else:
        return "Please provide either an audio file or a YouTube link.", "", None, None


def process_youtube_link(youtube_link):
    with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as temp_file:
        try:
            video = YouTube(youtube_link)
            audio_stream = video.streams.filter(only_audio=True).first()
            audio_stream.download(filename=temp_file.name)
            
            with open(temp_file.name, 'rb') as file_data:
                notes, quiz = upload_to_b2(file_data)
            
            return notes, quiz
        finally:
            os.unlink(temp_file.name)

info = InMemoryAccountInfo()
b2_api = B2Api(info)
b2_api.authorize_account("production", application_key_id_blackblaze, application_key_blackblaze)
bucket = b2_api.get_bucket_by_name(bucket_name)

def upload_to_b2(file):
    
    file_name = os.path.basename(file.name)
    file_info = {'description': 'Uploaded audio file'}
    
    with open(file.name, 'rb') as file_data:
        file_id = bucket.upload_bytes(file_data.read(), file_name, file_infos=file_info)

    audio_file_url = f'https://f005.backblazeb2.com/file/{bucket_name}/{file_name}'
    data = {"url": audio_file_url}
    res = requests.post(f"https://model-{model_id_whisper}.api.baseten.co/production/predict", headers={"Authorization": f"Api-Key {API_key_baseten}"}, json=data)    
    
    full_transcription = ""
    response = res.json()
    for segment in response['segments']:
        full_transcription += segment['text'] + " "
    
    model = genai.GenerativeModel("models/gemini-1.5-pro-latest")
    notes = model.generate_content([
        "from the transcript extracted from audio files generate notes. The generated notes should cover all the timestamps so that any student/person reading the notes should clearly understand the lecture/podcast. Cover all the points not just the main points. Don't be concise. Be very detailed with your response. Also, don't include timestamps in your response. The generated length of the notes should be as long as the transcripts length. Make sure to include headings and titles.",
        full_transcription
    ])
    
    quiz = agent(full_transcription)

    return notes.text, quiz

def agent(transcript):
    classifier = Agent(role="quiz generator",
                       goal="from the transcript extracted from audio files generate quiz questions with answers. The generated quiz questions should be in multiple choice format so that any student/person taking the quiz should clearly understand the lecture/podcast. Cover all the points not just the main points. Don't be concise. Be very detailed with your response.",
                       backstory="You are an AI assistant build to generate quiz questions from the transcript.",
                       verbose=True, allow_delegation=False)
    
    classify_email = Task(
        description=f"generate quiz from the '{transcript}'",
        agent=classifier,
        expected_output="detailed quiz questions based on the transcript",)
    
    crew = Crew(agents=[classifier], tasks=[classify_email], verbose=2, process=Process.sequential)
    output = crew.kickoff()
    
    return output

def embed_youtube_video(url):
    if url:
        # Extract the video ID from the URL
        video_id = url.split("v=")[1].split("&")[0] if "v=" in url else url.split("/")[-1]
        video_html = f'''
        <iframe width="560" height="315" src="https://www.youtube.com/embed/{video_id}" 
        frameborder="0" allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
        allowfullscreen></iframe>
        '''
        return video_html
    return "Please enter a YouTube URL."


if __name__ == "__main__":
    main()
