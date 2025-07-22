import tkinter as tk

root = tk.Tk()
root.title('Adding Option Menu')
root.geometry('200x200')

optionList = [
    '七龍珠','海賊王','鬼滅之刃','灌籃高手','排球少年'
]

value = tk.StringVar()
value.set('')

menu = tk.OptionMenu(
    root,
    value,
    *optionList
)
menu.pack()

root.mainloop()