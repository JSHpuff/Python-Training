import tkinter as tk

root = tk.Tk()
root.title('Create Line in the Canvas')
root.geometry('300x300')

canvas = tk.Canvas(root, width=300, height=300)
canvas.create_line(10, 10, 200, 10)
canvas.create_line(10, 30, 200, 30, width=10)
canvas.create_line(10, 50, 200, 150, width=10, fill='#f00')
canvas.create_line(10, 70, 200, 200, width=10, fill='#0a0', dash=(10, 2))
canvas.pack()

root.mainloop()