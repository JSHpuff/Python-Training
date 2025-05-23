import tkinter as tk

if __name__ == "__main__":
    # Create and instance of the tk.Tk class
    # It will create the applcation window
    # The main window in Tkinter is called root.
    root = tk.Tk()

    # Place a label on the root window
    # widget = WidgetName(master, **kw)
    # master:   the parent window or frame,
    #           where you want to place the widget.
    # kw:       one or more keyword arguments that
    #           specify the configurations of the widget.
    message = tk.Label(root, text="Hello, World!")

    # Positions the Label on the main window
    message.pack()

    # Keep the window displaying
    try:
        # If find the text and UI are blurry on Windows,
        # you can use the ctypes Python library to fix it.
        from ctypes import windll
        windll.shcore.SetProcessDpiAwareness(1)
    finally:
        # Call the mainloop() method of the main window object
        # Ensures the main window remain visible on the screen
        # If not, the window will display and disappear almost instantly
        # Ensures the main window continues to display and run until close it
        root.mainloop()