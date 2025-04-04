from tkinter import *
import tkinter as tk
from tkinter.scrolledtext import ScrolledText

root = Tk()
root.title("Admin Fenster")
root.geometry("1200x800")
root.configure(bg="white")


#DatenbankViewer
dbLabel = Label(root)
dbLabel.place(x=750, y=50, width=400, height=700) #Anordnung durch Place-Manager

st = ScrolledText(dbLabel, width=400, height =700)
st.pack()

#Fragen container
fragenContainer = Label(root, bg="lightgrey")
fragenContainer.place(x=50, y=100, width=650, height=70)

nrLabel = Label(fragenContainer, bg="white", fg="black", text="001")
nrLabel.place(width=160, height=70)

fragenLabel = Label(fragenContainer, bg="lightgreen", fg="black", text="Wie viele Haare hat Daniele?")
fragenLabel.place(x=160, height=70, width=485)


#Antworten container
answContainer = Label(root, bg="red")
answContainer.place(x=50, y=200, width = 650, height=350)



#Edit
edit = Button(root, bg="red", text="EDIT")
edit.place(x=50, y=650, width=300, height=70)

delete = Button(root, bg="red", text="DELETE")
delete.place(x=400, y=650, width=300, height=70)





root.mainloop()
