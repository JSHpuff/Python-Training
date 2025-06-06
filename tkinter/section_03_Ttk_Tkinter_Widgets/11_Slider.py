import tkinter as tk
from tkinter import ttk

class MainApp():
    def __init__ (self, root):
        self.root = root
        self.root.title("Slider Demo")
        self.root.geometry("300x200")
        self.root.resizable(False, False)

        self.ui()
    
    def ui(self):
        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=3)

        # slider current value
        self.current_value = tk.DoubleVar()

        # Label for the slider
        slider_label = ttk.Label(self.root, text="Slider:")
        slider_label.grid(column=0, row=0, sticky="w")
        
        # slider
        slider = ttk.Scale(
            self.root,
            from_=0,
            to=100,
            orient="horizontal",
            command=self.slider_changed,
            variable=self.current_value
        )
        slider.grid(column=1, row=0, sticky="we")

        # current value label
        current_value_label = ttk.Label(self.root, text="Current Value:")
        current_value_label.grid(row=1, columnspan=2, sticky="n", ipadx=10, ipady=10)

        # value label
        self.value_label = ttk.Label(self.root, text=self.get_current_value())
        self.value_label.grid(row=2, columnspan=2, sticky="n")

    def get_current_value(self):
        return "{: .2f}".format(self.current_value.get())
    
    def slider_changed(self, event):
        self.value_label.configure(text=self.get_current_value())


if __name__ == "__main__":
    root = tk.Tk()
    MainApp(root)
    root.mainloop()