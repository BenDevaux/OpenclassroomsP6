import csv
#from pyad import *
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *
from tkinter import ttk
import logging

#Fonction d'ouverture de fenêtre pour la création manuelle
def manualCreation():
    logging.info(" Ouverture de la fenêtre de création de compte via bouton 'Manuel' ")
    def manualCreation():
        fname = firstnameEntry.get()
        lname = lastnameEntry.get()
        password = passwordEntry.get()
        #globalGroup = pyad.adgroup.ADGroup.from_dn("CN=Global,OU=Groups,DC=opentp,DC=lan")
        #techGroup = pyad.adgroup.ADGroup.from_dn("CN=GRP_Tech,OU=Groups,DC=opentp,DC=lan")
        #comptaGroup = pyad.adgroup.ADGroup.from_dn("CN=GRP_Compta,OU=Groups,DC=opentp,DC=lan")
        #RHGroup = pyad.adgroup.ADGroup.from_dn("CN=GRP_RH,OU=Groups,DC=opentp,DC=lan")
        if len(fname) == 0:
            showwarning("Erreur", "Vous n'avez pas renseigné de prénom !")
            logging.warning("Tentative de création sans avoir de prénom renseigné")
        else:
            dname = fname + " " + lname
            user = fname[0] + lname
            if len(lname) == 0:
                showwarning("Erreur", "Vous n'avez pas renseigné de nom !")
                logging.warning("Tentative de création sans avoir de nom renseigné")
            else:
                if len(password) == 0:
                    showwarning("Erreur", "Vous n'avez pas renseigné de mot de passe !")
                    logging.warning("Tentative de création sans avoir de mot de passe renseigné")
                else:
                    if len(OUEntry.get()) == 0:
                        showwarning("Erreur", "Vous n'avez pas renseigné d'Unité Organisationelle !")
                        logging.warning("Tentative de création sans avoir d'OU renseigné")
                    else:
                        #ou = pyad.adcontainer.ADContainer.from_dn(OUEntry.get())
                        #new_user = pyad.aduser.ADUser.create(user,ou,password,optional_attributes={"givenName" : fname, "sn" : lname, "displayName" : dname})
                        selectUser = pyad.aduser.ADUser.from_cn(user)
                        if globalButton.state() == "('selected')" or "('focus, selected')":
                            selectUser.add_to_group(globalGroup)
                            print("sélectionné")
                        if techButton.state() == "('selected')" or "('focus, selected')":
                            selectUser.add_to_group(techGroup)
                        if comptaButton.state() == "('selected')" or "('focus, selected')":
                            selectUser.add_to_group(comptaGroup)
                        if RHButton.state() == "('selected')" or "('focus, selected')":
                            selectUser.add_to_group(RHGroup)
    
    manualCreationWindow = Tk()
    manualCreationWindow.configure(bg="white")

    #Génération des logs
    logging.basicConfig(filename="ScriptManualCreation.log", encoding="utf-8", format="%(asctime)s %(levelname)s: %(message)s", datefmt="%d/%m/%Y %H:%M:%S", level=logging.DEBUG)
    #Création d'une barre de menu
    menubar = Menu(manualCreationWindow)

    #Création du menu "Quitter"
    menu1 = Menu(menubar, tearoff=0)
    menu1.add_command(label="Quitter", command=quitMenu)
    menubar.add_cascade(label="Quitter", menu=menu1)
    manualCreationWindow.config(menu=menubar)

    #Texte de présentation
    titre = Label(manualCreationWindow, bg="white", text="Bienvenue sur l'outil de création de compte AD, \n\
    veuillez entrer les informations de l'utilisateur :", justify=CENTER)
    titre.grid(row=0, pady=20, padx=20, columnspan=4)

    #Prénom
    firstnameLabel = Label(manualCreationWindow, bg="white", text="Prénom :")
    firstnameLabel.grid(row=1, pady=20, padx=20, column=0)

    firstnameEntry = Entry(manualCreationWindow, bg="white", width=15)
    firstnameEntry.grid(row=1, pady=20, padx=20, column=1)

    #Nom de famille
    lastnameLabel = Label(manualCreationWindow, bg="white", text="Nom :")
    lastnameLabel.grid(row=1, pady=20, padx=20, column=2)

    lastnameEntry = Entry(manualCreationWindow, bg="white", width=15)
    lastnameEntry.grid(row=1, pady=20, padx=20, column=3)

    #Mot de passe
    passwordLabel = Label(manualCreationWindow, bg="white", text="Mot de passe :")
    passwordLabel.grid(row=2, pady=20, padx=20, column=0)

    passwordEntry = Entry(manualCreationWindow, bg="white", show="*", width=15)
    passwordEntry.grid(row=2, pady=20, padx=20, column=1)

    #OU
    OULabel = Label(manualCreationWindow, bg="white", text="OU :")
    OULabel.grid(row=2, pady=20, padx=20, column=2)

    OUEntry = Entry(manualCreationWindow, bg="white", width=15)
    OUEntry.grid(row=2, pady=20, padx=20, column=3)

    #Groupes
    groupsLabel = Label(manualCreationWindow, bg="white", text="Groupes :")
    groupsLabel.grid(row=3, padx=20, columnspan=4)

    groupsFrame = Frame(manualCreationWindow, borderwidth=2, relief=GROOVE)
    groupsFrame.grid(row=4, columnspan=4, pady=20)

    globalButton = ttk.Checkbutton(groupsFrame, text="Global")
    globalButton.state(['!alternate'])
    globalButton.grid(sticky=W)
    techButton = ttk.Checkbutton(groupsFrame, text="Technicien")
    techButton.state(['!alternate'])
    techButton.grid(sticky=W)
    comptaButton = ttk.Checkbutton(groupsFrame, text="Comptabilité")
    comptaButton.state(['!alternate'])
    comptaButton.grid(sticky=W)
    RHButton = ttk.Checkbutton(groupsFrame, text="Ressources Humaines")
    RHButton.state(['!alternate'])
    RHButton.grid(sticky=W)

    #Bouton confirmer
    manualCreationButton = Button(manualCreationWindow, text="Confirmer", command=manualCreation)
    manualCreationButton.grid(row=5, columnspan=4, pady=20)

#Fonction d'ouverture de fenêtre pour la création via fichier CSV
def csvCreation():
    logging.info(" Ouverture de la fenêtre de création de compte via bouton 'Fichier CSV' ")
    csvWindow = Tk()
    csvWindow.configure(bg="white")

    def filePathCommand():
        global filePath
        filePath = askopenfilename(title="Ouvrir fichier csv", filetypes=[("csv files",".csv")])
        testText = Label(pathFrame, text=filePath, bg="white")
        testText.pack()
        logging.info( f"Sélections du fichier {filePath} ")

    def createUser():
        if filePath.endswith(".csv"):
            contenu = open(filePath,encoding="utf-8")
            csv_contenu = csv.reader(contenu)
            donnees_ligne = list(csv_contenu)
            for line in donnees_ligne[1:]:
                lname = line[0]
                fname = line[1]
                user = line[2]
                dname = fname + " " + lname
                ou = pyad.adcontainer.ADContainer.from_dn("ou=Utilisateurs, ou=OPENTP, dc=opentp, dc=lan")
                new_user = pyad.aduser.ADUser.create(user,ou,password="Bouj15ko", optional_attributes={"givenName" : fname, "sn" : lname, "displayName" : dname})
                showinfo("Titre 3", f"L'utilisateur {fname} {lname} a bien été créé")
                logging.info(f"Création de l'utilisateur {fname} {lname}")
        else:
            showwarning("Titre 2", "Vous n'avez pas entré de fichier CSV, veuillez cliquer sur le bouton Parcourir")

    #Fonction pour quitter via le menu "Quitter"
    def quitMenu():
        if askyesno("Titre 1", "Souhaitez vous quitter ?"):
            logging.info(" Fermeture via le menu 'Quitter' ")
            csvWindow.destroy()

    #Génération des logs
    logging.basicConfig(filename="Scriptlogoo.log", encoding="utf-8", format="%(asctime)s %(levelname)s: %(message)s", datefmt="%d/%m/%Y %H:%M:%S", level=logging.DEBUG)
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
    pathFrame = Frame(csvWindow, bg="white", borderwidth=2, relief=GROOVE, width=315, height=25)
    pathFrame.grid(row=1, column=0, pady=15, padx=20, sticky=W)

    #Bouton parcourir
    chooseFileButton = Button(csvWindow, text ="Parcourir", command=filePathCommand)
    chooseFileButton.grid(row=1, column=1, pady=15, padx=20)

    #Bouton confirmer
    createButton = Button(csvWindow, text="Confirmer", command=createUser)
    createButton.grid(row=2, columnspan=2, pady=15)


    csvWindow.mainloop()
    

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
    logging.info(" Ouverture de la fenêtre 'à propos' ")

#Fonction pour quitter via le menu "Quitter"
def quitMenu():
    if askyesno("Titre 1", "Souhaitez vous quitter ?"):
        logging.info(" Fermeture via le menu 'Quitter' ")
        mainWindow.destroy()

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

#Bouton création manuelle
manualButton = Button(mainWindow, text="Manuel", command=manualCreation, width=15)
manualButton.pack(side=LEFT, pady=15, padx=70)

#Bouton fichier CSV
csvButton = Button(mainWindow, text="Fichier CSV", command=csvCreation, width=15)
csvButton.pack(side=RIGHT, pady=15, padx=70)

mainWindow.mainloop()
