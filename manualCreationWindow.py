#from pyad import *
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
from tkinter.filedialog import *
import logging

#Fonction pour quitter via le menu "Quitter"
def quitMenu():
    if askyesno("Titre 1", "Souhaitez vous quitter ?"):
        logging.info(" Fermeture via le menu 'Quitter' ")
        manualCreationWindow.destroy()

def manualCreation():
    fname = firstnameEntry.get()
    lname = lastnameEntry.get()
    password = passwordEntry.get()
    globalGroup = pyad.adgroup.ADGroup.from_dn("CN=Global,OU=Groups,DC=opentp,DC=lan")
    techGroup = pyad.adgroup.ADGroup.from_dn("CN=GRP_Tech,OU=Groups,DC=opentp,DC=lan")
    comptaGroup = pyad.adgroup.ADGroup.from_dn("CN=GRP_Compta,OU=Groups,DC=opentp,DC=lan")
    RHGroup = pyad.adgroup.ADGroup.from_dn("CN=GRP_RH,OU=Groups,DC=opentp,DC=lan")
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
                print(fname + " " + lname + " " + password)
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
logging.basicConfig(filename="Scriptlogoo.log", encoding="utf-8", format="%(asctime)s %(levelname)s: %(message)s", datefmt="%d/%m/%Y %H:%M:%S", level=logging.DEBUG)
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
