import tkinter as tk

class MainApp():
    def __init__ (self, root):
        self.root = root
        self.root.title("Canvas Demo - Text")
        self.root.geometry("800x600")
        self.canvas_ui()
    
    def canvas_ui(self):
        self.canvas = tk.Canvas(
            self.root,
            width=600,
            height=400,
            bg="white"
        )
        self.canvas.pack(
            anchor=tk.CENTER, expand=True
        )
        self.canvas.create_text(
            (300, 100),
            text="Canvas Demo",
            fill="orange",
            font="tkDefaultFont 24"
        )

if __name__ == "__main__":
    root = tk.Tk()
    MainApp(root)
    root.mainloop()