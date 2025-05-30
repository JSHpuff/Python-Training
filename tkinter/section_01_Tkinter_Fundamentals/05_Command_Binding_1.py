# Introduction to Tkinter command binding
# Learn how to respond to events using command bindings
import tkinter as tk
from tkinter import ttk

if __name__ == "__main__":
    root = tk.Tk()

    def button_clicked():
        print("Button clicked")

    button = ttk.Button(root, text="Click Me", command=button_clicked)
    button.pack()

    root.mainloop()