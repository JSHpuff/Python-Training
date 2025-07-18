import tkinter as tk

root = tk.Tk()
root.title('Style of Label')
root.geometry('200x200')

mylabel = tk.Label(
    root,
    text="HI\nThis is an label",
    font=('Arial', 20, 'bold'),
    fg='#f00'
)

mylabel.pack()

root.mainloop()