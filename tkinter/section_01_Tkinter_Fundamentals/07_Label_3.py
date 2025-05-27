# Creating image labels

import tkinter as tk
from tkinter import ttk

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Label Widtget Image")
    
    window_width = 300
    window_height = 200
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    center_x = int(screen_width / 2 - window_width / 2)
    center_y = int(screen_height / 2 - window_height / 2)
    root.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")
    root.resizable(False, False)
    root.iconbitmap("./000_testing_imgs/test_icon.ico")

    # Display an image label
    photo = tk.PhotoImage(file="./000_testing_imgs/python.png")
    image_label = ttk.Label(
        root,
        image=photo,
        padding=5
    )
    image_label.pack()

    root.mainloop()