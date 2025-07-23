import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Adding Canvas')
        self.geometry('300x300')
        self.setCanvas()
    def setCanvas(self):
        canvas = tk.Canvas(self, width=300, height=300)
        canvas.pack()

if __name__ == "__main__":
    app = App()
    app.mainloop()