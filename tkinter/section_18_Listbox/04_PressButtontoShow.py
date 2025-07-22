import tkinter as tk

root = tk.Tk()
root.title('Press Button to Show Listbox')
root.geometry('200x200')

def show():
    n, = listbox.curselection()
    text.set(listbox.get(n))

text = tk.StringVar()
label = tk.Label(
    root,
    textvariable=text
)
label.pack()

menu = tk.StringVar()
menu.set(
    (
        'Apple', 'Banana',
        'Orange', 'Grap',
        'Papaya', 'Coconut'
    )
)

listbox = tk.Listbox(
    root,
    listvariable=menu,
    height=8
)
listbox.pack()

btn = tk.Button(
    root,
    text='Show',
    command=show
)
btn.pack()

root.mainloop()