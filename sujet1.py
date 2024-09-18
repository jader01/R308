#####################################################################
#                   creation variable
#####################################################################

nom=input("nom de l'etudiant : ") #variable nom
prenom=input("prenom de l'etudiant : ") #variable prénom
notes=[]

########################################################################
#                      fonctions
########################################################################


def etudiant(nom, prenom): #fonction pour creer la liste des étudiants
    listeetudiant=[] #liste tous les étudiants nom + prenom
    listeetudiant.append([nom,prenom]) #insertion des variables dans la listes
    print(listeetudiant) #print debug

def notes(etudiant, notes): #creation de la liste des utiant lier avec les notes

    if etudiant in listeetudiant:

        notes.append([listeetudiant, insertnote, insertcoef])
    print(notes)


################################################################################
#                              apl de fonctions
################################################################################

etudiant(nom, prenom)

#notes(etudiant())