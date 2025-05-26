# Using the widget constructor when creating the widget
import tkinter as tk
from tkinter import ttk

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Testing Setting Widgets")
    window_width = 600
    window_height = 600
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    center_x = int(screen_width / 2 - window_width / 2)
    center_y = int(screen_height / 2 - window_height / 2)
    root.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")
    root.resizable(False, False)
    root.iconbitmap("./000_testing_imgs/test_icon.ico")

    ttk.Label(root, text="Testing text for ttk").pack()
    
    root.mainloop()