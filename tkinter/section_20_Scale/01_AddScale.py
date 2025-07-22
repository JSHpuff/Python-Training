import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Adding Scale')
        self.geometry('300x300')
        self.AddScale()
    def AddScale(self):
        self.v_scale()
        self.h_scale()
    def v_scale(self):
        scale_v = tk.Scale(self, from_=0, to=100)
        scale_v.pack()
    def h_scale(self):
        scale_h = tk.Scale(self, from_=0, to=100, orient='horizontal')
        scale_h.pack()

if __name__ == "__main__":
    app = App()
    app.mainloop()