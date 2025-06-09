import tkinter as tk

class MainApp():
    def __init__ (self, root):
        self.root = root
        self.root.title("Canvas Demo - Oval")
        self.root.geometry("800x600")

        self.points = ((50, 150), (200, 350),)

        self.canvas_ui()

    def canvas_ui(self):
        self.canvas = tk.Canvas(
            self.root,
            width=600,
            height=400,
            bg="white"
        )
        self.canvas.pack(anchor=tk.CENTER, expand=True)
        self.canvas.create_oval(*self.points, fill="purple")

if __name__ == "__main__":
    root = tk.Tk()
    MainApp(root)
    root.mainloop()
