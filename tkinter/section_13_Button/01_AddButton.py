import tkinter as tk

root = tk.Tk()
root.title('Adding Button')
root.geometry('200x200')

btn = tk.Button(
    root,
    text='I am Button'
)
btn.pack()

root.mainloop()