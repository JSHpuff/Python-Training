import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from calendar import month_name

root = tk.Tk()

# Window configuration
root.geometry("300x200")
root.resizable(False, False)
root.title("Combobox Widget")

# Label
label = ttk.Label(text="Please select a month:")
label.pack(fill=tk.X, padx=5, pady=5)

# Combo box
selected_month = tk.StringVar()
month_cb = ttk.Combobox(root, textvariable=selected_month)

# Get first 3 letters of every month name
month_cb["value"] = [month_name[m][0:3] for m in range(1, 13)]

# Prevent typing a value
month_cb["state"] = "readonly"

# Place the widget
month_cb.pack(fill=tk.X, padx=5, pady=5)

def month_changed(event):
    showinfo(
        title="Result",
        message=f"You selected {selected_month.get()}!"
    )

month_cb.bind("<<ComboboxSelected>>", month_changed)

root.mainloop()