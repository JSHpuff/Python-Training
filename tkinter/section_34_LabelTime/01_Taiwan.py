import tkinter as tk
import datetime

GMT = datetime.timezone(datetime.timedelta(hours=8))

root = tk.Tk()
root.title('Taiwan Time')
root.geometry('200x200')

a = tk.StringVar()

def showTime():
    now = datetime.datetime.now(tz=GMT).strftime('%H:%M:%S')
    a.set(now)
    root.after(1000, showTime)

tk.Label(root, text='Current Time', font=('Arial', 20)).pack()
tk.Label(root, textvariable=a, font=('Arial', 20)).pack()

showTime()

root.mainloop()