import streamlit as st
import base64

# Function to encode the local image file as Base64
# This is needed to embed the image in CSS for Streamlit background
def get_base64_image(file_path):
    with open(file_path, "rb") as file:
        data = file.read()
    return base64.b64encode(data).decode()

# Function to set a background image using CSS and Base64 encoding
# This gives a custom visual appearance to the Streamlit app
def set_background(image_file):
    base64_str = get_base64_image(image_file)  # Get base64 string of the image
    css = f"""
    <style>
        .stApp {{
            background-image: url("data:image/png;base64,{base64_str}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        .title {{
            text-align: center;
            font-weight: bold;
            color: purple;
            text-shadow: 2px 2px 4px gray;
            font-size: 2.5em;
            margin-top: 20px;
        }}
        h2 {{
            text-align: center;
            color: gray;
            font-size: 1.5em;
        }}
        .forgot, .register {{
            font-size: 0.9em;
            text-decoration: none;
        }}
        .forgot:hover {{
            color: red;
        }}
        .register:hover {{
            color: green;
        }}
        .footer {{
            text-align: center;
            font-size: 0.8em;
            color: gray;
            margin-top: 50px;
        }}
    </style>
    """
    # Inject the custom CSS into the Streamlit app
    st.markdown(css, unsafe_allow_html=True)
