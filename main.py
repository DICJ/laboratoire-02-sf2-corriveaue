from guerrier import Guerrier
from mage import Mage
from personnage import Personnage
from archer import Archer
from arene import Arene
import fonction
from armure import Armure

#créations des variables
quitter = False
choix = 0
indicatif1 = 0
indicatif2 = 0 

#création de l'object d'arène
arene1 = Arene()

#creation de la liste d'armure disponible. 
armure_soldat = Armure("Cotte de Maille", 15)
armure_guerrier = Armure("armure de plaque", 12)
armure_archer = Armure("tunique de cuir", 5)
armure_mage = Armure("armure magique", 7)

lst_armure = [armure_soldat,armure_guerrier,armure_archer,armure_mage]

#début de la boucle
while quitter != True : 
    fonction.afficher_menu() 
    choix = int(input("à quelle section voulez-vous accéder ? "))

    #match case des sections
    match choix :

        case 1 :
            Arene.ajouter_personnage(arene1,lst_armure)

        case 2 : 
            Arene.afficher_list(arene1)


        case 3 : 
            #verification que la liste de perso n'est pas vide.
            if len(arene1) < 2 : 
                print("veuillez d'abord allez rajouter des persos.")

            else : 
                #affichage de la liste des perso et sélections des personnages combattant
                Arene.afficher_list(arene1)
                indicatif1 = int(input("quelle est l'indicatif du premier combattant (situé à droite de sa description.)"))
                indicatif2 = int(input("quelle est l'indicatif du deuxième combattant (situé à droite de sa description.)"))
                Arene.simulation_combat(arene1,indicatif1,indicatif2)

        case 4 :
            #affichage de l'historique des combats
            Arene.historique_combat(arene1)

        case 5 :
            #affichage de la liste des personnages
            Arene.afficher_list(arene1)
            indice = int(input("veuillez entrer l'indice du personnage que vous souhaitez soigner."))
            #appel de fonction permettant de soigner un personnage
            Arene.soigner_personnage(arene1,indice)

        case 6 :
            #retirage des cadavres de l'arène.
            Arene.nettoyer_arene(arene1) 
            print("les personnages ont bel et bien été retirés")

        case 7 :
            #début du battle royal
            Arene.lancer_battle_royale(arene1)

        case 8 : 
            quitter = True

        case _ : 
            print("entrée incorrect, veuillez réessayer.")

print("fin du programme")
