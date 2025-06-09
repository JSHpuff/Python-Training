import tkinter as tk
from tkinter import ttk
import csv

def read_csv(filename):
    rows = []
    with open(filename, newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            rows.append(row)
    return rows

def format_currency(value):
    try:
        return f"${int(value):,}"
    except ValueError:
        return value

def create_table_view(root, employees):
    frame = ttk.Frame(root)
    treeview = ttk.Treeview(
        frame,
        columns=(
            "First Name",
            "Last Name",
            "Gender",
            "City",
            "Salary",
            "Bonus"
        ),
        show="headings"
    )
    
    treeview.heading("First Name", text="First Name")
    treeview.heading("Last Name", text="Last Name")
    treeview.heading("Gender", text="Gender")
    treeview.heading("City", text="City")
    treeview.heading("Salary", text="Salary")
    treeview.heading("Bonus", text="Bonus")

    treeview.column("First Name", width=150)
    treeview.column("Last Name", width=150)
    treeview.column("Gender", width=100)
    treeview.column("City", width=150)
    treeview.column("Salary", width=100, anchor=tk.E)
    treeview.column("Bonus", width=100, anchor=tk.E)

    for employee in employees:
        treeview.insert(
            "", tk.END,
            values=(
                employee["First Name"],
                employee["Last Name"],
                employee["Gender"],
                employee["City"],
                format_currency(employee["Salary"]),
                format_currency(employee["Bonus"]),
            ),
        )

    v_scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=treeview.yview)
    treeview.configure(yscrollcommand=v_scrollbar.set)

    treeview.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    v_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

def main():
    root = tk.Tk()
    root.title("Employee List")
    employees = read_csv("./tkinter/section_03_Ttk_Tkinter_Widgets/employees.csv")
    create_table_view(root, employees)
    root.mainloop()

if __name__ == "__main__":
    main()