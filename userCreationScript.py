"""
    .Description:
    Script de création de compte Active Directory, fenêtre de création manuelle

    .Notes
    Auteur : Benjamin DEVAUX
    Version: 1.0
    Date: 13/09/2021

    Réalisé sous Python 3.9.6, testé sur Windows server 2016
"""

from pyad import *

def userCreation(user, ou, password, fname, lname, dname):
    """
        userCreation : Fonction de création d'utilisateur
    """
    new_user = pyad.aduser.ADUser.create(user,ou,password,optional_attributes={"givenName" : fname, "sn" : lname, "displayName" : dname})

    return new_user
