import tkinter as tk

root = tk.Tk()
root.title('Create Arc in the Canvas')
root.geometry('300x300')

canvas = tk.Canvas(root, width=300, height=300)

canvas.create_arc(10, 10, 100, 100, extent=180)
canvas.create_arc(110, 10, 200, 100, start=60, extent=180)
canvas.create_arc(210, 10, 300, 100, start=60, extent=70, width=8, fill='#f00')
canvas.create_arc(10, 110, 100, 200, start=60, extent=180, width=8, fill='#f00', outline='#00f')
canvas.create_arc(110, 110, 200, 200, start=-60, extent=-120, width=3, fill='#fff', outline='#0a0', dash=(5, 5))
canvas.create_arc(210, 110, 300, 200, start=-60, extent=-90, width=3, fill='#ff0', outline='#f50', dash=(5, 10), style='arc')

canvas.pack()

root.mainloop()