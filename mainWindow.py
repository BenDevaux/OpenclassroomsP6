from tkinter import *
from tkinter.messagebox import *

#Fonction d'ouverture de fenêtre pour la création manuelle
def manualCreation():
    showinfo("Titre3","Test du bouton de création manuelle")

#Fonction d'ouverture de fenêtre pour la création via fichier CSV
def csvCreation():
    showinfo("Titre3","Test du bouton de création via fichier CSV")

#Fonction d'ouverture d'une fenêtre "à propos" depuis le menu "aide"
def helpMenu():
    helpWindow = Tk()
    helpWindow.configure(bg="white")
    helpTitle = Label(helpWindow, text="A propos", bg="white", font="Arial 14")
    helpTitle.pack(padx=5, pady=5)
    testLabel = Label(helpWindow, text="Outil créé par : Benjamin Devaux \n\
Version : 1.0 \n\
Date de la version : 30/07 \n ", justify=LEFT, bg="white" )
    testLabel.pack(padx=10, pady=10)

#Fonction pour quitter via le menu "Quitter"
def quitMenu():
    if askyesno("Titre 1", "Souhaitez vous quitter ?"):
        mainWindow.destroy()

#Création de la fenêtre principale
mainWindow = Tk()
#mainWindow.geometry("500x200")
mainWindow.configure(bg="white")

#Création d'une barre de menu
menubar = Menu(mainWindow)

#Création du menu "Quitter"
menu1 = Menu(menubar, tearoff=0)
menu1.add_command(label="Quitter", command=quitMenu)
menubar.add_cascade(label="Quitter", menu=menu1)

#Création du menu "Aide"
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

#Bouton création manuelle
manualButton = Button(mainWindow, text="Manuel", command=manualCreation, width=15)
manualButton.pack(side=LEFT, pady=15, padx=70)

#Bouton fichier CSV
csvButton = Button(mainWindow, text="Fichier CSV", command=csvCreation, width=15)
csvButton.pack(side=RIGHT, pady=15, padx=70)

mainWindow.mainloop()
