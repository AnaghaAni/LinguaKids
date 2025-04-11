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
🔧 Installation

Clone the repository:

git clone https://github.com/AnaghaAni/LinguaKids.git
cd LinguaKids/ai_lip_sync

Create a virtual environment:

python -m venv venv
source venv/bin/activate  # For Linux/Mac
venv\Scripts\activate     # For Windows

Install the dependencies:

pip install -r requirements.txt

Set up the .env file:

Create a .env file in the root with your keys:

GOOGLE_API_KEY=your_google_api_key

▶️ Run the App

streamlit run app.py

🚰 Technologies Used

Python

Streamlit

gTTS

Google Generative AI

PyTorch & Transformers

MySQL Connector

NumPy

pyaudio

📸 Example Output

Input: User-provided image and text/audio

Output: AI-generated video with synced lip movements
