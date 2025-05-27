# Creating button
# Simple Tkinter button example

import tkinter as tk
from tkinter import ttk

if __name__ == "__main__":
    # Main Window
    root = tk.Tk()
    root.title("Button Demo")
    window_width = 300
    window_height = 200
    root.geometry(f"{window_width}x{window_height}")
    root.resizable(False, False)
    root.iconbitmap("./000_testing_imgs/test_icon.ico")

    # Exit Button
    exit_button = ttk.Button(root, text="Exit",
                            command=lambda: root.quit())
    
    exit_button.pack(ipadx=5, ipady=5, expand=True)

    root.mainloop()