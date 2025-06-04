import tkinter as tk
import webbrowser

root = tk.Tk()
root.title("Text Widget Example")

text = tk.Text(root, height=8)
text.pack(padx=10, pady=10, expand=True, fill=tk.BOTH)
text.insert("1.0", "Click here to visit pythontutorial.net")

text.tag_add("link", "1.0", "1.10")
text.tag_config("link", foreground="blue", underline=True)

text.tag_bind(
    "link",
    "<Button-1>",
    lambda e: webbrowser.open("https://www.pythontutorial.net")
)

text.tag_bind(
    "link",
    "<Enter>",
    lambda e: text.config(cursor="hand2")
)

text.tag_bind(
    "link",
    "<Leave>",
    lambda e: text.config(cursor="")
)

text.pack(padx=10, pady=10, side=tk.LEFT)

root.mainloop()