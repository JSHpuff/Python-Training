import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Adding Scrollbar to Canvas')
        self.geometry('400x400')
        self.setFrame()
        self.createCanvas()
        self.setScrollX()
        self.setScrollY()
        self.setCanvas()
    def setFrame(self):
        self.frame = tk.Frame(self, width=200, height=300)
        self.frame.pack()
    def createCanvas(self):
        self.canvas = tk.Canvas(
            self.frame, width=200, height=300,
            bg='#faf', scrollregion=(0, 0, 400, 400)
        )
        self.canvas.create_rectangle(
            120, 10, 170, 100,
            width=8, fill='#f00'
        )
    def setScrollX(self):
        self.scrollX = tk.Scrollbar(self.frame, orient='horizontal')
        self.scrollX.pack(side='bottom', fill='x')
        self.scrollX.config(command=self.canvas.xview)
    def setScrollY(self):
        self.scrollY = tk.Scrollbar(self.frame, orient='vertical')
        self.scrollY.pack(side='right', fill='y')
        self.scrollY.config(command=self.canvas.yview)
    def setCanvas(self):
        self.canvas.config(
            xscrollcommand=self.scrollX.set,
            yscrollcommand=self.scrollY.set
        )
        self.canvas.pack(side='left')

if __name__ == "__main__":
    app = App()
    app.mainloop()