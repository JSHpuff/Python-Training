import tkinter as tk

class MainApp():
    def __init__ (self, root):
        self.root = root
        self.root.title("Cursor")
        self.root.geometry("300x300")
        self.root.config(cursor="watch")

if __name__ == "__main__":
    root = tk.Tk()
    MainApp(root)
    root.mainloop()