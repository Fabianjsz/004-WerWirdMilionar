#import
import sqlite3
import os

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

def returnQuestion(fragenNr):
    con = sqlite3.connect(dbName)
    cursor = con.cursor()
    cursor.execute(f"Select nr,Frage FROM {tableName} WHERE nr = {fragenNr};")
    data = cursor.fetchall()
    con.close()
    return data

def fetchQuestion(fragenNr):
    con = sqlite3.connect(dbName)
    cursor = con.cursor()
    cursor.execute(f"SELECT * FROM Fragen WHERE nr = {fragenNr}")
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
    


def editFrage(fragenNr, inputfrage, antwortA, antwortB, antwortC, antwortD):
    con = sqlite3.connect(dbName)
    cursor = con.cursor()
    print(inputfrage)
    cursor.execute(f"UPDATE Fragen SET Frage = '{inputfrage}', A1 = '{antwortA}', A2 = '{antwortB}', A3 = '{antwortC}', A4 = '{antwortD}' WHERE nr = {fragenNr};")
    con.commit()
    con.close



def closeConnection(dbName):
    con = sqlite3.connect(dbName)
    con.close()


# Creates 18 example questions to fill database
def exampleQuestions():
    insertFrage("Wie hoch ist der Eifelturm?", "312m", "39999m", "42", "1")
    insertFrage("Was ist die Hauptstadt von Österreich?", "Wien", "Salzburg", "Graz", "Innsbruck")
    insertFrage("Welches Tier ist das schnellste Landtier?", "Gepard", "Löwe", "Tiger", "Pferd")
    insertFrage("Wie viele Farben hat der Regenbogen?", "7", "6", "8", "5")
    insertFrage("Wer malte \"Das letzte Abendmahl\"?", "Leonardo da Vinci", "Michelangelo", "Raphael", "Donatello")
    insertFrage("Was ist die Hauptstadt von Japan?", "Tokio", "Kyoto", "Osaka", "Hiroshima")
    insertFrage("Welches Element hat das chemische Symbol H?", "Wasserstoff", "Helium", "Holmium", "Hafnium")
    insertFrage("Wie viele Spieler hat eine Fußballmannschaft?", "11", "10", "12", "9")
    insertFrage("Wer schrieb \"Harry Potter\"?", "J.K. Rowling", "J.R.R. Tolkien", "George R.R. Martin", "Suzanne Collins")
    insertFrage("Was ist die Hauptstadt von Kanada?", "Ottawa", "Toronto", "Vancouver", "Montreal")
    insertFrage("Welches Tier legt Eier?", "Huhn", "Hund", "Katze", "Pferd")
    insertFrage("Wie viele Stunden hat ein Tag?", "24", "12", "48", "36")
    insertFrage("Wer erfand die Glühbirne?", "Thomas Edison", "Nikola Tesla", "Alexander Graham Bell", "Albert Einstein")
    insertFrage("Was ist die Hauptstadt von Australien?", "Canberra", "Sydney", "Melbourne", "Brisbane")
    insertFrage("Welches Land hat die größte Fläche?", "Russland", "Kanada", "China", "USA")
    insertFrage("Wie viele Beine hat ein Insekt?", "6", "8", "4", "10")
    insertFrage("Wer schrieb \"Der Herr der Ringe\"?", "J.R.R. Tolkien", "C.S. Lewis", "George R.R. Martin", "J.K. Rowling")
    insertFrage("Was ist die Hauptstadt von Brasilien?", "Brasília", "Rio de Janeiro", "São Paulo", "Salvador")
    insertFrage("Welches Tier ist das größte Raubtier der Welt?", "Eisbär", "Löwe", "Tiger", "Hai")
    insertFrage("Wie viele Minuten hat eine Stunde?", "60", "50", "70", "100")
    insertFrage("Wer malte \"Sternennacht\"?", "Vincent van Gogh", "Claude Monet", "Pablo Picasso", "Salvador Dalí")
    insertFrage("Was ist die Hauptstadt von Indien?", "Neu-Delhi", "Mumbai", "Kalkutta", "Chennai")
    insertFrage("Welches Element hat das chemische Symbol C?", "Kohlenstoff", "Calcium", "Chlor", "Chrom")
    insertFrage("Wie viele Kontinente gibt es auf der Erde?", "7", "6", "5", "8")
    insertFrage("Wer schrieb \"Die Leiden des jungen Werther\"?", "Johann Wolfgang von Goethe", "Friedrich Schiller", "Heinrich Heine", "Thomas Mann")
    insertFrage("Was ist die Hauptstadt von Russland?", "Moskau", "Sankt Petersburg", "Kasan", "Nowosibirsk")
    insertFrage("Welches Tier ist das größte Säugetier der Welt?", "Blauwal", "Elefant", "Giraffe", "Nilpferd")
    insertFrage("Wie viele Tage hat ein Jahr?", "365", "366", "364", "367")
    insertFrage("Wer erfand den Buchdruck?", "Johannes Gutenberg", "Leonardo da Vinci", "Isaac Newton", "Galileo Galilei")
    insertFrage("Was ist die Hauptstadt von Schweden?", "Stockholm", "Göteborg", "Malmö", "Uppsala")
    insertFrage("Welches Land hat die meisten Inseln?", "Schweden", "Indonesien", "Philippinen", "Japan")
    insertFrage("Wie viele Beine hat ein Tausendfüßler?", "Unterschiedlich", "1000", "500", "200")
    insertFrage("Wer schrieb \"1984\"?", "George Orwell", "Aldous Huxley", "Ray Bradbury", "Philip K. Dick")
    insertFrage("Was ist die Hauptstadt von Norwegen?", "Oslo", "Bergen", "Trondheim", "Stavanger")
    insertFrage("Welches Tier ist das größte fliegende Tier?", "Wanderaalbatros", "Adler", "Fledermaus", "Kondor")
    insertFrage("Wie viele Sekunden hat eine Stunde?", "3600", "3000", "4000", "5000")
    insertFrage("Wer malte \"Die Geburt der Venus\"?", "Sandro Botticelli", "Leonardo da Vinci", "Michelangelo", "Raphael")
    insertFrage("Was ist die Hauptstadt von China?", "Peking", "Shanghai", "Hongkong", "Guangzhou")
    insertFrage("Welches Element hat das chemische Symbol Fe?", "Eisen", "Fluor", "Fermium", "Francium")
    insertFrage("Wie viele Zähne hat ein erwachsener Mensch?", "32", "30", "28", "34")
    insertFrage("Wer schrieb \"Der alte Mann und das Meer\"?", "Ernest Hemingway", "F. Scott Fitzgerald", "John Steinbeck", "William Faulkner")
    insertFrage("Was ist die Hauptstadt von Mexiko?", "Mexiko-Stadt", "Guadalajara", "Monterrey", "Cancún")
    insertFrage("Welches Tier ist das größte Reptil?", "Salzwasserkrokodil", "Komodowaran", "Anakonda", "Lederschildkröte")
    insertFrage("Wie viele Monate hat ein Jahr?", "12", "10", "11", "13")
    insertFrage("Wer erfand die Relativitätstheorie?", "Albert Einstein", "Isaac Newton", "Galileo Galilei", "Nikola Tesla")
    insertFrage("Was ist die Hauptstadt von Südafrika?", "Pretoria", "Kapstadt", "Johannesburg", "Durban")
    insertFrage("Welches Land hat die längste Küstenlinie?", "Kanada", "Indonesien", "Russland", "Australien")
    insertFrage("Wie viele Flügel hat eine Biene?", "4", "2", "6", "8")
    insertFrage("Wer schrieb \"Stolz und Vorurteil\"?", "Jane Austen", "Charlotte Brontë", "Emily Brontë", "Louisa May Alcott")
    insertFrage("Was ist die Hauptstadt von Argentinien?", "Buenos Aires", "Córdoba", "Rosario", "Mendoza")
    insertFrage("Welches Tier ist das größte Raubtier im Meer?", "Orca", "Hai", "Delfin", "Walross")
    insertFrage("Wie viele Tage hat der Februar in einem Schaltjahr?", "29", "28", "30", "31")
    insertFrage("Wer malte \"Guernica\"?", "Pablo Picasso", "Salvador Dalí", "Joan Miró", "Francisco Goya")
    insertFrage("Was ist die Hauptstadt von Ägypten?", "Kairo", "Alexandria", "Luxor", "Gizeh")
    insertFrage("Welches Element hat das chemische Symbol Au?", "Gold", "Silber", "Kupfer", "Platin")
    insertFrage("Wie viele Knochen hat ein erwachsener Mensch?", "206", "208", "210", "204")
    insertFrage("Wer schrieb \"Moby Dick\"?", "Herman Melville", "Mark Twain", "Nathaniel Hawthorne", "Edgar Allan Poe")
    insertFrage("Was ist die Hauptstadt von Griechenland?", "Athen", "Thessaloniki", "Patras", "Heraklion")
    insertFrage("Welches Tier ist das größte fliegende Säugetier?", "Flughund", "Fledermaus", "Adler", "Kondor")
    insertFrage("Wie viele Planeten gibt es in unserem Sonnensystem?", "8", "7", "9", "10")
    insertFrage("Wer erfand die Dampfmaschine?", "James Watt", "Thomas Newcomen", "George Stephenson", "Robert Fulton")
    insertFrage("Was ist die Hauptstadt von Portugal?", "Lissabon", "Porto", "Coimbra", "Braga")
    insertFrage("Welches Land hat die meisten Sprachen?", "Papua-Neuguinea", "Indien", "China", "Nigeria")
    insertFrage("Wie viele Herzen hat ein Oktopus?", "3", "1", "2", "4")
    insertFrage("Wer schrieb \"Die Schatzinsel\"?", "Robert Louis Stevenson", "Mark Twain", "Jules Verne", "Daniel Defoe")
    insertFrage("Was ist die Hauptstadt von Finnland?", "Helsinki", "Tampere", "Turku", "Oulu")
    insertFrage("Welches Tier ist das größte Tier der Welt?", "Blauwal", "Elefant", "Hai", "Giraffe")
    insertFrage("Wie viele Stunden hat eine Woche?", "168", "144", "156", "192")
    insertFrage("Wer malte \"Die Nachtwache\"?", "Rembrandt", "Vermeer", "Rubens", "Van Dyck")
    insertFrage("Was ist die Hauptstadt von Polen?", "Warschau", "Krakau", "Danzig", "Posen")
    insertFrage("Welches Element hat das chemische Symbol N?", "Stickstoff", "Neon", "Nickel", "Natrium")
    insertFrage("Wie viele Finger hat ein Mensch?", "10", "8", "12", "14")
    insertFrage("Wer schrieb \"Der große Gatsby\"?", "F. Scott Fitzgerald", "Ernest Hemingway", "John Steinbeck", "William Faulkner")
    insertFrage("Was ist die Hauptstadt von Kuba?", "Havanna", "Santiago de Cuba", "Camagüey", "Holguín")
    insertFrage("Welches Tier ist das größte Tier an Land?", "Elefant", "Giraffe", "Nilpferd", "Bär")
    insertFrage("Wie viele Tage hat der Monat März?", "31", "30", "28", "29")
    insertFrage("Wer erfand den Computer?", "Charles Babbage", "Alan Turing", "John von Neumann", "Konrad Zuse")
    insertFrage("Was ist die Hauptstadt von Thailand?", "Bangkok", "Chiang Mai", "Phuket", "Pattaya")
    insertFrage("Welches Land hat die meisten Berge?", "Nepal", "Schweiz", "China", "Indien")
    insertFrage("Wie viele Augen hat eine Spinne?", "8", "6", "4", "2")
    insertFrage("Wer schrieb \"Die drei Musketiere\"?", "Alexandre Dumas", "Victor Hugo", "Jules Verne", "Honoré de Balzac")
    insertFrage("Was ist die Hauptstadt von Südkorea?", "Seoul", "Busan", "Incheon", "Daegu")
    insertFrage("Welches Tier ist das größte Tier im Süßwasser?", "Nilkrokodil", "Flussdelfin", "Riesenwels", "Anakonda")
    insertFrage("Wie viele Tage hat der Monat Februar in einem normalen Jahr?", "28", "29", "30", "31")
    insertFrage("Wer malte \"Der Schrei\"?", "Edvard Munch", "Vincent van Gogh", "Claude Monet", "Pablo Picasso")
    insertFrage("Was ist die Hauptstadt von Kolumbien?", "Bogotá", "Medellín", "Cali", "Cartagena")
    insertFrage("Welches Element hat das chemische Symbol Ag?", "Silber", "Gold", "Kupfer", "Platin")
    insertFrage("Wie viele Chromosomen hat ein Mensch?", "46", "44", "48", "50")
    insertFrage("Wer schrieb \"Krieg und Frieden\"?", "Leo Tolstoi", "Fjodor Dostojewski", "Anton Tschechow", "Alexander Puschkin")
    insertFrage("Was ist die Hauptstadt von Chile?", "Santiago", "Valparaíso", "Concepción", "La Serena")


