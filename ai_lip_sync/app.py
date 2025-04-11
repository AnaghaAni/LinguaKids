import os
import streamlit as st
from modules.gemini_chat import get_gemini_response
from modules.text_to_speech import tts
import threading
from modules.lipsync_generator import generate_video
from modules.background import set_background
from modules.speech_to_text import capture_audio,start_capture,stop_capture
from modules.auth import authenticate_user, register_user



def app():
    # Set background image (implement set_background() if needed)
    set_background("pic2.jpg")

    if "page" not in st.session_state:
        st.session_state.page = "login"

    if st.session_state.page == "login":
        st.title("User Login")
        username = st.text_input("Username")
        password = st.text_input("Password", type='password')
        focus = st.text_input("Focus")

        if st.button("Login"):
            if username and password:
                user = authenticate_user(username, password)
                if user:
                    st.session_state.update({"focus": focus, "logged_in": True, "username": username, "page": "gemini_module"})
                    st.rerun()
                else:
                    st.error("Invalid username or password.")
            else:
                st.error("Please enter both username and password.")

        if st.button("Register Here"):
            st.session_state.page = "register"
            st.rerun()

    elif st.session_state.page == "register":
        st.title("User Registration")
        username = st.text_input("Choose a Username")
        password = st.text_input("Create a Password", type='password')

        if st.button("Register"):
            if not username or not password:
                st.error("All fields are required.")
            else:
                if register_user(username, password):
                    st.session_state.page = "login"
                    st.rerun()

        if st.button("Back to Login"):
            st.session_state.page = "login"
            st.rerun()

    elif st.session_state.page == "gemini_module":
        if 'logged_in' in st.session_state and st.session_state.logged_in:
            st.title(f"Welcome, {st.session_state.username}!")
            st.write(f"Focus on: {st.session_state.focus}")

            if "chat_history" not in st.session_state:
                st.session_state["chat_history"] = []

            chat_placeholder = st.empty()
            user_input = None

            # Speech-to-Text Button Controls
            col1, col2 = st.columns(2)
            with col1:
                if st.button("🎤 Start Recording"):
                    start_capture()
                    threading.Thread(target=capture_audio, daemon=True).start()

            with col2:
                if st.button("🛑 Stop Recording"):
                    user_input = stop_capture()

            if user_input:
                st.session_state["chat_history"].append({"role": "user", "content": user_input})

                corrected_sentence, explanation, gemini_reply = get_gemini_response(user_input, st.session_state["chat_history"])
                # **Extract Corrected Sentence and Explanation**
                corrected_sentence = gemini_reply.split("**Explanation:**")[0].replace("**Corrected Sentence:**", "").strip()
                explanation = gemini_reply.split("**Explanation:**")[1].strip() if "**Explanation:**" in gemini_reply else ""

                # Append AI response to chat history
                st.session_state["chat_history"].append({"role": "assistant", "content": gemini_reply})

                # **Display Conversation**
                chat_placeholder.empty()
                for msg in st.session_state["chat_history"]:
                    role = "You" if msg['role'] == "user" else "Gemini"
                    chat_placeholder.write(f"**{role}:** {msg['content']}")

                # **Generate AI Voice Response for Only the Corrected Sentence**
                  # Fixed file path to overwrite
                #audio_file=elevenlabs_tts(corrected_sentence, audio_files) 
                tts(corrected_sentence + explanation, lang='en', output_file="assets/audio/response.mp3")
               
                #st.audio("response.mp3", format="audio/mp3")

                # **Generate Lip-Sync Video**
                video_input = corrected_sentence + "\n\nShort Explanation: " + explanation
                video_path, error_message = generate_video(video_input)

                if error_message:
                    st.error(error_message)
                elif video_path:
                    st.success("✅ Lip-Sync Video Generated!")
                    st.video(video_path)

                    # **Provide Download Button**
                    with open(video_path, "rb") as file:
                        st.download_button("⬇️ Download Lip-Sync Video", file, "lipsync_output.mp4", "video/mp4")
if __name__ == "__main__":
    app()