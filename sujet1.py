#####################################################################
#                   creation variable
#####################################################################

nom=input("nom de l'etudiant : ") #variable nom
prenom=input("prenom de l'etudiant : ") #variable prénom

notesetcoef=(input('entrer la notes : '), input('entrer le coef : '))
nompromo=input('entrer le nom de la promo : ')

########################################################################
#                      fonctions
########################################################################


def createtudiant(nom, prenom): #fonction pour crée un étudiant
    etudiant={ #creation du dictionaire dans le quel on stock les étudiants
        "nom": "name", #nom de l'étudiant a qui on associe une variable pour commencer
        "prenom" : "firstname" #prénom de l'étudiant au quel on associe la variable pour commencer
    }
    etudiant["nom"]=nom #on associe le nom au nom rentré en input au début du programme
    etudiant["prenom"]=prenom #on associe
    #print(etudiant) #print 
    return(etudiant)


def ajouternotes(etudiant, notesetcoef): #creation de la liste des étudiants lier avec les notes
    listenotesetudiant={ #on creer la liste dans la quel on va stocker la liste des etudiant avec leur coef
        "etudiant":"etudiant", 
        "notesetcoef":(15,2) 
    }

    listenotesetudiant["etudiant"]=etudiant #ici ont associe l'étudiant de la fonction précédentes
    listenotesetudiant["notesetcoef"]=notesetcoef #ici ont associe la note et le coef a ce qui a été rentrer en input au debut
    #print(listenotesetudiant)
    return(listedesetudiant)

#def creationpromo(etudiantcoef, listepromo): #creation d'une promo avec les fonction crée précédement
    #promo = {
        #"nom de la promo" : "test",
        #"edutiant de la promo" : "etudiantx"
    #}
    
    #promo["nom de la promo"]=listeetudiant
    #promo["etudiant de la promo"]=etudiant
    #print(promo)
    #return(promo)


################################################################################
#                              apl de fonctions
################################################################################

etudiant=createtudiant(nom, prenom)

etudiantetnotes=ajouternotes(etudiant, notesetcoef)


#notesetetudiant=ajouternotes(etudiant(nom, prenom), notes, notesetcoef)

#creationpromo(notesetetudiant, promo)
