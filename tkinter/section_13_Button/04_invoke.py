import tkinter as tk

root = tk.Tk()
root.title('Invoke Button')
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
    text='Button',
    font=('Arial', 30, 'bold'),
    command=add
)

btn.pack()

for i in range(4):
    # 執行 invoke() 之後等同按下該顆按鈕
    btn.invoke()

root.mainloop()