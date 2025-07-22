import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Adding Spinbox')
        self.geometry('200x200')
        self.AddSpinbox()
    def AddSpinbox(self):
        spinbox = tk.Spinbox(self, from_=0, to=100)
        spinbox.pack()

if __name__ == "__main__":
    app = App()
    app.mainloop()