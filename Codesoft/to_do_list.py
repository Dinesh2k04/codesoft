import tkinter as tk
from tkinter import simpledialog, messagebox

def add_task():
    task = simpledialog.askstring("Add Task", "What task would you like to add?")
    if task is not None:
        listbox_tasks.insert(tk.END, task)

def remove_task():
    try:
        task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(task_index)
    except IndexError:
        messagebox.showerror("Sorry", "Please select a task to remove ")

def update_task():
    try:
        task_index = listbox_tasks.curselection()[0]
        task = listbox_tasks.get(task_index)
        new_task = simpledialog.askstring("Update Task", "Edit the task:", initialvalue=task)
        if new_task:
            listbox_tasks.delete(task_index)
            listbox_tasks.insert(task_index, new_task)
    except IndexError:
        messagebox.showerror("Sorry", "Please select a task to update ")

root = tk.Tk()
root.title("To-Do List")

listbox_tasks = tk.Listbox(root, height=20, width=50)
listbox_tasks.pack(pady=20)

button_add_task = tk.Button(root, text="Add Task", width=45, command=add_task)
button_add_task.pack(pady=10)

button_remove_task = tk.Button(root, text="Remove Task", width=45, command=remove_task)
button_remove_task.pack(pady=10)

button_update_task = tk.Button(root, text="Update Task", width=45, command=update_task)
button_update_task.pack(pady=10)

root.mainloop()
