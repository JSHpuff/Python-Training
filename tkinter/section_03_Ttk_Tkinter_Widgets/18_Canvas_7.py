import tkinter as tk
import os

def main (root):
    root.title("Canvas Demo - Image")
    root.geometry("800x600")
    
    python_image = tk.PhotoImage(
        file="./000_testing_imgs/python.png"
    )

    canvas = tk.Canvas(
        root,
        width=600, height=400, bg="white"
    )
    canvas.pack(anchor=tk.CENTER, expand=True)
    canvas.create_image(
        (100, 100),
        image=python_image
    )

    canvas.image = python_image

if __name__ == "__main__":
    root = tk.Tk()
    main(root)
    root.mainloop()