import tkinter as tk
from turtle import width

class MainApp():
    def __init__ (self, root):
        self.root = root
        self.root.title("Canvas Demo - Arc")
        self.root.geometry("800x600")
        self.canvas_ui()
    
    def canvas_ui(self):
        self.canvas = tk.Canvas(
            self.root, 
            width=600,
            height=600,
            bg="white"
        )
        self.canvas.pack(anchor=tk.CENTER, expand=True)
        self.canvas.create_arc((10, 10), (200, 200),
                               style=tk.PIESLICE,
                               width=2)
        self.canvas.create_arc((10, 200), (200, 390),
                               style=tk.CHORD,
                               width=2)
        self.canvas.create_arc((10, 400), (200, 590),
                               style=tk.ARC,
                               width=2)
    
if __name__ == "__main__":
    root = tk.Tk()
    MainApp(root)
    root.mainloop()