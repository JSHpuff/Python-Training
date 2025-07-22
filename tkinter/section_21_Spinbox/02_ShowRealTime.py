import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Show Value RealTime')
        self.geometry('300x300')
        self.setStringvalue()
        self.setLabel()
        self.setSpinbox()
    def setStringvalue(self):
        self.a = tk.StringVar()
        self.a.set('')
    def setLabel(self):
        label = tk.Label(self, textvariable=self.a)
        label.pack()
    def setSpinbox(self):
        self.spinbox = tk.Spinbox(self, from_=0, to=100, command=self.spin)
        self.spinbox.pack()
    def spin(self):
        val = self.spinbox.get()
        self.a.set(val)

if __name__ == "__main__":
    app = App()
    app.mainloop()