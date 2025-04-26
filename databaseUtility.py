#import
import sqlite3
import os
from utility import informationWindow

#Variablen
global dbName

dbName = "WerWirdMilionar.db"
tableName = "Fragen"

#Funktionen

def createTable():
    con = sqlite3.connect(dbName)
    cursor = con.cursor()
    cursor.execute("CREATE TABLE Fragen(nr INTEGER PRIMARY KEY AUTOINCREMENT, Frage VARCHAR, A1 VARCHAR, A2 VARCHAR, A3 VARCHAR, A4 VARCHAR);")
    con.commit()
    con.close()
    


def insertFrage(Frage, A1, A2, A3, A4):
    con = sqlite3.connect(dbName)
    cursor = con.cursor()
    cursor.execute(f"INSERT INTO Fragen(Frage, A1, A2, A3, A4) Values('{Frage}', '{A1}', '{A2}', '{A3}', '{A4}') ;")
    con.commit()
    con.close()

def returnTable():
    con = sqlite3.connect(dbName)
    cursor = con.cursor()
    cursor.execute(f"Select nr,Frage FROM {tableName};")
    data = cursor.fetchall()
    con.close()
    return data

def checkFrage(fragenNr):
    con = sqlite3.connect(dbName)
    cursor = con.cursor()
    cursor.execute(f"SELECT nr FROM {tableName} WHERE nr = {fragenNr}")
    temp = cursor.fetchall()
    con.close()
    return temp

def deleteFrage(fragenNr):
    con = sqlite3.connect(dbName)
    cursor = con.cursor()
    cursor.execute(f"DELETE FROM {tableName} WHERE nr = {fragenNr};")
    con.commit()
    con.close()
    informationWindow(f"Frage {fragenNr} wurde gelöscht")

def editFrage():
    fragenNr = input("welche Frage soll verändert werden? ")
    datensatz = input("welche Zeile soll bearbeitet werden? ")
    neuerInhalt = input("was soll im neuen Satz stehen? ")
    con = sqlite3.connect(dbName)
    cursor = con.cursor()
    cursor.execute(f"UPDATE Fragen SET {datensatz} = '{neuerInhalt}' WHERE nr = {fragenNr};")
    con.commit()
    con.close
    


def closeConnection(dbName):
    con = sqlite3.connect(dbName)
    con.close()


# Creates 18 example questions to fill database
def exampleQuestions():
    insertFrage("Wie hoch ist der Eifelturm?", "312m", "39999m", "42", "1")
    insertFrage("Wie viele Planeten hat unser Sonnensystem?", "8", "7", "9", "10")
    insertFrage("Wer schrieb \"Faust\"?", "Johann Wolfgang von Goethe", "Friedrich Schiller", "Heinrich Heine", "Thomas Mann")
    insertFrage("Was ist die Hauptstadt von Frankreich?", "Paris", "Berlin", "Madrid", "Rom")
    insertFrage("Welches Element hat das chemische Symbol O?", "Sauerstoff", "Gold", "Silber", "Wasserstoff")
    insertFrage("Wie viele Kontinente gibt es?", "7", "6", "5", "8")
    insertFrage("Wer malte die Mona Lisa?", "Leonardo da Vinci", "Pablo Picasso", "Vincent van Gogh", "Claude Monet")
    insertFrage("Welches Tier ist das größte Landtier?", "Elefant", "Giraffe", "Nilpferd", "Bär")
    insertFrage("Wie viele Sekunden hat eine Minute?", "60", "50", "70", "100")
    insertFrage("Was ist die Hauptstadt von Italien?", "Rom", "Mailand", "Venedig", "Florenz")
    insertFrage("Welches ist das größte Meerestier?", "Blauwal", "Hai", "Delfin", "Krake")
    insertFrage("Wie viele Tage hat ein Schaltjahr?", "366", "365", "364", "367")
    insertFrage("Wer erfand das Telefon?", "Alexander Graham Bell", "Thomas Edison", "Nikola Tesla", "Albert Einstein")
    insertFrage("Was ist die Hauptstadt von Deutschland?", "Berlin", "Hamburg", "München", "Köln")
    insertFrage("Welches Land hat die meisten Einwohner?", "China", "Indien", "USA", "Russland")
    insertFrage("Wie viele Beine hat eine Spinne?", "8", "6", "10", "12")
    insertFrage("Wer schrieb \"Die Verwandlung\"?", "Franz Kafka", "Hermann Hesse", "Bertolt Brecht", "Stefan Zweig")
    insertFrage("Was ist die Hauptstadt von Spanien?", "Madrid", "Barcelona", "Sevilla", "Valencia")




