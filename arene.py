import fonction
from guerrier import Guerrier
from mage import Mage
from personnage import Personnage
from archer import Archer
import time
from detailscombats import DetailsCombats

class Arene :

    #attributs de classe
    lst_perso = []
    lst_combat = []

    @classmethod
    def ajouter_personnage(cls) :
        """methode de classe prenant en note les informations des personnages pour les créer depuis les classe 
        """
        choix = int(input("à quelle catégorie de combattant votre personnage appartient-t-il : (1) guerrier (2) mage (3) archer "))
        match choix : 
            case 1 :
                nom,pv,attaque,force = fonction.information_personnage(1)
                nouveau_perso = Guerrier(nom,pv,attaque,force)
                

            case 2 : 
                nom,pv,attaque,mana = fonction.information_personnage(2)
                nouveau_perso = Mage(nom,pv,attaque,mana)


            case 3 : 
                nom,pv,attaque,dexterite = fonction.information_personnage(3) 
                nouveau_perso = Archer(nom,pv,attaque,dexterite)
                
        #ajout du personnage à la liste des persos.        
        Arene.lst_perso.append(nouveau_perso)

    @classmethod
    def afficher_list(cls) :
        """
        methode de classe permettant d'afficher la liste de personnage.
        """ 
        x = 0
        for personnage in Arene.lst_perso :
            print(f"({x}) {Arene.lst_perso[x]}")
            x += 1
    
    @classmethod
    def simulation_combat(cls,indicatif1 : int,indicatif2 : int) :
        """methode de classe simulant un combat entre deux personnages

        Args:
            indicatif1 (int): indicatif du premier personnage
            indicatif2 (int): indicatif du deuxième personnage
        """
        nbr_tour = 0
        while Arene.lst_perso[indicatif1].pv > 0 and Arene.lst_perso[indicatif2].pv > 0 : 

            
            #debut de combat et degat de perso 1 
            degats = Arene.lst_perso[indicatif1].attaquer()
            Arene.lst_perso[indicatif2].subir_degats(degats)
            print(f"{Arene.lst_perso[indicatif1].nom} inflige : {degats} pts de degats à {Arene.lst_perso[indicatif2].nom }")
            time.sleep(1)


            #verification de si perso 2 est mort
            if Arene.lst_perso[indicatif2].pv != 0 :

                #degat de perso 2
                degats = Arene.lst_perso[indicatif2].attaquer()
                Arene.lst_perso[indicatif1].subir_degats(degats)
                print(f"{Arene.lst_perso[indicatif2].nom} inflige : {degats} pts de degats à {Arene.lst_perso[indicatif1].nom }")
                time.sleep(1)
                nbr_tour += 1 
            

        if Arene.lst_perso[indicatif1].pv > 0 :
            gagnant = Arene.lst_perso[indicatif1]
        else : 
            gagnant = Arene.lst_perso[indicatif2]
        print(f"fin du combat ! le gagnant est : {gagnant.nom}")
        nouveau_combat = DetailsCombats(Arene.lst_perso[indicatif1].nom,Arene.lst_perso[indicatif2].nom,gagnant.nom,nbr_tour)
        Arene.lst_combat.append(nouveau_combat)


    @classmethod
    def historique_combat(cls) :
        """methode de classe permettant d'afficher l'historique des combats 
        """
        for combat in Arene.lst_combat : 
            print(combat)

            


                
            
