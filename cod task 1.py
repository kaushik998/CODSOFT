import tkinter as tk
from tkinter import messagebox
import os
class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To Do List")
        self.root.geometry("300x550")
        self.root.resizable(False, False)
        self.task_lists = []
        self.create_widgets()
        self.load_tasks()
    def create_widgets(self):
        heading = tk.Frame(self.root, width=400, height=50, bg="blue")
        heading.pack()
        tk.Label(self.root, text="ADD TASK", font=("Arial Bold", 18), bg="yellow", fg="red").place(x=75, y=5)
        frame = tk.Frame(self.root, width=300, height=48, bg="white")
        frame.place(x=0, y=100)
        self.task_entry = tk.Entry(frame, width=18, font="Arial 20", bd=0)
        self.task_entry.place(x=10, y=7)
        self.task_entry.focus()
        tk.Button(frame, text="Add", font="Arial 20 bold", width=6, bg="green", fg="white", bd=0, command=self.add_task).place(x=200, y=0)
        lb = tk.Frame(self.root, bd=3, width=700, height=280, bg="blue")
        lb.pack(pady=(100, 0))
        self.box = tk.Listbox(lb, font=("Arial", 12), width=40, height=16, bg="blue", fg="white", cursor="hand2", selectbackground="white")
        scroll = tk.Scrollbar(lb)
        self.box.config(yscrollcommand=scroll.set)
        scroll.pack(side=tk.RIGHT, fill=tk.BOTH)
        self.box.pack(side=tk.LEFT, fill=tk.BOTH, padx=2)
        tk.Button(self.root, text="Delete", font=("Arial Bold", 15), width=6, bg="blue", fg="white", command=self.delete_task).pack(pady=(15, 0))
    def load_tasks(self):
        if os.path.exists("taskfile.txt"):
            with open("taskfile.txt", "r") as taskfile:
                tasks = taskfile.readlines()
            for task in tasks:
                task = task.strip()
                if task:
                    self.task_lists.append(task)
                    self.box.insert(tk.END, task)
    def add_task(self):
        task = self.task_entry.get().strip()
        self.task_entry.delete(0, tk.END)
        if task:
            with open("taskfile.txt", "a") as taskfile:
                taskfile.write(f"{task}\n")
            self.task_lists.append(task)
            self.box.insert(tk.END, task)
    def delete_task(self):
        selected_task_index = self.box.curselection()
        if selected_task_index:
            task = self.box.get(selected_task_index)
            if messagebox.askyesno("Delete Task", f"Are you sure you want to delete '{task}'?"):
                self.task_lists.remove(task)
                with open("taskfile.txt", "w") as taskfile:
                    for task in self.task_lists:
                        taskfile.write(f"{task}\n")
                self.box.delete(selected_task_index)
if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
