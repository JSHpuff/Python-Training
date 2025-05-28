# Internal paddings: ipadx & ipady

import tkinter as tk

class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tkinter Pack Layout")
        self.root.geometry("600x400")

        self.build_ui()
    
    def build_ui(self):
        label1 = tk.Label(self.root, text="Pack", bg="red", fg="white")
        label2 = tk.Label(self.root, text="Pack", bg="green", fg="white")
        label3 = tk.Label(self.root, text="Pack", bg="blue", fg="white")
        label4 = tk.Label(self.root, text="Pack", bg="purple", fg="white")

        label1.pack(side=tk.TOP, fill=tk.X, pady=10)
        label2.pack(side=tk.TOP, fill=tk.X, pady=20)
        label3.pack(side=tk.TOP, fill=tk.X, pady=40)
        label4.pack(side=tk.TOP, fill=tk.X, pady=60)

if __name__ == "__main__":
    root = tk.Tk()
    MainApp(root)
    root.mainloop()