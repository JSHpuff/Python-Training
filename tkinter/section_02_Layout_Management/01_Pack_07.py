import tkinter as tk

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Tkinter Pack Layout")
    root.geometry("600x400")

    label1 = tk.Label(root, text="Tkinter", bg="red", fg="white")
    label2 = tk.Label(root, text="Pack Layout", bg="green", fg="white")
    label3 = tk.Label(root, text="Demo", bg="blue", fg="white")

    label1.pack(side=tk.TOP, expand=True)
    label2.pack(side=tk.TOP, expand=False)
    label3.pack(side=tk.TOP, expand=False)

    root.mainloop()