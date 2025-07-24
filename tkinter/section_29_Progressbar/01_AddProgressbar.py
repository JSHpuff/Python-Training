import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title('Adding Progress Bar')
root.geometry('200x200')

bar = ttk.Progressbar(root)
bar.pack(pady=20)
bar.start(100)

root.mainloop()