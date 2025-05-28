import tkinter as tk
import os

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Tkinter Pack Layout")
    window_width = 600
    window_height = 400
    root.geometry(f"{window_width}x{window_height}")
    
    try:
        if os.path.exists("./000_testing_imgs/test_icon.ico"):
            root.iconbitmap("./000_testing_imgs/test_icon.ico")
    except Exception as e:
        print(f"Icon load failed: {e}")

    root.attributes("-alpha", 0.9)

    label1 = tk.Label(root, text="Tkinter", bg="red", fg="white")
    label2 = tk.Label(root, text="Pack Layout", bg="green", fg="white")
    label3 = tk.Label(root, text="Demo", bg="blue", fg="white")

    label1.pack(side=tk.BOTTOM, pady=10)
    label2.pack(side=tk.BOTTOM, pady=10)
    label3.pack(side=tk.BOTTOM, pady=10)

    root.mainloop()