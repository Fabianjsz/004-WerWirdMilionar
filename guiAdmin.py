"""
Diese Datei beinhaltet die GUI und Funktionen,welche für die Admin Maske benötigt werden
Name: guiAdmin.py
Autor: Fabianjsz
Datum: 27.04.2025
"""


#import
from tkinter import *
import tkinter as tk
from tkinter import ttk, simpledialog, messagebox
from databaseUtility import checkFrage, returnTable, returnQuestion, fetchQuestion, deleteFrage, editFrage, insertFrage
from tkinter.scrolledtext import ScrolledText
from tkinter.messagebox import showinfo



#Variablen

global fragenText, aText, bText, cText, dText, fragenNummer, data

fragenNummer = "001"
fragenText = "Frage"
aText = "Antwort A"
bText = "Antwort B"
cText = "Antwort C"
dText = "Antwort D"


#funktion

"""
edit_item
Fenster, für das Bearbeiten der Fragen
"""
def delete_popup():
    win = tk.Toplevel()
    win.wm_title("Frage Löschen")
    win.geometry("200x80")

    deleteLabel = Label(win, text="Welche Nummer willst du Löschen?")
    deleteLabel.place(width=200)
    eingabe = tk.Entry(win)
    eingabe.place(width=40, y=20, x=80)
    deleteButton = Button(win, text="Lösche Nummer", bg="red")
    deleteButton.place(width = 100, y=50, x =50)


"""
edit item
Bearbeitungsfenster für das Bearbeiten von Fragen
"""
def edit_item(fragenNr):
    global frageEntry, aEntry, bEntry, cEntry, dEntry

    win = tk.Toplevel()
    win.wm_title("Frage Bearbeiten")
    win.geometry("400x300")

    # Fetch data from database
    questionTuple = fetchQuestion(fragenNr)
    question = questionTuple[0]

    edit = Label(win, text="Frage Bearbeiten")
    edit.place(x=0, y=0, width=400)

    frageEntry = Entry(win)
    frageEntry.place(x=30, y=20, width=340)
    frageEntry.insert(0, question[1])

    antwortLabel = Label(win, text="Antworten bearbeiten")
    antwortLabel.place(x=0, y=70, width=400)

    aEntry = Entry(win)
    aEntry.place(x=30, y=100, width=340)
    aEntry.insert(0, question[2])

    bEntry = Entry(win)
    bEntry.place(x=30, y=130, width=340)
    bEntry.insert(0, question[3])

    cEntry = Entry(win)
    cEntry.place(x=30, y=160, width=340)
    cEntry.insert(0, question[4])

    dEntry = Entry(win)
    dEntry.place(x=30, y=190, width=340)
    dEntry.insert(0, question[5])


    confirmation = Button(win, text="Bearbeiten",command=lambda: editQuestion(fragenNr, question[1:], win))
    confirmation.place(x=150, y=240, width=100)



def editQuestion(fragenNr, question, win):
    edit = (frageEntry.get(), aEntry.get(), bEntry.get(),cEntry.get(),dEntry.get())

    print(f"question {question}, and edit {edit}")
    if question != edit:
        print(f"unterschiedlich {edit[0]},{edit[1]},{edit[2]},{edit[3]},{edit[4]}")
        editFrage(fragenNr, edit[0], edit[1],edit[2],edit[3],edit[4],)
        updateData()
    else:
        pass
    updateData()
    temp = fetchQuestion(fragenNr)
    print(temp)
    tempo = temp[0]
    print(tempo)
    updateLable(fragenNr,tempo[1],tempo[2],tempo[3],tempo[4],tempo[5])
    win.destroy()



"""
edit item
Bearbeitungsfenster für das Bearbeiten von Fragen
"""

def add_item():
    global frageEntry, aEntry, bEntry, cEntry, dEntry

    win = tk.Toplevel()
    win.wm_title("Frage erstellen")
    win.geometry("400x300")

    edit = Label(win, text="Frage Erstellen")
    edit.place(x=0, y=0, width=400)

    frageEntry = Entry(win)
    frageEntry.place(x=30, y=20, width=340)

    antwortLabel = Label(win, text="Antworten Erstellen")
    antwortLabel.place(x=0, y=70, width=400)

    aEntry = Entry(win)
    aEntry.place(x=30, y=100, width=340)

    bEntry = Entry(win)
    bEntry.place(x=30, y=130, width=340)

    cEntry = Entry(win)
    cEntry.place(x=30, y=160, width=340)

    dEntry = Entry(win)
    dEntry.place(x=30, y=190, width=340)

    confirmation = Button(win, text="Frage hinzufügen",command=lambda: createFrage(win))
    confirmation.place(x=150, y=240, width=100)

    
def popup_showinfo(text):
    showinfo(f"Information", f"{text}")



def createFrage(win):
    insertFrage(frageEntry.get(), aEntry.get(), bEntry.get(), cEntry.get(), dEntry.get())
    popup_showinfo("Frage wurde erfolgreich eingefügt!")
    updateData()
    win.destroy()





"""
delete_item
Popup welches das Löschen bestätigen soll
"""
def delete_item(fragenNr):
    #bestätigung des Löschvorganges
    answer = messagebox.askyesno("löschen", "Wollen sie diese Frage löschen?")
    if answer:
        deleteFrage(fragenNr)
        showinfo("", f"Frage {fragenNr} wurde erfolgreich gelöscht")
    updateData()



"""
Update Data
Setzt die in die Funktion eingesetzten Daten in das Treeviewfenster
"""
def updateData():
    for item in data.get_children():
        data.delete(item)

    tempData = returnTable()
    i = 1
    for row in tempData:
        #print(f"Laufvariable:{i}, datenTuple{row}")
        tempTuple = tempData[i-1]
        temp = tempTuple[0]
        data.insert("", tk.END, iid=temp, values=(i, row[1])) # iid == primary key Fragen
        i = i + 1



"""
show popup
erstellt ein kontextMenü bei Rechtsklick auf dem Treeview
"""
def show_popup(event):

    selected_item = data.identify_row(event.y)
    if selected_item:
        data.selection_set(selected_item)
        fragenNr = selected_item

        menu = tk.Menu(root, tearoff=0)
        menu.add_command(label="Bearbeiten", command=lambda: edit_item(fragenNr))
        menu.add_command(label="Löschen", command=lambda:delete_item(fragenNr))
        menu.add_command(label="Neue Frage", command=add_item)
        menu.post(event.x_root, event.y_root)


"""
on double click
Reagiert auf Doppelklick auf dem Treeviewfenster und gibt die ausgewählte FragenNr weiter an die returnTable Funktion
"""
def on_double_click(event):
    

    selected_item = data.selection()[0]  # da der primary key im iid ist, wird hier der primary key ausgegeben
    
    displayData = fetchQuestion(selected_item)
    nonTuple = displayData[0]

    nonTuple = displayData[0]
    # Einsetzen der Daten in globale Variablen

    fragenNummer = nonTuple[0]
    fragenText = nonTuple[1]
    aText = nonTuple[2]
    bText = nonTuple[3]
    cText = nonTuple[4]
    dText = nonTuple[5]

    updateLable(fragenNummer,fragenText, aText, bText, cText, dText)



"""
update Lable
ersetzt die alten Inhalte mit den neuen aus den vorhergesehenen Variablen
"""
def updateLable(fragenNummer,fragenText, aText, bText, cText, dText):
    nrLabel.config(text=fragenNummer)
    fragenLabel.config(text=fragenText)
    antwortA.config(text=aText)
    antwortB.config(text=bText)
    antwortC.config(text=cText)
    antwortD.config(text=dText)


#GUI

root = Tk()
root.title("Admin Fenster")
root.geometry("1200x800")


#DatenbankViewer
dbLabel = Label(root)
dbLabel.place(x=750, y=50, width=400, height=600) #Anordnung durch Place-Manager

#Definierung der Spalten
columns = ("Nr", "Frage")

# Erstellung des Tabellenobjektes
data = ttk.Treeview(dbLabel, columns=columns, show="headings")
data.pack(side="left", fill="both", expand=True)

# Konfigurierung der Spalten
data.column("Nr", width=50)
data.column("Frage", width=450)

# Einsetzen der Spalten
for col in columns:
    data.heading(col, text=col)

# Bind the double-click event
data.bind("<Double-1>", on_double_click)
data.bind("<Button-3>", show_popup)


# Einfügen der Scrollleiste
scrollbar = ttk.Scrollbar(dbLabel, orient="vertical", command=data.yview)
data.configure(yscrollcommand=scrollbar.set)
scrollbar.pack(side="right", fill="y")




#Fragen container
fragenContainer = Label(root, bg="lightgrey")
fragenContainer.place(x=50, y=100, width=650, height=70)

nrLabel = Label(fragenContainer, bg="white", text=fragenNummer)
nrLabel.place(width=100, height=70)

fragenLabel = Label(fragenContainer, bg="lightgreen", text=fragenText)
fragenLabel.place(x=100, height=70, width=545)


#Antworten container
answContainer = Label(root, bg="lightgrey")
answContainer.place(x=50, y=200, width = 650, height=280)


#Antwort A
answerOneContainer = Label(answContainer, bg="green")
answerOneContainer.place(x=0, y=0, width = 650, height=70)

letterOne = Label(answerOneContainer, text="A")
letterOne.place(width=100, height= 70)

antwortA = Label(answerOneContainer, bg="grey", text=aText)
antwortA.place(x=100,width=550, height=70)



#Antwort B
answerTwoContainer = Label(answContainer, bg="blue")
answerTwoContainer.place(x=0, y=70, width = 650, height=70)


letterTwo = Label(answerTwoContainer, text="B")
letterTwo.place(width=100, height= 70)

antwortB = Label(answerTwoContainer, bg="grey", text=bText)
antwortB.place(x=100,width=550, height=70)



#Antwort C
answerThreeContainer = Label(answContainer, bg="red")
answerThreeContainer.place(x=0, y=140, width = 650, height=70)

letterThree = Label(answerThreeContainer,  text="C")
letterThree.place(width=100, height= 70)

antwortC = Label(answerThreeContainer, bg="grey", text=cText)
antwortC.place(x=100,width=550, height=70)


#Antowrt D
answerFourContainer = Label(answContainer, bg="yellow")
answerFourContainer.place(x=0, y=210, width = 650, height=70)

letterFour = Label(answerFourContainer, text="D")
letterFour.place(width=100, height= 70)

antwortD = Label(answerFourContainer, bg="grey", text=dText)
antwortD.place(x=100,width=550, height=70)


updateData()
