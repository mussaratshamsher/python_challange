import streamlit as st
import string

st.set_page_config(page_title="Encoder & Decoder", page_icon="🔐", layout="centered")

# Function to handle the Caesar Cipher
def caesar_cipher(message, shift, mode='encode'):
    result = []
    
    for char in message:
        if char.isalpha():
            # Determine the base (A for uppercase or a for lowercase)
            base = ord('A') if char.isupper() else ord('a')
            if mode == 'encode':
                new_char = chr((ord(char) - base + shift) % 26 + base)
            elif mode == 'decode':
                new_char = chr((ord(char) - base - shift) % 26 + base)
            result.append(new_char)
        else:
            result.append(char)  # Non-alphabetic characters are added as-is
    
    return ''.join(result)

# Function to change the background color with gradient and custom button styles
def set_custom_css():
    st.markdown("""
        <style>
        /* Overall app styling */
        .stApp {
           background: linear-gradient(to right, #ff0000, #ff7300, #fffb00, #00d900, #00b8b8, #3200ff, #8a00ff);
            color: white;
        }
        /* Title animation: typing effect */
        h1 {
            color: white;
            font-size: 36px;
            font-weight: bold;
        }
        /* Keyframes for typing effect */
        @keyframes typing {
            from {
                width: 0;
            }
            to {
                width: 100%;
            }
        }

        /* Keyframes for blinking cursor effect */
        @keyframes blink {
            50% {
                border-color: transparent;
            }
            100% {
                border-color: white;
            }
        }

        /* Stylish button with gradient and a moving underline */
        .stButton button {
            background: linear-gradient(to right, #ff7e5f, #feb47b);
            color: white;
            border: none;
            padding: 10px 20px;
            text-align: center;
            display: inline-block;
            font-size: 18px;
            border-radius: 12px;
            position: relative;
            transition: background 0.3s ease-in-out;
            overflow: hidden;
        }

        .stButton > button:hover {
            background: linear-gradient(to right, #feb47b, #ff7e5f);
        }

        /* Adding a moving underline effect to buttons */
        .stButton button:before {
            content: '';
            position: absolute;
            bottom: 0;
            left: 50%;
            width: 0;
            height: 3px;
            background: #e1e1e1;  /* Light color for better visibility on dark background */
            transition: width 0.4s, left 0.4s;
        }

        .stButton > button:hover:before {
            width: 100%;
            left: 0;
        }

        /* Text area custom styling */
        .stTextArea textarea {
            background-color: #f7f7f7;
            border-radius: 8px;
            padding: 10px;
            font-size: 16px;
        }

        </style>
    """, unsafe_allow_html=True)

# Set custom CSS for background, button, and text area styles
set_custom_css()

# Streamlit UI
st.title("🔐📌Caesar Cipher Encoder & Decoder")

message = st.text_area("Enter your message:", "")
shift = st.slider("Choose the shift value:", 1, 25, 3)

# Create columns for the buttons to control encoding and decoding
col1, col2 = st.columns(2)

# Add buttons to encode or decode the message
with col1:
    if st.button('Encode Message'):
        if message:
            encoded_message = caesar_cipher(message, shift, mode='encode')
            st.info(f"Encoded Message: {encoded_message}")
            st.balloons()
        else:
            st.info("Please enter a message to encode.")

with col2:
    if st.button('Decode Message'):
        if message:
            decoded_message = caesar_cipher(message, shift, mode='decode')
            st.info(f"Decoded Message: {decoded_message}")
            st.snow()
        else:
          st.info("Please encode a message first.") 
