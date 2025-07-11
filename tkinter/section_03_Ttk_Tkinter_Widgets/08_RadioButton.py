import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

root = tk.Tk()
root.geometry("300x220")
root.resizable(False, False)
root.title("Radio Button Demo")

def show_selected_size():
    showinfo(
        title="Result",
        message=selected_size.get()
    )

selected_size = tk.StringVar()
sizes = (("Small", "S"),
        ("Medium", "M"),
        ("Large", "L"),
        ("Extra Large", "XL"),
        ("Extra Extra Large", "XXL"))

label = ttk.Label(text="What's your t-shirt size?")
label.pack(fill="x", padx=5, pady=5)

for size in sizes:
    r = ttk.Radiobutton(
        root,
        text=size[0],
        value=size[1],
        variable=selected_size
    )
    r.pack(fill="x", padx=5, pady=5)

button = ttk.Button(
    root,
    text="Get Selected Size",
    command=show_selected_size
)
button.pack(fill="x", padx=5, pady=5)

root.mainloop()