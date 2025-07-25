import tkinter as tk
from tkinter import Variable, filedialog
import zipfile

root = tk.Tk()
root.title('Zip the selected files')
root.geometry('400x200')

def show():
    files = filedialog.askopenfilenames()
    for i, e in enumerate(files):
        text.insert('end', f'{e}\n')
        if i == len(files):
            text.insert('end')

def zip():
    content = text.get(1.0, 'end-1c')
    new_files = content.split('\n')
    del new_files[-1]
    print(new_files)
    with zipfile.ZipFile('test.zip', mode='w') as zf:
        for i in new_files:
            zf.write(i)

btn_open = tk.Button(
    root,
    text='Adding Files',
    font=('Arial', 14),
    command=show
)
btn_open.grid(column=0, row=0)

btn_zip = tk.Button(
    root,
    text='Compress',
    font=('Arial', 14),
    command=zip
)
btn_zip.grid(column=1, row=0)

text = tk.Text(root, height=8, width=50)
text.grid(column=0, row=1, columnspan=2)

root.mainloop()