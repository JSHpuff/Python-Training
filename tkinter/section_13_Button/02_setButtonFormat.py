import tkinter as tk

root = tk.Tk()
root.title('Set Button Format')
root.geometry('1200x200')

btn = tk.Button(
    root,
    text='I am button',
    font=('Arial', 30, 'bold'),
    padx=10, pady=10,
    activeforeground='#f00'
)
btn.pack()

root.mainloop()