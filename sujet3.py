################################################################################
#                              creation de class
################################################################################

class Node:
    def __init__(self, data): #fonction d'initialisation des data
        self.data = data
        self.next = None

    def printNode(self): #ici ont créé la fonction qui va permettre d'afficher dans l'odre les infos rentrer
        print(self.data, end= " ") #on print notre data
        if self.next is not None: #si ont constate que la valeur qui suis n'est pas nul 
            self.next.printNode() # alors la fonction s'apelle elle même pour print le suivant

    def printNodeRev(self): #ici on créé la fonction qui va permettre d'afficher dans l'odre INVERSE les infos rentrer
        if self.next is not None : #si ont constate que la valeur après n'est pas nul
            self.next.printNodeRev() #alors la fonction s'apelle elle meme
        print(self.data, end= " ") # une fois fini on affiche la data
    #la différence entre les deux et que dans la fonction printNode et la fonction prinNodeRev :
    # dans un premier temps on affiche et en ensuite on regarde si une info suis
    # alors que dans le print de la fonction inverse, on regarde si quelque chose suis, si ça suis on continue ce qui fait que l'on arrive a la fin et ensuite on print une fois qu'il n'y a plus rien après
    # le fait qu'on print quand la suite est vide fait que l'on commence a print par la fin et comme quand ont fait un apelle recurcive ça met en pause les fonction précédentes
    # alors on reprend a chaque fin de fonction et ça print en sens inverse


class LinkedList:
    def __init__(self):
        self.head = None

    def printListRec(self): #fonction qui fait le lien avec printNode dans la class Node
        if self.head is not None:
            self.head.printNode()
        print()
    
    def printListeRecRev(self): #fonction qui fait le lien avec printNodeRev dans la class Node
        if self.head is not None:
            self.head.printNodeRev()
        print()



################################################################################
#                              apl de fonctions
################################################################################

myLinkedList = LinkedList()
myNode1 = Node(10)
myNode2 = Node(20)
myNode3 = Node(30)
myNode4 = Node(40)

#########################################################################
#                           association de l'odre
########################################################################

myLinkedList.head = myNode1
myNode1.next = myNode3
myNode3.next = myNode2
myNode2.next = myNode4
print("Les elements de la liste : \n")
myLinkedList.printListRec()
myLinkedList.printListeRecRev()
