import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Adding Scrollbar')
        self.geometry('200x200')
        self.setScrollbar()
    def setScrollbar(self):
        scrollbar = tk.Scrollbar(self)
        scrollbar.pack(side='right', fill='y')

if __name__ == "__main__":
    app = App()
    app.mainloop()