from personnage import Personnage 
import random

class Mage(Personnage) : 

    def __init__(self, nom : str, pv : int, attaque : int, mana : int ):
        super().__init__(nom,pv,attaque)
        
        #creation des attributs
        self._mana = 0

        #validation des attributs
        self.mana = mana


    @property
    def mana(self) :
        return self._mana
    
    @mana.setter
    def mana(self,nouveau_mana) : 
        if nouveau_mana >= 0 and nouveau_mana <= 100 : 
            self._mana = nouveau_mana
        else : 
            self._mana = 0
            print("vous avez essayer de tricher et avez donc eu votre mana reset à 0")

    def attaquer(self) -> int : 
        """methode permettant de calculer les dégats issue d'une attauqe

        Returns:
            int: le montant des degats
        """
        if self.mana > 0 :
            return self.attaque + 60 
        else : 
            return self.attaque
        
    def diminuer_mana(self) -> None: 
        """
        methode permettant de diminuer le mana après une attaque
        """

        perte_mana = random.randint(15,25)
        self.mana -= perte_mana


    def __str__(self):
        return f"mage du nom de : {self.nom}, avec {self.pv} pv, {self.attaque} pts d'attaques et {self.mana} pts de mana "




