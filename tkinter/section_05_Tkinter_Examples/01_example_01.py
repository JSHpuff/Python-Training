import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror

root = tk.Tk()
root.title("Temperature Converter")
root.geometry("350x70")
root.resizable(False, False)

def fahrenheit_to_celsius(f):
    return (f-32) * 5/9

frame = ttk.Frame(root)

options = {"padx": 5, "pady": 5}

temperautre_label = ttk.Label(frame, text="Fahrenheit")
temperautre_label.grid(column=0, row=0, sticky="W", **options)

temperature = tk.StringVar()
temperature_entry = ttk.Entry(frame, textvariable=temperature)
temperature_entry.grid(column=1, row=0, **options)
temperature_entry.focus()

def convert_button_clicked():
    try:
        f = float(temperature.get())
        c = fahrenheit_to_celsius(f)
        result = f"{f} Fahrenheit = {c:.2f} Celsius"
        result_label.config(text=result)
    except ValueError as error:
        showerror(title="Error", message=error)
    
convert_button = ttk.Button(frame, text="Convert")
convert_button.grid(column=2, row=0, sticky="W", **options)
convert_button.configure(command=convert_button_clicked)

result_label = ttk.Label(frame)
result_label.grid(row=1, columnspan=3, **options)

frame.grid(padx=10, pady=10)

root.mainloop()