import streamlit as st

# Set page title and icon
st.set_page_config(page_title="Anagram Checker", page_icon="📌" , layout="centered")

# Function to check if two words are anagrams
def is_anagram(word1, word2):
    # Remove any spaces and convert to lowercase for case-insensitive comparison
    word1 = word1.replace(" ", "").lower()
    word2 = word2.replace(" ", "").lower()
    
    # Check if sorted characters of both words are the same
    if sorted(word1) == sorted(word2):
        return "✅ Yes, it's an anagram!"
    else:
        return "❌ No, it's not an anagram!"

# Streamlit UI
st.title("📌📌Anagram Checker")
st.write("🎨📝Enter two words to check if they are anagrams:")

# Custom CSS for enhanced UI styling
st.markdown("""
    <style>
        body {
            background-color: #f7f7f7;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            color: #333;
        }

        .stTitle {
            color: #ff6347;
            text-align: center;
            font-size: 3rem;
            margin-top: 30px;
            font-weight: bold;
        }

        .stTextInput label {
            font-size: 1.2rem;
            color: #555;
            margin-bottom: 10px;
        }

        .stTextInput input {
            padding: 20px;
            font-size: 1.1rem;
            border: 2px solid #0077cc;
            border-radius: 8px;
            width: 100%;
            margin-bottom: 20px;
            background-color: #f4f4f4;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        }

        .stTextInput input:focus {
            outline: none;
            border-color: #ff6347;
            background-color: #fff;
        }

        .stButton button {
            background-color: #ff6347;
            color: white;
            padding: 12px 28px;
            border-radius: 30px;
            border: none;
            font-size: 1.1rem;
            cursor: pointer;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            transition: all 0.3s ease;
        }

        .stButton button:hover {
            color: #0077cc !important;
            background-color: #ff4500;
            transform: translateY(-3px);
        }

        .stButton button:active {
            color: white;
            background-color: #ff4500;
            transform: translateY(2px);
        }

        .result {
            font-size: 1.5rem;
            font-weight: bold;
            color: #333;
            text-align: center;
            margin-top: 30px;
        }

        .result.success {
            color: #28a745;
        }

        .result.error {
            color: #dc3545;
        }

        .footer {
            text-align: center;
            font-size: 0.9rem;
            color: #777;
            margin-top: 50px;
        }

        .footer a {
            color: #0077cc;
            text-decoration: none;
        }
    </style>
""", unsafe_allow_html=True)

# Input fields for words
word1 = st.text_input("✍Enter the first word:")
word2 = st.text_input("✍Enter the second word:")

# Button to check anagram status
if st.button("Check Anagram"):
    if word1 and word2:
        result = is_anagram(word1, word2)
        result_class = "success" if "Yes" in result else "error"
        st.markdown(f'<div class="result {result_class}">{result}</div>', unsafe_allow_html=True)
    else:
        st.write("❗ Please enter both words.")

# Footer for additional info
st.markdown('<div class="footer">Made with ❤️ by Streamlit</div>', unsafe_allow_html=True)
