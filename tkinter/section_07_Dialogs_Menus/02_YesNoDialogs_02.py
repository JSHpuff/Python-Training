import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import askyesno

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Tkinter Yes/No Dialog")
        self.geometry("350x150")

        # Quit Button
        quit_button = ttk.Button(self, text="Quit", command=self.confirm)
        quit_button.pack(expand=True)

    def confirm(self):
        answer = askyesno(
            title="Confirmation",
            message="Are you sure that you wnat to quit?"
        )
        if answer:
            self.destroy()
        
if __name__ == "__main__":
    app = App()
    app.mainloop()