"""
Diese Datei beinhaltet die GUI und Funktionen, welche für das eigentliche Spiel benötigt werden
Name: guiGame.py
Autor: Fabianjsz
Datum: 12.06.2025
"""

from tkinter import *
import tkinter as tk
from tkinter import messagebox
from databaseUtility import fetchQuestion, get_nr_all
import random

#Variablen
global question, textA, textB, textC, textD
question = "Wie viele Haare hat Daniele auf seinem Kopf?"

textA = ""
textB = ""
textC = ""
textD = ""

counter = 0

playing = True


#funktionen

def update_random_question():
    Nr_tupple = get_nr_all()
    print("laenge: ", len(get_nr_all()))
    print("Nr: ", Nr_tupple)
    tempNr = Nr_tupple[random.randint(0, len(Nr_tupple)-1)]
    data = fetchQuestion(tempNr)
    data = data[0]
    print("data: ",data)
    
    # Frage in Fenster einsetzen
    question = data[1]
    textA = data[2]
    textB = data[3]
    textC = data[4]
    textD = data[5]
    
    
    
    
    
    #fetchQuestion(tempNr)

update_random_question()

def guess(answer):
    if answer == "a":
        pass
    elif answer == "b":
        pass
    elif answer == "c":
        pass
    elif answer == "d":
        pass

def message(counter):
    if counter == 15:
        messagebox.showinfo("Gewonnen!", "SIE SIND DER MILIONAR!!!")
    else:
        messagebox.showinfo("Falsch", f"Falsch. Sie haben {counter} Fragen richtig.")

def get_questions(fragenNr):
    data = fetchQuestion(fragenNr)
    print(data)
    tupple = data[0]
    print(tupple)

    question = tupple[1]

def start_quiz():
    pass
    #while True:
      #  update_random_question()
        


def launch_game_ui(root):
    game = tk.Toplevel(root)
    game.title("Wer Wird Milionar")
    game.geometry("700x400")
    game.config(bg="#053C5E")
    
    #lable
    questionLabel = tk.Label(game, text=question, font=("Arial", 16), bg="#053C5E", fg="white", wraplength=600)
    questionLabel.pack(pady=40)
    
    #Buttons
    answerA = Button(game, text=textA, font=("Arial", 14), command=lambda: guess("a"))
    answerA.place(x=50,y=110, height=50, width=400)

    answerB = Button(game, text=textB, font=("Arial", 14), command=lambda: guess("b"))
    answerB.place(x=50,y=180, height=50, width=400)

    answerC = Button(game, text=textC, font=("Arial", 14), command=lambda: guess("c"))
    answerC.place(x=50,y=250, height=50, width=400)

    answerD = Button(game, text=textD, font=("Arial", 14), command=lambda: guess("d"))
    answerD.place(x=50,y=320, height=50, width=400)
    
    start_quiz()

