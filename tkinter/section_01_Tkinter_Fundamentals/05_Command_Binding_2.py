# Tkinter botton command arguments
import tkinter as tk
from tkinter import ttk

if __name__ == "__main__":
    root = tk.Tk()

    def select(option):
        print(option)
    
    ttk.Button(root, text="Rock", command=lambda: select("Rock")).pack()
    ttk.Button(root, text="Paper", command=lambda: select("Paper")).pack()
    ttk.Button(root, text="Scissors", command=lambda: select("Scissors")).pack()

    root.mainloop()