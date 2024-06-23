# Video and Audio Summarizer

This project provides a web application for summarizing video and audio content using Google's Generative AI and the Sphinx speech recognition engine. The application allows users to upload video files, extracts the audio, transcribes the audio to text, and generates a concise summary of the content.

## Features

- Extracts audio from video files.
- Transcribes audio to text using Sphinx.
- Generates summaries using Google's Generative AI.
- Supports various video file formats such as MP4, MKV, AVI, and MOV.
- Simple web interface built with Streamlit.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/gauravyadav016-png/Vedio-Audio-Summarizing-webapp.git
   cd Video-Audio-Summarizer-webapp


2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your Google API key:
   - Create a `.env` file in the project root directory and add your Google API key:
     ```
     GOOGLE_API_KEY=your_google_api_key_here
     ```

## Usage

1. Run the Streamlit application:
   ```bash
   streamlit run sum.py
   ```

2. Open your web browser and navigate to `http://localhost:8501`.

3. Upload your video file using the provided interface.

4. Click the "Generate Summary" button to get a summary of the video's content.

## Code Overview

- `sum.py`: The main application file that sets up the Streamlit interface and handles file uploads and summarization.
- `VideoAudioSummarizer`: A class that provides methods to extract audio, transcribe it, and generate a summary.

## Dependencies

- `streamlit`: For building the web application interface.
- `moviepy`: For extracting audio from video files.
- `dotenv`: For loading environment variables from a `.env` file.
- `google-generativeai`: For interacting with Google's Generative AI.
- `speech_recognition`: For transcribing audio to text.
- `unittest`: For running unit tests.

## Unit Tests

To run the unit tests, use the following command:
```bash
python -m unittest test_video_audio_summarizer.py
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.
