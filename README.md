# SCRIPT DE GESTION DE L'ACTIVE DIRECTORY

## POURQUOI ?

Ce script permet de centraliser et simplifier la gestion d'utilisateurs sur l'Active Directory.  
Il permet, à l'aide d'une interface graphique, de créer et supprimer des utilisateurs avec possibilité de choix des OU et groupes dont lesquels l'utilisateur doit faire parti.  
  
## COMMENT S'EN SERVIR ?  
  
Au lancement du script est présenté trois options : Manuel, Delete, CSV  
  
* Manuel : Permet une création manuelle d'un utilisateur.  
Ce bouton ouvre une fenêtre avec plusieurs champs à remplir (Nom, prénom, mot de passe), une liste déroulante de choix d'OU ainsi que cases à cocher pour chaque groupe auquel il faudrait rattacher l'utilisateur.  
Pour que l'utilisateur puisse être créé il est nécessaire que chaque paramètre soit rempli.  
  
* Delete : Permet la suppression d'un utilisateur.  
Ce bouton mène à une fenêtre qui propose tout d'abord de sélectionner l'OU dans laquelle se trouve l'utilisateur à supprimer, puis ouvre une deuxième fenêtre avec la liste des utilisateurs de l'OU sélectionnée.  
Une fois l'utilisateur sélectionné dans la liste déroulante il est possible de le supprimer avec le bouton "confirmer".  
  
* CSV : Permet la création de plusieurs utilisateurs à l'aide d'un fichier CSV.  
Ce bouton ouvre une fenêtre qui mène à un explorateur de fichier, il est nécessaire de sélectionner un fichier CSV. Tout autre type de fichier ne fonctionnera pas.  
Le fichier doit être construit comme ceci : Nom, prénom, OU  
Le bouton "confirmer" permet ensuite la création de tous les utilisateurs présents dans le fichier.  
  
## MANUEL D'EXPLOITATION
  
* Ajouter un groupe :  
Les groupes sont gérés à l'aide du fichier de configuration configuration.ini  
Il faut ajouter le nouveau groupe dans la catégorie [GROUPS] sous la forme suivante :  
nomdugroupe = CN=nomdugroupe,OU=Groupes,DC=opentp,DC=lan  
Une nouvelle checkbox apparaitra alors dans la fenêtre de création manuelle.  
  
* Ajouter une OU :  
Les OU sont également gérées à l'aide du fichier configuration.ini  
Elles sont à ajouter dans la catégorie [OU] sous la forme suivante :  
nomdel'ou = ou=nomdel'ou, ou=Utilisateurs, ou=OPENTP, dc=opentp, dc=lan  
  

