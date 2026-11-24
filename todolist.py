
# Project 4: To-Do List Application

tasks = []


def add_task():
    task_name = input("Enter task: ").strip()

    if not task_name:
        print("Task cannot be empty!")
        return

    task = {
        "name": task_name,
        "completed": False
    }

    tasks.append(task)
    print("Task added successfully!")


def view_tasks():
    if not tasks:
        print("No tasks available!")
        return

    print("\n===== YOUR TASKS =====")

    for index, task in enumerate(tasks, start=1):
        status = "Done" if task["completed"] else "Pending"

        print(f"{index}. {task['name']} [{status}]")


def update_task():
    view_tasks()

    if not tasks:
        return

    try:
        number = int(input("Enter task number to update: "))

        if 1 <= number <= len(tasks):
            new_name = input("Enter new task name: ").strip()

            if new_name:
                tasks[number - 1]["name"] = new_name
                print("Task updated successfully!")
            else:
                print("Task name cannot be empty!")
        else:
            print("Invalid task number!")

    except ValueError:
        print("Please enter a valid number!")


def complete_task():
    view_tasks()

    if not tasks:
        return

    try:
        number = int(input("Enter task number to complete: "))

        if 1 <= number <= len(tasks):
            tasks[number - 1]["completed"] = True
            print("Task marked as completed!")
        else:
            print("Invalid task number!")

    except ValueError:
        print("Please enter a valid number!")


def delete_task():
    view_tasks()

    if not tasks:
        return

    try:
        number = int(input("Enter task number to delete: "))

        if 1 <= number <= len(tasks):
            removed = tasks.pop(number - 1)
            print(f"Deleted: {removed['name']}")
        else:
            print("Invalid task number!")

    except ValueError:
        print("Please enter a valid number!")


def main():
    while True:
        print("\n===== TO-DO LIST =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Complete Task")
        print("5. Delete Task")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            add_task()

        elif choice == "2":
            view_tasks()

        elif choice == "3":
            update_task()

        elif choice == "4":
            complete_task()

        elif choice == "5":
            delete_task()

        elif choice == "6":
            print("Thank you for using To-Do List!")
            break

        else:
            print("Invalid choice! Try again.")


if __name__ == "__main__":
    main()
