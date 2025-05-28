# Two-way binding with a StringVar object
# Tracing text changes

import tkinter as tk
from tkinter import ttk
import os

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Tracing Text")
    window_width = 300
    window_height = 200
    root.geometry(f"{window_width}x{window_height}")

    # Safely set icon
    try:
        if os.path.exists("./000_testing_imgs/test_icon.ico"):
            root.iconbitmap("./000_testing_imgs/test_icon.ico")
    except Exception as e:
        print(f"Icon load failed: {e}")

    # StringVar binding
    name_var = tk.StringVar()

    name_entry = ttk.Entry(root, textvariable=name_var)
    name_entry.pack()
    name_entry.focus()

    output_label = ttk.Label(root)
    output_label.pack()

    # Trace changes & auto-uppercase
    def update_output(*_):
        output_label.config(text=name_var.get().upper())

    trace_id = name_var.trace_add("write", update_output)


    root.mainloop()