import tkinter as tk
from tkinter import ttk

class MainApp():
    def __init__ (self, root):
        self.root = root
        self.root.title("Tkinter Treeview")
        self.root.geometry("400x300")
        self.treeview_ui()
    
    def treeview_ui(self):
        self.treeview = ttk.Treeview()
        level1 = self.treeview.insert("", tk.END, text="San Jose")
        self.treeview.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)


if __name__ == "__main__":
    root = tk.Tk()
    MainApp(root)
    root.mainloop()