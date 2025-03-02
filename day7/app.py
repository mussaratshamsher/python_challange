import streamlit as st

# Initialize session state if tasks_list doesn't exist
if "tasks_list" not in st.session_state:
    st.session_state.tasks_list = []

# Function to add a task
def add_task(task):
    st.session_state.tasks_list.append(task)

# Function to delete a task
def delete_task(task_index):
    del st.session_state.tasks_list[task_index]

# Streamlit UI layout
st.set_page_config(page_title="To-Do List App", page_icon="📝", layout="centered")

# Add a custom header with a style
st.markdown("""
    <style>
        .header {font-size: 48px; font-weight: bold; color:rgb(205, 130, 11); text-align: center;}
        .button {font-size: 16px; background-color: #1abc9c; color: white; border-radius: 8px; padding: 10px 20px;}
        .task {background-color:rgb(12, 160, 131); color: white; padding: 15px; border-radius: 10px;
         margin: 5px 0; font-size: 18px; transition: transform 0.3s; box-shadow: 0px 0px 10px rgb(132, 239, 218);}
        .task:hover {background-color: #1abc9c; box-shadow: 0px 0px 20px rgb(117, 219, 199);}
        .task-btn {background-color:rgb(12, 160, 131); color: white; border-radius: 5px; padding: 8px 16px; font-size: 14px; transition: background-color 0.3s;}
        .task-btn:hover {background-color: #1abc9c; }
        .add-btn {background-color: #3498db; color: white; border-radius: 8px; padding: 10px 20px; font-size: 18px; transition: background-color 0.3s;}
        .add-btn:hover {background-color: #2980b9;}
        .exit-btn {background-color: #e67e22; color: white; border-radius: 8px; padding: 10px 20px; font-size: 18px; transition: background-color 0.3s;}
        .exit-btn:hover {background-color: #d35400;}
    </style>
""", unsafe_allow_html=True)

# Header Section
st.markdown('<p class="header">✍📜To-Do List App</p>', unsafe_allow_html=True)

# Display current tasks
if len(st.session_state.tasks_list) > 0:
    st.subheader("Current Tasks:")

    # Create columns for task display (two columns: task and delete button)
    for idx, task in enumerate(st.session_state.tasks_list):
        col1, col2 = st.columns([5, 1])
        with col1:
            st.markdown(f'<div class="task">{task}</div>', unsafe_allow_html=True)
        with col2:
            delete_button = st.button(f"Delete", key=f"delete_{idx}", 
            help="Delete this task", use_container_width=True)
            if delete_button:
                delete_task(idx)
                st.rerun()  # Refresh the app to reflect changes
else:
    st.write("👉 No tasks available. Add some tasks!")

# Input field to add a new task
new_task = st.text_input("✍ Add a new task:", placeholder="Enter task here..." )

# Create a row with two columns for Add Task and Exit buttons
col1, col2 = st.columns([1, 1])

with col1:
    if st.button("Add Task", help="Click to add a new task", use_container_width=True, key="add_task"):
        if new_task:
            add_task(new_task)
            st.rerun()  # Refresh the app to show the new task
        else:
            st.warning("📝Please enter a task before adding!")

with col2:
    if st.button("⬅Exit", help="Exit the app", use_container_width=True, key="exit"):
        st.write("💫Exiting... Have a productive day! 👋")
        st.stop()
