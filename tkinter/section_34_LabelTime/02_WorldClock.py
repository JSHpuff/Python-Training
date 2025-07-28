import tkinter as tk
import datetime

def timezone(h):
    GMT = datetime.timezone(datetime.timedelta(hours=h))
    now = datetime.datetime.now(tz=GMT).strftime('%H:%M:%S')
    return now

root = tk.Tk()
root.title('World Clock')
root.geometry('200x300')

name = ['London', 'Taiwan', 'Japan', 'NewYork']
loc_time = [1, 8, 9, -4]
arr = [tk.StringVar() for i in range(4)]

def showTime():
    for i in range(4):
        arr[i].set(timezone(loc_time[i]))
    root.after(1000, showTime)

for i in range(4):
    tk.Label(root, text=name[i], font=('Arial', 20)).pack()
    tk.Label(root, textvariable=arr[i], font=('Arial', 20)).pack()

showTime()

root.mainloop()