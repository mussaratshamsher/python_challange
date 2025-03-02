import streamlit as st
import pandas as pd
import os

# File to store tasks (CSV format)
TASKS_FILE = "tasks.csv"

# Function to load tasks from a file
def load_tasks():
    if os.path.exists(TASKS_FILE):
        return pd.read_csv(TASKS_FILE)
    else:
        return pd.DataFrame(columns=["Task"])

# Function to save tasks to the file
def save_tasks(tasks_df):
    tasks_df.to_csv(TASKS_FILE, index=False)

# Function to add a task
def add_task(task):
    tasks_df = load_tasks()
    # Use pd.concat to add a new task as a new row to the DataFrame
    new_task_df = pd.DataFrame({"Task": [task]})
    tasks_df = pd.concat([tasks_df, new_task_df], ignore_index=True)
    save_tasks(tasks_df)

# Function to delete a task
def delete_task(task_index):
    tasks_df = load_tasks()
    tasks_df = tasks_df.drop(task_index)
    save_tasks(tasks_df)

# Streamlit UI layout
st.set_page_config(page_title="To-Do List App", page_icon="📝", layout="wide")

# Add a custom header with a style
st.markdown("""
    <style>
        .header {font-size: 40px; font-weight: bold; color: #f39c12;}
        .button {font-size: 16px; background-color: #1abc9c; color: white; border-radius: 5px;}
        .task {background-color: #34495e; color: white; padding: 10px; border-radius: 5px;}
        .task-btn {background-color: #e74c3c; color: white; border-radius: 5px;}
        .task-list {padding-left: 0px; margin-top: 15px;}
    </style>
""", unsafe_allow_html=True)

# Header Section
st.markdown('<p class="header">To-Do List App</p>', unsafe_allow_html=True)

# Load tasks
tasks_df = load_tasks()

# Show tasks if available
if len(tasks_df) > 0:
    st.subheader("Current Tasks:")

    # Create columns for task display (two columns: task and delete button)
    for idx, task in tasks_df.iterrows():
        task_id = task.name  # Get the task's index

        # Layout: Task and a Delete button
        col1, col2 = st.columns([5, 1])
        with col1:
            st.markdown(f'<div class="task">{task["Task"]}</div>', unsafe_allow_html=True)
        with col2:
            # Delete button
            delete_button = st.button(f"Delete", key=f"delete_{task_id}", help="Delete this task", use_container_width=True)
            if delete_button:
                delete_task(task_id)
                st.rerun()  # Refresh the app to reflect changes

else:
    st.write("No tasks available. Add some tasks!")

# Input field to add a new task
new_task = st.text_input("Add a new task:", placeholder="Enter task here...")

if st.button("Add Task", help="Click to add a new task", use_container_width=True):
    if new_task:
        add_task(new_task)
        st.rerun()  # Refresh the app to show the new task
    else:
        st.warning("Please enter a task before adding!")

# Option to Exit the app (simple exit message)
if st.button("Exit", help="Exit the app", use_container_width=True):
    st.write("Exiting... Have a productive day! 👋")
    st.stop()
