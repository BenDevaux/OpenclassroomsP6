from pyad import *
from tkinter import *
from tkinter import ttk
import configparser

def userWindow(selectedOU):

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
    global userCombo, userList, selectedUser
    selectedUser = userCombo.get()
    selectedUser = selectedUser.replace("<ADUser '","")
    selectedUser = selectedUser.replace("'>","")
    print(selectedUser)


def deleteUser():
    global selectedUser
    pyad.adobject.ADObject.from_dn(selectedUser).delete()
