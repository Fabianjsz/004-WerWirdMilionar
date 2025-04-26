import tkinter as tk
from tkinter import ttk
import sqlite3

root = tk.Tk()
root.title("Treeview Table Example")

# Define columns
columns = ("ID", "Name", "Age")

tree = ttk.Treeview(root, columns=columns, show="headings")
tree.pack(side="left", fill="both", expand=True)

# Define headings (column titles)
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=100)  # optional: set width

# Sample data (like from database)
con = sqlite3.connect("WerWirdMilionar.db")
cur = con.cursor()
cur.execute("SELECT * FROM Fragen")
data = cur.fetchall()
con.close()


# Insert data into Treeview
for row in data:
    tree.insert("", tk.END, values=row)

# Add scrollbar
scrollbar = ttk.Scrollbar(root, orient="vertical", command=tree.yview)
tree.configure(yscrollcommand=scrollbar.set)
scrollbar.pack(side="right", fill="y")

root.mainloop()
