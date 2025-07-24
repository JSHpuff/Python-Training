import tkinter as tk
from tkinter import ttk
import time

root = tk.Tk()
root.title('Using with Loop')
root.geometry('200x200')

bar = ttk.Progressbar(root, mode='determinate')
bar.pack(pady=10)

def show():
    button['state'] = 'disabled'
    button2['state'] = 'disabled'
    for i in range(101):
        bar['value'] = i
        val.set(f'{i}%')
        root.update()
        time.sleep(0.01)
    button2['state'] = 'normal'

def clear():
    button['state'] = 'normal'
    button2['state'] = 'disabled'
    bar['value'] = 0
    val.set('0%')

val = tk.StringVar()
val.set('0%')

label = tk.Label(root, textvariable=val)
label.pack()

button = tk.Button(root, text='Start', command=show)
button.pack()

button2 = tk.Button(root, text='Again', command=clear, state='disabled')
button2.pack()

root.mainloop()