import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

root = tk.Tk()
root.title("Text Widget Example")

text = tk.Text(root, height=8)
text.config(
    font=("Consolas", 12),
    fg="#F0F0F0",
    bg="#282C34",
    insertbackground="white"
)

text.pack(padx=10, pady=10, expand=True, fill=tk.BOTH)
text.insert(
    index="1.0",
    chars="This is a Text widget demo"
)

root.mainloop()