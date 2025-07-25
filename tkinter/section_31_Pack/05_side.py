import tkinter as tk

root = tk.Tk()
root.title('Using side with pack')
root.geometry('200x200')

a = tk.Label(root, text='AAA', background='#f90')
b = tk.Label(root, text='BBB', background='#09c')
c = tk.Label(root, text='CCC', background='#fc0')
d = tk.Label(root, text='DDD', background='#f9c')
e = tk.Label(root, text='EEE', background='#aaa')

a.pack(side='left')
b.pack(side='left')
c.pack(side='top')
d.pack(side='bottom')
e.pack(side='right')

root.mainloop()