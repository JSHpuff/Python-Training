import tkinter as tk

root = tk.Tk()
root.title("Adding Radiobutton")
root.geometry('200x200')

radio_btn1 = tk.Radiobutton(
    root,
    text='Apple'
)

radio_btn1.pack()

radio_btn2 = tk.Radiobutton(
    root,
    text='Banana'
)

radio_btn2.pack()

root.mainloop()