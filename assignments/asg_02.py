# Utilize if else while and for loop to create a program covering all the concepts.

tasks = []  # list to store tasks

while True:
    print("\nTo-Do List Manager")
    print("1. Add a Task")
    print("2. View Tasks")
    print("3. Remove a Task")
    print("4. Exit")
    
    choice = int(input("Choose an option (1-4): "))
    
    if choice == 1:  # add a task
        task = input("Enter the task: ")
        tasks.append(task)
        print("Task added successfully.")
    elif choice == 2:  # view all tasks
        print("\nYour Tasks:")
        if tasks:
            for i in range(0, len(tasks)):
                print(i + 1, tasks[i])
        else:
            print("No .. Tasks")

