from propriete import *

class Terrain (Propriete):
    # on rajoute
    # nbMaisons
    # loyers (liste)

    def __init__(self, titre, valeur, valeurHypothecaire, loyers, quartier):
        # appel du constructeur de la classe parent
        Propriete.__init__(self, titre, valeur, valeurHypothecaire)

        # terminer l'initialisation
        self.__nbMaisons = 0
        self.__loyers = loyers
        self.__sonQuartier = quartier
        #quartier.AjouterPropriete(self)

    def getNbMaisons (self):
        return self.__nbMaisons

    def calculerLoyers(self):
        print("je cacule le loyer du terrain" + self.getTitre())

        # en première approximation, ça pourrait ressembler à 
        #return self.__loyers[self.__nbMaisons]