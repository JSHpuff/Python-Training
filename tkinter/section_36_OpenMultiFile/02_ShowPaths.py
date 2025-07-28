import os
os.chdir('/')

import tkinter as tk
from tkinter import Variable, filedialog

root = tk.Tk()
root.title('Show Files Paths after open files')
root.geometry('300x200')

def show():
    files = filedialog.askopenfilenames()
    for i, e in enumerate(files):
        text.insert('end', f'{e}')
        if i != len(files):
            text.insert('end', '\n')

btn_open = tk.Button(
    root,
    text='Open Files',
    font=('Arial', 20, 'bold'),
    command=show
)
btn_open.pack()

text = tk.Text(root, height=8)
text.pack()

root.mainloop()