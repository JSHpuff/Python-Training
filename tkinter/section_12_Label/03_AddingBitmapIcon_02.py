import tkinter as tk

root = tk.Tk()
root.title('Adding Bitmap')
root.geometry('200x200')

mylabel = tk.Label(
    root,
    text='Hello',
    font=('Arial', 20, 'bold'),
    fg='#f00',
    bitmap='info',
    compound='left'
)

mylabel.pack()

root.mainloop()