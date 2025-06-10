import tkinter as tk

class MainApp():
    def __init__ (self, root):
        self.root = root
        self.root.geometry("300x300")
        self.root.bind("<Motion>", self.change_cursor)
    
    def change_cursor(self, event):
        if event.x in range(100, 300):
            self.root.config(cursor="watch")
        else:
            self.root.config(cursor="")
    
if __name__ == "__main__":
    root = tk.Tk()
    MainApp(root)
    root.mainloop()