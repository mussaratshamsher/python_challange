import streamlit as st
import re

# function to detect mood based on emoji
def detect_mood(message):
    # emoji patterns & moods
    happy_emoji = r'[😊😍😄😀😆]'
    sad_emoji = r'[😥😏😔☹😟😭]'
    angry_emoji = r'[😡🤬🥵😠😈👿]'
    neutral_emoji = r'[😐🤔😶😑]'
    curious_emoji = r'[😧😦🧐🤨]'
    sick_emoji = r'[😤🤧🤕🤒]'
    naughty_emoji = r'[🤪😝😜🤩😛😛]'
    lazy_emoji = r'[🥱😫😴😳🥴]'

    # Check for emojis in the message
    if re.search(happy_emoji, message):
        return "Happy Mood! 🎉"
    elif re.search(sad_emoji, message):
        return "Sad Mood! 😥"
    elif re.search(angry_emoji, message):
        return "Angry Mood! 😠"
    elif re.search(neutral_emoji, message):
        return "Neutral Mood! 😐"
    elif re.search(curious_emoji, message):
        return "Curious Mood! 🤨"
    elif re.search(sick_emoji, message):
        return "Sick! 🤒"
    elif re.search(naughty_emoji, message):
        return "Naughty Mood! 🤪"
    elif re.search(lazy_emoji, message):
        return "Feeling Lazy! 😴"
    else:
        return "No emoji found, can't detect mood! 🤗"

# streamlit page config
st.set_page_config(page_title="Emoji Mood Detector", page_icon="😃", layout="centered")

# Custom CSS for styling
st.markdown("""
    <style>
        body {
            font-family: 'Arial', sans-serif;
        }
       /* Button Styling */
            .stButton button {
        background: linear-gradient(45deg, #ff9a9e, #fad0c4, #f7fff7,  #b1f785);
        background-size: 400% 400%;
        color: red;
        font-size: 20px;
        padding: 15px 32px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-weight: bold;
        border: 2px solid transparent;
        border-radius: 50px;
        cursor: pointer;
        transition: 0.5s;
        animation: gradientAnimation 3s ease infinite; /* Only gradient animation */
    }

    /* Gradient animation for background (blowing wind effect) */
    @keyframes gradientAnimation {
        0% {
            background-position: 0% 50%;
        }
        50% {
            background-position: 100% 50%;
        }
        100% {
            background-position: 0% 50%;
        }
    }

    /* Hover effect to enlarge the button slightly */
    .stButton button:hover {
            color: white;
        transform: scale(1.05);
        background-position: 100% 50%; /* Push the gradient to full color change */
    }
        .stTextInput>div>div>input {
            font-size: 18px;
            padding: 10px;
            border-radius: 8px;
            border: 2px solid red;
        }
    </style>
""", unsafe_allow_html=True)

st.title("Welcome to the Emoji Mood Detector! 😎")
st.subheader("Enter a message with emojis, & let's detect your mood!")

# input from the user
message = st.text_input("Type a message with emojis to detect mood", "")

# Using session state to store the result
if 'detected_mood' not in st.session_state:
    st.session_state.detected_mood = None

# Custom button to detect mood on single click
if st.button("Detect Mood"):
    if message:
        st.session_state.detected_mood = detect_mood(message)
    else:
        st.warning("Please enter a message first!")

# Display the result if available
if st.session_state.detected_mood:
    st.markdown(f"<h3 style='color: red;'>{st.session_state.detected_mood}</h3>", unsafe_allow_html=True)
