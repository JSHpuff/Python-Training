from tkinter import Tk, Frame, Menu

# root window
root = Tk()
root.geometry('320x150')
root.title('Menu Demo')

# Create a menubar
menubar = Menu(root)
root.config(menu=menubar)

# Create the file_menu
file_menu = Menu(
    menubar,
    tearoff=0
)

# Add menu items to the File menu
file_menu.add_command(label='New')
file_menu.add_command(label='Open...')
file_menu.add_command(label='Close')
file_menu.add_separator()

# Add Exit menu item
file_menu.add_command(
    label='Exit',
    command=root.destroy
)

# Add the File menu to the menubar
menubar.add_cascade(
    label="File",
    menu=file_menu
)

# Create the Help menu
help_menu = Menu(
    menubar,
    tearoff=0
)

help_menu.add_command(label='Welcome')
help_menu.add_command(label='About...')

# Add the Help menu to the menubar
menubar.add_cascade(
    label="Help",
    menu=help_menu
)

root.mainloop()