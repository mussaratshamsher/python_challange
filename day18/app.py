import tkinter as tk

def add_task():
    task = task_entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
        save_tasks()

def delete_task():
    try:
        selected_task_index = task_listbox.curselection()
        task_listbox.delete(selected_task_index)
        save_tasks()
    except IndexError:
        pass

def mark_completed(event):
    selected_task_index = task_listbox.curselection()
    if selected_task_index:
        task = task_listbox.get(selected_task_index)
        # Strike-through or change color
        task_listbox.itemconfig(selected_task_index, {'fg': 'gray', 'font': ('Arial', 10, 'italic')})
        task_listbox.insert(selected_task_index, f"✔ {task}")
        save_tasks()

def save_tasks():
    with open('tasks.txt', 'w') as file:
        for task in task_listbox.get(0, tk.END):
            file.write(task + '\n')

def load_tasks():
    try:
        with open('tasks.txt', 'r') as file:
            for line in file:
                task_listbox.insert(tk.END, line.strip())
    except FileNotFoundError:
        pass

# Set up the main window
root = tk.Tk()
root.title("To-Do List App")

# UI Components
task_entry = tk.Entry(root, width=40)
task_entry.pack(pady=10)
tk.Button(root, text="Add Task", width=20, command=add_task).pack()
task_listbox = tk.Listbox(root, width=40, height=10)
task_listbox.pack(pady=10)
tk.Button(root, text="Delete Task", width=20, command=delete_task).pack()

task_listbox.bind("<Double-1>", mark_completed)

# Load tasks on start
load_tasks()

# Start the app
root.mainloop()
