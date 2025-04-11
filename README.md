# 🎓 Linguakids – AI-Powered English Learning Platform

**Linguakids** is an AI-driven educational web application designed to make English learning fun and engaging for kids. With features like avatar-based lip syncing, voice interaction, and generative AI responses, children can interact with a digital tutor that speaks, listens, and responds—making the learning experience more immersive.

---

## ✨ Key Features

- 🎙️ **Text-to-Speech & Voice Interaction**  
  Converts text to speech using `gTTS` and allows users to listen to AI-generated answers.

- 🧒 **Lip-Synced Avatar Animation**  
  Upload an avatar image and audio, and the app generates a lip-synced video to enhance visual engagement.

- 🤖 **AI-Powered Answers**  
  Uses **Google Generative AI** (Gemini) to answer children’s questions intelligently.

- 🌐 **Simple Web Interface**  
  Built using **Streamlit** for easy use on web browsers.

---
## ⚙️ Installation & Setup
    - git clone https://github.com/AnaghaAni/LinguaKids.git
      cd Linguakids/ai_lip_sync

##  Create a Virtual Environment
    - python -m venv venv
##  Activate the virtual environment:
      venv\Scripts\activate
##   Run the Application
      streamlit run app.py


## 🛠️ Tech Stack

- Frontend/UI: `Streamlit`
- AI & NLP: `Google Generative AI`, `Transformers`, `Torch`
- Audio: `gTTS`, `PyAudio`
- Database: `MySQL`
- Utility Libraries: `python-dotenv`, `NumPy`

---

## 📁 Project Structure

```plaintext
Linguakids/ai_lip_sync
├── assets/
│   ├── images/
│   │   └── avatar.jpg
│   └── audio/
│       └── response.mp3
├── output/
│   └── lipsync_output.mp4
├── app.py
├── .env
├── requirements.txt
└── README.md

---
