import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.resizable(True, True)

sizegrip = ttk.Sizegrip(root)
sizegrip.place(relx=1, rely=1, anchor=tk.SE)

root.mainloop()