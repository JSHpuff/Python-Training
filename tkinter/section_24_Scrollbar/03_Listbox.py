import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Listbox with Scrollbar')
        self.geometry('200x200')
        self.setFrame()
        self.setScrollbar()
        self.setMenu()
        self.setListbox()
        self.configScrollbar()
    def setFrame(self):
        self.frame = tk.Frame(self, width=15)
        self.frame.pack()
    def setScrollbar(self):
        self.scrollbar = tk.Scrollbar(self.frame)
        self.scrollbar.pack(side='right', fill='y')
    def setMenu(self):
        self.menu = tk.StringVar()
        self.menu.set(
            (
                'Apple', 'Banana', 'Orange', 'Grap',
                'Papaya', 'Coconut', 'Pear', 'Nuts'
            )
        )
    def setListbox(self):
        self.listbox = tk.Listbox(
            self.frame,
            listvariable=self.menu,
            height=6, width=15,
            yscrollcommand=self.scrollbar.set
        )
        self.listbox.pack(side='left', fill='y')
    def configScrollbar(self):
        self.scrollbar.config(command=self.listbox.yview)

if __name__ == "__main__":
    app = App()
    app.mainloop()