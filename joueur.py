from abc import ABC, abstractclassmethod
from email import message

class ExecptionJoueurNonSolvable(Exception):
    def __init__(self, joueur, propriete):
        self.__joueur = joueur
        self.__propriete = propriete

        self.message = joueur.getPseudo() + "n'a pas assez de cash pour acheter" + propriete.getTitre() + "(cash disponible:" + str(joueur.getCash()) + ", valeur demandée:" + str(propriete.getValeur()) +  ")"

class Joueur(ABC):
    def __init__(self, pseudo, cash):
        self.__pseudo = pseudo 
        self.__cash = cash

        self.__sesProprietes = []

    def getPseudo(self):
        return self.__pseudo

    def getCash(self):
        return self.__cash

    def getPropriete(self):
        return self.__sesProprietes

    def acheter(self, laPropriete):
        if self.getCash() >= laPropriete.getValeur(): 
            raise ExecptionJoueurNonSolvable(self, laPropriete.getValeur())
        else: 
            self.__sesProprietes.append(laPropriete)
            self.__cash -= laPropriete.getValeur()
            laPropriete.setProprietaire(self)

