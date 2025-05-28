# Use the pack geometry manager to arrange widgets on a window
# Tkinter pack parameters

import tkinter as tk
import os

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Tkinter Pack Layout")
    window_width = 600
    window_height = 400
    root.geometry(f"{window_width}x{window_height}")

    try:
        if os.path.exists("./000_testing_imgs/test_icon.ico"):
            root.iconbitmap("./000_testing_imgs/test_icon.ico")
    except Exception as e:
        print(f"Icon load failed: {e}")
    
    root.attributes("-alpha", 0.9)

    tk.Label(root, text="Tkinter", bg="red", fg="white").pack(pady=20)
    tk.Label(root, text="Pack Layout", bg="green", fg="white").pack(pady=20)
    tk.Label(root, text="Demo", bg="blue", fg="white").pack(pady=20)

    root.mainloop()
