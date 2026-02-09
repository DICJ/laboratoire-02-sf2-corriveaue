class Personnage :
    
    def __init__(self,nom : str,pv : int, attaque : int) : 
        #création des variables
        self.nom = nom
        self._pv = 0
        self._attaque = 0

        #verification avec property
        self.pv = pv
        self.attaque = attaque

    @property
    def pv(self) -> int : 
        return self._pv
    
    @pv.setter 
    def pv(self,nouveau_pv) : 
        if nouveau_pv >= 0 and nouveau_pv <= 500 : 
            self._pv = nouveau_pv
        else : 
            self._pv = 0
            print("vous avez essayer de tricher et avez donc eu vos pv reset à 0")

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
        self.pv -= degats   

 
        
