import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Frame Setting Format & Position')
        self.geometry('200x200')
        self.createFrame()
        self.setLabel1()
        self.setLabel2()
        self.setFrame()
    def createFrame(self):
        self.frame1 = tk.Frame(self, padx=10, pady=10, bg='#f90')
        self.frame2 = tk.Frame(self, padx=10, pady=10, bg='#09c')
    def setLabel1(self):
        label1 = tk.Label(self.frame1, text='Hello', width=10)
        label1.pack()
    def setLabel2(self):
        label2 = tk.Label(self.frame2, text='World', width=10)
        label2.pack()
    def setFrame(self):
        self.frame2.pack()
        self.frame1.pack()

if __name__ == "__main__":
    app = App()
    app.mainloop()