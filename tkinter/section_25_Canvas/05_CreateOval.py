import tkinter as tk

root = tk.Tk()
root.title('Create Oval in the Canvas')
root.geometry('300x300')

canvas = tk.Canvas(root, width=300, height=300)

canvas.create_oval(10, 10, 50, 100)
canvas.create_oval(60, 10, 100, 100, width=8)
canvas.create_oval(110, 10, 150, 100, width=8, fill='#f00')
canvas.create_oval(160, 10, 200, 100, width=8, fill='#f00', outline='#00f')
canvas.create_oval(210, 10, 250, 100, width=8, fill='#fff', outline='#0a0', dash=(5, 5))

canvas.create_oval(10, 120, 50, 160)
canvas.create_oval(60, 120, 100, 160, width=8)
canvas.create_oval(110, 120, 150, 160, width=8, fill='#f00')
canvas.create_oval(160, 120, 200, 160, width=8, fill='#f00', outline='#00f')
canvas.create_oval(210, 120, 250, 160, width=8, fill='#fff', outline='#0a0', dash=(5, 5))

canvas.pack()

root.mainloop()