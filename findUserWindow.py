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
import configparser
import logging

def userWindow(selectedOU):
    """
        userWindow : Création de la fenêtre de sélections d'utilisateur pour suppression
    """
    userWindow = Tk()
    userWindow.config(width=500)

    global userCombo, userList
    #user
    userList = []
    ou = pyad.adcontainer.ADContainer.from_dn(selectedOU)
    for obj in ou.get_children():
        userList.append(obj)
    userCombo = ttk.Combobox(userWindow, values=userList, width=100)
    userCombo.current(0)
    userCombo.grid(row=2, pady=20, padx=20, column=3)
    userCombo.bind("<<ComboboxSelected>>", selectUser)

    deleteButton = Button(userWindow, text="Supprimer", command=deleteUser)
    deleteButton.grid(row=5, columnspan=4, pady=20)
    

def selectUser(event):
    """
        selectUser : Récupération de la sélections dans la liste déroulante
    """
    global userCombo, userList, selectedUser
    selectedUser = userCombo.get()
    selectedUser = selectedUser.replace("<ADUser '","")
    selectedUser = selectedUser.replace("'>","")
    print(selectedUser)


def deleteUser():
    """
        deleteUser : Suppression de l'utilisateur sélectionné
    """
    global selectedUser
    pyad.adobject.ADObject.from_dn(selectedUser).delete()
    showinfo("Titre 3", "L'utilisateur a été supprimé")
    logging.info(f"Suppression de l'utilisateur {selectedUser}")
