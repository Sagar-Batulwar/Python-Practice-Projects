#to do list
def main():
    tasks = []
    while True:
        print("==== To-Do list ====")
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Mark Task As Done")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if (choice == "1"):
            print()
            n_tasks = int(input("How many tasks you want to add : "))

            for i in range(n_tasks):
                task = input("Enter the task: ")
                tasks.append({"task" : task, "done" : False})
                print("Task added!")

        elif (choice == "2"):
            print("Tasks :")
            for index, task in enumerate(tasks):
                status ="Done" if task["done"] else "Not Done"
                print(f"{index + 1}. {task['task']} - {status}")

        elif (choice == "3"):
            task_index = int(input("Enter the number to mark as done: "))
            if 0 <= task_index < len(tasks):
                tasks[task_index]["done"] = True
                print("Task marked as done!")
            else:
                print("Invalid task number.")

        elif (choice == "4"):
            print("exiting the TO-Do list.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__=="__main__":
    main()