import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class MainApp():
    def __init__ (self, root):
        self.root = root
        self.root.title("Tkinter Treeview")
        self.root.geometry("700x300")
        self.icon_city = ImageTk.PhotoImage(Image.open("./000_testing_imgs/city.png").resize((20, 20)))
        self.icon_male = ImageTk.PhotoImage(Image.open("./000_testing_imgs/male.png").resize((20, 20)))
        self.icon_female = ImageTk.PhotoImage(Image.open("./000_testing_imgs/female.png").resize((20, 20)))
        self.treeview_ui()

    def treeview_ui(self):
        self.frame = ttk.Frame(self.root)
        self.treeview = ttk.Treeview(self.frame, columns=("Salary", "Bonus"))
        self.treeview.heading("#0", text="Employee")
        self.treeview.heading("Salary", text="Salary")
        self.treeview.heading("Bonus", text="Bonus")

        level1 = self.treeview.insert("", tk.END, text="San Jose", image=self.icon_city)
        self.treeview.insert(level1, tk.END, text="John Doe",
                             values=(f"${100000: ,}", f"${8000: ,}"),
                             image=self.icon_male)
        self.treeview.insert(level1, tk.END, text="Jane Doe",
                             values=(f"${120000: ,}", f"${9000: ,}"),
                             image=self.icon_female)

        v_scrollbar = ttk.Scrollbar(self.frame, orient=tk.VERTICAL, 
                                    command=self.treeview.yview)
        self.treeview.configure(yscrollcommand=v_scrollbar.set)

        self.treeview.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        v_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)


if __name__ == "__main__":
    root = tk.Tk()
    MainApp(root)
    root.mainloop()
