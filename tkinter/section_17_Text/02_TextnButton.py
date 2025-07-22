import tkinter as tk

root = tk.Tk()
root.title('Text and Button')
root.geometry('200x200')

a = tk.StringVar()
a.set('')

label = tk.Label(
    root,
    textvariable=a
)
label.pack()

text = tk.Text(
    root,
    height=8
)
text.pack()

def show():
    a.set(text.get(1.0, 'end-1c'))
    # 執行 show 函式時，將 a 變數內容改變
    # 使用 end-1c 表示取得倒數第二個字元 ( 因為最後一個字元是換行符 )

def clear():
    a.set('')
    text.delete(1.0, 'end')

btn1 = tk.Button(
    root,
    text='show',
    command=show
)
btn1.pack()

btn2 = tk.Button(
    root,
    text='clear',
    command=clear
)
btn2.pack()

root.mainloop()