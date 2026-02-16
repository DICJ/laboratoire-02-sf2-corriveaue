from personnage import Personnage
from armure import Armure


class Soldat(Personnage) :

    def __init__(self, nom : str, pv : int, attaque : int, armure : Armure):
        super().__init__(nom, pv, attaque, armure)

    def subir_degats(self,degats : int): 
        """methode permettant de déduire le montant de degats infligés à la vie du personnage

        Args:
            degats (int): montant de degats infligés
        """
        self.pv -= (0.9 * degats)

    
    def __str__(self):
        return f"soldat du nom de : {self.nom}, avec {self.pv} pv et {self.attaque} pts d'attaques "
