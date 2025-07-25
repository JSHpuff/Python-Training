import tkinter as tk

root = tk.Tk()
root.title('Using pad params with pack')
root.geometry('200x200')

a = tk.Label(root, text='AAA', background='#f90')
b = tk.Label(root, text='BBB', background='#09c')
c = tk.Label(root, text='CCC', background='#fc0')
d = tk.Label(root, text='DDD', background='#f9c')
e = tk.Label(root, text='EEE', background='#aaa')

a.pack(fill='x', padx=20)
b.pack(ipadx=20)
c.pack(fill='x', ipady=20)
d.pack(ipady=20)
e.pack()

root.mainloop()