import tkinter as tk

class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tkinter Pack Layout")
        self.root.geometry("600x400")

        self.build_ui()
    
    def build_ui(self):
        label1 = tk.Label(self.root, text="Tkinter", bg="red", fg="white")
        label2 = tk.Label(self.root, text="Pack Layout", bg="green", fg="white")
        label3 = tk.Label(self.root, text="Demo", bg="blue", fg="white")

        label1.pack(side=tk.LEFT, expand=True)
        label2.pack(side=tk.LEFT, expand=True)
        label3.pack(side=tk.LEFT, expand=True)

if __name__ == "__main__":
    root = tk.Tk()
    MainApp(root)
    root.mainloop()