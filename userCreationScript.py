#from pyad import *
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
from tkinter.filedialog import *
import logging

def userCreation(user, ou, password, fname, lname, dname):
    ou = pyad.adcontainer.ADContainer.from_dn(OUEntry.get())
    new_user = pyad.aduser.ADUser.create(user,ou,password,optional_attributes={"givenName" : fname, "sn" : lname, "displayName" : dname})
