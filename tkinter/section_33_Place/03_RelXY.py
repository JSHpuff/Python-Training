import tkinter as tk

root = tk.Tk()
root.title('Using Relx and Rely in the Place')
root.geometry('200x200')

a = tk.Label(root, text='AAA', background='#f90')
b = tk.Label(root, text='BBB', background='#09c')
c = tk.Label(root, text='CCC', background='#fc0')
d = tk.Label(root, text='DDD', background='#0c9')

a.place(relx=0.1, rely=0.1)
b.place(relx=0.3, rely=0.3)
c.place(relx=0.5, rely=0.5)
d.place(relx=0.7, rely=0.7)

root.mainloop()