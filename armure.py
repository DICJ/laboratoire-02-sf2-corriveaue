
class Armure : 
    def __init__(self,nom_armure : str, pts_armure : int) : 
        self.nom_armure = nom_armure
        self._pts_armure = pts_armure

    @property 
    def pts_armure(self) -> int : 
        return self._pts_armure
    
    @pts_armure.setter
    def pts_armure(self, nouveaux_pts_armure : int) -> int : 
        if nouveaux_pts_armure > 0 and nouveaux_pts_armure <= 20 : 
            self._pts_armure = nouveaux_pts_armure
        else : 
            self._pts_armure = 0
            print("comme vous avez essayer de tricher, vos pts d'armure ont été mis à 0.")
    
    