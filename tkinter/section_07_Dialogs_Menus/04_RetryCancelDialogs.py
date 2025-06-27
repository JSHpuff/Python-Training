import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import askretrycancel, showinfo

root = tk.Tk()
root.title("Tkinter Retry/Cancel Dialog")
root.geometry("350x150")

def confirm():
    answer = askretrycancel(
        title="Connection Issue",
        message="The database server is unreachable. Do you want to retry?"
    )

    if answer:
        showinfo(
            title="Information",
            message="Attempt to connect to the database again."
        )

ttk.Button(
    root,
    text="Connect to the Database Server",
    command=confirm
).pack(expand=True)

root.mainloop()