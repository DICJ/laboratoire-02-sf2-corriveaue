from personnage import Personnage
from armure import Armure
import random

class Guerrier(Personnage) : 

    def __init__(self, nom : str, pv : int,attaque : int, force : int, armure : Armure) : 
        super().__init__(nom, pv, attaque, armure)

        #creations des attributs
        self._force = 0

        #validation des attributs
        self.force = force

    @property
    def force(self) -> int :
        return self._force
    
    @force.setter
    def force(self, nouvelle_force : int) -> int : 
        if nouvelle_force >= 1 and nouvelle_force <= 50 : 
            self._force = nouvelle_force
        else : 
            self._force = 0
            print("vous avez essayer de tricher en rentrant une donnée incohérente et avez dont recu une force de 0")

    def attaquer(self) -> int : 
        """methode permettant de calculer les dégats causés par une attaque

        Returns:
            int: le montant total des dégats
        """
        return (self.attaque + (self.force/2) + random.randint(-2,2))
    

    def __str__(self):
        return f"guerrier du nom de : {self.nom}, avec {self.pv} pv, {self.attaque} pts d'attaques et {self.force} pts de force "