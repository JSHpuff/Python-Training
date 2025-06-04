import tkinter as tk
from tkinter import ttk

class MainApp():
    def __init__ (self, root):
        # Create the main window
        self.root = root
        self.root.title("Listbox")
        self.root.geometry("400x180")

        self.ui()

    def ui(self):
        # Create a variable object
        languages = ("Java", "C", "C++",
                     "C#", "Python", "Go",
                     "JavaScript", "PHP",
                     "Swift")
        self.list_variable = tk.Variable(value=languages)

        # Label
        self.label = ttk.Label(
            self.root,
            text="Select your favorite programming languages"
        )
        self.label.pack(padx=10, pady=10, side=tk.TOP, fill=tk.X)

        self.listbox = tk.Listbox(
            self.root,
            listvariable=self.list_variable,
            height=6,
        )
        self.listbox.pack(padx=10, pady=10, expand=True, fill=tk.BOTH, side=tk.LEFT)

if __name__ == "__main__":
    root = tk.Tk()
    MainApp(root)
    root.mainloop()