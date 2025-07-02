import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo

root = tk.Tk()
root.title("Tkinter Open File Dialog")
root.resizable(False, False)
root.geometry("350x150")

def select_file():
    filetypes = (
        ('text files', '.txt'),
        ('All files', '*.*')
    )
    
    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes
    )

    showinfo(
        title='Selected File',
        message=filename
    )

open_button = ttk.Button(
    root,
    text='Open a File',
    command=select_file
)

open_button.pack(expand=True)

root.mainloop()