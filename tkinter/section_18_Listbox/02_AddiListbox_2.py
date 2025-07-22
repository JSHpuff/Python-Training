import tkinter as tk

root = tk.Tk()
root.title('Adding Listbox')
root.geometry('200x200')

listbox = tk.Listbox(root)
listbox.insert(tk.END, 'Apple')
listbox.insert(tk.END, 'Banana')
listbox.insert(tk.END, 'Orange')
listbox.pack()

root.mainloop()