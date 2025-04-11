import torch
import pyaudio
import numpy as np
import threading
from transformers import WhisperProcessor, WhisperForConditionalGeneration

# Device setup
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Load the Whisper model and processor
processor = WhisperProcessor.from_pretrained("openai/whisper-small")
model = WhisperForConditionalGeneration.from_pretrained("openai/whisper-small").to(device)
model.eval()  # Set the model to evaluation mode

# Audio recording settings
FORMAT = pyaudio.paInt16  # 16-bit resolution
CHANNELS = 1  # Mono channel
RATE = 16000  # Whisper requires 16kHz
CHUNK = 1024  # Buffer size

# Global variables
audio = pyaudio.PyAudio()
stream = None
recording = False
audio_buffer = b""
audio_thread = None  # Thread for capturing audio


def transcribe_audio(audio_buffer):
    """Transcribe the recorded speech into English text."""
    # Convert audio buffer to NumPy array (normalize to -1.0 to 1.0 range)
    audio_np = np.frombuffer(audio_buffer, dtype=np.int16).astype(np.float32) / 32768.0

    # Process audio input for Whisper
    inputs = processor(audio_np, sampling_rate=RATE, return_tensors="pt")
    input_features = inputs["input_features"].to(device)

    # Generate transcription with English language constraint
    with torch.no_grad():
        predicted_ids = model.generate(
            input_features,
            forced_decoder_ids=processor.tokenizer.get_decoder_prompt_ids(language="en", task="transcribe")
        )

    # Decode transcription
    transcription = processor.batch_decode(predicted_ids, skip_special_tokens=True)[0]
    return transcription


def capture_audio():
    """Continuously read audio while recording."""
    global stream, recording, audio_buffer

    while recording:
        try:
            audio_chunk = stream.read(CHUNK, exception_on_overflow=False)
            audio_buffer += audio_chunk  # Accumulate audio data
        except Exception as e:
            print(f"Error reading audio: {e}")
            break

    print("Stopped capturing audio.")


def start_capture():
    """Start capturing audio in a separate thread."""
    global stream, recording, audio_buffer, audio_thread

    if recording:
        print("Already recording...")
        return

    stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)
    recording = True
    audio_buffer = b""
    print("Listening...")

    # Start audio capture in a separate thread
    audio_thread = threading.Thread(target=capture_audio)
    audio_thread.start()


def stop_capture():
    """Stop capturing audio and return transcription."""
    global stream, recording, audio_buffer, audio_thread

    if not recording:
        print("Not recording...")
        return ""

    recording = False
    if audio_thread:
        audio_thread.join()  # Wait for the thread to finish

    stream.stop_stream()
    stream.close()
    print("Processing audio...")

    transcription = transcribe_audio(audio_buffer)
    return transcription


# Example usage
if __name__ == "__main__":
    start_capture()
    input("Press Enter to stop recording...\n")
    result = stop_capture()
    print(f"Transcription: {result}")

    # Close the PyAudio instance properly
    audio.terminate()