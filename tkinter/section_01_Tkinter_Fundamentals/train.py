import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

def button_clicked():
    print("Button clicked")

def select(option):
    print(option)

def return_pressed(event):
    print("Return key pressed")

def return_pressed_2(event=None):
    print("Triggered! event:", event)

def log(event):
    print(event)

def handle_click():
    showinfo(
        title="information",
        message="Downlaod button clicked"
    )

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Test Tkinter Window")

    window_width = 300
    window_height = 900

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    center_x = int(screen_width / 2 - window_width / 2)
    center_y = int(screen_height / 2 - window_height / 2)

    root.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")

    root.resizable(True, True)
    root.minsize(window_width, window_height)
    root.maxsize(window_width+200, window_height+200)

    root.attributes("-alpha", 0.9)

    try:
        root.iconbitmap("./000_testing_imgs/test_icon.ico")
    except Exception as e:
        print(f"Loading image error: {e}")

    tk.Label(root, text="Hey").pack(pady=30)
    ttk.Label(root, text="ttk Label").pack(pady=10)

    ttk.Button(root, text="Click me", command=button_clicked).pack()
    ttk.Button(root, text="Rock", command=lambda: select("Rock")).pack(pady=10)
    ttk.Button(root, text="Paper", command=lambda: select("Paper")).pack(pady=10)
    ttk.Button(root, text="Scissors", command=lambda: select("Scissors")).pack(pady=10)

    btn = ttk.Button(root, text="Press Enter")
    btn.bind("<Return>", return_pressed)
    btn.bind("<Return>", log, add="+")
    btn.focus()
    btn.pack(pady=10)

    btn2 = ttk.Button(root, text="Event Test")
    btn2.bind("<Return>", return_pressed_2)
    btn2.config(command=return_pressed_2)
    btn2.focus()
    btn2.pack(pady=10)

    ttk.Label(root, text="font test", font=("Helvetica")).pack()
    photo = tk.PhotoImage(file="./000_testing_imgs/python.png")
    image_label = ttk.Label(
        root, 
        image=photo, 
        padding=5, 
        text="Python", 
        compound=tk.TOP).pack()
    
    ttk.Button(
        root, 
        text="Exit", 
        command=lambda: root.quit()
        ).pack(ipadx=5, ipady=5)
    
    photo_download = tk.PhotoImage(file="./000_testing_imgs/download.png")
    download_button = ttk.Button(
        root, 
        image=photo_download, 
        text="Download",
        compound=tk.LEFT,
        command=handle_click
        ).pack(ipadx=5, ipady=5, pady=10)
    
    ttk.Entry(root).pack()

    ttk.Label(root, text="Name: ").pack(pady=2)
    name_entry = ttk.Entry(root)
    name_entry.pack(pady=5)
    name_entry.focus()

    ttk.Label(root, text="Password").pack(pady=5)
    ttk.Entry(root, show="*").pack(pady=5)

    text_var = tk.StringVar()
    text_entry = ttk.Entry(root, textvariable=text_var)
    text_entry.pack()
    text_entry.focus()

    output_label = ttk.Label(root)
    output_label.pack()

    text_var.trace_add(
        "write",
        lambda *args: output_label.config(text=text_var.get())
    )


    root.mainloop()