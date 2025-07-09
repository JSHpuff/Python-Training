# Element options
import tkinter as tk
from tkinter import ttk

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        style = ttk.Style(self)

        # Layout
        layout = style.layout('TLabel')
        print(layout)

        # Element options
        print(style.element_options('Label.border'))
        print(style.element_options('Label.padding'))
        print(style.element_options('Label.label'))

if __name__ == "__main__":
    app = App()
    app.mainloop()