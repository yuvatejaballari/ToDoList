class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print("Task '{}' added successfully!".format(task))

    def complete_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            print("Task '{}' completed!".format(task))
        else:
            print("Task '{}' not found!".format(task))

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            print("Task '{}' removed successfully!".format(task))
        else:
            print("Task '{}' not found!".format(task))

    def display_tasks(self):
        if self.tasks:
            print("Tasks:")
            for index, task in enumerate(self.tasks, start=1):
                print("{}. {}".format(index, task))
        else:
            print("No tasks found!")

def main():
    manager = TaskManager()
    while True:
        print("\nTask Manager")
        print("1. Add Task")
        print("2. Complete Task")
        print("3. Remove Task")
        print("4. Display Tasks")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter task: ")
            manager.add_task(task)
        elif choice == '2':
            task = input("Enter task to complete: ")
            manager.complete_task(task)
        elif choice == '3':
            task = input("Enter task to remove: ")
            manager.remove_task(task)
        elif choice == '4':
            manager.display_tasks()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
