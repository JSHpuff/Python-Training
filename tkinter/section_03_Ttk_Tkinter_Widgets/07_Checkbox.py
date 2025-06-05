import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

class MainApp():
    def __init__(self, root):
        self.root = root
        self.root.title("Checkbox Demo")
        self.root.geometry("300x200")

        self.ui()

    def ui(self):
        self.agreement_var = tk.BooleanVar()
        self.checkbox = ttk.Checkbutton(
            self.root,
            text="I agree",
            command=self.show_message,
            variable=self.agreement_var
        )
        self.checkbox.pack()
    
    def show_message(self):
        showinfo(
            title="Result",
            message="You agreed." if self.agreement_var.get() 
                else "You did not agree."
        )

if __name__ == "__main__":
    root = tk.Tk()
    MainApp(root)
    root.mainloop()