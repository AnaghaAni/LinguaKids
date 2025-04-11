import streamlit as st
import requests
import json
import os
import time

from dotenv import load_dotenv
import os

# # Load .env file
# load_dotenv()

# # Access the API key
# api_key = os.getenv("GOOEY_API_KEY ")
GOOEY_API_KEY = "sk-IPc9cIf3kf8sGBH8809BxnDOvfbXAHplK7XMLC58dm61yWBY"
API_URL = "https://api.gooey.ai/v2/Lipsync/form/"



# Run the video generation automatically when the page loads
def generate_video(video_input):
    image_path = "assets/images/avatar.jpg"
    audio_path = "assets/audio/response.mp3"

  

    # Ensure both files exist
    if not os.path.exists(image_path):
        return None, "❌ Error: Image file does not exist!"
    if not os.path.exists(audio_path):
        return None, "❌ Error: Audio file does not exist!"

    print(f"📂 Using image: {image_path}")
    print(f"📂 Using audio: {audio_path}")

    with st.spinner("Processing... Please wait ⏳"):
        files = {
            "input_face": open(image_path, "rb"),
            "input_audio": open(audio_path, "rb")
        }

        payload = {"language": "en"}

        try:
            response = requests.post(
                API_URL,
                headers={"Authorization": f"Bearer {GOOEY_API_KEY}"},
                files=files,
                data={"json": json.dumps(payload)}
            )
        finally:
            files["input_face"].close()
            files["input_audio"].close()

        if response.status_code == 200:
            result = response.json()
            if "output" in result and "output_video" in result["output"]:
                video_url = result["output"]["output_video"]

                # Download the video
                video_response = requests.get(video_url)
                if video_response.status_code == 200:
                    output_path = "output\lipsync_output.mp4"
                    with open(output_path, "wb") as video_file:
                        video_file.write(video_response.content)

                    return output_path, None  # Return video path, no error
                else:
                    return None, "❌ Failed to download video"
            else:
                return None, "❌ Unexpected API response format"
        else:
            return None, f"❌ API Error: {response.status_code} - {response.text}"
