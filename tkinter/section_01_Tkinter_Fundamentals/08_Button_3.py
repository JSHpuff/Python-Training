# Displaying an image button

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

def handle_click():
    showinfo(
        title="Information",
        message="Download button clicked"
    )

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Image Button Demo")
    window_width = 300
    window_height = 200
    root.geometry(f"{window_width}x{window_height}")
    root.resizable(False, False)
    root.iconbitmap("./000_testing_imgs/test_icon.ico")

    download_icon = tk.PhotoImage(file="./000_testing_imgs/download.png")

    download_button = ttk.Button(
        root, 
        image=download_icon,
        text="Download",
        compound=tk.LEFT,
        command=handle_click
    )

    download_button.pack(
        ipadx=5,
        ipady=5,
        expand=True
    )

    root.mainloop()