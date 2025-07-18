import tkinter as tk

root = tk.Tk()
root.title('Accumulate Number')
root.geometry('200x200')

n = 0
a = tk.StringVar()
a.set(n)

def add():
    global n
    n += 1
    a.set(n)

mylabel = tk.Label(
    root,
    textvariable=a,
    font=('Arial', 20)
)
mylabel.pack()

btn = tk.Button(
    root,
    text='HitMe',
    font=('Arial', 30, 'bold'),
    command=add
)
btn.pack()

root.mainloop()