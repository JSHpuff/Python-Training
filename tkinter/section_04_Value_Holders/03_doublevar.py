import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

root = tk.Tk()
root.geometry("400x300")
root.title("DoubleVar Demo")

amount_var = tk.DoubleVar()

label = ttk.Label(root, text="Amount:")
label.pack(side=tk.LEFT, padx=5, pady=10, anchor=tk.W)

amount_entry = ttk.Entry(root, textvariable=amount_var)
amount_entry.pack(side=tk.LEFT, padx=5, pady=10, anchor=tk.W)

button = ttk.Button(
    root, text="Submit",
    command=lambda: showinfo(
        title="Amount",
        message=amount_var.get()
    )
)
button.pack(side=tk.LEFT, padx=5, pady=10, anchor=tk.W)


root.mainloop()