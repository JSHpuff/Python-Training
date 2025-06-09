import tkinter as tk
from tkinter import ttk

class MainApp():
    def __init__(self, root):
        self.root = root
        self.root.title("Tkinter Treeview")
        self.root.geometry("500x300")
        self.treeview_ui()
    
    def treeview_ui(self):
        self.treeview = ttk.Treeview()
        self.treeview.pack(padx=10, pady=10, expand=True, fill=tk.BOTH)


if __name__ == "__main__":
    root = tk.Tk()
    MainApp(root)
    root.mainloop()