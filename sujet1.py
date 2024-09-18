#####################################################################
#                   creation variable
#####################################################################

nom=input("nom de l'etudiant : ") #variable nom
prenom=input("prenom de l'etudiant : ") #variable prénom
notes=[]
notesetcoef=(input('entrer la notes : '), input('entrer le coef : '))
promo=[]
nompromo=input('entrer le nom de la promo : ')

########################################################################
#                      fonctions
########################################################################


def etudiant(nom, prenom): #fonction pour creer la liste des étudiants
    listeetudiant=[] #liste tous les étudiants nom + prenom
    for elm in listeetudiant :
        listeetudiant.append([nom,prenom]) #insertion des variables dans la listes
    #print(listeetudiant) #print debug
    return(listeetudiant)

def ajouternotes(etudiant, notes,notescoef): #creation de la liste des étudiants lier avec les notes
    #print(etudiant)
    notes.append([etudiant, notescoef])
    #print(notes)
    return notes

def creationpromo(etudiantcoef, listepromo): #creation d'une promo avec les fonction crée précédement
    for elm in etudiantcoef :
        listepromo.append(etudiantcoef)
    print(listepromo)



################################################################################
#                              apl de fonctions
################################################################################

#etudiant(nom, prenom)

notesetetudiant=ajouternotes(etudiant(nom, prenom), notes, notesetcoef)

creationpromo(notesetetudiant, promo)
