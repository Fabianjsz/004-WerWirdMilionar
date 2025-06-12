"""
Diese Datei beinhaltet die GUI und Funktionen,welche für das Hauptmenü des Spieles benötigt werden
Name: guiMain.py
Autor: Fabianjsz
Datum: 12.06.2025
"""

#Imports
from guiAdmin import adminRoot
from tkinter import *
import tkinter as tk
from tkinter import PhotoImage


#Functions
def startGame():
    pass

def editQuestions():
    if not adminRoot.winfo_exists():
        print("Admin window doesn't exist anymore.")
    else:
        adminRoot.deiconify()
        adminRoot.lift()


#GUI

#Root
root = Tk()
root.title("Wer wird Millionar")
root.geometry("760x450")
root.config(bg="#053C5E")



#Buttons
playButton = Button(root, text="Speil spielen", command=startGame)
playButton.place(x=50,y=300, width=150, height=50)

adminButton = Button(root, text="Fragen bearbeiten", command=lambda: editQuestions())
adminButton.place(x=50, y= 360, width=150, height=50)

#logo
image = PhotoImage(file="logo.png")
logo = Label(root)
logo.image = image
logo.place(x=300, y=30, width=400, height=400)


root.mainloop()