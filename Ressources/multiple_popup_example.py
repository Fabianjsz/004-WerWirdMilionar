import tkinter as tk
from tkinter import Toplevel

def create_second_popup():
    # Create the second popup window
    second_popup = Toplevel()  # Toplevel creates a new popup window
    second_popup.title("Second Popup")
    
    label = tk.Label(second_popup, text="This is the second popup window")
    label.pack(padx=20, pady=20)

    close_button = tk.Button(second_popup, text="Close", command=second_popup.destroy)
    close_button.pack(padx=10, pady=10)

def create_first_popup():
    # Create the first popup window
    first_popup = Toplevel()  # Toplevel creates a new popup window
    first_popup.title("First Popup")
    
    label = tk.Label(first_popup, text="This is the first popup window")
    label.pack(padx=20, pady=20)

    open_second_button = tk.Button(first_popup, text="Open Second Popup", command=create_second_popup)
    open_second_button.pack(padx=10, pady=10)

    close_button = tk.Button(first_popup, text="Close", command=first_popup.destroy)
    close_button.pack(padx=10, pady=10)

# Set up the main window
root = tk.Tk()
root.title("Main Window")

open_first_popup_button = tk.Button(root, text="Open First Popup", command=create_first_popup)
open_first_popup_button.pack(padx=20, pady=20)

root.mainloop()
