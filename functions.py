import sqlite3
import os


global dbName

dbName = "WerWirdMilionar.db"



def createTable(dbName):
    con = sqlite3.connect(dbName)
    cursor = con.cursor()
    cursor.execute("CREATE TABLE Fragen(nr INTEGER PRIMARY KEY AUTOINCREMENT, Frage VARCHAR, A1 VARCHAR, A2 VARCHAR, A3 VARCHAR, A4 VARCHAR);")
    con.commit()
    con.close()
    


def insertFrage(dbName, Frage, A1, A2, A3, A4):
    con = sqlite3.connect(dbName)
    cursor = con.cursor()
    cursor.execute(f"INSERT INTO Fragen(Frage, A1, A2, A3, A4) Values('{Frage}', '{A1}', '{A2}', '{A3}', '{A4}') ;")
    con.commit()
    con.close()

def returnTable(dbName, tableName):
    con = sqlite3.connect(dbName)
    cursor = con.cursor()
    cursor.execute(f"Select * FROM {tableName};")
    print(cursor.fetchall(),)
    con.close()

def deleteFrage(dbName, tableName):
    returnTable(dbName, tableName)
    fragenNr = input("Welche Frage möchtest du löschen? ")
    con = sqlite3.connect(dbName)
    cursor = con.cursor()
    cursor.execute(f"DELETE FROM {tableName} WHERE nr = {fragenNr};")
    con.commit()
    print(f"Frage {fragenNr} erfolgreich gelöscht")
    con.close()

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




#createTable(dbName)

insertFrage(dbName, "Wie viele Namen hat Daniele?", "4", "42", "2", "5")
editFrage()
#returnTable(dbName, "Fragen")
deleteFrage(dbName, "Fragen")


closeConnection(dbName)






