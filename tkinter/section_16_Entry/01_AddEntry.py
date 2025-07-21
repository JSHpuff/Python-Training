import tkinter as tk

root = tk.Tk()
root.title('Adding Entry')
root.geometry('200x200')

entry = tk.Entry(root)
entry.pack()

root.mainloop()