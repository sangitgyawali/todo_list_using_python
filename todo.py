import os

FILENAME = 'tasks.txt'

def load_tasks():
    if not os.path.exists(FILENAME):
        return []
    with open(FILENAME, 'r') as file:
        return [line.strip() for line in file.readlines()]
    
def save_tasks(tasks):
    with open(FILENAME, 'w') as file:
        for task in tasks:
            file.write(task + '\n')

def show_tasks(tasks):
    if not tasks:
        print("No tasks available.")
    else:
        print("Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
        print()

def main():
    tasks = load_tasks()
    
    while True:
        print("Todo List")
        print("1. Show tasks")
        print("2. Add task")
        print("3. Remove task")
        print("4. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            show_tasks(tasks)
        elif choice == '2':
            task = input("Enter a new task: ")
            tasks.append(task)
            save_tasks(tasks)
            print(f"Task '{task}' added.\n")
        elif choice == '3':
            show_tasks(tasks)
            if tasks:
                try:
                    index = int(input("Enter the task number to remove: ")) - 1
                    if 0 <= index < len(tasks):
                        removed_task = tasks.pop(index)
                        save_tasks(tasks)
                        print(f"Task '{removed_task}' removed.\n")
                    else:
                        print("Invalid task number.\n")
                except ValueError:
                    print("Please enter a valid number.\n")
        elif choice == '4':
            break
        else:
            print("Invalid option, please try again.\n")

if __name__ == "__main__":
    main()