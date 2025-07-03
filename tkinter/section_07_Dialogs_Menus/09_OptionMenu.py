import tkinter as tk
from tkinter import ttk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("350x80")
        self.title("Tkinter OptionMenu Widget")

        # Initialize Data
        self.languages = ('Python', 'JavaScript', 'Java',
                          'Swift', 'GoLang', 'C#', 'C++', 'Scala')

        # Setup Variables
        self.option_var = tk.StringVar(self)

        # Create Widget
        self.create_widgets()
    
    def create_widgets(self):
        # Padding for widgets using the grid layout
        paddings = {'padx': 5, 'pady':5}

        # Label
        label = ttk.Label(self, text='Select your most favorite language:')
        label.grid(column=0, row=0, sticky=tk.W, **paddings)

        # Option Menu
        option_menu = ttk.OptionMenu(
            self,
            self.option_var,
            self.languages[0],
            *self.languages,
            command=self.option_changed
        )

        option_menu.grid(column=1, row=0, sticky=tk.W, **paddings)

        # Output Label
        self.output_label = ttk.Label(self, foreground='red')
        self.output_label.grid(column=0, row=1, sticky=tk.W, **paddings)
    
    def option_changed(self, *args):
        self.output_label['text'] = f"You selected: {self.option_var.get()}"
    
if __name__ == "__main__":
    app = App()
    app.mainloop()