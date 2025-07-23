import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.title('Using Label')
root.geometry('200x200')

img = Image.open('./000_testing_imgs/city.png')
tk_img = ImageTk.PhotoImage(img)

label = tk.Label(root, image=tk_img, width=200, height=200)
label.pack()

root.mainloop()