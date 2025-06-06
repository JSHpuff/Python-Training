import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("300x200")
root.resizable(True, True)

sizegrip = ttk.Sizegrip(root)
sizegrip.pack(side="bottom", anchor=tk.SE)

root.mainloop()