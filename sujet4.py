################################################################################
#                              creation de class
################################################################################

class Node :
    def __init__(self, valeur, gauche=None, droite=None): #initialisation du noeuf
        self.valeur = valeur #valeur que l'on associera
        self.gauche = gauche #enfant de gauche
        self.droite = droite #enfant de droite


class Tree :
    def __init__(self):
        self.head = None



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
