# import sounddevice as sd
# from scipy.io.wavfile import write
# import speech_recognition as sr
# import google.generativeai as genai
# from dotenv import load_dotenv
# import os
# from elevenlabs import ElevenLabs, play

# # ✅ Load API keys from .env
# load_dotenv()
# GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
# ELEVEN_API_KEY = os.getenv("ELEVENLABS_API_KEY")

# # ✅ Configure Gemini
# genai.configure(api_key=GEMINI_API_KEY)
# model = genai.GenerativeModel("gemini-1.5-flash")

# # ✅ Initialize Eleven Labs
# client = ElevenLabs(api_key=ELEVEN_API_KEY)
# VOICE_ID = "6OzrBCQf8cjERkYgzSg8"  # Your custom voice ID

# # 🎤 Record audio from microphone
# def record_audio(filename="input.wav", duration=5, fs=44100):
#     print("🎤 Speak now...")
#     audio = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
#     sd.wait()
#     write(filename, fs, audio)
#     print("✅ Recording saved.")
#     return filename

# # 🧠 Transcribe with Google Speech Recognition
# def transcribe_audio(file_path):
#     recognizer = sr.Recognizer()
#     with sr.AudioFile(file_path) as source:
#         audio = recognizer.record(source)
#         try:
#             return recognizer.recognize_google(audio)
#         except sr.UnknownValueError:
#             return None
#         except sr.RequestError:
#             print("❌ Google STT service error.")
#             return None

# # 💬 Get response from Gemini
# def ask_gemini(prompt):
#     response = model.generate_content(prompt)
#     return response.text.strip()

# # 🔊 Speak response using Eleven Labs
# def speak_response(text):
#     print(f"🧠 Gemini: {text}")
#     audio = client.text_to_speech.convert(
#         text=text,
#         voice_id=VOICE_ID,
#         model_id="eleven_multilingual_v2",
#         output_format="mp3_44100_128"
#     )
#     play(audio)

# # 🚀 Main App Flow
# if __name__ == "__main__":
#     audio_file = record_audio()
#     text = transcribe_audio(audio_file)

#     if not text:
#         print("❗ Could not understand your voice.")
#     else:
#         print(f"📥 You said: {text}")
#         reply = ask_gemini(text)
#         speak_response(reply)


import sounddevice as sd
from scipy.io.wavfile import write
import speech_recognition as sr
import google.generativeai as genai
from gtts import gTTS
from playsound import playsound
from dotenv import load_dotenv
import os

#  Load API key from .env
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

#  Configure Gemini
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

#  Record audio from microphone
def record_audio(filename="input.wav", duration=8, fs=44100):
    print("Speak now...")
    audio = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()
    write(filename, fs, audio)
    print("Recording saved.")
    return filename

#  Transcribe with Google Speech Recognition
def transcribe_audio(file_path):
    recognizer = sr.Recognizer()
    with sr.AudioFile(file_path) as source:
        audio = recognizer.record(source)
        try:
            return recognizer.recognize_google(audio)
        except sr.UnknownValueError:
            return None
        except sr.RequestError:
            print("Google STT service error.")
            return None

# 💬 Get response from Gemini
def ask_gemini(prompt):
    response = model.generate_content(prompt)
    return response.text.strip()

# 🔊 Speak response using gTTS
def speak_response(text, output_path="response.mp3"):
    print(f" Gemini: {text}")
    tts = gTTS(text=text, lang='en')
    tts.save(output_path)
    playsound(output_path)

# 🚀 Main App Flow
if __name__ == "__main__":
    audio_file = record_audio()
    text = transcribe_audio(audio_file)

    if not text:
        print("❗ Could not understand your voice.")
    else:
        print(f"You said: {text}")
        reply = ask_gemini(text)
        speak_response(reply)