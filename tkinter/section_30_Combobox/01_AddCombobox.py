import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title('Adding Combobox')
root.geometry('200x200')

box = ttk.Combobox(root, values=['123', '456', '789'])
box.pack()

root.mainloop()