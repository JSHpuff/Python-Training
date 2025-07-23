import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.title('Using with Canvas')
root.geometry('400x400')

img = Image.open('./000_testing_imgs/city.png')
img_tk = ImageTk.PhotoImage(img)

canvas = tk.Canvas(root, width=400, height=400)
canvas.create_image(0, 0, anchor='nw', image=img_tk)
canvas.pack()

root.mainloop()