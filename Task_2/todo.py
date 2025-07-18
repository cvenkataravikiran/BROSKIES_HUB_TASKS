def display_menu():
    print("\n TO-DO LIST MENU ")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

def view_tasks(tasks):
    if len(tasks) == 0:
        print("You have no tasks yet.")
    else:
        print("\nYour Tasks:")
        for i in range(len(tasks)):
            print(f"{i+1}. {tasks[i]}")

def add_task(tasks):
    new_task = input("Enter a new task: ").strip()
    if new_task:
        tasks.append(new_task)
        print("Task added.")
    else:
        print("Empty task not added.")

def remove_task(tasks):
    view_tasks(tasks)
    if tasks:
        try:
            number = int(input("Enter task number to remove: "))
            if 1 <= number <= len(tasks):
                removed = tasks.pop(number - 1)
                print(f"Task '{removed}' removed.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

def main():
    tasks = []
    print("Welcome to Your To-Do List!")
    while True:
        display_menu()
        choice = input("Choose an option (1-4): ")
        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
