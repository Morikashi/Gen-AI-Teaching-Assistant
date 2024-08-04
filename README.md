# 🌟 GenAI-Powered Teaching Assistant 🌟

Transform your learning experience with an innovative app designed to **automatically summarize lecture recordings** and create engaging quizzes to test your knowledge!

## Key Features:

- **🎤 Audio Lecture Input**  
  Upload your audio lectures effortlessly.

- **📝 Comprehensive Notes Generation**  
  Utilizing the **OpenAI Whisper model** for accurate transcription, your lectures are transformed into detailed notes.

- **🤖 Advanced Note Generation**  
  The **Gemini AI 1.5** processes the transcribed text to produce insightful summaries and notes.

- **📚 Quiz Creation**  
  An intelligent AI agent powered by the **Meta LLaMA3 model** through **Groq** generates quizzes and assessments tailored to your learning needs.

## How It Works:

1. **Upload Lecture**  
   Simply upload your audio lecture to the app.

2. **Transcription**  
   The **OpenAI Whisper model** transcribes the audio into text with high accuracy.

3. **Note Generation**  
   The **Gemini AI 1.5** synthesizes the transcription into comprehensive notes.

4. **Quiz Development**  
   The AI agent creates quizzes based on the generated notes, helping reinforce your understanding.

## Benefits:

- **📈 Enhance Learning**  
  Improve retention and understanding of lecture material.

- **⏰ Save Time**  
  No more manual note-taking; focus on learning instead.

- **📊 Personalized Assessments**  
  Tailored quizzes ensure you master the content effectively.

## Get Started Today!

## Prerequisites

You must have:

- **🐍 [Python](https://www.python.org/)** installed 
- **📦 [pip](https://pip.pypa.io/en/stable/installation/)** installed 
- **🔑 [Google API Key](https://ai.google.dev/)** 
- **🔑 [OpenAI API Key](https://console.groq.com/)**
- **🔑 [Baseten API Key (Optional)](https://www.baseten.co/)**
- **🔑 [Backblaze B2 API Key (Optional)](https://www.backblaze.com/)**

## Setup and Installation Instructions:

### Install Dependencies


pip install -r requirements.txt

## Set Your API Keys (Optional)
In the .env file, add all your API keys, which you can copy by visiting the official pages. Here is the format:
```
GOOGLE_API_KEY = ''
OPENAI_API_KEY = ''
bucket_name = ''
API_key_baseten = ''
model_id_whisper = ""
application_key_id_blackblaze = ''
application_key_blackblaze = ''
```
### Run the Application
* Start the app
```gradio run app.py```

### Use the Application
1. Select the lecture file or YouTube link.
2. You can use either an audio or video file, and the file can be locally stored, remotely stored (and publicly accessible), or on YouTube.

![How This App Works](https://private-user-images.githubusercontent.com/44226488/326292146-3b212637-690b-482c-9ef6-f227ebc979fa.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MjI3NTk4NjUsIm5iZiI6MTcyMjc1OTU2NSwicGF0aCI6Ii80NDIyNjQ4OC8zMjYyOTIxNDYtM2IyMTI2MzctNjkwYi00ODJjLTllZjYtZjIyN2ViYzk3OWZhLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDA4MDQlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQwODA0VDA4MTkyNVomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWVmOTZmODJkNjU3NDIyMjU0ODM0YTRhMDA5M2JhMTE1ZGFlMDViNDk0YzkwNDhjZTMyMmExMWE0NWRlZDY0ZjkmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.VghpEIKsPpx8e266eIUaWo2SFL3qdL27i9MiBcu24eg)

Unlock the power of AI in your education and elevate your learning journey with our AI-Powered Teaching Assistant! 🚀
