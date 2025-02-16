# code logic
#user will add tasks to the list.#
# The user will remove tasks from the list by specifying the task number.
#The user can view all tasks in the list.
#The app will run in a loop until the user decides to exit.



#add display, add, remove and view task

def display_menu():
    print('\n Task Manager')
    print('1. Add Task')
    print('2. Remove Task')
    print('3. View Task')
    print('4. Exit')

def add_task(tasks):
    task = input('Please enter the task you want to add: ')
    tasks.append(task)
    print(f'{task} has been successfully added to you list.')

def remove_task(tasks):
    if not tasks:
        print('No tasks to remove.')
        return

    for i, task in enumerate(tasks, start=1):
        print(f'{i}. {task}')

    try:
        task_number = int(input('Please enter the task you want to remove: '))
        if 1 <= task_number <= len(tasks):
            removed_task = tasks.pop(task_number - 1)
            print(f'{removed_task} removed successfully.')
        else:
            print('INVALID task number.')

    except ValueError:
        print('Please enter a valid number.')



def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
    else:
        print("Your Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")



def main():
    tasks = []

    while True:
        display_menu()
        your_choice = input("Please enter the operation you want... : ")

        if your_choice == '1':
            add_task(tasks)
        elif your_choice == '2':
            remove_task(tasks)
        elif your_choice == '3':
            view_tasks(tasks)
        elif your_choice == '4':
            print("Thank you for using the Task Manager. Goodbye!!!!!")
            break
        else:
            print("Invalid choice. Please choose a number between 1 and 4.")


if __name__ == "__main__":
    main()





