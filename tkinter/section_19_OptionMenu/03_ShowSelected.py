import tkinter as tk

root = tk.Tk()
root.title('Show Selected')
root.geometry('200x200')

def show(*e):
    a.set(value.get())

a = tk.StringVar()
a.set('')

label = tk.Label(root, textvariable=a)
label.pack()

optionList = ['七龍珠','海賊王','鬼滅之刃','灌籃高手','排球少年']
value = tk.StringVar()
value.set('七龍珠')

menu = tk.OptionMenu(root, value, *optionList)
menu.config(width=10, fg='#f00')
menu.pack()

button = tk.Button(root, text='Show', command=show)
button.pack()

root.mainloop()