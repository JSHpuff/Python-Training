import tkinter as tk

root = tk.Tk()
root.title('Checkbutton Combine of Text')
root.geometry('400x200')

result = tk.StringVar()

result.set('')

mylabel = tk.Label(
    root,
    textvariable=result,
    font=('Arial', 30),
    fg='#f00'
)

mylabel.pack()

def show():
    text = f'{var1.get()}{var2.get()}'
    result.set(text)

var1 = tk.StringVar()

check_btn1 = tk.Checkbutton(
    root,
    text='Apple',
    variable=var1,
    onvalue='Apple',
    offvalue='',
    command=show
)

check_btn1.pack()

check_btn1.deselect()

var2 = tk.StringVar()

check_btn2 = tk.Checkbutton(
    root,
    text='Banana',
    variable=var2,
    onvalue='Banana',
    offvalue='',
    command=show
)

check_btn2.pack()

check_btn2.deselect()

root.mainloop()