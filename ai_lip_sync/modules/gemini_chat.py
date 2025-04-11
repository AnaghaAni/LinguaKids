# gemini_chat.py
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
OPENAI_API_KEY = os.getenv("API_KEY")
genai.configure(api_key=OPENAI_API_KEY)

# Function to interact with Gemini and return the response
def get_gemini_response(user_input, chat_history):
    # Prompt structure
    prompt_base = (
        "You are an English tutor who helps kids improve their speaking and writing. "
        "When given a sentence, follow these steps:\n"
        "1. Correct the sentence if there are any grammar, spelling, punctuation, or structure mistakes.\n"
        "2. Provide only the corrected version of the sentence. Do not add extra words, explanations, or formatting in the sentence.\n"
        "3. After the corrected sentence, give a short explanation of what was wrong. Keep it simple, clear, and friendly so a child can understand.\n"
        "4. Make sure the corrected sentence is easy to read.\n"
        "5. Do not use any symbols like *, -, ~, #, or emojis.\n"
        "Here is the sentence to correct:\n"
        f"{user_input}\n"
        "Corrected Sentence: <Write only the corrected sentence here>\n"
        "Explanation: <Briefly explain the mistake in simple and friendly language>"
    )

    # Build conversation context
    conversation_history = "\n".join(
        [f"{msg['role'].capitalize()}: {msg['content']}" for msg in chat_history]
    )
    prompt = f"{prompt_base}\n\n{conversation_history}"

    # Generate response
    model = genai.GenerativeModel('gemini-2.0-flash')
    response = model.generate_content(prompt)
    reply_text = response.text.strip()

    # Parse response
    corrected_sentence = ""
    explanation = ""

    if "Explanation:" in reply_text:
        parts = reply_text.split("Explanation:")
        corrected_sentence = parts[0].replace("Corrected Sentence:", "").strip()
        explanation = parts[1].strip()
    else:
        corrected_sentence = reply_text.strip()

    return corrected_sentence, explanation, reply_text
