import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk  # Better handling

class MainApp():
    def __init__(self, root):
        self.root = root
        self.root.title("Tkinter Treeview")
        self.root.geometry("700x300")

        # Load images AFTER root is ready
        self.icon_city = ImageTk.PhotoImage(Image.open("./000_testing_imgs/city.png").resize((20, 20)))
        self.icon_male = ImageTk.PhotoImage(Image.open("./000_testing_imgs/male.png").resize((20, 20)))
        self.icon_female = ImageTk.PhotoImage(Image.open("./000_testing_imgs/female.png").resize((20, 20)))

        # Create Treeview
        self.treeview = ttk.Treeview(self.root, columns=("Salary", "Bonus"))
        self.treeview.heading("#0", text="Employee")
        self.treeview.heading("Salary", text="Salary")
        self.treeview.heading("Bonus", text="Bonus")
        self.treeview.column("#0", width=160)

        # Insert items
        level1 = self.treeview.insert("", tk.END, text="San Jose", image=self.icon_city)
        self.treeview.insert(level1, tk.END, text="John Doe", image=self.icon_male, 
                             values=("$100,000", "$8,000"))
        self.treeview.insert(level1, tk.END, text="Jane Doe", image=self.icon_female, 
                             values=("$120,000", "$9,000"))

        self.treeview.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()
