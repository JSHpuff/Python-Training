import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

class MainApp():
    def __init__(self, root):
        self.root = root
        self.root.title("Text Widget Example")

        self.text_ui()
        self.button_ui()
    
    def text_ui(self):
        self.text = tk.Text(self.root, height=8)
        self.text.pack(padx=10, pady=10, expand=True, fill=tk.BOTH)
        # fill=tk.BOTH: expand fill both horizontally and vertically
        self.text.insert(
            index="1.0",
            chars="This is a Text widget demo"
        )

    def button_ui(self):
        self.get_button = ttk.Button(
            self.root,
            text="Get Text",
            command=lambda: showinfo(
                title="Text Data",
                message=self.text.get("1.0", tk.END)
            )
        )
        self.get_button.pack(padx=10, pady=10, side=tk.LEFT)

        self.clear_button = ttk.Button(
            self.root,
            text="Clear All Text",
            command=lambda: self.text.delete("1.0", tk.END)
        )
        self.clear_button.pack(padx=10, pady=10, side=tk.RIGHT)

if __name__ == "__main__":
    root = tk.Tk()
    MainApp(root)
    root.mainloop()