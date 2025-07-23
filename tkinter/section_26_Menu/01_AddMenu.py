import tkinter as tk

root = tk.Tk()
root.title('Adding Menu')
root.geometry('200x200')

menubar = tk.Menu(root)
menubar.add_command(label='Open')
menubar.add_command(label='Save')
menubar.add_command(label='Exit')

root.config(menu=menubar)

root.mainloop()