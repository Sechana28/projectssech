class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({'task': task, 'completed': False})

    def mark_completed(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]['completed'] = True
        else:
            print("Invalid task index")

    def update_task(self, index, new_description):
        if 0 <= index < len(self.tasks):
            self.tasks[index]['task'] = new_description
        else:
            print("Invalid task index")

    def remove_task(self,index , task):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
        else:
            print("Invalid task index")

    def display_tasks(self):
        for i, task in enumerate(self.tasks):
            status = "Completed" if task['completed'] else "Not Completed"
            print(f"{i + 1}.{task['task']}-{status}")


def main():
    todo_list = ToDoList()

    while True:
        print("\n1. Add Task")
        print("2. Mark Task as Completed")
        print("3. Update Task Description")
        print("4. Remove Tasks")
        print("5. Display Tasks")
        print("6. Exit")

        choice = input("Enter your choice:")

        if choice == '1':
            task = input("enter the task description:")
            todo_list.add_task(task)
        elif choice == '2':
            index = int(input("enter the task number to mark as completed:")) - 1
            todo_list.mark_completed(index)
        elif choice == '3':
            index = int(input("enter the task number to update:")) - 1
            new_description = input("enter the new description:")
            todo_list.update_task(index, new_description)
        elif choice == '4':
            index = int(input("enter the task number to remove:")) - 1
            todo_list.remove_task(index)
        elif choice == '5':
            todo_list.display_tasks()
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "_main_":
    main()