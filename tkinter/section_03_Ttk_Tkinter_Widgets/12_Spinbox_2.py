import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("300x200")
root.resizable(False, False)
root.title("Spinbox Demo")

current_value = tk.StringVar()
spin_box = ttk.Spinbox(
    root,
    from_=0,
    to=50,
    values=(0, 10, 20, 30 ,40, 50),
    textvariable=current_value,
    wrap=True
)

spin_box.pack()

root.mainloop()