import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title('Using with Buttons')
root.geometry('200x200')

bar = ttk.Progressbar(root, mode='determinate')
bar.pack(pady=10)

a = 0
def show():
    global a
    if a < bar['maximum']:
        a += 10
        bar['value'] = a
        val.set(f'{a}%')

val = tk.StringVar()
val.set('0%')

label = tk.Label(root, textvariable=val)
label.pack()

button = tk.Button(root, text='Increase Progress', command=show)
button.pack()

root.mainloop()