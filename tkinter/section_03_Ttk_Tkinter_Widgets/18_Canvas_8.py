import tkinter as tk

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("800x600")
    root.title("Canvas Demo - Binding Event")

    canvas = tk.Canvas(root, width=600, height=400, bg="white")
    canvas.pack(anchor=tk.CENTER, expand=True)

    python_image = tk.PhotoImage(file="./000_testing_gifs/python.gif")
    python_image = python_image.subsample(5, 5)
    canvas.create_image((100, 100),
                        image=python_image)
    
    root.mainloop()