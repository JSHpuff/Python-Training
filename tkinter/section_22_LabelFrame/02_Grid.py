import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Using with Grid')
        self.geometry('200x200')
        self.setLabelFrame1()
        self.setLabel1()
        self.setLabelFrame2()
        self.setLabel2()
    def setLabelFrame1(self):
        self.g1 = tk.LabelFrame(self, text='G1', 
                                padx=10, pady=10, background='#0c9')
        self.g1.grid(column=0, row=0, ipadx=10, ipady=10)
    def setLabel1(self):
        tk.Label(self.g1, text='AAA').pack()
        tk.Label(self.g1, text='BBB').pack()
        tk.Label(self.g1, text='CCC').pack()
    def setLabelFrame2(self):
        self.g2 = tk.LabelFrame(self, text='G2',
                                padx=10, pady=10, background='#f90')
        self.g2.grid(column=1, row=0, ipadx=10, ipady=10)
    def setLabel2(self):
        tk.Label(self.g2, text='XXX').pack()
        tk.Label(self.g2, text='YYY').pack()
        tk.Label(self.g2, text='ZZZ').pack()

if __name__ == "__main__":
    app = App()
    app.mainloop()
