import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Adding Label Frame')
        self.geometry('200x200')
        self.setGroup()
        self.setLabel()
    def setGroup(self):
        self.group = tk.LabelFrame(
            self, text='test',
            padx=10, pady=10
        )
        self.group.pack()
    def setLabel(self):
        a = tk.Label(self.group, text='AAA').pack()
        b = tk.Label(self.group, text='BBB').pack()
        c = tk.Label(self.group, text='CCC').pack()

if __name__ == "__main__":
    app = App()
    app.mainloop()
