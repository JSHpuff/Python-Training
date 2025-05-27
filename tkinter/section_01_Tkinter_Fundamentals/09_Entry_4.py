# Two-way binding with a StringVar object
# Tracing text changes

import tkinter as tk
from tkinter import ttk

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Tracing Text")
    window_width = 300
    window_height = 200
    root.geometry(f"{window_width}x{window_height}")
    root.iconbitmap("./000_testing_imgs/test_icon.ico")

    name_var = tk.StringVar()
    name_entry = ttk.Entry(root, textvariable=name_var)
    name_entry.pack()
    name_entry.focus()

    output_label = ttk.Label(root)
    output_label.pack()

    name_var.trace_add(
        "write",
        lambda *args: output_label.config(text=name_var.get().upper())
    )

    root.mainloop()