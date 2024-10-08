################################################################################
#                              creation de class
################################################################################

class Node :
    def __init__(self, valeur, gauche=None, droite=None): #initialisation du noeuf
        self.valeur = valeur #valeur que l'on associera
        self.gauche = gauche #enfant de gauche
        self.droite = droite #enfant de droite

    def printeNode2(self): #affichage de toutes les valeur en parcourant tout l'arbre
        print(self.valeur) #ici ont affiche la valeur
        if self.gauche is not None : #si il y a quelque chose a gauche
            return self.gauche.printeNode2() #alors on rapelle la fonction et gauche deviens le debut rt on retourne la valeur

        if self.droite is not None : #si il y a quelque chose droite
            return self.droite.printeNode2() #alors on rapelle la fonction et gauche deviens le debut rt on retourne la valeur



class Tree :
    def __init__(self):
        self.head = None #on initialise la te de la liste
    
    def printTree(self) :
        if self.head is not None : #si la tete n'est pas vide
            self.head.printeNode2() #on apelle la fonction printNode2 ci dessus



################################################################################
#                    association des valeurs a des variables
################################################################################

myLinkedList = Tree()
myNode1 = Node(10)
myNode2 = Node(20)
myNode3 = Node(30)
myNode4 = Node(15)
myNode5 = Node(40)


########################################################################
#                           association dans l'arbre
#######################################################################

myLinkedList.head = myNode1
myNode1.gauche = myNode2
myNode2.droite = myNode3
myNode3.gauche = myNode4
myNode3.droite = myNode5

########################################################################
#                           apl des fonctions
#######################################################################

myLinkedList.printTree()
