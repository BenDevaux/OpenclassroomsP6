"""
    .Description:
    Script de création de compte Active Directory manuellement ou par fichier CSV

    .Notes
    Auteur : Benjamin DEVAUX
    Version: 1.0
    Date: 13/09/2021

    Réalisé sous Python 3.9.6, testé sur Windows server 2016
    Code disponnible sur le dépôt https://github.com/BenDevaux/OpenclassroomsP6
    Code diffusé sous licence GNU GPLv3
"""

from pyad import *
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
from tkinter.filedialog import *
import logging
import userCreationScript

OUList = dict()
groupsList = dict()
selected = {}
groupe = {}

#Fonction pour quitter via le menu "Quitter"
def quitMenu():
    """
        quitMenu : Menu quitter
    """
    if askyesno("Titre 1", "Souhaitez vous quitter ?"):
        logging.info(" Fermeture via le menu 'Quitter' ")
        manualCreationWindow.destroy()

def selectedGroup():
    """
        selectedGroup : Récupère les groupes cochés dans un dictionnaire
    """
    global groupe
    groupe = {}
    for key in groupsList:
        print(selected[key].get())
        if selected[key].get():
            groupe[key] = groupsList[key]
    print(groupe)

def callUserCreation():
    """
        callUserCreation : Appelle la fonction de création d'utilisateur
    """
    global user, ou, password, fname, lname, dname
    userCreationScript.userCreation(user, ou, password, fname, lname, dname)


def selectOU(event):
    """
        selectOU : Récupère la valeur sélectionnée dans la liste déroulante
    """
    global OUList, OUCombo, selectedOU
    OU = OUCombo.get()
    selectedOU = OUList[OU]

def manualCreation():
    """
        manualCreation : Récupération des données remplies pour création de l'utilisateur
    """
    global OUEntry, user, ou, password, fname, lname, dname, selectedOU
    global groupsList, groupe, selected

    fname = firstnameEntry.get()
    lname = lastnameEntry.get()
    password = passwordEntry.get()
    
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
                #Création de l'utilisateur et attribution des groupes
                ou = pyad.adcontainer.ADContainer.from_dn(selectedOU)
                callUserCreation()
                showinfo("Titre 3", f"L'utilisateur {fname} {lname} a bien été créé")
                logging.info(f"Création de l'utilisateur {fname} {lname}")
                selectUser = pyad.aduser.ADUser.from_cn(user)
                print(groupe)
                for key in groupe:
                    grp = groupe[key]
                    print(grp)
                    pyad.adgroup.ADGroup.from_dn(grp).add_members(selectUser)
                

def manualWindow(configuration, mainWindow):
    """
        manualWindow : Création de la fenêtre de création manuelle d'utilisateur
    """
    manualCreationWindow = Toplevel(mainWindow)
    manualCreationWindow.configure(bg="white")


    #Génération des logs
    #logging.basicConfig(filename="ScriptManualCreation.log", encoding="utf-8", format="%(asctime)s %(levelname)s: %(message)s", datefmt="%d/%m/%Y %H:%M:%S", level=logging.DEBUG)
    #Création d'une barre de menu
    menubar = Menu(manualCreationWindow)

    #Création du menu "Quitter"
    menu1 = Menu(menubar, tearoff=0)
    menu1.add_command(label="Quitter", command=quitMenu)
    menubar.add_cascade(label="Quitter", menu=menu1)
    manualCreationWindow.config(menu=menubar)

    #Texte de présentatio
    titre = Label(manualCreationWindow, bg="white", text="Bienvenue sur l'outil de création de compte AD, \n\
    veuillez entrer les informations de l'utilisateur :", justify=CENTER)
    titre.grid(row=0, pady=20, padx=20, columnspan=4)

    #Prénom
    firstnameLabel = Label(manualCreationWindow, bg="white", text="Prénom :")
    firstnameLabel.grid(row=1, pady=20, padx=20, column=0)

    global firstnameEntry
    firstnameEntry = Entry(manualCreationWindow, bg="white", width=15)
    firstnameEntry.grid(row=1, pady=20, padx=20, column=1)


    #Nom de famille
    lastnameLabel = Label(manualCreationWindow, bg="white", text="Nom :")
    lastnameLabel.grid(row=1, pady=20, padx=20, column=2)
    global lastnameEntry

    lastnameEntry = Entry(manualCreationWindow, bg="white", width=15)
    lastnameEntry.grid(row=1, pady=20, padx=20, column=3)

    #Mot de passe
    passwordLabel = Label(manualCreationWindow, bg="white", text="Mot de passe :")
    passwordLabel.grid(row=2, pady=20, padx=20, column=0)
    global passwordEntry

    passwordEntry = Entry(manualCreationWindow, bg="white", show="*", width=15)
    passwordEntry.grid(row=2, pady=20, padx=20, column=1)
    
    #OU
    OULabel = Label(manualCreationWindow, bg="white", text="OU :")
    OULabel.grid(row=2, pady=20, padx=20, column=2)

    global OUCombo, OUkey, OUList
    OUKey = []
    for key in configuration['OU']:
        OUList[key]=configuration['OU'][key]
        OUKey.append(key)
    OUCombo = ttk.Combobox(manualCreationWindow, values=OUKey)
    OUCombo.current(0)
    OUCombo.grid(row=2, pady=20, padx=20, column=3)
    OUCombo.bind("<<ComboboxSelected>>", selectOU)


    #Groupes
    groupsLabel = Label(manualCreationWindow, bg="white", text="Groupes :")
    groupsLabel.grid(row=3, padx=20, columnspan=4)

    groupsFrame = Frame(manualCreationWindow, borderwidth=2, relief=GROOVE)
    groupsFrame.grid(row=4, columnspan=4, pady=20)


    for key in configuration['Groups']:
        groupsList[key]=configuration['Groups'][key]

    for key in groupsList:
        selected[key] = BooleanVar()
        button = ttk.Checkbutton(groupsFrame, text=key, variable=selected[key], command=selectedGroup)
        button.state(['!alternate'])
        button.grid(sticky=W)


    #Bouton confirmer
    manualCreationButton = Button(manualCreationWindow, text="Confirmer", command=manualCreation)
    manualCreationButton.grid(row=5, columnspan=4, pady=20)

    


