import tkinter as tk
from tkinter import ttk
from tkinter import simpledialog, messagebox

def show_popup(event):
    # Identify the row under the mouse
    selected_item = tree.identify_row(event.y)
    if selected_item:
        tree.selection_set(selected_item)  # Select it visually

        # Create popup menu
        menu = tk.Menu(root, tearoff=0)
        menu.add_command(label="Edit", command=lambda: edit_item(selected_item))
        menu.add_command(label="Delete", command=lambda: delete_item(selected_item))
        menu.post(event.x_root, event.y_root)

def edit_item(item_id):
    # Get current values
    values = tree.item(item_id, "values")
    # Simple dialog to edit (for example, just edit the Name field)
    new_name = simpledialog.askstring("Edit Name", "Enter new name:", initialvalue=values[1])
    if new_name:
        # Update the treeview item
        tree.item(item_id, values=(values[0], new_name, values[2]))
        print(f"Updated item {values[0]} with new name: {new_name}")

def delete_item(item_id):
    # Confirm delete
    answer = messagebox.askyesno("Delete", "Are you sure you want to delete this item?")
    if answer:
        tree.delete(item_id)
        print(f"Deleted item.")

root = tk.Tk()
root.title("Right Click Menu on Treeview")

# Setup Treeview
columns = ("ID", "Name", "Age")
tree = ttk.Treeview(root, columns=columns, show="headings")
tree.pack(fill="both", expand=True)

for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=100)

# Sample data
data = [
    (1, "Alice", 24),
    (2, "Bob", 30),
    (3, "Charlie", 28),
]

for row in data:
    tree.insert("", tk.END, values=row)

# Bind right-click to the Treeview
tree.bind("<Button-3>", show_popup)

root.mainloop()
