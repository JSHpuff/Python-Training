import tkinter as tk

root = tk.Tk()
root.title('Adding Listbox')
root.geometry('200x200')

listbox = tk.Listbox(root)
listbox.insert(1, 'Apple')
listbox.insert(2, 'Banana')
listbox.insert(3, 'Orange')
listbox.pack()

root.mainloop()