task_list_1 = []
task_list_2 = []
task_list_3 = []
removed_tasks = []


def high_priority():
    task = input("Enter the task: ")
    task_list_1.append(task)
    print(f"{task} is added.")


def medium_priority():
    task = input("Enter the task: ")
    task_list_2.append(task)
    print(f"{task} is added.")


def low_priority():
    task = input("Enter the task: ")
    task_list_3.append(task)
    print(f"{task} is added.")


def remove_task():
    task = input("Enter the task to be removed: ")
    removed_tasks.append(task)
    if task in task_list_1:
        task_list_1.remove(task)
        print(f"Task {task} is removed.")
    elif task in task_list_2:
        task_list_2.remove(task)
        print(f"Task {task} is removed.")
    elif task in task_list_3:
        task_list_3.remove(task)
        print(f"Task {task} is removed.")
    else:
        print("To do list is empty")


def view_tasks():
    print(len(task_list_1))
    if len(task_list_1) == 0 and len(task_list_2) == 0 and len(task_list_3) == 0:
        print("Todo list is empty!")
    else:
        if len(task_list_1) != 0:
            print("High priority tasks:")
            for tasks in range(len(task_list_1)):
                print(task_list_1[tasks])
        if len(task_list_2) != 0:
            print("Medium priority tasks:")
            for tasks in range(len(task_list_1)):
                print(task_list_2[tasks])
        if len(task_list_3) != 0:
            print("Low priority tasks:")
            for tasks in range(len(task_list_1)):
                print(task_list_3[tasks])
        print("Tasks that you have removed:")
        for tasks in removed_tasks:
            print(removed_tasks[tasks])


while True:
    print("1:Add Task\n2:Remove Tasks\n3:View Tasks\n4:Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        print("1:High priority\n2:Medium priority\n3:Low priority")
        priority = int(input("Enter the priority: "))
        if priority == 1:
            high_priority()
        elif priority == 2:
            medium_priority()
        else:
            low_priority()
    elif choice == 2:
        remove_task()
    elif choice == 3:
        view_tasks()
    elif choice == 4:
        exit()
    else:
        print("Enter valid input!")
