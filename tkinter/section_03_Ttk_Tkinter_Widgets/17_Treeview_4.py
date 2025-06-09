import tkinter as tk
from tkinter import ttk

class MainApp():
    def __init__ (self, root):
        self.root = root
        self.root.title("Tkinter Treeview")
        self.treeview_ui()
    
    def treeview_ui(self):
        self.treeview = ttk.Treeview(columns=("Salary", "Bonus"))
        self.treeview.heading("#0", text="Employee")
        self.treeview.heading("Salary", text="Salary")
        self.treeview.heading("Bonus", text="Bonus")

        level1 = self.treeview.insert("", tk.END, text="San Jose")
        self.treeview.insert(level1, tk.END, text="John Doe",
                             values=(f"${100000: ,}", f"${8000: ,}"))
        self.treeview.insert(level1, tk.END, text="Jane Doe",
                             values=(f"${120000: ,}", f"${9000: ,}"))
        self.treeview.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    MainApp(root)
    root.mainloop()