import fonction
from guerrier import Guerrier
from mage import Mage
from archer import Archer
from soldat import Soldat
import time
from detailscombats import DetailsCombats
import random

class Arene :

    def __init__(self):
        self.lst_perso = []
        self.lst_combats = []

    def ajouter_personnage(self,lst_armure) :

        """methode de classe prenant en note les informations des personnages pour les créer depuis les classe 
        """

        choix = int(input("à quelle catégorie de combattant votre personnage appartient-t-il : (1) guerrier, (2) mage, (3) archer, (4) soldat "))
        match choix : 
            case 1 :
                nom,pv,attaque,force = fonction.information_personnage(1)
                nouveau_perso = Guerrier(nom,pv,attaque,force,lst_armure[1])
                

            case 2 : 
                nom,pv,attaque,mana = fonction.information_personnage(2)
                nouveau_perso = Mage(nom,pv,attaque,mana,lst_armure[3])


            case 3 : 
                nom,pv,attaque,dexterite = fonction.information_personnage(3) 
                nouveau_perso = Archer(nom,pv,attaque,dexterite,lst_armure[2])

            case 4 : 
                nom,pv,attaque = fonction.information_personnage(0)
                nouveau_perso = Soldat(nom,pv,attaque,lst_armure[0])
                
        #ajout du personnage à la liste des persos.        
        self.lst_perso.append(nouveau_perso)


    def afficher_list(self) :
        """
        methode de classe permettant d'afficher la liste de personnage.
        """ 
        x = 0
        for personnage in self.lst_perso :
            print(f"({x}) {self.lst_perso[x]}")
            x += 1
    
    def simulation_combat(self,indicatif1 : int,indicatif2 : int) :
        """methode de classe simulant un combat entre deux personnages

        Args:
            indicatif1 (int): indicatif du premier personnage
            indicatif2 (int): indicatif du deuxième personnage
        """
        nbr_tour = 0
        while self.lst_perso[indicatif1].pv > 0 and self.lst_perso[indicatif2].pv > 0 : 

            
            #debut de combat et degat de perso 1 à perso 2
            degats = self.lst_perso[indicatif1].attaquer()
            self.lst_perso[indicatif2].subir_degats(degats)
            print(f"{self.lst_perso[indicatif1].nom} inflige : {degats} pts de degats à {self.lst_perso[indicatif2].nom }")
            time.sleep(1)


            #verification de si perso 2 est mort
            if self.lst_perso[indicatif2].pv != 0 :

                #degat de perso 2
                degats = self.lst_perso[indicatif2].attaquer()
                self.lst_perso[indicatif1].subir_degats(degats)
                print(f"{self.lst_perso[indicatif2].nom} inflige : {degats} pts de degats à {self.lst_perso[indicatif1].nom }")
                time.sleep(1)
                nbr_tour += 1 
            

        if self.lst_perso[indicatif1].pv > 0 :
            gagnant = self.lst_perso[indicatif1]
        else : 
            gagnant = self.lst_perso[indicatif2]
        print(f"fin du combat ! le gagnant est : {gagnant.nom}")
        nouveau_combat = DetailsCombats(self.lst_perso[indicatif1].nom,self.lst_perso[indicatif2].nom,gagnant.nom,nbr_tour)
        self.lst_combats.append(nouveau_combat)

    
    def historique_combat(self) :
        """methode de classe permettant d'afficher l'historique des combats 
        """
        for combat in self.lst_combats : 
            print(combat)

            
    def __len__(self) -> int :
        """fonction retournant la liste de personnage prêt a combattre

        Returns:
            int: nombre de personnage prêt au combat.
        """
        return len(self.lst_perso)


                
    def soigner_personnage(self,indice) -> None : 
        """
        fonction permettant de soigner un personnage selon son index.
        """
        self.lst_perso[indice].reset()
            

    def nettoyer_arene(self) -> None : 
        """
        methode d'arene permettant de supprimer l'ensemble des personnages morts.
        """
        for personnage in self.lst_perso :
            if personnage.pv <= 0 :
                self.lst_perso.remove(personnage)
            else : 
                pass

    def lancer_battle_royale(self) -> None : 
        """
        Fonction de battle royale, le personnage qui fait les dégats sera tirer au sort, puis le personnage qui recoit les dgts aussi, et ce, jusqu'à ce qu'il ne reste qu'un perso.
        """
        
        x = 0
        for personnage in self.lst_perso :
            Arene.soigner_personnage(self,x)
            x += 1
        while len(self.lst_perso) > 1 :
            #boucle permettant de faire se battre des personnages jusqu'à ce qu'il n'en reste plus qu'un.

            #perso infligeant des dégats : 
            perso1 = random.randint(0,(len(self.lst_perso))-1)

            #perso recevant les dégats
            perso2 = random.randint(0,(len(self.lst_perso))-1)

            #verif que les deux persos ne sont pas égaux.
            if perso2 == perso1 : 
                perso2 = random.randint(0,(len(self.lst_perso))-1)

                        
            #debut de combat et degat de perso 1 à perso 2
            degats = self.lst_perso[perso1].attaquer()
            self.lst_perso[perso2].subir_degats(degats)
            print(f"{self.lst_perso[perso1].nom} inflige : {degats} pts de degats à {self.lst_perso[perso2].nom }")
            time.sleep(0.4)

            #clear de l'arène si un des perso est mort
            Arene.nettoyer_arene(self)






