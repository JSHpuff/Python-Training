from email.policy import default
import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Show Value in Real Time')
        self.geometry('300x300')
        self.stringvalue()
        self.setlabel()
        self.setScaleh()
        self.setScalev()
    def stringvalue(self):
        self.a = tk.StringVar()
        self.a.set('0, 0')
    def setlabel(self):
        label = tk.Label(self, textvariable=self.a)
        label.pack()
    def setScaleh(self):
        self.scale_h = tk.Scale(
            self,
            from_=0,
            to=100,
            orient='horizontal',
            command=self.show
        )
        self.scale_h.pack()
    def setScalev(self):
        self.scale_v = tk.Scale(
            self,
            from_=0,
            to=100,
            orient='vertical',
            command=self.show
        )
        self.scale_v.pack()
    # 定義顯示函式，注意一定要有一個參數
    def show(self, e):
        self.a.set(f'{self.scale_h.get()}, {self.scale_v.get()}')
    
if __name__ == "__main__":
    app = App()
    app.mainloop()