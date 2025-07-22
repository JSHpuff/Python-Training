import tkinter as tk

root = tk.Tk()
root.title('Adding Multi-Options')
root.geometry('200x200')

listbox = tk.Listbox(root)

menu = [
    'Apple', 'Banana',
    'Orange', 'Grap',
    'Papaya', 'Coconut'
]

for i in menu:
    listbox.insert(tk.END, i)

listbox.pack()

root.mainloop()