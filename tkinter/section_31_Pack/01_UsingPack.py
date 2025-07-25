import tkinter as tk

root = tk.Tk()
root.title('Using Pack')
root.geometry('200x200')

a = tk.Label(root, text='AAA', background='#f90')
b = tk.Label(root, text='BBB', background='#09c')

a.pack()
b.pack()

root.mainloop()