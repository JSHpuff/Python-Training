import tkinter as tk

root = tk.Tk()
root.title("Text Widget Example")

text = tk.Text(root, height=8)
text.pack(padx=8, pady=8, expand=True, fill=tk.BOTH)
text.insert(index="1.0", chars="This is a Text widget demo")

image = tk.PhotoImage(file="./000_testing_imgs/python.png")
text.image_create("1.0", image=image)

root.mainloop()