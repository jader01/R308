########################################################################
#                      classe étudiants
########################################################################

class Etudiant :

    def __init__(self, nom, prénom): #on créé la fonction d'initialisation avec en paramètre le nom et et le prénom pour la création d'étudiant
        #print('lancement initialisation')
        self.name = nom
        self.firstname = prénom
        self.note = []
        #print("initialisation étudiant : ", nom, prénom, "\n") 

    def ajoutnotes(self, note, coef): #creation de la fonction initialisation de notes
        #print("ajout de la note")
        self.note.append((note, coef))
        #print("fin ajout notes la note est ", note, "et le coef", coef, "\n")
        
    def totalnotes(self):
        #print("calcul du total des notes........")
        return len(self.note)
    
    def fairemoyenne(self):
        additionnotes=0 #varriable à 0 que l'on va utiliser plus tard pour le calcul de moyenn
        addcoef=0 #varriable à 0 que l'on va utiliser plus tard pour le calcul de moyenn
        for elm in self.note: #ici on parcours tous les élément dans le dictionnaire étudiant mais on parcours seulement leur 'notes'
            print("calcule de la moyenne............") #print pour vérif
            addcoef = addcoef + elm[1]
            additionnotes = additionnotes + (elm[0]*elm[1])
        print("la moyenne de", self.name, self.firstname,  "est : ", additionnotes/addcoef, "\n") #print pour vérif
        return additionnotes/addcoef
        




########################################################################
#                      classe promo
########################################################################


def creationpromo(): #creation d'une promo 
    print("creation de la promo.................") #print pour vérif
    promo = { #création du dico promo
        "nom de la promo" : "but 2 PILPRO", #nom de la promo sous format texte
        "etudiant de la promo" : [] #création d'un tableau au quel on va associer les etudiant de la promo et leur note trouvé précédement
    }
    print("promo créée..........\n") #print pour vérif
    return(promo)


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


etudiante1 = Etudiant("Jade", "RUEDA LUCANTIS")
etudiante2 = Etudiant("Dana", "NELTU")
etudiante3 =Etudiant("Moon", "MOONY")

etudiante1.ajoutnotes(15, 1)
etudiante1.ajoutnotes(10, 3)

etudiante2.ajoutnotes(10, 3)

etudiante1.totalnotes()
etudiante2.totalnotes()

etudiante1.fairemoyenne()
etudiante2.fairemoyenne()
