import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title('Show Selected in Combobox')
root.geometry('200x200')

def show():
    a.set(f'{box.current()}:{box.get()}')

a = tk.StringVar()
a.set('')

label = tk.Label(root, textvariable=a)
label.pack()

box = ttk.Combobox(
    root,
    width=15,
    values=['123', '456', '789']
)
box.pack()

btn = tk.Button(root, text='Show', command=show)
btn.pack()

root.mainloop()