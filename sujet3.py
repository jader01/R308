################################################################################
#                              creation de class
################################################################################

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    def printNode(self):
        print(self.data, end= " ")
        if self.next is not None:
            self.next.printNode()

class LinkedList:
    def __init__(self):
        self.head = None

    def printListRec(self):
        if self.head is not None:
            self.head.printNode()
        print()
    
    def printListeRecRev(self):
        if self.head is not None:
            self.head.printNode()
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
