# Note if you  see idx and are confused it means index

class Task:
    def __init__(self, title: str):
        self.__title = title
        self.__is_completed = False

    # Creates two properties, one for the title one to check completion
    @property
    def title(self) -> str:
        return self.__title

    @property
    def is_completed(self) -> bool:
        return self.__is_completed

    # Sets the is completed property as true so t
    def mark_complete(self):
        self.__is_completed = True

    def __str__(self):
        status = "✓" if self.__is_completed else " "
        return f"[{status}] {self.__title}"


class TaskManager:
    def __init__(self):
        # Creates a new list to keep track of tasks
        self.__tasks = []

    def add_task(self, title: str):
        task = Task(title)
        self.__tasks.append(task)
        print(f"Task added: '{title}'")

    # We use this same system for the delete task
    def mark_complete(self, index: int):
        # Checks for a valid number
        if 0 <= index < len(self.__tasks):
            # Marks as True so it wont show in pending tasks
            self.__tasks[index].mark_complete()
            # Added 1 to start at one instead of zero
            print(f"Task {index + 1} marked as complete.")
        else:
            print("Invalid task number.")

    def delete_task(self, index: int):
        # Also checks for a valid number
        if 0 <= index < len(self.__tasks):
            removed = self.__tasks.pop(index)
            print(f"Deleted task: '{removed.title}'")
        else:
            print("Invalid task number.")

    def list_pending_tasks(self):
        print("\nPending Tasks")
        # Checks if t is false
        pending = [t for t in self.__tasks if not t.is_completed]
        if not pending:
            print("No pending tasks!")
        for idx, task in enumerate(self.__tasks):
            if not task.is_completed:
                print(f"{idx + 1}. {task}")

    def list_completed_tasks(self):
        print("\nCompleted Tasks")

        # Checks if t is True
        completed = [t for t in self.__tasks if t.is_completed]
        if not completed:
            print("No completed tasks yet!")
        for idx, task in enumerate(self.__tasks):
            if task.is_completed:
                print(f"{idx + 1}. {task}")

if __name__ == "__main__":
    manager = TaskManager()
    
    while True:
        print("\nTask Manager Menu: ")
        print("1. Add Task")
        print("2. Mark Task Complete")
        print("3. Delete Task")
        print("4. List Pending Tasks")
        print("5. List Completed Tasks")
        print("6. Exit")
        
        choice = input("Choose an option (1-6): ")
        
        if choice == "1":
            title = input("Enter task title: ")
            manager.add_task(title)
        elif choice == "2":
            manager.list_pending_tasks()
            try:
                idx = int(input("Enter task number to mark complete: ")) - 1
                manager.mark_complete(idx)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "3":
            try:
                idx = int(input("Enter task number to delete: ")) - 1
                manager.delete_task(idx)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "4":
            manager.list_pending_tasks()
        elif choice == "5":
            manager.list_completed_tasks()
        elif choice == "6":
            print("Exiting Task Manager")
            break
        else:
            print("Invalid choice. Please choose between 1 and 6.")