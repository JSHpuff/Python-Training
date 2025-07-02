from tkinter import Tk, Menu

root = Tk()
root.geometry('350x150')
root.title('Menu Demo')

menubar = Menu(root)
root.config(menu=menubar)

file_menu = Menu(
    menubar,
    tearoff=0
)

file_menu.add_command(label='New')
file_menu.add_command(label='Open...')
file_menu.add_command(label='Close')
file_menu.add_separator()

sub_menu = Menu(
    file_menu,
    tearoff=0
)
sub_menu.add_command(label='Keyboard Shortcuts')
sub_menu.add_command(label='Color Themes')

file_menu.add_cascade(
    label='Preferences',
    menu=sub_menu
)

file_menu.add_separator()
file_menu.add_command(
    label='Exit',
    command=root.destroy
)

menubar.add_cascade(
    label='File',
    menu=file_menu,
    underline=0
)

help_menu = Menu(
    menubar,
    tearoff=0
)

help_menu.add_command(label='Welcome')
help_menu.add_command(label='About...')

menubar.add_cascade(
    label='Help',
    menu=help_menu,
    underline=0
)

root.mainloop()