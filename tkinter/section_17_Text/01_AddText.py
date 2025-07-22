import tkinter as tk

root = tk.Tk()
root.title('Adding Text')
root.geometry('200x200')

text = tk.Text(root)
text.pack()

root.mainloop()