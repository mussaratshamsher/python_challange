import random
import streamlit as st

# Set up the page title with an icon
st.set_page_config(page_title="🎨📌 Number Guessing Game", page_icon="🎮")

# Inject custom CSS to style the UI
st.markdown("""
    <style>
    /* Add a border around the whole content */
    .stApp {
        border-radius: 15px;
        padding: 20px;
        border: 2px solid #4CAF50;
        background-color: #f0f8ff;
    }

    /* Style the submit button with dynamic gradient animation */
    .stButton button {
        background: linear-gradient(45deg, #ff9a9e, #fad0c4, #f7fff7,  #b1f785);
        background-size: 400% 400%;
        color: white;
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
        transform: scale(1.05);
        background-position: 100% 50%; /* Push the gradient to full color change */
    }

    /* Title and subtitle styling */
    h1 {
        font-size: 36px;
        text-align: center;
    }

    h2 {
        font-size: 24px;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# Game title and instructions
st.title("🎨📌 Welcome to the Number Guessing Game!")
st.subheader("💭 You have 6 chances to guess the number between 50 & 100.")

# Check if game is over or in progress
if 'game_over' not in st.session_state:
    st.session_state.game_over = False

# Function to start the game again by resetting the game variables
def start_again():
    st.session_state.number_to_guess = random.randrange(50, 100)
    st.session_state.guess_counter = 0
    st.session_state.game_over = False
    st.session_state.user_guess = 0  # Reset the user's guess

# Start a new game if not already over
if not st.session_state.game_over:
    # Generate a random number to guess
    if 'number_to_guess' not in st.session_state:
        st.session_state.number_to_guess = random.randrange(50, 100)

    chances = 6

    # Store session state variables
    if 'guess_counter' not in st.session_state:
        st.session_state.guess_counter = 0
    if 'guessed_numbers' not in st.session_state:
        st.session_state.guessed_numbers = []

    # Function to handle guesses
    def make_guess():
        guess = st.session_state.user_guess

        if guess == st.session_state.number_to_guess:
            st.session_state.guess_counter += 1
            st.success(f"🎉 Congratulations! You guessed the number {st.session_state.number_to_guess} correctly in {st.session_state.guess_counter} attempts!")
            st.balloons()
            st.session_state.game_over = True
        elif st.session_state.guess_counter >= chances:
            st.session_state.game_over = True
            st.error(f"💥 Oops, you have used all your chances! The correct number was {st.session_state.number_to_guess}. Better luck next time!")
        elif guess < st.session_state.number_to_guess:
            st.session_state.guess_counter += 1
            st.warning("🔽 Your guess is too low! Try again.")
        elif guess > st.session_state.number_to_guess:
            st.session_state.guess_counter += 1
            st.warning("🔼 Your guess is too high! Try again.")

    # Allow user to input a guess
    st.session_state.user_guess = st.number_input("✍ Enter your guess (between 50 and 100):", min_value=50, max_value=100, step=1)

    # Button to submit guess
    if st.button("Submit Guess"):
        make_guess()

    # Show remaining chances
    remaining_chances = chances - st.session_state.guess_counter
    if remaining_chances > 0:
        st.info(f"You have {remaining_chances} chances remaining.")
    else:
        st.info("Game over! Click the button above to start a new game.")

else:
    # If the game is over, hide the Submit button and show the Start Again button
    if st.button("Start Again"):
        start_again()  # Reset the game state immediately without needing to refresh
