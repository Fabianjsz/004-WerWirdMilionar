"""
Main Funktion, welche das ganze Programm aufruft
Name: Main.py
Autor: Fabianjsz
Datum: 27.04.2025
"""

global root

# Import
from tkinter import *
import tkinter as tk
from tkinter import PhotoImage
from guiGame import launch_game_ui
from guiAdmin import edit_questions
from functools import partial

#GUI

root = Tk()
root.title("Wer wird Millionar")
root.geometry("760x450")
root.config(bg="#053C5E")


#Buttons
playButton = Button(root, text="Speil spielen", command=lambda: launch_game_ui(root))
playButton.place(x=50,y=300, width=150, height=50)

adminButton = Button(root, text="Fragen bearbeiten", command=lambda: edit_questions(root))
adminButton.place(x=50, y= 360, width=150, height=50)

#logo
photo = PhotoImage(file="wwm.png")
logo = Label(root, image=photo)

logo.place(x=300, y=30, width=400, height=400)
logo.image = photo




# Main funktion
if __name__ == "__main__":
    
    root.mainloop()
