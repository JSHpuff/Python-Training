import tkinter as tk

if __name__ == "__main__":

    root = tk.Tk()

    # Change the window title
    root.title('Tkinter Window Demo')

    """     Change window size and location
            - width x height +- x +- y

            - width:    represents the window's width in pixels
            - height:   represents the window's height in pixels
            - x:        denotes the window's horizontal position
                        +n: the left edge of the window be positioned n pixels
                        -n: the right edge of the window be positioned n pixels
            - y:        denotes the window's vertical position
                        + m: the top edge of the window be positioned m pixels
                        - m: the bottom edge of the windwo be positioned m pixels
    """
    window_height = 600
    window_width = 400
    window_x = 50
    window_y = 50
    root.geometry(f"{window_height}x{window_width}+{window_x}+{window_y}")

    # Resizing behavior
    # root.resizable(widht, height)
    root.resizable(True, True)

    # window minsize and maxsize
    root.minsize(550, 350)
    root.maxsize(800, 600)

    # Transparency
    # setting alpha channel
    # ranging from 0.0 (fully transparent) to 1.0 (fully opaque)
    root.attributes("-alpha", 0.5)

    # Window stacking order
    root.attributes("-topmost", 1)

    # Change the default icon
    root.iconbitmap('./000_testing_imgs/test_icon.ico')


    root.mainloop()