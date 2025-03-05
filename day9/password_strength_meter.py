import streamlit as st
import re

# Set page title and icon
st.set_page_config(page_title="Password Strength Checker", page_icon="🔐" , layout="centered")

# Function to check password strength
def check_password_strength(password):
    # Check for weak password
    if len(password) < 6 or password.isalpha():
        return "Weak ❌"
    
    # Check for moderate password
    if len(password) >= 8 and not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return "Moderate ⚠"
    
    # Check for strong password
    if (len(password) >= 8 and 
        re.search(r'[A-Z]', password) and 

        re.search(r'[a-z]', password) and 
        re.search(r'[0-9]', password) and 
        re.search(r'[!@#$%^&*(),.?":{}|<>]', password)):
        return "Strong ✅"
    
    # If no condition is met
    return "Weak ❌"

def apply_styles():
    st.markdown("""
        <style>
            body {
                background-color: #f1f1f1;
                font-family: 'Arial', sans-serif;
            }

            /* Title styling */
            h1 {
                color: #2c3e50;
                text-align: center;
                font-size: 36px;
                font-weight: bold;
            }

            /* Subtitle styling */
            h3 {
                color: #34495e;
                text-align: center;
                font-size: 20px;
            }

            /* Password Strength Styling */
            .password-strength {
                color: black;
                text-align: center;
                font-size: 22px;
                font-weight: bold;
            }

            /* Button Styling */
            button {
                background: linear-gradient(45deg, #ff6b6b, #ff4081);
                color: white;
                padding: 16px 40px;
                font-size: 22px;
                font-weight: bold;
                border-radius: 50px;
                cursor: pointer;
                border: 2px solid transparent;
                text-transform: uppercase;
                letter-spacing: 1px;
                transition: all 0.3s ease;
                box-shadow: 0 10px 20px rgba(0, 0, 0, 0.2);
                display: inline-block;
            }

            button:hover {
                background: linear-gradient(45deg, #ff4081, #ff6b6b);  
                color: white !important;             
                transform: translateY(-4px);
                box-shadow: 0 12px 30px rgba(0, 0, 0, 0.3);
                border: 2px solid #fff;
                animation: glow 1.5s ease-in-out infinite;
            }

            @keyframes glow {
                0% { 
                    box-shadow: 0 0 10px rgba(255, 105, 135, 0.8), 
                    0 0 20px rgba(255, 105, 135, 0.6);
                }
                100% { 
                    box-shadow: 0 0 20px rgba(255, 105, 135, 1), 
                    0 0 30px rgba(255, 105, 135, 1);
                }
            }

        </style>
    """, unsafe_allow_html=True)

# Streamlit app
def app():
    # Apply custom CSS styles directly
    apply_styles()

    # Display Title
    st.markdown('<h1>Password Strength Checker</h1>', unsafe_allow_html=True)

    # Subtitle
    st.markdown('<h3>Enter your password to check its strength</h3>', unsafe_allow_html=True)

    # User input for password
    password = st.text_input("", type="password", help="Password must be at least 6 characters", placeholder="Enter your password...", key="password_input")

    # Stylish Check Strength button
    if st.button("Check Strength", key="check_strength_button", help="Click to check your password strength"):
        if password:
            password_strength = check_password_strength(password)
            st.markdown(f'<div class="password-strength">{password_strength}</div>', unsafe_allow_html=True)
        else:
            st.warning("Please enter a password to check its strength.")

if __name__ == "__main__":
    app()
