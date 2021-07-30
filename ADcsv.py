import csv
from pyad import *
from tkinter import *
from tkinter.messagebox import *

fenetre = Tk()

def createuser():
    Filecsv = entree.get()
    contenu = open(Filecsv,encoding="utf-8")
    csv_contenu = csv.reader(contenu)
    donnees_ligne = list(csv_contenu)
    for line in donnees_ligne[1:]:
        lname = line[0]
        fname = line[1]
        user = line[2]
        dname = fname + " " + lname
        ou = pyad.adcontainer.ADContainer.from_dn("ou=Utilisateurs, ou=OPENTP, dc=opentp, dc=lan")
        new_user = pyad.aduser.ADUser.create(user,ou,password="Bouj15ko", optional_attributes={"givenName" : fname, "sn" : lname, "displayName" : dname})
        showinfo("Titre 3", f"L'utilisateur {fname} {lname} a bien été créé")
    
    
titre = Label(fenetre, text="Bienvenue sur l'outil de création de compte AD, veuillez entrer le chemin du fichier CSV :")
titre.pack(pady=20, padx=20)

value = StringVar()
value.set("texte")
entree = Entry(fenetre, textvariable=value, width=30)
entree.pack(pady=5)

bouton = Button(fenetre, text="Valider", command=createuser)
bouton.pack(pady=10)


fenetre.mainloop()
