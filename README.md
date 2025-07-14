# 🎙️ Voice Assistant with Gemini AI

A simple voice assistant built with Python that:
- Records your voice
- Transcribes it to text using **Google Speech Recognition**
- Sends the query to **Gemini LLM (Google Generative AI)**
- Speaks the response using **gTTS**

Perfect for experimenting with voice interfaces, LLMs, and real-time audio processing!

---

## 🧠 Features

- 🎤 Voice input from your microphone
- 📝 Speech-to-text using `speech_recognition`
- 🤖 LLM-based answers via Gemini (`gemini-1.5-flash`)
- 🔊 Text-to-speech using `gTTS` and audio playback with `playsound`
- 🔐 Secure API key management with `.env` file

---

## 📦 Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/gemini-voice-assistant.git
   cd gemini-voice-assistant

2. **Create and Activate Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt

3. **Set environment variables**
   Create a .env file in the root directory:
   GEMINI_API_KEY=your_google_gemini_api_key

3. **Run the assistant**
   ```bash
   python main.py
