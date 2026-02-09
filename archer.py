from personnage import Personnage 
import random

class Archer(Personnage) :

    def __init__(self, nom : int, pv : int, attaque : int, dexterite : int):
        super().__init__(nom, pv, attaque)

        #creation des attributs 
        self._dexterite = 0

        #validation des attributs 
        self.dexterite = dexterite

    @property
    def dexterite(self) -> int : 
        return self._dexterite
    
    @dexterite.setter
    def dexterite(self,nouvelle_dexterite : int) -> int : 
        if nouvelle_dexterite >= 40 and nouvelle_dexterite <= 70 :
            self._dexterite = nouvelle_dexterite

        else : 
            self._dexterite = 0
            print("vous avez essayer de tricher, Karma !")

    def attaquer(self) -> int : 
        """fonction permettant de générer le montant de dégats exercé à l'adversaire.

        Returns:
            int: le montant de dégats
        """
        nombre_test = random.randint(0,100)
        if self.dexterite >= nombre_test : 
            degats = (2*(self.attaque + 15 ))
        else :  
            degats = self.attaque +15
            
        return degats
    
    def __str__(self):
        return f"archer du nom de : {self.nom}, avec {self.pv} pv, {self.attaque} pts d'attaques et {self.dexterite} pts de dextérité "
