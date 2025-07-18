import tkinter as tk

root = tk.Tk()
root.title('Set Format')
root.geometry('200x200')

mylabel = tk.Label(
    root,
    text='Hello',
    font=('Arial', 20, 'bold'),
    fg='#fff',
    bg='#f50',
    relief='groove',
    padx=20, pady=20
)

mylabel.pack()

root.mainloop()