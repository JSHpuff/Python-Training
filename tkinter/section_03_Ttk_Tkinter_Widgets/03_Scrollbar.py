import tkinter as tk
from tkinter import ttk

class MainApp():
    def __init__(self, root):
        self.root = root
        self.root.title("Tkinter Scrollbar")

        self.ui()

    def ui(self):
        self.frame = ttk.Frame(self.root)
        self.frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        # Create a scrollbar and add it to the frame
        self.v_scrollbar = ttk.Scrollbar(self.frame)
        self.v_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Create a text widget and add it to the frame
        self.text = tk.Text(self.frame, height=8)
        self.text.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)

        # Configure scrollbar
        self.text["yscrollcommand"] = self.v_scrollbar.set
        self.v_scrollbar.config(command=self.text.yview)

        # Insert some text into the text widget
        self.text.insert(tk.END, "\n" * 20)


if __name__ == "__main__":
    root = tk.Tk()
    MainApp(root)
    root.mainloop()