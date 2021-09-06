"""
    .Description:
    Script de création de compte Active Directory, fenêtre de création manuelle

    .Notes
    Auteur : Benjamin DEVAUX
    Version: Alpha 0.1
    Date: 23/08/2021

    Réalisé sous Python 3.9.6, testé sur Windows server 2016
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
    """
    globalGroup = pyad.adgroup.ADGroup.from_dn("CN=GLOBAL,OU=Groupes,DC=opentp,DC=lan")
    techGroup = pyad.adgroup.ADGroup.from_dn("CN=GRP_TECH,OU=Groupes,DC=opentp,DC=lan")
    comptaGroup = pyad.adgroup.ADGroup.from_dn("CN=GRP_Compta,OU=Groupes,DC=opentp,DC=lan")
    RHGroup = pyad.adgroup.ADGroup.from_dn("CN=GRP_RH,OU=Groupes,DC=opentp,DC=lan")
    """
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
                
                
                """
                if globalButton.instate(['selected']):
                    selectUser.add_to_group(globalGroup)
                if techButton.instate(['selected']):
                    selectUser.add_to_group(techGroup)
                if comptaButton.instate(['selected']):
                    selectUser.add_to_group(comptaGroup)
                if RHButton.instate(['selected']):
                    selectUser.add_to_group(RHGroup)
                """

def manualWindow(configuration, mainWindow):
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
    firstnameEntry.insert(0, configuration['manualWindow']['prenom'])


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

    
    """
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
    """

    #Bouton confirmer
    manualCreationButton = Button(manualCreationWindow, text="Confirmer", command=manualCreation)
    manualCreationButton.grid(row=5, columnspan=4, pady=20)

    


