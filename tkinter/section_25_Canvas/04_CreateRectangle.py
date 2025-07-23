import tkinter as tk

root = tk.Tk()
root.title('Create Rectangle in the Canvas')
root.geometry('300x300')

canvas = tk.Canvas(root, width=300, height=300)
canvas.create_rectangle(10, 10, 50, 100)
canvas.create_rectangle(60, 10, 110, 100, width=8)
canvas.create_rectangle(120, 10, 170, 100, 
                        width=8, fill='#f00')
canvas.create_rectangle(180, 10, 230, 100, 
                        width=8, fill='#f00', outline='#00f')
canvas.create_rectangle(240, 10, 290, 100, 
                        width=3, fill='#fff', outline='#0a0', dash=(5, 5))
canvas.pack()

root.mainloop()