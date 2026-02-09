from guerrier import Guerrier
from mage import Mage
from personnage import Personnage
from archer import Archer
from arene import Arene
import fonction

quitter = False
choix = 0
#début de la boucle
while quitter != True : 
    fonction.afficher_menu() 
    choix = int(input("à quelle section voulez-vous accéder ? "))

    #match case des sections
    match choix :

        case 1 :
            Arene.ajouter_personnage()

        case 2 : 
            Arene.afficher_list()


        case 3 : 
            #verification que la liste de perso n'est pas vide.
            if len(Arene.lst_perso) < 2 : 
                print("veuillez d'abord allez rajouter des persos.")

            else : 
                #affichage de la liste des perso et sélections des personnages combattant
                Arene.afficher_list()
                indicatif1 = int(input("quelle est l'indicatif du premier combattant (situé à droite de sa description.)"))
                indicatif2 = int(input("quelle est l'indicatif du deuxième combattant (situé à droite de sa description.)"))
                Arene.simulation_combat(indicatif1,indicatif2)

        case 4 :
            #affichage de l'historique des combats
            Arene.historique_combat()
        
        case 5 : 
            quitter = True

print("fin du programme")
