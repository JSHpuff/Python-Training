import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.title('Open file and read path')
root.geometry('200x200')

def show():
    file_path = filedialog.askopenfilename()
    print(file_path)

btn = tk.Button(
    root,
    text='Open File',
    font=('Arial', 20, 'bold'),
    command=show
)
btn.pack()

root.mainloop()