from propriete import *

class Gare(Propriete):
    def __init__(self, titre, valeur, valeurHypothecaire, quartier):
        #appel du constructeur de la classe parent
        Propriete.__init__(self, titre, valeur, valeurHypothecaire)

        #terminer l'initialisation
        self.__sonQuartier = quartier
        quartier.ajouterPropriete(self)

    def ToString(self):
        return "je suis la gare" + self.gettitre()

    def calculerLoyer(self):
        # 1- recherche du nombre de gare du proprietaire...
        leProprietaire = self.getProprietaire()
        leQuartier = self.__sonQuartier

        nbGaresProprietaire = leQuartier.nbProprietesJoueur(leProprietaire)
        
        # 2- selon...
        if (nbGaresProprietaire == 1):
            return 25
        elif (nbGaresProprietaire == 2):
            return 50
        elif (nbGaresProprietaire == 3):
            return 100
        elif (nbGaresProprietaire == 4):
            return 200
        else:
            # pas possible...
            return 0