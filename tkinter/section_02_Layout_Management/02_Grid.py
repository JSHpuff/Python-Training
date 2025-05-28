# Introduction to the Tkinter grid geometry manager

import tkinter as tk
from tkinter import ttk

class MainApp():
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("240x100")
        self.root.iconbitmap("./000_testing_imgs/test_icon.ico")

        self.grid()
        self.username()
        self.password()
        self.login_button()

    def grid(self):
        self.root.rowconfigure(0, weight=1)
        self.root.rowconfigure(1, weight=1)
        self.root.rowconfigure(2, weight=1)
        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=3)
    
    def username(self):
        username_label = ttk.Label(self.root, text="Username: ")
        username_label.grid(column=0, row=0, sticky=tk.EW, padx=5, pady=5)

        username_entry = ttk.Entry(self.root)
        username_entry.grid(column=1, row=0, sticky=tk.EW, padx=5, pady=5)
    
    def password(self):
        username_label = ttk.Label(self.root, text="Password: ")
        username_label.grid(column=0, row=1, sticky=tk.EW, padx=5, pady=5)

        username_entry = ttk.Entry(self.root, show="*")
        username_entry.grid(column=1, row=1, sticky=tk.EW, padx=5, pady=5)

    def login_button(self):
        login_button = ttk.Button(self.root, text="Login")
        login_button.grid(column=1, row=3, sticky=tk.E, padx=5, pady=5)

if __name__ == "__main__":
    root = tk.Tk()
    MainApp(root)
    root.mainloop()