import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.createFrame()
        self.setScrollbar()
        self.setText()
        self.combineFrameScrollbar()
        self.packFrame()
    def createFrame(self):
        self.frame = tk.Frame(self, height=10, width=15)
    def setScrollbar(self):
        self.scrollbar = tk.Scrollbar(self.frame)
        self.scrollbar.pack(side='right', fill='y')
    def setText(self):
        self.text = tk.Text(self.frame, height=10, width=15,
                            yscrollcommand=self.scrollbar.set)
        self.text.pack()
    def combineFrameScrollbar(self):
        self.scrollbar.config(command=self.text.yview)
    def packFrame(self):
        self.frame.pack()

if __name__ == "__main__":
    app = App()
    app.mainloop()