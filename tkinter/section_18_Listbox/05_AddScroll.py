import tkinter as tk

root = tk.Tk()
root.title('Adding Scroll to Listbox')
root.geometry('200x200')

frame = tk.Frame(
    root,
    width=15
)
frame.pack()

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(
    side='right',
    fill='y'
)

menu = tk.StringVar()
menu.set(
    (
        'Apple', 'Banana',
        'Orange', 'Grap',
        'Payaya', 'Coconut',
        'Pear', 'Nuts'
    )
)

listbox = tk.Listbox(
    frame,
    listvariable=menu,
    height=6,
    width=15,
    yscrollcommand=scrollbar.set
)
listbox.pack(
    side='left',
    fill='y'
)

scrollbar.config(
    command=listbox.yview
)

root.mainloop()