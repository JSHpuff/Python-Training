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
        label3 = tk.Label(self.root, text="Fill", bg="blue", fg="white")
        label4 = tk.Label(self.root, text="Demo", bg="purple", fg="white")

        label1.pack(side=tk.TOP, expand=True, fill=tk.X)
        label2.pack(side=tk.TOP, expand=True, fill=tk.Y)
        label3.pack(side=tk.TOP, expand=True, fill=tk.NONE)
        label4.pack(side=tk.TOP, expand=True, fill=tk.BOTH)

if __name__ == "__main__":
    root = tk.Tk()
    MainApp(root)
    root.mainloop()