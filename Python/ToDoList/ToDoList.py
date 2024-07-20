import json

def create_task(task):
    """
    Creates a new task in the to-do list.
    """
    with open("todo.json", "r") as f:
        data = json.load(f)

    data["tasks"].append({"task": task, "completed": False})

    with open("todo.json", "w") as f:
        json.dump(data, f, indent=4)

def list_tasks():
    """
    Lists all tasks in the to-do list.
    """
    with open("todo.json", "r") as f:
        data = json.load(f)

    if data["tasks"]:
        for i, task in enumerate(data["tasks"]):
            status = "Completed" if task["completed"] else "Pending"
            print(f"{i+1}. {task['task']} - {status}")
    else:
        print("Your to-do list is empty.")

def mark_task_completed(task_index):
    """
    Marks a task as completed.
    """
    with open("todo.json", "r") as f:
        data = json.load(f)

    if 0 <= task_index < len(data["tasks"]):
        data["tasks"][task_index]["completed"] = True
        with open("todo.json", "w") as f:
            json.dump(data, f, indent=4)
        print("Task marked as completed.")
    else:
        print("Invalid task index.")

def remove_task(task_index):
    """
    Removes a task from the to-do list.
    """
    with open("todo.json", "r") as f:
        data = json.load(f)

    if 0 <= task_index < len(data["tasks"]):
        del data["tasks"][task_index]
        with open("todo.json", "w") as f:
            json.dump(data, f, indent=4)
        print("Task removed.")
    else:
        print("Invalid task index.")

def main():
    """
    Main function for the to-do list app.
    """
    try:
        with open("todo.json", "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {"tasks": []}
        with open("todo.json", "w") as f:
            json.dump(data, f, indent=4)

    while True:
        print("\nTo-Do List App")
        print("1. Create task")
        print("2. List tasks")
        print("3. Mark task as completed")
        print("4. Remove task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter task: ")
            create_task(task)
        elif choice == "2":
            list_tasks()
        elif choice == "3":
            task_index = int(input("Enter task index to mark as completed: ")) - 1
            mark_task_completed(task_index)
        elif choice == "4":
            task_index = int(input("Enter task index to remove: ")) - 1
            remove_task(task_index)
        elif choice == "5":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()