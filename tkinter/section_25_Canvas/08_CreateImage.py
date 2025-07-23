import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.title('Create Image in the Canvas')
root.geometry('300x300')

img = Image.open('./000_testing_imgs/city.png')
tk_img = ImageTk.PhotoImage(img)

canvas = tk.Canvas(root, width=300, height=300)
canvas.create_image(0, 0, anchor='nw', image=tk_img)
canvas.pack()

root.mainloop()