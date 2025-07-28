import os 
os.chdir('/')

import tkinter as tk
from tkinter import Variable, filedialog
from PIL import Image, ImageTk

root = tk.Tk()
root.title('Open Image')
root.geometry('300x360')

def show():
    img_path = filedialog.askopenfilename(filetypes=[
        ('png', '*.png'), 
        ('jpg', '*.jpg'),
        ('gif', '*.gif')])
    img = Image.open(img_path)
    w, h = img.size
    tk_img = ImageTk.PhotoImage(img)
    canvas.delete('all')
    canvas.config(scrollregion=(0, 0, w, h))
    canvas.create_image(0, 0, anchor='nw', image=tk_img)
    canvas.tk_img = tk_img

button = tk.Button(root, text='Open Figure', command=show)
button.pack()

frame = tk.Frame(root, width=300, height=300)
frame.pack()

canvas = tk.Canvas(frame, width=300, height=300, bg='#fff')

scrollX = tk.Scrollbar(frame, orient='horizontal')
scrollX.pack(side='bottom', fill='x')
scrollX.config(command=canvas.xview)

scrollY = tk.Scrollbar(frame, orient='vertical')
scrollY.pack(side='right', fill='y')
scrollY.config(command=canvas.yview)

canvas.config(xscrollcommand=scrollX.set, yscrollcommand=scrollY.set)
canvas.pack(side='left')

root.mainloop()