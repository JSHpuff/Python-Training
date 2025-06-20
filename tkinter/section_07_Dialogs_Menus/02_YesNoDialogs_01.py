import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import askyesno

root = tk.Tk()
root.title("Tkinter Yes/No Dialog")
root.geometry("350x150")

# Click Event Handler
def confirm():
    answer = askyesno(
        title="confirmation",
        message="Are you sure that you want to quit?"
    )
    if answer:
        root.destroy()
    
ttk.Button(
    root,
    text="Ask Yes/No",
    command=confirm
).pack(expand=True)

root.mainloop()