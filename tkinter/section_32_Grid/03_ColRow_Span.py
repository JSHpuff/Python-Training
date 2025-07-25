import tkinter as tk

root = tk.Tk()
root.title('Using Columnspan & Rowsapn')
root.geometry('200x200')

a = tk.Label(root, text='AAA', background='#f90')
b = tk.Label(root, text='BBB', background='#09c')
c = tk.Label(root, text='CCC', background='#fc0')
d = tk.Label(root, text='DDD', background='#0c9')
e = tk.Label(root, text='EEE', background='#ccc')

a.grid(column=0, row=0, columnspan=2)
b.grid(column=2, row=0, rowspan=2)
c.grid(column=0, row=2)
d.grid(column=1, row=2)
e.grid(column=0, row=1, columnspan=2)

root.mainloop()