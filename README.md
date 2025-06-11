# LinguaKids 

**An AI-powered English Learning Assistant for Kids** — combining voice recognition, grammar correction, text-to-speech, and lip-sync animation to make learning interactive and fun!
  

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

## Follow these steps to clone and run the project on a different machine:
  ### 1. Clone the Repository
      
          git clone https://github.com/AnaghaAni/LinguaKids.git
          cd LinguaKids/ai_lip_sync

  ### 2. Create and Activate Virtual Environment
         
        python -m venv venv
        For Windows
        .\venv\Scripts\activate

  ### 3. Install Dependencies
  
          pip install -r requirements.txt

  ### 4. Set Up Environment Variables

        create .env file -to manage sensitive data like API keys
   ### Install dotenv (if not already installed)

      
          pip install python-dotenv

  ### 5. MySQL Connector (XAMPP Integration)

      To connect Python with the MySQL server running in XAMPP, install the official MySQL connector:
      
      
          pip install mysql-connector-python

  ### 6.   Run the App
            python -m streamlit run app.py



          
