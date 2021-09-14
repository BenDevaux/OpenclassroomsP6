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

def userCreation(user, ou, password, fname, lname, dname):
    """
        userCreation : Fonction de création d'utilisateur
    """
    new_user = pyad.aduser.ADUser.create(user,ou,password,optional_attributes={"givenName" : fname, "sn" : lname, "displayName" : dname})

    return new_user
