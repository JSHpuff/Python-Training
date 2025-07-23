import tkinter as tk

root = tk.Tk()
root.title('Create Polygon in the Canvas')
root.geometry('300x300')

canvas = tk.Canvas(root, width=300, height=300)

canvas.create_polygon([10, 10, 100, 10, 50, 50, 20, 100], outline='#f00')
canvas.create_polygon([110, 10, 200, 10, 150, 50, 120, 100], outline='#f00', fill='')
canvas.create_polygon([10, 110, 100, 110, 50, 150, 20, 200], outline='#0a0', fill='#fff', width=5)
canvas.create_polygon([110, 110, 200, 110, 150, 150, 120, 200], outline='#f00', fill='', width=3, dash=(5, 5))

canvas.pack()

root.mainloop()