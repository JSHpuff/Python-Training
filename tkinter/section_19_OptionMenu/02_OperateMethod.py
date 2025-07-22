import tkinter as tk

root = tk.Tk()
root.title('Option Menu s Operate Method')
root.geometry('200x200')

def show(*e):
    a.set(value.get())

a = tk.StringVar()
a.set('七龍珠')

label = tk.Label(root, textvariable=a)
label.pack()

optionList = [
    '七龍珠','海賊王','鬼滅之刃','灌籃高手','排球少年'
]

value = tk.StringVar()
value.set('七龍珠')

menu = tk.OptionMenu(
    root,
    value,
    *optionList
)
menu.config(
    width=10,
    fg='#f00'
)
menu.pack()

value.trace('w', show)

root.mainloop()