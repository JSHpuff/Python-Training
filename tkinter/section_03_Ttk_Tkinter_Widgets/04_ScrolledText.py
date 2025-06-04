import tkinter as tk
from tkinter.scrolledtext import ScrolledText

class MainApp():
    def __init__(self, root):
        self.root = root
        self.root.title("ScrolledText Widget")

        self.text_ui()
    
    def text_ui(self):
        self.text = ScrolledText(self.root, width=80, height=8)
        self.text.pack(padx=10, pady=10, fill=tk.BOTH, side=tk.LEFT, expand=True)
    
if __name__ == "__main__":
    root = tk.Tk()
    MainApp(root)
    root.mainloop()
    