import tkinter as tk

root = tk.Tk()
root.title('Adding Label')
root.geometry('200x200')

mylabel = tk.Label(
    root,
    text='Hello'
)
mylabel.pack()

root.mainloop()