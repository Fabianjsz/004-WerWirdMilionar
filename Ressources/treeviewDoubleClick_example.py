import tkinter as tk
from tkinter import ttk

def on_double_click(event):
    selected_item = tree.selection()[0]  # Get the selected item's ID
    values = tree.item(selected_item, "values")  # Get the values
    print(f"You double-clicked on: {values}")
    # Here you can run any other code you want!

root = tk.Tk()
root.title("Double Click on Treeview")

columns = ("ID", "Name", "Age")
tree = ttk.Treeview(root, columns=columns, show="headings")
tree.pack(fill="both", expand=True)

for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=100)

# Example data
data = [
    (1, "Alice", 24),
    (2, "Bob", 30),
    (3, "Charlie", 28),
]

for row in data:
    tree.insert("", tk.END, values=row)

# Bind the double-click event
tree.bind("<Double-1>", on_double_click)

root.mainloop()
