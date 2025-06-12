"""
Diese Datei beinhaltet die GUI und Funktionen, welche für das eigentliche Spiel benötigt werden
Name: guiGame.py
Autor: Fabianjsz
Datum: 12.06.2025
"""

import tkinter as tk
from tkinter import messagebox
from databaseUtility import fetchQuestion
import random

class QuizGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Wer wird Millionär - Spiel")
        self.master.geometry("700x400")
        self.master.config(bg="#053C5E")

        self.current_question = 1
        self.score = 0
        self.max_questions = self.get_max_questions()
        self.correct_index = 0  # Track the correct answer's button index

        self.question_label = tk.Label(master, text="", font=("Arial", 16), bg="#053C5E", fg="white", wraplength=600)
        self.question_label.pack(pady=40)

        self.buttons = []
        for i in range(4):
            btn = tk.Button(master, text="", font=("Arial", 14), width=40, command=lambda idx=i: self.check_answer(idx))
            btn.pack(pady=5)
            self.buttons.append(btn)

        self.status_label = tk.Label(master, text="", font=("Arial", 12), bg="#053C5E", fg="yellow")
        self.status_label.pack(pady=20)

        self.load_question()

    def get_max_questions(self):
        # Versuche, Fragen abzurufen, bis eine Abfrage fehlschlägt
        idx = 1
        while True:
            q = fetchQuestion(idx)
            if not q:
                break
            idx += 1
        return idx - 1

    def load_question(self):
        question_data = fetchQuestion(self.current_question)
        if not question_data:
            self.end_game()
            return

        q = question_data[0]
        self.question_label.config(text=f"Frage {self.current_question}: {q[1]}")

        # Prepare answers as (text, is_correct) tuples
        answers = [
            (str(q[2]) if q[2] else "", True),   # A1 is always correct in your DB
            (str(q[3]) if q[3] else "", False),
            (str(q[4]) if q[4] else "", False),
            (str(q[5]) if q[5] else "", False)
        ]
        random.shuffle(answers)
        # Find the index of the correct answer after shuffling
        self.correct_index = next(idx for idx, ans in enumerate(answers) if ans[1])

        for i in range(4):
            self.buttons[i].config(
                text=answers[i][0],
                state=tk.NORMAL,
                bg="SystemButtonFace",
                fg="black"
            )
        self.status_label.config(text=f"Frage {self.current_question} von {self.max_questions}")

    def check_answer(self, idx):
        if idx == self.correct_index:
            self.score += 1
            self.status_label.config(text="Richtig!", fg="lightgreen")
        else:
            self.status_label.config(text="Falsch! Das Spiel ist vorbei.", fg="red")
            for btn in self.buttons:
                btn.config(state=tk.DISABLED)
            messagebox.showinfo("Game Over", f"Falsch! Du hast {self.score} richtige Antworten.\nSpiel beendet.")
            self.master.after(1000, self.master.destroy)
            return

        self.current_question += 1
        if self.current_question > self.max_questions:
            self.end_game()
        else:
            self.master.after(800, self.load_question)

    def end_game(self):
        for btn in self.buttons:
            btn.config(state=tk.DISABLED)
        self.status_label.config(text=f"Spiel beendet! Richtige Antworten: {self.score} von {self.max_questions}", fg="yellow")
        messagebox.showinfo("Spiel beendet", f"Du hast {self.score} von {self.max_questions} Fragen richtig beantwortet!")
        self.master.after(1000, self.master.destroy)

def start_quiz():
    quiz_window = tk.Toplevel()
    QuizGame(quiz_window)

