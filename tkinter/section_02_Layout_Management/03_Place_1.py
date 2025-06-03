import tkinter as tk

class MainAPP():
    def __init__(self, root):
        self.root = root
        self.root.title("Tkinter Place Geometry Manager")
        window_width = 600
        window_height = 400
        self.root.geometry(f"{window_width}x{window_height}")

        self.ui()
    
    def ui(self):
        label1 = tk.Label(master=self.root, text="Place", bg="red", fg="white")
        label1.place(x=0, y=0, width=120, height=60)

if __name__ == "__main__":
    root = tk.Tk()
    MainAPP(root)
    root.mainloop()