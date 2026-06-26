# 3)	Build a to-do list manager that
# •	Allows users to add tasks with priorities (e.g., "Buy milk - high").
# •	Lets them view the current list, delete tasks by number, and mark tasks as complete.
# •	Keeps looping until the user types "exit".
# •	Shows a summary at the end: number of completed tasks vs pending.

tasks = []

while True:
    print("\n--- TO-DO LIST MANAGER ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Complete Task")
    print("Type 'exit' to quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task_name = input("Enter task name: ")
        priority = input("Enter priority (high, medium, low): ")

        task = {
            "name": task_name,
            "priority": priority,
            "completed": False
        }

        tasks.append(task)
        print("Task added successfully!")

    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            print("\nCurrent Tasks:")
            for i, task in enumerate(tasks, start=1):
                status = "Completed" if task["completed"] else "Pending"
                print(f"{i}. {task['name']} | Priority: {task['priority']} | Status: {status}")

    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks to delete.")
        else:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task['name']}")

            try:
                task_num = int(input("Enter task number to delete: "))
                if 1 <= task_num <= len(tasks):
                    removed_task = tasks.pop(task_num - 1)
                    print(f"Deleted: {removed_task['name']}")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

    elif choice == "4":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task['name']}")

            try:
                task_num = int(input("Enter task number to mark complete: "))
                if 1 <= task_num <= len(tasks):
                    tasks[task_num - 1]["completed"] = True
                    print("Task marked as complete!")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

    elif choice == "5" or choice.lower() == "exit":
        break

    else:
        print("Invalid option. Try again.")

completed_count = 0
pending_count = 0

for task in tasks:
    if task["completed"]:
        completed_count += 1
    else:
        pending_count += 1

print("\n--- Summary ---")
print(f"Completed Tasks: {completed_count}")
print(f"Pending Tasks: {pending_count}")
print(f"Total Tasks: {len(tasks)}")