from abc import ABC, abstractmethod
from tkinter.messagebox import RETRY

class Propriete(ABC):
    #champs :
    #__titre
    #_valeur
    #_valeurHypothecaire

    def __init__ (self, titre, valeur, valeurHypothecaire):
        self.__titre = titre
        self.__valeur = valeur
        self.__valeurHypothecaire = valeurHypothecaire

        self.__leProprietaire = None

    def gettitre(self):
        return self.__titre
    def getvaleur(self):
        return self.__valeur
    def getvaleurHypothecaire(self):
        return self.__valeurHypothecaire
    def getProprietaire(self):
        return self.__leProprietaire
        def getvaleurHypothecaire(self):
        return self.__valeurHypothecaire
    
    def __str__(self):
        return self.ToString()

    @abstractmethod
    def calculerLoyer(self):
        pass

    # ou def __str__(self):
    def ToString(self):
        return self.__titre + str(self.__valeur) + "€"