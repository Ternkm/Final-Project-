import tkinter as tk
from tkinter import messagebox

class Task:
    def __init__(self, subject, description, due_date):
        self.subject = subject
        self.description = description
        self.due_date = due_date

class PriorityQueue:
    def __init__(self):
        self.tasks = []

    def enqueue(self, task):
        self.tasks.append(task)
        self.tasks.sort(key=lambda x: x.due_date)

    def dequeue(self):
        if self.is_empty():
            return None
        return self.tasks.pop(0)

    def is_empty(self):
        return len(self.tasks) == 0

class BinarySearchTree:
    class Node:
        def __init__(self, task):
            self.task = task
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None

    def insert(self, task):
        if not self.root:
            self.root = self.Node(task)
        else:
            self._insert_recursive(task, self.root)

    def _insert_recursive(self, task, current_node):
        if task.subject < current_node.task.subject:
            if current_node.left:
                self._insert_recursive(task, current_node.left)
            else:
                current_node.left = self.Node(task)
        elif task.subject > current_node.task.subject:
            if current_node.right:
                self._insert_recursive(task, current_node.right)
            else:
                current_node.right = self.Node(task)
        else:
            pass

    def search(self, subject):
        return self._search_recursive(subject, self.root)

    def _search_recursive(self, subject, current_node):
        if not current_node:
            return None
        if subject == current_node.task.subject:
            return current_node.task
        elif subject < current_node.task.subject:
            return self._search_recursive(subject, current_node.left)
        else:
            return self._search_recursive(subject, current_node.right)

class HomeworkManagerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Homework Manager")

        # Create priority queue and binary search tree
        self.priority_queue = PriorityQueue()
        self.binary_search_tree = BinarySearchTree()

        # Add Task Frame
        self.add_task_frame = tk.Frame(self.root)
        self.add_task_frame.pack(padx=10, pady=10)

        tk.Label(self.add_task_frame, text="Subject:").grid(row=0, column=0, padx=5, pady=5)
        self.subject_entry = tk.Entry(self.add_task_frame)
        self.subject_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self.add_task_frame, text="Description:").grid(row=1, column=0, padx=5, pady=5)
        self.description_entry = tk.Entry(self.add_task_frame)
        self.description_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(self.add_task_frame, text="Due Date (YYYY-MM-DD):").grid(row=2, column=0, padx=5, pady=5)
        self.due_date_entry = tk.Entry(self.add_task_frame)
        self.due_date_entry.grid(row=2, column=1, padx=5, pady=5)

        self.add_task_button = tk.Button(self.add_task_frame, text="Add Task", command=self.add_task)
        self.add_task_button.grid(row=3, columnspan=2, padx=5, pady=5)

        # View Task Frame
        self.view_task_frame = tk.Frame(self.root)
        self.view_task_frame.pack(padx=10, pady=10)

        tk.Label(self.view_task_frame, text="Enter Subject to View Tasks:").grid(row=0, column=0, padx=5, pady=5)
        self.view_subject_entry = tk.Entry(self.view_task_frame)
        self.view_subject_entry.grid(row=0, column=1, padx=5, pady=5)

        self.view_task_button = tk.Button(self.view_task_frame, text="View Tasks", command=self.view_tasks)
        self.view_task_button.grid(row=1, columnspan=2, padx=5, pady=5)

        # View Next Task Due Frame
        self.view_next_task_frame = tk.Frame(self.root)
        self.view_next_task_frame.pack(padx=10, pady=10)

        self.view_next_task_button = tk.Button(self.view_next_task_frame, text="View Next Task Due", command=self.view_next_task)
        self.view_next_task_button.pack(padx=5, pady=5)

    def add_task(self):
        subject = self.subject_entry.get()
        description = self.description_entry.get()
        due_date = self.due_date_entry.get()

        if subject and description and due_date:
            task = Task(subject, description, due_date)
            self.priority_queue.enqueue(task)
            self.binary_search_tree.insert(task)
            messagebox.showinfo("Success", "Task added successfully!")
            # Clear entry fields
            self.subject_entry.delete(0, tk.END)
            self.description_entry.delete(0, tk.END)
            self.due_date_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Please fill in all fields.")

    def view_tasks(self):
        subject = self.view_subject_entry.get()
        if subject:
            task = self.binary_search_tree.search(subject)
            if task:
                messagebox.showinfo("Tasks", f"Subject: {task.subject}\nDescription: {task.description}\nDue Date: {task.due_date}")
            else:
                messagebox.showwarning("Warning", f"No tasks found for subject: {subject}")
        else:
            messagebox.showerror("Error", "Please enter a subject.")

    def view_next_task(self):
        next_task = self.priority_queue.dequeue()
        if next_task:
            messagebox.showinfo("Next Task Due", f"Description: {next_task.description}\nDue Date: {next_task.due_date}")
        else:
            messagebox.showwarning("Warning", "No tasks in queue.")

if __name__ == "__main__":
    root = tk.Tk()
    app = HomeworkManagerGUI(root)
    root.mainloop()

class Task:
    def __init__(self, subject, description, due_date):
        self.subject = subject
        self.description = description
        self.due_date = due_date

class PriorityQueue:
    def __init__(self):
        self.tasks = []

    def enqueue(self, task):
        # Add a task to the priority queue and sort tasks by due date
        self.tasks.append(task)
        self.tasks.sort(key=lambda x: x.due_date)

    def dequeue(self):
        # Remove and return the task with the earliest due date
        if self.is_empty():
            return None
        return self.tasks.pop(0)

    def is_empty(self):
        # Check if the priority queue is empty
        return len(self.tasks) == 0

class BinarySearchTree:
    class Node:
        def __init__(self, task):
            self.task = task
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None

    def insert(self, task):
        # Insert a task into the binary search tree
        if not self.root:
            self.root = self.Node(task)
        else:
            self._insert_recursive(task, self.root)

    def _insert_recursive(self, task, current_node):
        # Helper function for recursive insertion
        if task.subject < current_node.task.subject:
            if current_node.left:
                self._insert_recursive(task, current_node.left)
            else:
                current_node.left = self.Node(task)
        elif task.subject > current_node.task.subject:
            if current_node.right:
                self._insert_recursive(task, current_node.right)
            else:
                current_node.right = self.Node(task)
        else:
            # Handle duplicate subjects
            pass

    def search(self, subject):
        # Search for a task by subject in the binary search tree
        return self._search_recursive(subject, self.root)

    def _search_recursive(self, subject, current_node):
        # Helper function for recursive search
        if not current_node:
            return None
        if subject == current_node.task.subject:
            return current_node.task
        elif subject < current_node.task.subject:
            return self._search_recursive(subject, current_node.left)
        else:
            return self._search_recursive(subject, current_node.right)

# Command-line interface for testing
if __name__ == "__main__":
    # priority queue and binary search tree
    priority_queue = PriorityQueue()
    binary_search_tree = BinarySearchTree()

    while True:
        print("\nHomework Management Application")
        print("1. Add Task")
        print("2. View Tasks by Subject")
        print("3. View Next Task Due")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            # Add a new task
            subject = input("Enter subject: ")
            description = input("Enter task description: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            task = Task(subject, description, due_date)
            priority_queue.enqueue(task)
            binary_search_tree.insert(task)
            print("Task added successfully!")

        elif choice == "2":
            # View tasks by subject
            subject = input("Enter subject to view tasks: ")
            task = binary_search_tree.search(subject)
            if task:
                print("Tasks for subject", subject + ":")
                print(task.description, "-", task.due_date)
            else:
                print("No tasks found for subject", subject)

        elif choice == "3":
            # View next task due
            next_task = priority_queue.dequeue()
            if next_task:
                print("Next task due:", next_task.description, "-", next_task.due_date)
            else:
                print("No tasks in queue.")

        elif choice == "4":
            # Exit the application
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")



