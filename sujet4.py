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
            self.gauche.printeNode2() #alors on rapelle la fonction et gauche deviens le debut rt on retourne la valeur
        if self.droite is not None : #si il y a quelque chose droite
            self.droite.printeNode2() #alors on rapelle la fonction et gauche deviens le debut rt on retourne la valeur

    def printcountNode(self): #affichage du comptage de noeud
        compteur=1 #on initialise le compteur à 1
        if self.gauche is not None : # si a gauche il n'y a pas rien
            compteur=compteur + self.gauche.printcountNode() 
        if self.droite is not None : # si a droite il n'y a pas rien
            compteur=compteur + self.droite.printcountNode() # on incrémente le compteur
        return compteur #on return le compteur pour affichage

class Tree :
    def __init__(self):
        self.head = None #on initialise la te de la liste
    
    def printTree(self) :
        if self.head is not None : #si la tete n'est pas vide
            self.head.printeNode2() #on apelle la fonction printNode2 ci dessus

    def countNodes(self): # pour compter les noeud
        if self.head is not None : # si la tete n'est pas vide 
            return self.head.printcountNode() #on retourne la valeur de la fonction au dessus
        else :
            return 0 #sinon c'est que y a rien et on affiche 0

################################################################################
#                    association des valeurs a des variables
################################################################################

myTree = Tree()
myNode1 = Node(10)
myNode2 = Node(20)
myNode3 = Node(30)
myNode4 = Node(35)
myNode5 = Node(40)


########################################################################
#                        association dans l'arbre
#######################################################################

myTree.head = myNode1
myTree.head.gauche = myNode2
myTree.head.droite = myNode3
myTree.head.droite.gauche = myNode4
myTree.head.droite.droite = myNode5


########################################################################
#                           apl des fonctions
#######################################################################

myTree.printTree()

nombreelement = myTree.countNodes() # on associe le resultat a la variable nombre d'element pour print ensuite
print(" \n il y a ", nombreelement , "éléments dans l'arbre") # on print

