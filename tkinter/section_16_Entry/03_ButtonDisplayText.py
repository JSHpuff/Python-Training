import tkinter as tk

root = tk.Tk()
root.title('Press Button to Display Input Text')
root.geometry('200x200')

a = tk.StringVar()
b = tk.StringVar()
a.set('')

def show():
    a.set(b.get())

def clear():
    b.set('')
    entry.delete(0, 'end')

label = tk.Label(
    root,
    textvariable=a
)
label.pack()

entry = tk.Entry(
    root,
    textvariable=b
)
entry.pack()

btn1 = tk.Button(
    root,
    text='Show',
    command=show
)
btn1.pack()

btn2 = tk.Button(
    root,
    text='Clear',
    command=clear
)
btn2.pack()

root.mainloop()