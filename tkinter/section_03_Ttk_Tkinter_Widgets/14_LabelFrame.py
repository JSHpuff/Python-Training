import tkinter as tk
from tkinter import ttk

root = tk.Tk()

root.geometry("300x200")
root.resizable(False, False)
root.title("LabelFrame Demo")

lf = ttk.LabelFrame(root, text="Alignment")
lf.grid(column=0, row=0, padx=20, pady=20)

alignment_var = tk.StringVar()
alignments = ("Left", "Center", "Right")

grid_column = 0
for alignment in alignments:
    radio = ttk.Radiobutton(
        lf, 
        text=alignment,
        value=alignment,
        variable=alignment_var
        )
    radio.grid(
        column=grid_column,
        row=0,
        ipadx=10, ipady=10
    )
    grid_column += 1

root.mainloop()
