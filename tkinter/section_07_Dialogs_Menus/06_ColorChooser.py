import tkinter as tk
from tkinter import ttk
from tkinter.colorchooser import askcolor

root = tk.Tk()
root.title("Tkinter Color Chooser")
root.geometry("350x150")

def change_color():
    colors = askcolor(
        title="Tkinter Color Chooser"
    )
    root. config(bg=colors[1])

ttk.Button(
    root,
    text="Select a Color",
    command=change_color
).pack(expand=True)

root.mainloop()
