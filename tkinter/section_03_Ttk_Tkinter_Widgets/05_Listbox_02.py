import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.title("Listbox")
root.geometry("400x180")

# Create a variable object
languages = ("Java", "C", "C++", "C#", "Python", "Go", "JavaScript", "PHP", "Swift")
list_variable = tk.Variable(value=languages)

# Label
label = ttk.Label(
    root,
    text="Select your favorite programming languages:"
)
label.pack(padx=10, pady=0, side=tk.TOP, fill=tk.X)

listbox = tk.Listbox(
    root,
    listvariable=list_variable,
    height=6,
    selectmode=tk.MULTIPLE,
)

listbox.pack(padx=10, pady=10, expand=True, fill=tk.BOTH, side=tk.LEFT)

root.mainloop()