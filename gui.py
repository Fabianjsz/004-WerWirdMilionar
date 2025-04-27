#import
from tkinter import *
import tkinter as tk
from tkinter import ttk
from utility import informationWindow
from databaseUtility import checkFrage, returnTable, returnQuestion, fetchQuestion
from tkinter.scrolledtext import ScrolledText



#Variablen

global fragenText, aText, bText, cText, dText, fragenNummer

fragenNummer = "001"
fragenText = "Frage"
aText = "Antwort A"
bText = "Antwort B"
cText = "Antwort C"
dText = "Antwort D"


#funktion


    

def delete_popup():
    win = tk.Toplevel()
    win.wm_title("Frage Löschen")
    win.geometry("200x80")
    
    deleteLabel = Label(win, text="Welche Nummer willst du Löschen?")
    deleteLabel.place(width=200)
    
    eingabe = tk.Entry(win)
    eingabe.place(width=40, y=20, x=80)
    
    deleteButton = Button(win, text="Lösche Nummer", bg="red", command=lambda:confirmation_window(eingabe))
    deleteButton.place(width = 100, y=50, x =50)


def confirmation_window(entry):
    confirmation = tk.Toplevel()
    confirmation.wm_title("sind sie sich sicher?")
    confirmation.geometry("200x80")
    
    conLabel = Label(confirmation, text="möchten sie die Frage löschen?")
    conLabel.place(width=200)
    
    yes = Button(confirmation, text="Ja", bg="green", fg="white", command=lambda:confirmation_yes(entry))
    yes.place(y=20,width=100, height=60)    

    no = Button(confirmation, text="Nein",bg="red", fg="white", command=lambda:confirmation_no())
    no.place(y=20, x=100, width=100, height="60")


def confirmation_yes(entry):
    fragenNr = entry.get()
    print(checkFrage(fragenNr))



    
    
def confirmation_no():
    pass

"""
edit_item

"""
def edit_item():
    pass

"""
delete_item

"""
def delete_item():
    pass


"""
Update Data
Setzt die in die Funktion eingesetzten Daten in das Treeviewfenster
"""
def updateData(data):
    tempData = returnTable()
    for row in tempData:
        data.insert("", tk.END, values=row)


"""
visualize Data
Hollt sich daten mit der returnTable Funktion und zeigt diese dann in den vorgesehenen Fenstern an
"""
def visualizeData(fragenNr):
    displayData = returnQuestion(fragenNr)
    nonTuple = displayData[0]
    fragenNummer = nonTuple[0]
    fragenText = nonTuple[0]
    aText = nonTuple[0]
    bText = nonTuple[0]
    cText = nonTuple[0]
    dText = nonTuple[0]

    updateLable()


"""
show popup
erstellt ein kontextMenü bei Rechtsklick auf dem Treeview
"""
def show_popup(event):

    selected_item = data.identify_row(event.y)
    if selected_item:
        data.selection_set(selected_item)

        menu = tk.Menu(root, tearoff=0)
        menu.add_command(label="Bearbeiten", command=lambda: edit_item(selected_item))
        menu.add_command(label="Löschen", command=lambda:delete_item(selected_item))
        menu.post(event.x_root, event.y_root)


"""
on double click
Reagiert auf Doppelklick auf dem Treeviewfenster und gibt die ausgewählte FragenNr weiter an die returnTable Funktion
"""
def on_double_click(event):

    selected_item = data.selection()[0]  # Item Id wird ausgelesen
    values = data.item(selected_item, "values")  # Item Id wird in die einzelnen daten übersetzt, wobei die FragenNr im index [0] steckt

    displayData = fetchQuestion(values[0])
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
def updateLable(fragenNummer, fragenText, aText, bText, cText, dText):
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
data.column("Nr", width=20)
data.column("Frage", width=480)

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



#Edit
edit = Button(root, bg="red", text="EDIT")
edit.place(x=50, y=700, width=300, height=70)

delete = Button(root, bg="red", text="DELETE")
delete.place(x=400, y=700, width=300, height=70)




updateData(data)


root.mainloop()

