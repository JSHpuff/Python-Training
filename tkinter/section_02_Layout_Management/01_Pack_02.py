# The side parameter determines the direction of the widgets in the layout
""" 
    The side parameter has 4 options:
    - 'top':        arrange widgets from top to bottom vertically
    - 'bottom':     arrange widgets from bottom to top vertically
    - 'left':       arrange widgets from left to right horizontally
    - 'right':      arrange widgets from right to left horizontally
"""

import tkinter as tk
import os

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Tkinter Pack Layout")
    window_width = 600
    window_height = 400
    root.geometry(f"{window_width}x{window_height}")
    root.resizable(False, False)

    try:
        if os.path.exists("./000_testing_imgs/test_icon.ico"):
            root.iconbitmap("./000_testing_imgs/test_icon.ico")
    except Exception as e:
        print(f"Icon load failed: {e}")
    
    root.attributes("-alpha", 0.9)

    tk.Label(root, text="Tkinter", bg="red", fg="white").pack(side=tk.TOP)
    tk.Label(root, text="Pack Layout", bg="green", fg="white").pack(side=tk.TOP)
    tk.Label(root, text="Demo", bg="blue", fg="white").pack(side=tk.TOP)

    root.mainloop()