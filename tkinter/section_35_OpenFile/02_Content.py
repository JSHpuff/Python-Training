import os
os.chdir('/')

import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.title('Reading with content')
root.geometry('200x200')

text = tk.StringVar()
text.set('')

def show():
    file_path = filedialog.askopenfilename()
    f = open(file_path, 'r')
    a = f.read()
    text.set(a)
    f.close()

btn = tk.Button(
    root,
    text='Im Button',
    font=('Arial', 20, 'bold'),
    command=show
)
btn.pack()

mylabel = tk.Label(root, textvariable=text, font=('Arial', 20))
mylabel.pack()

root.mainloop()