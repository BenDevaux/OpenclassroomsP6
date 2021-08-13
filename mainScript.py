"""
    .Description:
    Script de création de compte Active Directory manuellement ou par fichier CSV

    .Notes
    Auteur : Benjamin DEVAUX
    Version: Alpha 0.1
    Date: 02/08/2021

    Réalisé sous Python 3.9.6, testé sur Windows server 2016
"""

#import des librairies
import csv #Exploitation de fichier CSV
#from pyad import * #Communication avec l'AD
from tkinter import * #Création d'interface graphique
from tkinter.messagebox import * #Affichage de message d'information
from tkinter.filedialog import * #Recherche de fichier via l'explorateur
from tkinter import ttk #Création de checkbox
import logging #Gestion des logs
import ADcsv
import manualCreationWindow
import configparser

#Fonction d'ouverture d'une fenêtre "à propos" depuis le menu "aide"
def helpMenu():
    """
        helpMenu : Affiche le menu 'à propos'
    """
    helpWindow = Tk()
    helpWindow.configure(bg="white")
    helpTitle = Label(helpWindow, text="A propos", bg="white", font="Arial 14")
    helpTitle.pack(padx=5, pady=5)
    testLabel = Label(helpWindow, text="Outil créé par : Benjamin Devaux \n\
Version : 1.0 \n\
Date de la version : 30/07 \n ", justify=LEFT, bg="white" )
    testLabel.pack(padx=10, pady=10)
    logging.info(" Ouverture de la fenêtre 'à propos' ")

#Fonction pour quitter via le menu "Quitter"
def quitMenu():
    """
            quitMenu : Fermeture de la fenêtre principale via le menu 'Quitter'
    """
    if askyesno("Titre 1", "Souhaitez vous quitter ?"):
        logging.info(" Fermeture via le menu 'Quitter' ")
        mainWindow.destroy()

configuration = configparser.ConfigParser()
configuration.read('configuration.ini')

#Génération des logs
logging.basicConfig(filename="Scriptlog.log", encoding="utf-8", format="%(asctime)s %(levelname)s: %(message)s", datefmt="%d/%m/%Y %H:%M:%S", level=logging.DEBUG)

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

def displayManualCreationWindow():
    global configuration
    manualCreationWindow.manualWindow(configuration)
#Bouton création manuelle
manualButton = Button(mainWindow, text="Manuel", command=displayManualCreationWindow, width=15)
manualButton.pack(side=LEFT, pady=15, padx=70)

#Bouton fichier CSV
csvButton = Button(mainWindow, text="Fichier CSV", command=ADcsv.CSVFileWindow, width=15)
csvButton.pack(side=RIGHT, pady=15, padx=70)

mainWindow.mainloop()
