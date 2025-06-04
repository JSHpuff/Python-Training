import tkinter as tk
from tkinter.messagebox import showinfo
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.geometry("400x180")
root.title("Listbox")

# Create a variable object
languages = ("Java", "C", "C++", "C#", "Python", "Go", "JavaScript", "PHP", "Swift")
list_variable = tk.Variable(value=languages)

# Label
label = ttk.Label(
    root,
    text="Select your favorite programming languages:"
)
label.pack(padx=10, pady=0, side=tk.TOP, fill=tk.X)

listbox = tk.Listbox(
    root,
    listvariable=list_variable,
    height=6,
    selectmode=tk.MULTIPLE,
)
listbox.pack(padx=10, pady=10, expand=True, fill=tk.BOTH, side=tk.LEFT)

def handle_item_select(event):
    selected_indices = listbox.curselection()
    selected_languages = ",".join([listbox.get(i) for i in selected_indices])

    showinfo(
        title="Information",
        message=f"You selected: {selected_languages}"
    )

listbox.bind("<<ListboxSelect>>", handle_item_select)

# Link a scrollbar to a list
v_scrollbar = ttk.Scrollbar(
    root,
    orient=tk.VERTICAL,
    command=listbox.yview
)

listbox["yscrollcommand"] = v_scrollbar.set
v_scrollbar.pack(pady=10, side=tk.RIGHT, fill=tk.Y)

root.mainloop()