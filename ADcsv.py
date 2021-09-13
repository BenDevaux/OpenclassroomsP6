"""
    .Description:
    Script de création de compte Active Directory, fenêtre de création via fichier CSV

    .Notes
    Auteur : Benjamin DEVAUX
    Version: 1.0
    Date: 13/09/2021

    Réalisé sous Python 3.9.6, testé sur Windows server 2016
"""

import csv
from pyad import *
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *
import logging
import userCreationScript

def filePathCommand():
    """
        filePathCommand : Ouverture de fichier CSV
    """
    global filePath
    global pathFrame
    filePath = askopenfilename(title="Ouvrir fichier csv", filetypes=[("csv files",".csv")])
    testText = Label(pathFrame, text=filePath, bg="white")
    testText.pack()
    logging.info( f"Sélections du fichier {filePath} ")

def callUserCreation():
    """
        callUserCreation : Appelle la fonction de création d'utilisateur avec les attributs correspondants
    """
    global user, ou, password, fname, lname, dname
    userCreationScript.userCreation(user, ou, password, fname, lname, dname)

def createUser():
    """
        createUser : Récupère les données du fichier CSV pour création des utilisateurs
    """
    global filePath
    if filePath.endswith(".csv"):
        contenu = open(filePath,encoding="utf-8")
        csv_contenu = csv.reader(contenu)
        donnees_ligne = list(csv_contenu)
        for line in donnees_ligne[1:]:
            global user, ou, password, fname, lname, dname
            lname = line[0]
            fname = line[1]
            user = line[2]
            dname = fname + " " + lname
            password = 'Bonsoir15'
            ou = pyad.adcontainer.ADContainer.from_dn("ou=Utilisateurs, ou=OPENTP, dc=opentp, dc=lan")
            callUserCreation()
            #new_user = pyad.aduser.ADUser.create(user,ou,password="Bouj15ko", optional_attributes={"givenName" : fname, "sn" : lname, "displayName" : dname})
            showinfo("Titre 3", f"L'utilisateur {fname} {lname} a bien été créé")
            logging.info(f"Création de l'utilisateur {fname} {lname}")
    else:
        showwarning("Titre 2", "Vous n'avez pas entré de fichier CSV, veuillez cliquer sur le bouton Parcourir")

def quitMenu():
    """
        quitMenu : Menu quitter
    """
    if askyesno("Titre 1", "Souhaitez vous quitter ?"):
        logging.info(" Fermeture via le menu 'Quitter' ")
        csvWindow.destroy()

def CSVFileWindow():
    """
        CSVFileWindow : Configuration de la fenêtre de création d'utilisateur via fichier CSV
    """
    csvWindow = Tk()
    csvWindow.configure(bg="white")
    #Génération des logs
    logging.basicConfig(filename="ScriptCSVCreation.log", encoding="utf-8", format="%(asctime)s %(levelname)s: %(message)s", datefmt="%d/%m/%Y %H:%M:%S", level=logging.DEBUG)
    #Création d'une barre de menu
    menubar = Menu(csvWindow)

    #Création du menu "Quitter"
    menu1 = Menu(menubar, tearoff=0)
    menu1.add_command(label="Quitter", command=quitMenu)
    menubar.add_cascade(label="Quitter", menu=menu1)
    csvWindow.config(menu=menubar)

    #Texte de présentation
    titre = Label(csvWindow, bg="white", text="Bienvenue sur l'outil de création de compte AD, \n\
    veuillez entrer le chemin du fichier CSV :", justify=CENTER)
    titre.grid(row=0, pady=20, padx=20, columnspan=2)

    #Frame du chemin
    global pathFrame
    pathFrame = Frame(csvWindow, bg="white", borderwidth=2, relief=GROOVE, width=315, height=25)
    pathFrame.grid(row=1, column=0, pady=15, padx=20, sticky=W)

    #Bouton parcourir
    chooseFileButton = Button(csvWindow, text ="Parcourir", command=filePathCommand)
    chooseFileButton.grid(row=1, column=1, pady=15, padx=20)

    #Bouton confirmer
    createButton = Button(csvWindow, text="Confirmer", command=createUser)
    createButton.grid(row=2, columnspan=2, pady=15)


    csvWindow.mainloop()
