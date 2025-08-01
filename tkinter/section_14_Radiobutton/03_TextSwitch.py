import tkinter as tk

root = tk.Tk()
root.title('Text Switch')
root.geometry('200x200')

val = tk.StringVar()

radio_btn1 = tk.Radiobutton(
    root,
    text='Apple',
    variable=val,
    value='Apple'
)

radio_btn1.pack()

radio_btn1.select()

radio_btn2 = tk.Radiobutton(
    root,
    text='Banana',
    variable=val,
    value='Banana'
)

radio_btn2.pack()

mylabel = tk.Label(
    root,
    textvariable=val,
    font=('Arial', 30),
    fg='#f00'
)

mylabel.pack()

root.mainloop()