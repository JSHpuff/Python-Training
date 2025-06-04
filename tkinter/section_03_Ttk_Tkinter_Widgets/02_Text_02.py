import tkinter as tk

class MainApp():
    def __init__(self, root):
        self.root = root
        self.root.title("Text Widget Example")

        self.text_ui()

    def text_ui(self):
        text = tk.Text(self.root, height=8)
        text.pack(padx=10, pady=10, expand=True, fill=tk.BOTH)
        text.insert(
            index='1.0',
            chars='This is a Text widget demo'
        )

if __name__ == "__main__":
    root = tk.Tk()
    MainApp(root)
    root.mainloop()
