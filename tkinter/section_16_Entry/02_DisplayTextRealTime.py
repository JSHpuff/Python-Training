import tkinter as tk

root = tk.Tk()
root.title('Display the Text in Real Time')
root.geometry('200x200')

a = tk.StringVar()
a.set('')

tk.Label(
    root,
    textvariable=a
).pack()

tk.Entry(
    root,
    textvariable=a
).pack()

root.mainloop()