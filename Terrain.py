from propriete import Propriete
from Quartier import Quartier


class Terrain(Propriete):
    # on rajoute
    # nbMaisons : int
    # loyers : {m1:float, m2:float, m3:float, m4:float, m5:float}

    def __init__(self, titre, valeur, loyers, valeurHypothecaire, quartier):
        # super().__init__(titre,valeur,valeurHypothecaire)
        Propriete.__init__(self, titre, valeur, valeurHypothecaire)
        # terminer l'initialisation
        self.__nbMaisons = 0
        self.__loyers = loyers
        self.__sonQuartier = quartier
        quartier.ajouterPropriete(self)

    def getNbMaisons(self):
        return self.__nbMaisons

    def getLoyers(self):
        return self.__loyers

    def calculerLoyer(self):
        # return self.__loyers[self.__nbMaisons]
        return print("je calcule le loyer du terrain" + self.getTitre())