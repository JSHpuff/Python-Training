import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title('Get Messagebox Selection Result')
root.geometry('300x300')

def askyesno():
    result = messagebox.askyesno('askyesno', 'askyesno')
    print(result)

btn_askyesno = tk.Button(root, text='askyesno', command=askyesno)
btn_askyesno.pack()

root.mainloop()