import tkinter as tk
from tkinter import ttk

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Tkinter Pack Layout")
    window_width = 300
    window_height = 200
    root.geometry(f"{window_width}x{window_height}")
    root.iconbitmap("./000_testing_imgs/test_icon.ico")
    root.attributes("-alpha", 0.9)

    name_label = ttk.Label(root, text="Name: ")
    name_label.pack(side=tk.LEFT)

    name_entry = ttk.Entry(root)
    name_entry.pack(side=tk.LEFT)

    button = ttk.Button(root, text="Submit")
    button.pack(side=tk.LEFT)

    root.mainloop()