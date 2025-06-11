# LinguaKids 

**An AI-powered English Learning Assistant for Kids** — combining voice recognition, grammar correction, text-to-speech, and lip-sync animation to make learning interactive and fun!

##  Project Structure
  ai_lip_sync/
      │
      ├── app.py # Main Streamlit app
      ├── requirements.txt # Python dependencies
      ├── .env # Environment variables (e.g., API keys)
      ├── assets/ # Static assets like images or video templates
      ├── modules/ # Modular code (Whisper, Gemini API, gTTS, etc.)
      ├── output/ # Generated media/output files

 ## 🌟 Features

  ###  AI-Driven Learning
  - Uses **Google Gemini API** to correct grammar and explain sentence structure in a kid-friendly way.
  
  ### Voice Input
  - Kids can **speak sentences** using a microphone.
  - Audio is transcribed using **OpenAI's Whisper** model for accurate speech recognition.
  
  ### Grammar Correction
  - Spoken sentences are analyzed and corrected by Gemini.
  - Provides **easy explanations** to help children learn from their mistakes.
  
  ### Text-to-Speech (TTS)
  - The corrected sentence is spoken back using **Google Text-to-Speech (gTTS)**.
  - Helps kids understand pronunciation and fluency.
  
  ### Lip-Sync Animation
  - Generates **talking face animations** that sync with the corrected audio.
  - Makes learning **visually engaging and fun** for children.

  ###  Kid-Friendly Interface
- Built with **Streamlit** for a simple, interactive web UI.
- Encourages self-learning through play.
