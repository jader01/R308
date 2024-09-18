#####################################################################
#                   creation variable
#####################################################################

nom=input("nom de l'etudiant : ") #variable nom
prenom=input("prenom de l'etudiant : ") #variable prénom
notes=[(12,1), (13,4), (16,3)]

########################################################################
#                      fonctions
########################################################################


def etudiant(nom, prenom): #fonction pour creer la liste des étudiants
    listeetudiant=[] #liste tous les étudiants nom + prenom
    listeetudiant.append([nom,prenom]) #insertion des variables dans la listes
    print(listeetudiant) #print debug

def notes(etudiant, notes): #creation de la liste des étudiants lier avec les notes
    for nom in etudiant :
        notes.append([etudiant, notes])
    print(notes)


################################################################################
#                              apl de fonctions
################################################################################

#etudiant(nom, prenom)

notes(etudiant(nom, prenom), notes)
