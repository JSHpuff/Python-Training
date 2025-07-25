import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from calendar import month_name
from datetime import datetime

root = tk.Tk()

# Configure the main window
window_width = 300
window_height = 200
root.geometry(f"{window_width}x{window_height}")
root.resizable(False, False)
root.title("Combobox Widget")

# Label
label = ttk.Label(text="Please select a month:")
label.pack(fill=tk.X, padx=5, pady=5)

# Create a combobox
selected_month = tk.StringVar()
month_cb = ttk.Combobox(root, textvariable=selected_month)

# Get first 3 letters of every month name
month_cb["values"] = [month_name[m][0:3] for m in range(1, 13)]

# Prevent typing a value
month_cb["state"] = "readonly"

# Place the widget
month_cb.pack(fill=tk.X, padx=5, pady=5)

# Bind the selected value changes
def month_changed(event):
    showinfo(
        title="Result",
        message=f"You selected {selected_month.get()}!"
    )

month_cb.bind("<<ComboboxSelected>>", month_changed)

# Set the current month
current_month = datetime.now().strftime("%b")
month_cb.set(current_month)

root.mainloop()