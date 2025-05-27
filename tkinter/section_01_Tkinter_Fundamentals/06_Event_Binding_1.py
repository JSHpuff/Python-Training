# show how to use the bind() method to bind an event of a widget
import tkinter as tk
from tkinter import ttk

def return_pressed(event):
    print("Return key pressed")

def pressed_button():
    print("Hello")

if __name__ == "__main__":
    root = tk.Tk()

    btn = ttk.Button(root, text="Save")

    # Press "Enter" Key
    btn.bind("<Return>", return_pressed)
    btn.config(command=lambda: pressed_button()) 

    # Give this widget keyboard focus so it's ready to receive key events
    btn.focus()
    # expand=True: give extra space if possible
    btn.pack(expand=True)

    root.mainloop()