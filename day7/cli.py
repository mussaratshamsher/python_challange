import os

# Initialize task list
tasks_list = []

# Function to add a task
def add_task(task):
    tasks_list.append(task)

# Function to delete a task
def delete_task(task_index):
    if 0 <= task_index < len(tasks_list):
        tasks_list.pop(task_index)

# Function to display tasks
def display_tasks():
    if tasks_list:
        print("\nCurrent Tasks:")
        for idx, task in enumerate(tasks_list):
            print(f"{idx + 1}. {task}")
    else:
        print("\n👉 No tasks available. Add some tasks!")

# Main loop for CLI interaction
def main():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen for better UX
        display_tasks()
        
        print("\nOptions:")
        print("1. Add a Task")
        print("2. Delete a Task")
        print("3. Exit")
        
        choice = input("Select an option (1/2/3): ")

        if choice == "1":
            new_task = input("Enter the task to add: ")
            if new_task:
                add_task(new_task)
            else:
                print("📝 Please enter a valid task!")
                input("Press Enter to continue...")

        elif choice == "2":
            try:
                task_number = int(input("Enter task number to delete: "))
                delete_task(task_number - 1)  # Adjust for 0-based index
            except (ValueError, IndexError):
                print("❌ Invalid task number!")
                input("Press Enter to continue...")
        
        elif choice == "3":
            print("💫 Exiting... Have a productive day! 👋")
            break
        
        else:
            print("❌ Invalid choice! Please choose again.")
            input("Press Enter to continue...")

if __name__ == "__main__":
    main()
