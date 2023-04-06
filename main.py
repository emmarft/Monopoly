from logging import exception
from joueur import ExecptionJoueurNonSolvable, Joueur
from propriete import Propriete
from Gare import *
from Terrain import *
from Quartier import *
#from joueurHumain import *
#from Banque import *

#unePropriete = Propriete("Rue de la Paix ", 400, 200)
#print (unePropriete.ToString())
#print (unePropriete.gettitre())
#print (unePropriete.getvaleur())
#print (unePropriete.getvaleurHypothecaire())

#uneGare = Gare("Gare du Nord", 200, 100)
#print(uneGare.ToString())

LeQuartierBleuClair = Quartier("bleu clair", 50, 50)
lePremierTerrain = Terrain("Rue de Vaugirard", 100, 50, [6, 30, 90, 270, 400, 550],
                            LeQuartierBleuClair)

leDeuxièmeTerrain = Terrain("Rue de Courcelle", 100, 50, [6, 30, 90, 270, 400, 550],
                            LeQuartierBleuClair)

leTroisièmeTerrain = Terrain("Avenue de la République", 100, 50, [6, 30, 90, 270, 400, 550],
                            LeQuartierBleuClair)


#Le quartier des gares
leQuartierDesGares = Quartier("noir")
laPremiereGare = Gare("Gare de l'Est", 200, 100, leQuartierDesGares)
laDeuxièmeGare = Gare("Gare Montparnasse", 200, 100, leQuartierDesGares)
laTroisièmeGare = Gare("Gare de Lyon", 200, 100, leQuartierDesGares)
laQuatrièmeGare = Gare("Gare de Saint-Lazare", 200, 100, leQuartierDesGares)

print(LeQuartierBleuClair.toString())

try:
    moi = Joueur("mini", 1000)
    moi.acheter(lePremierTerrain)
    moi.acheter(laPremiereGare)
    print ("achat effectué")

    print("loyer pour la gare de l'Est:", laPremiereGare.calculerLoyer())

except ExecptionJoueurNonSolvable as execption:
    print(execption.message)