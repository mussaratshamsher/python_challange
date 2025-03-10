# 🚀 Challenge: Create a Text-Based Adventure Game where the user makes choices that impact the story! 🎮✨

# 🔥 Requirements:
# ⿡ Display a short intro story.
# ⿢ Give the player two choices at each step.
# ⿣ The choices should lead to different outcomes (win/lose/continue).
# ⿤ Keep it simple & interactive using input().


import streamlit as st

st.set_page_config(page_title="The Great Escape: A Mystery Adventure",page_icon= "🧩",layout="centered")

# Initial game state
if 'step' not in st.session_state:
    st.session_state.step = 'intro'

# CSS Styling for Background, Buttons, and Animations
st.markdown("""
    <style>
     .stApp {
    background: #ffefba;  /* Fallback for older browsers */
    background: -webkit-linear-gradient(to top, #ff9a8b, #ffb3ba, #ffefba);  /* Chrome 10-25, Safari 5.1-6 */
    background: linear-gradient(to top, #ff9a8b, #ffb3ba, #ffefba); /* W3C, IE 10+, Edge, Firefox 16+, Chrome 26+, Opera 12+, Safari 7+ */
    height: 100vh;
    margin: 0;
    padding: 0;
}
    .stButton>button {
        background: linear-gradient(45deg, #ff6b81, #6a1b9a, #4caf50, #ffeb3b);
        background-size: 400% 400%;
        color: white;
        border: none;
        border-radius: 12px;
        padding: 10px 24px;
        text-align: center;
        display: inline-block;
        font-size: 16px;
        margin: 10px 2px;
        cursor: pointer;
        transition: all 0.5s ease;
        animation: gradientAnimation 3s ease infinite;
    }
    .stButton>button:hover {
            color: white;
            font: bold;
        transform: scale(1.1);
    }
    @keyframes gradientAnimation {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    .fade-in {
        animation: fadeIn 2s ease-out;
    }
    @keyframes fadeIn {
        0% { opacity: 0; }
        100% { opacity: 1; }
    }
    .balloon {
        position: absolute;
        top: 20%;
        left: 50%;
        width: 100px;
        height: 150px;
        background-color: #ff0000;
        border-radius: 50%;
        animation: floatBalloons 10s infinite;
        animation-delay: 0.5s;
    }
    @keyframes floatBalloons {
        0% { transform: translate(-50%, -50%) scale(1); }
        25% { transform: translate(-50%, -60%) scale(1.1); }
        50% { transform: translate(-50%, -50%) scale(1); }
        75% { transform: translate(-50%, -40%) scale(1.1); }
        100% { transform: translate(-50%, -50%) scale(1); }
    }
    </style>
            
""", unsafe_allow_html=True)
#page title

st.title("🧩The Great Escape: A Mystery Adventure")

# Game functions
def intro():
    st.markdown('<p class="fade-in">You wake up in a strange room, surrounded by dim light. There\'s a bed and a locked door in front of you.</p>', unsafe_allow_html=True)
    st.markdown('<p class="fade-in">You don\'t remember how you got here, but you need to escape.</p>', unsafe_allow_html=True)

    if st.button("Search the room"):
        st.session_state.step = 'search_room'
    elif st.button("Try the door"):
        st.session_state.step = 'try_door'

def search_room():
    st.markdown('<p class="fade-in">You find a desk with a drawer, a high window, and a rug covering something.</p>', unsafe_allow_html=True)

    if st.button("Check the drawer"):
        st.session_state.step = 'drawer'
    elif st.button("Lift the rug"):
        st.session_state.step = 'rug'
    elif st.button("Look out the window"):
        st.session_state.step = 'window'

def drawer():
    st.markdown('<p class="fade-in">The drawer contains a rusty key and a note: "The key unlocks the door, but only if you choose wisely."</p>', unsafe_allow_html=True)
    
    if st.button("Take the key"):
        st.session_state.step = 'try_door_key'
    elif st.button("Leave it"):
        st.session_state.step = 'search_room'

def rug():
    st.markdown('<p class="fade-in">You lift the rug and find a trapdoor leading underground.</p>', unsafe_allow_html=True)
    
    if st.button("Open the trapdoor"):
        st.session_state.step = 'underground_path'
    elif st.button("Leave it closed"):
        st.session_state.step = 'search_room'

def window():
    st.markdown('<p class="fade-in">The window is too high, but you spot a tree outside.</p>', unsafe_allow_html=True)
    
    if st.button("Climb the tree"):
        st.markdown('<p class="fade-in">You escape by climbing down the tree!</p>', unsafe_allow_html=True)
        st.session_state.step = 'win'
    elif st.button("Leave the window alone"):
        st.session_state.step = 'search_room'

def try_door():
    st.markdown('<p class="fade-in">You try the door. It\'s locked!</p>', unsafe_allow_html=True)
    
    if st.button("Search the room again"):
        st.session_state.step = 'search_room'
    elif st.button("Look for another way out"):
        st.session_state.step = 'search_room'

def try_door_key():
    st.markdown('<p class="fade-in">You unlock the door and step into a dark hallway.</p>', unsafe_allow_html=True)
    if st.button("Go down the hallway"):
        st.session_state.step = 'hallway'

def underground_path():
    st.markdown('<p class="fade-in">The underground passage is dark and narrow.</p>', unsafe_allow_html=True)
    
    if st.button("Continue down the passage"):
        st.session_state.step = 'underground_continue'
    elif st.button("Go back"):
        st.session_state.step = 'search_room'

def underground_continue():
    st.markdown('<p class="fade-in">You find an underground river and escape to freedom!</p>', unsafe_allow_html=True)
    st.session_state.step = 'win'

def hallway():
    st.markdown('<p class="fade-in">The hallway has two doors, one on the left and one on the right.</p>', unsafe_allow_html=True)
    
    if st.button("Go left"):
        st.session_state.step = 'left_room'
    elif st.button("Go right"):
        st.session_state.step = 'right_room'

def left_room():
    st.markdown('<p class="fade-in">You find a book of spells on a shelf.</p>', unsafe_allow_html=True)
    
    if st.button("Read the book"):
        st.session_state.step = 'spellbook'
    elif st.button("Leave the book"):
        st.session_state.step = 'trap'

def right_room():
    st.markdown('<p class="fade-in">You find a glowing portal in the center of the room.</p>', unsafe_allow_html=True)
    
    if st.button("Step into the portal"):
        st.session_state.step = 'portal'
    elif st.button("Leave the room"):
        st.session_state.step = 'hallway'

def spellbook():
    st.markdown('<p class="fade-in">You read the book and learn a powerful spell to escape! You win!</p>', unsafe_allow_html=True)
    st.balloons()
    st.session_state.step = 'win'

def portal():
    st.markdown('<p class="fade-in">You step into the portal and are transported to a new world. Congratulations, you’ve found freedom!</p>', unsafe_allow_html=True)
    st.balloons()
    st.session_state.step = 'win'

def trap():
    st.markdown('<p class="fade-in">You leave the book and explore more. Unfortunately, a trap is triggered, and you fall into a pit.</p>', unsafe_allow_html=True)
    st.session_state.step = 'lose'

def win():
    st.markdown('<p class="fade-in">🎉 Congratulations! You\'ve escaped to freedom! 🎉</p>', unsafe_allow_html=True)
    st.balloons() 
    st.markdown('<div class="balloon"></div>', unsafe_allow_html=True)  # Add a floating balloon
    
    if st.button("Play Again"):
        reset_game()

def lose():
    st.markdown('<p class="fade-in">You lost! Try again.</p>', unsafe_allow_html=True)
    if st.button("Play Again"):
        reset_game()

def reset_game():
    st.session_state.step = 'intro'

# Main game loop
if st.session_state.step == 'intro':
    intro()
elif st.session_state.step == 'search_room':
    search_room()
elif st.session_state.step == 'drawer':
    drawer()
elif st.session_state.step == 'rug':
    rug()
elif st.session_state.step == 'window':
    window()
elif st.session_state.step == 'try_door':
    try_door()
elif st.session_state.step == 'try_door_key':
    try_door_key()
elif st.session_state.step == 'underground_path':
    underground_path()
elif st.session_state.step == 'underground_continue':
    underground_continue()
elif st.session_state.step == 'hallway':
    hallway()
elif st.session_state.step == 'left_room':
    left_room()
elif st.session_state.step == 'right_room':
    right_room()
elif st.session_state.step == 'spellbook':
    spellbook()
elif st.session_state.step == 'portal':
    portal()
elif st.session_state.step == 'trap':
    trap()
elif st.session_state.step == 'win':
    win()
elif st.session_state.step == 'lose':
    lose()
