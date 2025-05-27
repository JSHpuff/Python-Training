# Setting the focus

import tkinter as tk
from tkinter import ttk

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Entry Widget Demo")
    window_width = 300
    window_height = 200
    root.geometry(f"{window_width}x{window_height}")
    root.iconbitmap("./000_testing_imgs/test_icon.ico")

    name_label = ttk.Label(root, text="Name: ")
    name_label.pack(pady=2)

    name_entry = ttk.Entry(root)
    name_entry.pack(pady=5)
    name_entry.focus()

    email_label = ttk.Label(root, text="Email: ")
    email_label.pack(pady=2)
    
    email_entry = ttk.Entry(root)
    email_entry.pack(pady=5)

    root.mainloop()