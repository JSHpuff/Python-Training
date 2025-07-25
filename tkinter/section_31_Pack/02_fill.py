import tkinter as tk

root = tk.Tk()
root.title('Using fill with pack')
root.geometry('200x200')

a = tk.Label(root, text='AAA', background='#f90')
b = tk.Label(root, text='BBB', background='#09c')

a.pack(fill='x')
b.pack(fill='y', side='left')

root.mainloop()