import tkinter as tk
from tkinter import ttk

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        # Root Window
        self.title('Theme Demo')
        self.geometry('450x300')
        self.style = ttk.Style(self)

        # Label
        label = ttk.Label(self, text='Name:')
        label.grid(column=0, row=0, padx=10, pady=10, sticky='w')

        # Entry
        textbox = ttk.Entry(self)
        textbox.grid(column=1, row=0, padx=10, pady=10, sticky='w')

        # Button
        btn = ttk.Button(self, text='Show')
        btn.grid(column=2, row=0, padx=10, pady=10, sticky='w')

        # Radio Button
        self.selected_theme = tk.StringVar()
        theme_frame = ttk.LabelFrame(self, text='Themes')
        theme_frame.grid(padx=10, pady=10, ipadx=20, ipady=20, sticky='w')

        for theme_name in self.style.theme_names():
            rb = ttk.Radiobutton(
                theme_frame,
                text=theme_name,
                value=theme_name,
                variable=self.selected_theme,
                command=self.change_theme
            )
            rb.pack(expand=True, fill='both')
    
    def change_theme(self):
        self.style.theme_use(self.selected_theme.get())

if __name__ == "__main__":
    app = App()
    app.mainloop()