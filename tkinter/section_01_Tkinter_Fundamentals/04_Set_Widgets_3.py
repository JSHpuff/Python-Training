# Using the config() method with keyword arguments
import tkinter as tk
from tkinter import ttk

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Test set widgets 3")
    window_width = 600
    window_height = 600
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    center_x = int(screen_width / 2 - window_width / 2)
    center_y = int(screen_height / 2 - window_height / 2)
    root.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")
    root.resizable(False, False)
    root.iconbitmap("./000_testing_imgs/test_icon.ico")

    label = ttk.Label(root)
    label.config(text="Hi Hi Hi")
    label.pack()

    root.mainloop()