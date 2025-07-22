import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Adjust and Sum the Number in Real Time')
        self.geometry('300x300')
        self.setString()
        self.setLabel()
        self.setSpinbox()
    def setString(self):
        self.a = tk.StringVar()
        self.a.set('0.0')
    def setLabel(self):
        label = tk.Label(self, textvariable=self.a)
        label.pack()
    def setSpinbox(self):
        self.spinbox1 = tk.Spinbox(
            self, 
            from_=0, 
            to=100, 
            command=self.spin
        )
        self.spinbox1.pack()
        self.spinbox2 = tk.Spinbox(
            self, 
            from_=0, 
            to=100.0, 
            increment=0.1, 
            command=self.spin
        )
        self.spinbox2.pack()
    def spin(self):
        val1 = float(self.spinbox1.get())
        val2 = float(self.spinbox2.get())
        self.a.set(val1+val2)

if __name__ == "__main__":
    app = App()
    app.mainloop()
