# Use the pack geometry manager to arrange widgets on a window
# Tkinter pack parameters

import tkinter as tk

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Tkinter Pack Layout")
    window_width = 600
    window_height = 400
    root.geometry(f"{window_width}x{window_height}")

    tk.Label(root, text="Tkinter", bg="red", fg="white").pack(pady=20)
    tk.Label(root, text="Pack Layout", bg="green", fg="white").pack(pady=20)
    tk.Label(root, text="Demo", bg="blue", fg="white").pack(pady=20)

    root.mainloop()
