tasks_list = []

def add(task):
    if task.lower() not in (t.lower() for t in tasks_list):
        tasks_list.append(task)
        print(f"'{task}' added to the list.")
    else:
        print(f"'{task}' is already in the list.")

def display_list():
    if not tasks_list:
        print("Your list is empty.")
    else:
        print("Your task list:")
        for index, task in enumerate(tasks_list, start=1):
            print(f"{index}. {task}")

def check(task):
    if task.lower() in (t.lower() for t in tasks_list):
        print(f"Yes, '{task}' is on the list.")
    else:
        print(f"No, '{task}' is not on the list.")

def remove(task):
    if task.lower() in (t.lower() for t in tasks_list):
        tasks_list.remove(task)
        print(f"'{task}' has been removed.")
    else:
        print(f"'{task}' is not on the list.")

while True:
    print("\n1. Add a task\n2. Display your list\n3. Check if a task is on the list\n4. Remove a task\n5. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        task_name = input("Enter the task: ")
        add(task_name)
    elif choice == "2":
        display_list()
    elif choice == "3":
        task_to_check = input("Enter the task to check: ")
        check(task_to_check)
    elif choice == "4":
        task_to_remove = input("Enter the task to remove: ")
        remove(task_to_remove)
    elif choice == "5":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 5.")
