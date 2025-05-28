# Anchor
"""
    - 'n':          North or Top Center
    - 's':          South or Bottom Center
    - 'e':          East or Right Center
    - 'w':          West or Left Center
    - 'nw':         North West or Top Left
    - 'ne':         North East or Top Right
    - 'se':         South East or Bottom Right
    - 'sw':         South West or Bottom Left
    - 'center':     Center
"""

import tkinter as tk

class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Pack Demo")
        self.root.geometry("350x200")

        self.build_ui()
    
    def build_ui(self):
        box1 = tk.Label(self.root, text="Box 1", bg="green", fg="white")
        box2 = tk.Label(self.root, text="Box 2", bg="red", fg="white")

        box1.pack(ipadx=20, ipady=20, anchor=tk.E, expand=True)
        box2.pack(ipadx=20, ipady=20, anchor=tk.W, expand=True)

if __name__ == "__main__":
    root = tk.Tk()
    MainApp(root)
    root.mainloop()