################################################################################
#                              creation de class
################################################################################

class Node :
    def __init__(self, valeur, gauche=None, droite=None): #initialisation du noeuf
        self.valeur = valeur #valeur que l'on associera
        self.gauche = gauche #enfant de gauche
        self.droit = droite #enfant de droite
