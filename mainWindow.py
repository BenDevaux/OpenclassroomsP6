from tkinter import *
from tkinter.messagebox import *
import sys

def manualCreation():
    showinfo("Titre3","Test du bouton de création manuelle")

def csvCreation():
    showinfo("Titre3","Test du bouton de création via fichier CSV")

def helpMenu():
    showinfo("Titre3","Test")

def quitMenu():
    if askyesno("Titre 1", "Souhaitez vous quitter ?"):
        mainWindow.destroy()

mainWindow = Tk()
#mainWindow.geometry("500x200")
mainWindow.configure(bg="white")

#colorLine = PanedWindow(mainWindow, orient=HORIZONTAL)
#colorLine.pack(side=TOP, expand=Y, fill=BOTH)
#colorLine.add(Label(colorLine, text="", bg="grey", font="Arial 1"))
#colorLine.pack()

menubar = Menu(mainWindow)

menu1 = Menu(menubar, tearoff=0)
menu1.add_command(label="Quitter", command=quitMenu)
menubar.add_cascade(label="Quitter", menu=menu1)

menu2 = Menu(menubar, tearoff=0)
menu2.add_command(label="à propos", command=helpMenu)
menubar.add_cascade(label="Aide", menu=menu2)
mainWindow.config(menu=menubar)

mainTitle = Label(mainWindow, text="Bienvenue sur l'outil de gestion de l'Active Directory", bg="white", font="Nunito 14")
mainTitle.pack(pady=20, padx=20)

tutorialFrame = Frame(mainWindow, bg="white", borderwidth=2, relief=GROOVE)
tutorialFrame.pack(pady=10, padx=5)
tutorialLabel = Label(tutorialFrame, text = "Cet outil permet de créer un ou plusieurs utilisateurs Active Directory. \n\
Vous pouvez les créer manuellement ou à l'aide d'un fichier CSV.\n\
Veuillez appuyer sur le bouton correspondant à la méthode que vous souhaitez utiliser.", justify=LEFT, bg="white")
tutorialLabel.pack(padx=5, pady=10)


manualButton = Button(mainWindow, text="Manuel", command=manualCreation, width=15)
manualButton.pack(side=LEFT, pady=15, padx=70)

csvButton = Button(mainWindow, text="Fichier CSV", command=csvCreation, width=15)
csvButton.pack(side=RIGHT, pady=15, padx=70)

mainWindow.mainloop()
