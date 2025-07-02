import tkinter as tk
from tkinter import Menu

# Root Window
root = tk.Tk()
root.title('Menu Demo')
root.geometry("350x150")

# Create a Menubar
menubar = Menu(root)
root.config(menu=menubar)

# Create a Menu
file_menu = Menu(menubar)

# Add a menu item to the menu
file_menu.add_command(
    label='Exit',
    command=root.destroy
)

# Add the file menu to the menubar
menubar.add_cascade(
    label="File",
    menu=file_menu
)

root.mainloop()