import tkinter as tk

class MainApp():
    def __init__ (self, root):
        self.root = root
        self.root.title("Canvas Demo")
        self.root.geometry("800x600")
        self.canvas_ui()
    
    def canvas_ui(self):
        self.canvas = tk.Canvas(self.root,
                                width=600,
                                height=400,
                                bg="white")
        self.canvas.create_line((50, 50), (100, 100), width=4, fill="red")
        self.canvas.pack(anchor=tk.CENTER, expand=True)

if __name__ == "__main__":
    root = tk.Tk()
    MainApp(root)
    root.mainloop()