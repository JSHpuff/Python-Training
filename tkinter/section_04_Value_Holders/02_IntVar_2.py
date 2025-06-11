import tkinter as tk
from tkinter import ttk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("400x300")
        self.title("Scale Example with IntVar and ttk")
        self.create_ui()
    
    def create_ui(self):
        int_var = tk.IntVar()
        scale = ttk.Scale(
            self,
            from_=0,
            to=100,
            orient=tk.HORIZONTAL,
            variable=int_var,
            command=lambda val: label.config(
                text=f"Scale Value: {int_var.get()}"
            )
        )
        scale.pack(pady=20)

        label = ttk.Label(
            self, text="Scale Value: 0"
        )
        label.pack(pady=10)

if __name__ == "__main__":
    app = App()
    app.mainloop()