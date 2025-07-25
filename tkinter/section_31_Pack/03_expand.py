import tkinter as tk

root = tk.Tk()
root.title('Using expand with pack')
root.geometry('200x200')

a = tk.Label(root, text='AAA', background='#f90')
b = tk.Label(root, text='BBB', background='#09c')

a.pack(fill='y', expand=1)
b.pack(fill='both', expand=1)

root.mainloop()