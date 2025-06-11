import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

class MainApp(tk.Tk):
    def __init__ (self):
        super().__init__()
        self.geometry("400x300")
        self.title("IntVar Demo")
        self.quantity_var = tk.IntVar()
        self.label_ui()
        self.entry_ui()
        self.button_ui()
    
    def label_ui(self):
        label = ttk.Label(self, text="Quantity:")
        label.pack(
            side=tk.LEFT, padx=5,pady=10, anchor=tk.W
        )
    
    def entry_ui(self):
        quantity_entry = ttk.Entry(
            self, textvariable=self.quantity_var
        )
        quantity_entry.pack(
            side=tk.LEFT, padx=5, pady=10, anchor=tk.W
        )
    
    def button_ui(self):
        button = ttk.Button(
            self,
            text="Submit",
            command=lambda: showinfo(
                title="Quantity",
                message=self.quantity_var.get()
            )
        )
        button.pack(
            side=tk.LEFT, padx=5, pady=10, anchor=tk.W
        )

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()