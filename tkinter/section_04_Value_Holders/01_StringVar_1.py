import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Tkinter StringVar")
root.geometry("250x100")

pack_attr = {"anchor": tk.W, "padx": 5, "pady": 5, "fill": tk.X}

ttk.Label(root, text="Name").pack(**pack_attr)

name_var = tk.StringVar()

name_entry = ttk.Entry(root, textvariable=name_var)
name_entry.pack(**pack_attr)
name_entry.focus()

output_label = ttk.Label(root, textvariable=name_var)
output_label.pack(**pack_attr)

root.mainloop()