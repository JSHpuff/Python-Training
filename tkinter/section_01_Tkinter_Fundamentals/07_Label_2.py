# Setting fonts for the Label widget

import tkinter as tk
from tkinter import ttk

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Label Widget Demo")
    window_width = 300
    window_height = 200
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    center_x = int(screen_width / 2 - window_width / 2)
    center_y = int(screen_height / 2 - window_height / 2)
    root.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")
    root.resizable(True, True)
    root.iconbitmap("./000_testing_imgs/test_icon.ico")

    label = ttk.Label(
        root,
        text="A Label with the Helvetica font",
        font=("Helvetica", 14)
    )

    label.pack()

    root.mainloop()