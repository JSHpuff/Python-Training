import tkinter as tk
from tkinter import ttk

def return_pressed(event=None):
    print("Triggered! event:", event)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Event Binding Test")
    window_width = 300
    window_height = 100
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    center_x = int(screen_width / 2 - window_width / 2)
    center_y = int(screen_height / 2 - window_height / 2)
    root.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")
    root.resizable(True, True)
    
    try:
        root.iconbitmap("./000_testing_imgs/test_icon.ico")
    except Exception as e:
        print(f"Loading image error: {e}")
    
    root.attributes("-alpha", 0.7)

    btn = ttk.Button(root, text="Event Test")
    btn.bind("<Return>", return_pressed)
    btn.config(command=return_pressed)

    btn.focus()
    btn.pack(expand=True)

    root.mainloop()