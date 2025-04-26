#import
from tkinter import *
import tkinter as tk
from utility import informationWindow
from databaseUtility import checkFrage
from tkinter.scrolledtext import ScrolledText



#Variablen
fragenText = "Frage"
aText = "Antwort A"
bText = "Antwort B"
cText = "Antwort C"
dText = "Antwort D"


#funktion

def edit_popup():
    pass
    

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




def search_popup():
    win = tk.Toplevel()
    win.wm_title("Frage Suchen")
    win.geometry("200x80")
    
    searchLabel = Label(win, text="Welche Nummer willst du suchen?")
    searchLabel.place(width=200)
    
    eingabe = tk.Entry(win)
    eingabe.place(width=40, y=20, x=80)
    
    searchButton = Button(win, text="Suche Nummer", bg="red")
    searchButton.place(width = 100, y=50, x =50)
    



#GUI

root = Tk()
root.title("Admin Fenster")
root.geometry("1200x800")


#DatenbankViewer
dbLabel = Label(root)
dbLabel.place(x=750, y=50, width=400, height=600) #Anordnung durch Place-Manager

st = ScrolledText(dbLabel, width=400, height =700)
st.pack()

#Fragen container
fragenContainer = Label(root, bg="lightgrey")
fragenContainer.place(x=50, y=100, width=650, height=70)

nrLabel = Label(fragenContainer, bg="white", text="001")
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
edit = Button(root, bg="red", text="EDIT", command = edit_popup)
edit.place(x=50, y=700, width=300, height=70)

delete = Button(root, bg="red", text="DELETE", command = delete_popup)
delete.place(x=400, y=700, width=300, height=70)

search = Button(root, bg="red", text="SEARCH", command = search_popup)
search.place(x=800, y=700, width=300, height=70)





root.mainloop()

