import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.title('Open Multiple Files')
root.geometry('200x200')

def show():
    files = filedialog.askopenfilenames()
    print(files)

btn = tk.Button(
    root,
    text='Open Files',
    font=('Arial', 20, 'bold'),
    command=show
)
btn.pack()

root.mainloop()