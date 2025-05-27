# Entering sensitive information

import tkinter as tk
from tkinter import ttk

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Entry Widget Demo")
    window_width = 300
    window_height = 200
    root.geometry(f"{window_width}x{window_height}")
    root.iconbitmap("./000_testing_imgs/test_icon.ico")

    password_label = ttk.Label(root, text="Password")
    password_label.pack(pady=5)

    password_entry = ttk.Entry(root, show="*")
    password_entry.pack(pady=5)

    root.mainloop()