import tkinter as tk
from tkinter import ttk
import time

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Tkinter after() Demo')
        self.geometry('350x100')

        self.style = ttk.Style(self)

        self.button = ttk.Button(self, text='Wait 3 seconds')
        self.button['command'] = self.start
        self.button.pack(
            expand=True,
            ipadx=10,
            ipady=5
        )
    
    def start(self):
        self.change_button_color('red')
        time.sleep(3)
        self.change_button_color('black')

    def change_button_color(self, color):
        self.style.configure('TButton', foreground=color)
    
if __name__ == "__main__":
    app = App()
    app.mainloop()