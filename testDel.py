from pyad import *
from tkinter import *
from tkinter import ttk
import configparser
import findUserWindow

OUList = dict()

def selectOU(event):
    global OUList, OUCombo, selectedOU
    OU = OUCombo.get()
    selectedOU = OUList[OU]

def displayFindUser():
    global selectedOU
    findUserWindow.userWindow(selectedOU)
    

configuration = configparser.ConfigParser()
configuration.read('configuration.ini')

window = Tk()
OULabel = Label(window, bg="white", text="OU :")
OULabel.grid(row=2, pady=20, padx=20, column=2)

global OUCombo
OUKey = []
for key in configuration['OU']:
    OUList[key]=configuration['OU'][key]
    OUKey.append(key)
OUCombo = ttk.Combobox(window, values=OUKey)
OUCombo.current(0)
OUCombo.grid(row=2, pady=20, padx=20, column=3)
OUCombo.bind("<<ComboboxSelected>>", selectOU)

manualCreationButton = Button(window, text="Confirmer", command=displayFindUser)
manualCreationButton.grid(row=5, columnspan=4, pady=20)
    


window.mainloop
