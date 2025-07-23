import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.title('Adding Icon to Menu')
root.geometry('200x200')

img = Image.open('./000_testing_imgs/city.png')
img = img.resize((20, 20))
icon = ImageTk.PhotoImage(img)

menu = tk.Menu(root)

menubar = tk.Menu(menu)
menubar.add_command(label='Open', image=icon, command='left')
menubar.add_command(label='Save')
menubar.add_command(label='Exit')
menu.add_cascade(label='File', menu=menubar)

root.config(menu=menu)

root.mainloop()