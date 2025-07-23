import tkinter as tk

root = tk.Tk()
root.title('Adding Comment into Menu')
root.geometry('200x200')

def open_cmd(): print('open')

def save_cmd(): print('save')

def exit_cmd(): print('exit')

def open(event): open_cmd()

def save(event): save_cmd()

def exit(event): exit_cmd()

menu = tk.Menu(root)

menubar = tk.Menu(menu)
menubar.add_command(label='Open', command=open_cmd, accelerator="Ctrl+O")
menubar.add_command(label='Save', command=save_cmd, accelerator="Ctrl+S")
menubar.add_command(label='Exit', command=exit_cmd, accelerator="Ctrl+E")
menu.add_cascade(label='File', menu=menubar)

root.bind_all("<Control-o>", open)
root.bind_all("<Control-s>", save)
root.bind_all("<Control-e>", exit)

root.config(menu=menu)

root.mainloop()