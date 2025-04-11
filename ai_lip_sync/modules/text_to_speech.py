from gtts import gTTS
import os


def tts(text, lang='en', output_file="assets/audio/response.mp3"):
    """
    Converts the given text into speech and saves it as an MP3 file.

    Parameters:
    - text (str): The text to convert to speech.
    - lang (str): Language for the text-to-speech conversion (default: 'en').
    - output_file (str): Name of the output MP3 file.
    """
    try:
        # Create TTS object
        tts = gTTS(text=text, lang=lang)
        tts.save(output_file)
        # audio = AudioSegment.from_mp3(output_file)

    except Exception as e:
        print(f"An error occurred: {e}")

    #return audio

# if _name_ == "_main_":
#     # Example usage
#     input_text = "Hello world"
#     tts(input_text)