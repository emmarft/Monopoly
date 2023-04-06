class Quartier:
    def __init__(self, couleur, prixMaison = 0, prixHotel = 0):
        self.__couleur = couleur
        self.__prixMaison = prixMaison
        self.__prixHotel = prixHotel
        self.__lesProprietesDuQuartier = []

    def getCouleur(self):
        return self.__couleur
    def getPrixMaison(self):
        return self.__prixMaison
    def getPrixHotel(self):
        return self.__prixHotel
    def getProprietaires(self):
        return self.__lesProprietesDuQuartier
    
    def ajouterPropriete(self, laPropriete):
        self.__lesProprietesDuQuartier.append(laPropriete)

    def toString(self):
        print("Couleur du quartier: " + self.__couleur)
        # print("Prix d'une maison: " + str(self.__prixMaison))
        # print("Prix d'un hotel: " + str(self.__prixHotel))
        print(len(self.__lesProprietesDuQuartier) ,"Proprietaires: ")
        for p in self.__lesProprietesDuQuartier:
            print(p.ToString())

    def nbProprietes(self):
        return len(self.__lesProprietesDuQuartier)



    def nbPropietesJoueur(self, joueur):
        nb = 0
        for p in self.__lesProprietesDuQuartier:
            if p.getProprietaire().getPseudo() == joueur.getPseudo():
                nb += 1
        return nb