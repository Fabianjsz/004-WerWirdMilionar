"""
Dieses Programm dient zur Einrichtung der nötigen Datenbanken
Name: setup.py
Autor: Fabianjsz
Datum: 27.04.2025
"""

#Import
from databaseUtility import createTable, exampleQuestions


# Erstellen der WerWirdMilionar Datenbank
createTable()

# Füllt die Datenbank mit Fragen
exampleQuestions()

temp = input("Datenbank wurde erfolgreich erstellt und mit Beispielen gefüllt (*enter*)")