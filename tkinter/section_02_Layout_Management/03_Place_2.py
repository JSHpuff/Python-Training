import tkinter as tk

class MainApp():
    def __init__(self, root):
        self.root = root
        self.root.title("Tkinter Place Geometry Manager")
        window_width = 600
        window_height = 400
        self.root.geometry(f"{window_width}x{window_height}")

        self.ui()
    
    def ui(self):
        label1 = tk.Label(master=self.root, text="Place", bg="red", fg="white")
        label1.place(relx=0.5, rely=0.5, width=100, height=50)
    
if __name__ == "__main__":
    root = tk.Tk()
    MainApp(root)
    root.mainloop()