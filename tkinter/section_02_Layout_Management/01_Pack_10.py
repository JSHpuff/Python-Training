import tkinter as tk
from tkinter import ttk

class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tkinter Pack Layout")
        self.root.geometry("300x200")

        self.build_ui()
    
    def build_ui(self):
        name_label = ttk.Label(self.root, text="Name: ")
        name_entry = ttk.Entry(self.root)
        button = ttk.Button(self.root, text="Submit")

        name_label.pack(side=tk.LEFT)
        name_entry.pack(side=tk.LEFT, expand=True)
        button.pack(side=tk.LEFT)

if __name__ == "__main__":
    root = tk.Tk()
    MainApp(root)
    root.mainloop()