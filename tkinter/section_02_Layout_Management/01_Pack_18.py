import tkinter as tk
from tkinter import ttk

class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("320x200")

        self.build_ui()
    
    def build_ui(self):
        fields = {}
        fields["username_label"] = ttk.Label(self.root, text="Username: ")
        fields["username"] = ttk.Entry(self.root)

        fields["password_label"] = ttk.Label(self.root, text="Password: ")
        fields["password"] = ttk.Entry(self.root, show="*")

        for field in fields.values():
            field.pack(anchor=tk.W, padx=10, pady=5, fill=tk.X)
        
        ttk.Button(text="Login").pack(anchor=tk.W, padx=10, pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    MainApp(root)
    root.mainloop()