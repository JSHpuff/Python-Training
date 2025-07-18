import tkinter as tk

root = tk.Tk()
root.title('Set Pack Parameters')
root.geometry('200x200')

img = tk.PhotoImage(file='./000_testing_imgs/city.png')

mylabel = tk.Label(
    root,
    text='Hello',
    font=('Arial', 20, 'bold'),
    bg='#ff0'
)

mylabel.pack(
    side='right',
    padx=20, pady=20,
    anchor='nw'
)

root.mainloop()