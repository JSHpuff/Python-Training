import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror

class TemperatureConverter:
    @staticmethod
    def fahrenheit_to_celsius(f):
        return (f-32) * 5 / 9
    
class ConverterFrame(ttk.Frame):
    def __init__ (self, container):
        super().__init__(container)
        
        # Field options
        options = {"padx": 5, "pady": 5}

        # Temperature label
        self.temperature_label = ttk.Label(self, text="Fahrenheit")
        self.temperature_label.grid(column=0, row=0, sticky=tk.W, **options)

        # Temperature entry
        self.temperature = tk.StringVar()
        self.temperature_entry = ttk.Entry(self, textvariable=self.temperature)
        self.temperature_entry.grid(column=1, row=0, **options)
        self.temperature_entry.focus()

        self.convert_button = ttk.Button(self, text="Convert")
        self.convert_button["command"] = self.convert
        self.convert_button.grid(column=2, row=0, sticky=tk.W, **options)

        # Result label
        self.result_label = ttk.Label(self)
        self.result_label.grid(row=1, columnspan=3, **options)

        # Add padding to the frame and show it
        self.grid(padx=10, pady=10, sticky=tk.NSEW)

    def convert(self):
        try:
            f = float(self.temperature.get())
            c = TemperatureConverter.fahrenheit_to_celsius(f)
            result = f"{f} Fahrenheit = {c:.2f} Celsius"
            self.result_label.config(text=result)
        except ValueError as error:
            showerror(title="Error", message=error)

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Temperature Converter")
        self.geometry("350x70")
        self.resizable(False, False)

if __name__ == "__main__":
    app = App()
    ConverterFrame(app)
    app.mainloop()