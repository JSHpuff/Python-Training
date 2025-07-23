import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Create Text')
        self.geometry('300x300')
        self.setCanvas()
    def setCanvas(self):
        self.canvas = tk.Canvas(self, width=300, height=300)
        self.canvas.create_text(10, 0, 
                                text='hello', anchor='nw')
        self.canvas.create_text(20, 20, 
                                text='world', anchor='nw',
                                font=('Arial', 20))
        self.canvas.create_text(30, 40,
                                text='I am\n1234', anchor='nw',
                                fill='#f00', font=('Arial', 30, 'bold'))
        self.canvas.create_text(40, 100,
                                text='Chinese Test', anchor='nw',
                                fill='#0a0', 
                                font=('Arial', 30, 'bold', 
                                      'italic', 'underline'))
        self.canvas.pack()

if __name__ == "__main__":
    app = App()
    app.mainloop()