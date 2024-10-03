################################################################################
#                              creation de class
################################################################################

class Node:
    def __init__(self, data): #fonction d'initialisation des datas
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
    #dans un premier temps on affiche et en ensuite on regarde si une info suis
    #alors que dans le print de la fonction inverse, on regarde si quelque chose suis, si ça suis on continue ce qui fait que l'on arrive a la fin et ensuite on print une fois qu'il n'y a plus rien après
    #le fait qu'on print quand la suite est vide fait que l'on commence a print par la fin et comme quand ont fait un apelle recurcive ça met en pause les fonction précédentes
    #alors on reprend a chaque fin de fonction et ça print en sens inverse


    
    def printcountNode(self, compteur=1): #ici on créé la fonction qui va permettre de compter le nombre de noeud
        if self.next is not None : #si il y a quelque chose après
            compteur=compteur+1 #on rajoute un compteur pour rajoteur a chaque fois 
            self.next.printcountNode(compteur) #ici la fonctoin s'apelle elle meme
        else :
            print("\nil y a ",compteur, "element dans la liste") #print de verif



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
    
    def countNodes(self): #fonction de lien avec printcountNode
        if self.head is not None:
            self.head.printcountNode()
        print()

    def addInhead(self, valeur):
        nouvellevaleur = Node(valeur) #ici ont associe la nouvelle valeur passer en paramètre a une varibale
        nouvellevaleur.next = self.head #ici le lien entre nouvel élément (nouveau nœud) est lié à l'ancienne tête de la liste comme ont fait dans "association de l'odre" en dessous
        self.head = nouvellevaleur #ici ont dit que la self.head (la tete de liste, donc le premier element) sera maintant notre nouvelle valeur passer en paramètre

    def reverseListe(self):
        print("creation d'une nouvelle liste initialisé a l'envers")
        nouvelleliste = LinkedList() # on crée une nouvelle liste
        noeudactuel = self.head #on attribue le noeud de la liste sur le quel on se trouve
        while noeudactuel is not None : #temps que le noeuf actuelle sur le quel on se trouve n'est pas nul
            nouvelleliste.addInhead(noeudactuel.data) # alors on ajoute a la nouvelle liste "nouvelleliste" au début de la liste "addInHead" les données associé au noeud sur le quel on se trouve "noeudactuelle.data"
            noeudactuel = noeudactuel.next #ensuite on associe le noeud a celui d'après pour que le prochain tour de boucle, le current regarde celui d'après
        nouvelleliste.printListeRecRev() #j'affiche la liste
        return nouvelleliste #on retourne la nouvelle liste
            

################################################################################
#                    association des valeurs a des variables
################################################################################

myLinkedList = LinkedList()
myNode1 = Node(10)
myNode2 = Node(20)
myNode3 = Node(30)
myNode4 = Node(40)


########################################################################
#                           association de l'odre
########################################################################

myLinkedList.head = myNode1
myNode1.next = myNode3
myNode3.next = myNode2
myNode2.next = myNode4


########################################################################
#                           apl des fonctions
########################################################################

#apl de la fonction permettant d'ajouter une nouvelle valeur en début de lsite
print("on rajoute  une valeur a la liste............")
myLinkedList.addInhead(3) #question 2. c)

#apl des fonction permettant d'afficher les différents éléments de la liste
print("Les elements de la liste sont :")
myLinkedList.printListRec() #question 1.
myLinkedList.printListeRecRev() #question 2. a)
myLinkedList.countNodes() #question 2. b)

#apl des fonctions créant cette fois ci une autre liste ou les élément seont inséré a l'envers
listeretourner=myLinkedList.reverseListe() #question 2. d)
