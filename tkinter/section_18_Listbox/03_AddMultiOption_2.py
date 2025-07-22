import tkinter as tk

root = tk.Tk()
root.title('Adding Multi-Options')
root.geometry('200x200')

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
    listvariable=menu
)
listbox.pack()

root.mainloop()