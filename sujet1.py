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
    print("lancement creation etudiant.....") #print pour vérif
    etudiant={ #creation du dictionaire dans le quel on stock les étudiants
        "nom": nom, #nom de l'étudiant a qui on associe une variable pour commencer
        "prenom" : prenom, #prénom de l'étudiant au quel on associe la variable pour commencer
        "notes" : [] #ici on crée un tableau vide au quel on associera le tuple note + coef après
    }
    #print(etudiant)
    print("etudiant créée\n")#print pour vérif
    return(etudiant)


def ajouternotes(etudiant, note, coef): #creation de la liste des étudiants lier avec les notes
    print("ajout des notes de l'étudiant.........")#print pour vérif
    etudiant['notes'].append((note, coef)) #ici on associe la note et le coef rentré précédement a la variable "notes" dans la table étudiant
    print("etudiant et notes : ", etudiant, "\n")#print pour vérif
    return(etudiant)

def totalnotes(dico):
    print("calcul total de note \n")#print pour vérif
    return len(dico["notes"]) #ici on calcule le nombre de notes présente dans le dictionnaire au total, pour ensuite pouvoir calculer la moyenne


def creationpromo(): #creation d'une promo 
    print("creation de la promo.................") #print pour vérif
    promo = { #création du dico promo
        "nom de la promo" : "but 2 PILPRO", #nom de la promo sous format texte
        "etudiant de la promo" : [] #création d'un tableau au quel on va associer les etudiant de la promo et leur note trouvé précédement
    }
    print("promo créée..........\n") #print pour vérif
    return(promo)

#moyenne
def fairemoyenne(liste): # on crrée une fonction permettant d'effectuer un calcul de moyenne
    additionnotes=0 #varriable à 0 que l'on va utiliser plus tard pour le calcul de moyenn
    addcoef=0 #varriable à 0 que l'on va utiliser plus tard pour le calcul de moyenn
    for elm in liste['notes']: #ici on parcours tous les élément dans le dictionnaire étudiant mais on parcours seulement leur 'notes'
        print("calcule de la moyenne............") #print pour vérif
        addcoef = addcoef + elm[1]
        additionnotes = additionnotes + (elm[0]*elm[1])
        #print("la moyenne est : ", additionnotes/addcoef, "\n") #print pour vérif
    return additionnotes/addcoef

def addetudiantpromo(promo, etudiant): #cette fonction permettra d'ajouter un étudiant a la promotion
    print("association de l'étudiant a une promotion") #print pour vérif
    promo["etudiant de la promo"].append(etudiant) #ici on ajoute l'étudiant a la variable sous forme de liste créé dans le dico
    print(promo)
    print("l'étudiant a été associer\n") #print pour vérif
    return(promo)

def totalpromo(promo): #cette fonction va parmettre de compter le nomre d'étudiant présent dans une promo
    print("compte du nombre d'étudiant............") #print pour vérif
    print("il y a : ", len(promo['etudiant de la promo']), "étudiant(s) dans la promo", promo['nom de la promo'], "\n")  #print pour vérif de tout les détails souhaiter
    return(len(promo['etudiant de la promo'])) #print pour vérif

def moypromo(promo): #cette fonction va permettre de calculer la moyenne de la promotion
    moyenne = 0
    print("calcul de la moyenne de la promo ...........;") #print pour vérif
    totaletudiant=totalpromo(promo) #on apelle la fonction de compte du nombre d'étudiant
    for elm in promo['etudiant de la promo'] : #on parcours la liste des etudiant
        moyenne = moyenne + fairemoyenne(elm) #on utilise le calcul de moyenne avec la fonction créée précédement
    print("la moyenne de la promo est :", moyenne/totaletudiant, "\n") #moyenne final
    return(moyenne/totaletudiant)


################################################################################
#                              apl de fonctions prog principal
################################################################################

def main():
    resultetudiant=createtudiant("rueda lucantis", "jade") 

    etudiantetnotes=ajouternotes(resultetudiant, int(15), int(2))

    fairemoyenne(etudiantetnotes)

    promo=creationpromo()

    promocomplette=addetudiantpromo(promo, etudiantetnotes)

    #totalpromo(promocomplette)

    moypromo(promocomplette)


########################################################################
#             lancement programme
###########################################################################

main()
