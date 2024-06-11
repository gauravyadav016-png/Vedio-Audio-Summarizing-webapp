import os
import streamlit as st
import moviepy.editor as mp
from dotenv import load_dotenv
import google.generativeai as genai
import speech_recognition as sr

class VideoAudioSummarizer:
    def __init__(self, google_api_key):
        """Initialize the summarizer with the necessary API key for Google's generative AI."""
        os.environ["GOOGLE_API_KEY"] = google_api_key
        genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
        self.model = genai.GenerativeModel('gemini-1.5-flash')

    def extract_audio(self, video_path):
        """Extract audio from video and save as .wav file."""
        video = mp.VideoFileClip(video_path)
        audio_path = video_path.replace('.mp4', '.wav')
        video.audio.write_audiofile(audio_path)
        return audio_path

    def transcribe_audio(self, audio_path):
        """Transcribe audio using Sphinx recognizer."""
        recognizer = sr.Recognizer()
        with sr.AudioFile(audio_path) as source:
            audio = recognizer.record(source)
        
        try:
            transcript = recognizer.recognize_sphinx(audio)
        except sr.UnknownValueError:
            transcript = "Sphinx could not understand audio"
        except sr.RequestError as e:
            transcript = f"Sphinx request failed; {e}"
        
        print(transcript)
        return transcript

    def generate_summary(self, transcript):
        """Generate a summary of the provided transcript using the configured AI model."""
        prompt_text = f"Please provide a concise and relevant summary of the following text, focusing on key points and omitting any unnecessary details: {transcript}"
        response = self.model.generate_content(prompt_text)
        return response.text

    def get_video_summary(self, video_path):
        """Extract audio, transcribe, and generate a summary for the given video."""
        audio_path = self.extract_audio(video_path)
        transcript = self.transcribe_audio(audio_path)
        summary_text = self.generate_summary(transcript)
        return summary_text

    def save_uploaded_file(self, uploaded_file):
        """Save the uploaded file to a temporary directory."""
        base_path = "tempDir"
        if not os.path.exists(base_path):
            os.mkdir(base_path)
        file_path = os.path.join(base_path, uploaded_file.name)
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        return file_path

def main():
    st.title("Video and Audio Summarizer")
    summarizer = VideoAudioSummarizer("Your Gemini API key")
    video_file = st.file_uploader("Upload your video file", type=["mp4", "mkv", "avi", "mov"])
    
    if video_file and st.button("Generate Summary"):
        video_path = summarizer.save_uploaded_file(video_file)
        summary_text = summarizer.get_video_summary(video_path)
        st.write("Summary:", summary_text)

if __name__ == "__main__":
    main()

# Unit Test Case
import unittest

class TestVideoAudioSummarizer(unittest.TestCase):
    def test_transcribe_audio(self):
        """Test the transcription of audio."""
        summarizer = VideoAudioSummarizer("dummy_api_key")
        # Assuming 'example.wav' is a valid audio file in the correct format
        transcript = summarizer.transcribe_audio('example.wav')
        self.assertIsNotNone(transcript, "Transcription should not be None")

