#####################################################################
#                   creation variable
#####################################################################

nom=input("nom de l'etudiant : ") #variable nom
prenom=input("prenom de l'etudiant : ") #variable prénom
notes=[]
notesetcoef=(input('entrer la notes : '), input('entrer le coef : '))

########################################################################
#                      fonctions
########################################################################


def etudiant(nom, prenom): #fonction pour creer la liste des étudiants
    listeetudiant=[] #liste tous les étudiants nom + prenom
    listeetudiant.append([nom,prenom]) #insertion des variables dans la listes
    #print(listeetudiant) #print debug
    return(listeetudiant)

def ajouternotes(etudiant, notes,notescoef): #creation de la liste des étudiants lier avec les notes
    #print(etudiant)
    notes.append([etudiant, notescoef])
    print(notes)


################################################################################
#                              apl de fonctions
################################################################################

#etudiant(nom, prenom)

ajouternotes(etudiant(nom, prenom), notes, notesetcoef)
