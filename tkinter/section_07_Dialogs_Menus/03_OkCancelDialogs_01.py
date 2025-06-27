import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import askokcancel, showinfo, WARNING

root = tk.Tk()
root.title("Tkinter Ok/Cancel Dialog")
root.geometry("300x150")

def confirm():
    answer = askokcancel(
        title="Confirmation",
        message="Deleting will delete all the data.",
        icon=WARNING
    )
    
    if answer:
        showinfo(
            title="Deletion Status",
            message="The data is deleted successfully"
        )

ttk.Button(
    root, text="Delete All", command=confirm
).pack(expand=True)

root.mainloop()