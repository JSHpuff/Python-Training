# Use Tkinter Entry widget to create a textbox
# Introduction to Tkinter Entry widget

import tkinter as tk
from tkinter import ttk

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Entry Widget Demo")
    window_width = 300
    window_height = 200
    root.geometry(f"{window_width}x{window_height}")
    root.iconbitmap("./000_testing_imgs/test_icon.ico")

    name_entry = ttk.Entry(root)
    name_entry.pack()

    root.mainloop()