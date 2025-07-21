import tkinter as tk

root = tk.Tk()
root.title('Distinguish if Checking')
root.geometry('200x200')

def show():
    print(var1.get(), var2.get())

var1 = tk.StringVar()

check_btn1 = tk.Checkbutton(
    root,
    text='Apple',
    variable=var1,
    onvalue='Apple',
    offvalue='--',
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
    offvalue='--',
    command=show
)

check_btn2.pack()

check_btn2.deselect()

root.mainloop()