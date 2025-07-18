import tkinter as tk

root = tk.Tk()
root.title('Using Text Variables')
root.geometry('200x200')

a = tk.StringVar()
a.set('hello')
mylabel = tk.Label(
    root,
    textvariable=a,
    font=('Arial', 20)
)
mylabel.pack()

root.mainloop()