import tkinter as tk
from tkinter import ttk

class InputFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(0, weight=3)
        self.__create_widgets()
    
    def __create_widgets(self):
        ttk.Label(self, text="Find what:").grid(column=0, row=0, sticky=tk.W)
        keyword = ttk.Entry(self, width=30)
        keyword.focus()
        keyword.grid(column=1, row=0, sticky=tk.W)

        ttk.Label(self, text="Replace with:").grid(
            column=0, row=1, sticky=tk.W
        )
        replacement = ttk.Entry(self, width=30)
        replacement.grid(column=1, row=1, sticky=tk.W)

        match_case = tk.StringVar()
        match_case_check = ttk.Checkbutton(
            self,
            text="Match case",
            variable=match_case,
            command=lambda: print(match_case.get())
        )
        match_case_check.grid(column=0, row=2, sticky=tk.W)

        wrap_around = tk.StringVar()
        wrap_around_check = ttk.Checkbutton(
            self,
            variable=wrap_around,
            text="Wrap around",
            command=lambda: print(wrap_around.get())
        )
        wrap_around_check.grid(column=0, row=3, sticky=tk.W)

        # winfo_children:
        # returns a list of all direct child widgets of the current widget
        for widget in self.winfo_children():
            widget.grid(padx=0, pady=5)

class ButtonFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        self.columnconfigure(0, weight=1)
        self.__create_widgets()
    
    def __create_widgets(self):
        ttk.Button(self, text="Find Next").grid(column=0, row=0)
        ttk.Button(self, text="Replace").grid(column=0, row=1)
        ttk.Button(self, text="Replace All").grid(column=0, row=2)
        ttk.Button(self, text="Cancel").grid(column=0, row=3)
        for widget in self.winfo_children():
            widget.grid(padx=0, pady=3)

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Replace")
        self.geometry("400x150")
        self.resizable(0, 0)
        self.attributes("-toolwindow", True)

        self.columnconfigure(0, weight=4)
        self.columnconfigure(1, weight=1)

        self.__create_widgets()
    
    def __create_widgets(self):
        input_frame = InputFrame(self)
        input_frame.grid(column=0, row=0)

        button_frame = ButtonFrame(self)
        button_frame.grid(column=1, row=0)

if __name__ == "__main__":
    app = App()
    app.mainloop()