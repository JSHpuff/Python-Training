import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Separator Widget Demo")
root.geometry("300x200")

# top frame
top_frame = tk.Frame(root)
top_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
ttk.Label(top_frame, text="Top frame").pack(pady=20)

# Create a horizontal separator
separator = ttk.Separator(root, orient=tk.HORIZONTAL)
separator.pack(side=tk.TOP, fill=tk.X, pady=5)

# Bottom frame
bottom_frame = tk.Frame(root)
bottom_frame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
ttk.Label(bottom_frame, text="Bottom frame").pack(pady=20)

root.mainloop()