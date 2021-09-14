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
import configparser
import findUserWindow

OUList = dict()

def selectOU(event):
    """
        selectOU : Permet de récupérer la sélection dans la liste déroulante
    """
    global OUList, OUCombo, selectedOU
    OU = OUCombo.get()
    selectedOU = OUList[OU]

def displayFindUser():
    """
        displayFindUser : Appelle le script de sélection d'utilisateur dans l'OU choisie
    """
    global selectedOU
    findUserWindow.userWindow(selectedOU)
    
def selectOUWindow(configuration, mainWindow):
    """
        selectOUWindow : Création de la fenêtre de sélection d'OU
    """
    selectOUWindow = Toplevel(mainWindow)
    OULabel = Label(selectOUWindow, bg="white", text="OU :")
    OULabel.grid(row=2, pady=20, padx=20, column=2)

    #Liste déroulante des OU
    global OUCombo
    OUKey = []
    for key in configuration['OU']:
        OUList[key]=configuration['OU'][key]
        OUKey.append(key)
    OUCombo = ttk.Combobox(selectOUWindow, values=OUKey)
    OUCombo.current(0)
    OUCombo.grid(row=2, pady=20, padx=20, column=3)
    OUCombo.bind("<<ComboboxSelected>>", selectOU)
    
    #Bouton confirmer
    selectOUButton = Button(selectOUWindow, text="Confirmer", command=displayFindUser)
    selectOUButton.grid(row=5, columnspan=4, pady=20)
    

