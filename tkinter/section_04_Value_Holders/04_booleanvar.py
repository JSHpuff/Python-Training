import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

root = tk.Tk()
root.title("BooleanVar Example")
root.geometry("300x80")

check_var = tk.BooleanVar(value=True)

check_button = ttk.Checkbutton(
    root,
    text="Check me",
    variable=check_var,
    command=lambda: showinfo(
        title="Checkbutton State",
        message="Checked" if check_var.get() else "Unchecked"
    )
)
check_button.pack()

root.mainloop()