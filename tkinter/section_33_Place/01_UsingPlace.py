import tkinter as tk

root = tk.Tk()
root.title('Using Place')
root.geometry('200x200')

a = tk.Label(root, text='AAA', background='#f90')
b = tk.Label(root, text='BBB', background='#09c')
c = tk.Label(root, text='CCC', background='#fc0')
d = tk.Label(root, text='DDD', background='#0c9')

a.place(x=0, y=0)
b.place(x=50, y=50)
c.place(x=100, y=100)
d.place(x=150, y=150)

root.mainloop()