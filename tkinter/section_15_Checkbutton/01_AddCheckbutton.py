import tkinter as tk

root = tk.Tk()
root.title('Adding Checkbutton')
root.geometry('200x200')

check_btn1 = tk.Checkbutton(
    root,
    text='Apple'
)

check_btn1.pack()

check_btn2 = tk.Checkbutton(
    root,
    text='Banana'
)

check_btn2.pack()

root.mainloop()