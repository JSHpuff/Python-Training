"""
    Compound
    - the position of the image relative to the text.
    
    - 'top':        Display the image above the text.
    - 'bottom':     Display the image below the text.
    - 'left':       Display the image to the left of the text.
    - 'right':      Display the image to the right of the text.
    - 'none':       Display the image if there's one ;
                    otherwise, display the text.
                    The compound option defaults to 'none'.
    - 'text':       Display the text, not the iamge
    - 'image':      Display the image, not the text. 
"""

import tkinter as tk
from tkinter import ttk

if __name__ == "__main__":
    # Main Window
    root = tk.Tk()
    root.title("Label Widget Image")

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
        text="Python",
        compound=tk.TOP
    )
    image_label.pack()

    root.mainloop()