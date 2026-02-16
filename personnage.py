from armure import Armure

class Personnage :
    
    def __init__(self,nom : str,pv : int, attaque : int, armure : Armure) : 
        #création des variables
        self.nom = nom
        self._pv = 0
        self._attaque = 0
        self.armure = armure

        #verification avec property
        self.pv = pv
        self.attaque = attaque

        self._vie_max = pv


    @property
    def pv(self) -> int : 
        return self._pv
    
    @pv.setter 
    def pv(self,nouveau_pv) : 
        if nouveau_pv >= 0 and nouveau_pv <= 500 : 
            self._pv = nouveau_pv
        else : 
            self._pv = 0

    @property
    def attaque(self) -> int :
        return self._attaque
    
    @attaque.setter
    def attaque(self, nouvelle_attaque : int) -> int : 
        if nouvelle_attaque >= 1 and nouvelle_attaque <= 50 : 
            self._attaque = nouvelle_attaque
        else :
            self._attaque = 0
            print("comme vous avez essayer de tricher, votre attaque fut reset à 0")

    def marche(self) : 
        """méthode faisant marcher le personnage
        """
        print(f"{self.nom} marche")
    
    def subir_degats(self,degats : int): 
        """methode permettant de déduire le montant de degats infligés à la vie du personnage

        Args:
            degats (int): montant de degats infligés
        """
        if degats - self.armure.pts_armure > 0 :
            self.pv -= (degats - self.armure.pts_armure)
        else : 
            self.pv -= 0

    def attaquer(self) -> int : 
        """fonction calculant les dégats exercés par l'attaque du personnage.

        Returns:
            int: degats issus de l'attaque.
        """
        return self.attaque
 
    def __eq__(self,autre_perso : 'Personnage') -> bool : 
        """fonction disant si oui ou non les personnages sont égaux

        Returns:
            bool: vrai si les personnages sont identiques et faux s'ils ne le sont pas.
        """
        if self.pv == autre_perso.pv and self.nom == autre_perso.nom : 
            return True
        else : 
            return False

        
    def reset(self) -> None : 
        """
        méthode permettant de remettre un personnage à sa vie et à son mana initial.
        """
        self.pv = self._vie_max
