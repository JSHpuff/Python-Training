import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd

root = tk.Tk()
root.title("Display a Text File")
root.resizable(False, False)
root.geometry("650x250")

text = tk.Text(root, height=12)
text.grid(column=0, row=0, sticky='nsew')

def open_text_file():
    filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')
    )

    f = fd.askopenfile(filetypes=filetypes)

    text.insert('1.0', f.readlines())

open_button = ttk.Button(
    root,
    text='Open a File',
    command=open_text_file
)

open_button.grid(column=0, row=1, sticky='w', padx=10, pady=10)

root.mainloop()