import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("300x200")
root.title("Separator Widget Demo")

# Left frame
left_frame = tk.Frame(root)
left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
ttk.Label(left_frame, text="Left frame").pack(pady=20)

# right frame
right_frame = tk.Frame(root)
right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
ttk.Label(right_frame, text="Right frame").pack(pady=20)


# Create a vertical separator
separator = ttk.Separator(root, orient=tk.VERTICAL)
separator.pack(side=tk.LEFT, fill=tk.Y, padx=5)

root.mainloop()