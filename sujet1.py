#####################################################################
#                   creation variable
#####################################################################

#nom="rueda lucantis" #variable nom
#prenom="jade"#variable prénom

#note=int(14)
#coef=int(2)

#notesetcoef=(int(input('entrer la notes : ')), int(input('entrer le coef : ')))
nompromo="but2"

########################################################################
#                      fonctions
########################################################################


def createtudiant(nom, prenom): #fonction pour crée un étudiant
    print("lancement creation etudiant.....")
    etudiant={ #creation du dictionaire dans le quel on stock les étudiants
        "nom": nom, #nom de l'étudiant a qui on associe une variable pour commencer
        "prenom" : prenom, #prénom de l'étudiant au quel on associe la variable pour commencer
        "notes" : []
    }
    #print(etudiant)
    print("etudiant créée\n")
    return(etudiant)


def ajouternotes(etudiant, note, coef): #creation de la liste des étudiants lier avec les notes
    print("ajout des notes de l'étudiant.........")
    etudiant['notes'].append((note, coef)) #ici on associe la note et le coef rentré précédement a la variable "notes" dans la table étudiant
    print("etudiant et notes : ", etudiant, "\n")
    return(etudiant)

def totalnotes(dico):
    print("calcul total de note \n")
    return len(dico["notes"]) #ici on calcule le nombre de notes présente dans le dictionnaire au total, pour ensuite pouvoir calculer la moyenne


def creationpromo(): #creation d'une promo 
    print("creation de la promo.................")
    promo = {
        "nom de la promo" : "but 2 PILPRO",
        "etudiant de la promo" : []
    }
    print("promo créée..........")
    return(promo)

#moyenne
def fairemoyenne(liste): # on crrée une fonction de calcule de moyenne avec en paramètre la liste complete généré précédement
    additionnotes=0
    addcoef=0
    for elm in liste['notes']:
        print("calcule de la moyenne............")
        addcoef = addcoef + elm[1]
        additionnotes = additionnotes + (elm[0]*elm[1])
        print("la moyenne est : ", additionnotes/addcoef, "\n")
    return additionnotes/addcoef

def addetudiantpromo(promo, etudiant):
    print("association de l'étudiant a une promotion")
    promo["etudiant de la promo"].append(etudiant)
    print(promo)


################################################################################
#                              apl de fonctions
################################################################################

resultetudiant=createtudiant("rueda lucantis", "jade")

etudiantetnotes=ajouternotes(resultetudiant, int(15), int(2))

fairemoyenne(etudiantetnotes)

promo=creationpromo()

addetudiantpromo(promo, etudiantetnotes)

