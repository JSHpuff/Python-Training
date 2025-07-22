import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Adding Frame')
        self.geometry('200x200')
        self.setFrame()
        self.setLabel()
    def setFrame(self):
        self.frame = tk.Frame(self)
        self.frame.pack()
    def setLabel(self):
        label = tk.Label(self.frame, text='hello')
        label.pack()

if __name__ == "__main__":
    app = App()
    app.mainloop()