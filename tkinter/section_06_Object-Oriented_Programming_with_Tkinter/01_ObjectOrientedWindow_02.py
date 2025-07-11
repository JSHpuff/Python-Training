import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("My Awesome App")
        self.geometry("300x50")

        self.label = ttk.Label(self, text="Hello, Tkinter!")
        self.label.pack()

        self.button = ttk.Button(self, text="Click Me")
        self.button["command"] = self.button_clicked
        self.button.pack()

    def button_clicked(self):
        showinfo(title="Information", message="Hello, Tkinter!")

if __name__ == "__main__":
    app = App()
    app.mainloop()
