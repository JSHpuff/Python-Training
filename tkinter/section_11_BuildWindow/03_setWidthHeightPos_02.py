import tkinter as tk

root = tk.Tk()
root.title("Hello")

window_width = root.winfo_screenwidth()
window_height = root.winfo_screenheight()

width = 600
height = 400
left = int((window_width - width) / 2)
top = int((window_height - height) / 2)
root.geometry(f"{width}x{height}+{left}+{top}")

root.mainloop()