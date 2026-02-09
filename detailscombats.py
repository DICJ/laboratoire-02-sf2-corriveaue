

class DetailsCombats : 


    def __init__(self,nom_perso1,nom_perso2,vainqueur,nombre_tour):
        self.nom_perso1 = nom_perso1
        self.nom_perso2 = nom_perso2
        self.vainqueur = vainqueur 
        self.nombre_tour = nombre_tour
    

    def __str__(self):
        return f"combat entre : {self.nom_perso1} et {self.nom_perso2} dont {self.vainqueur} est ressorti gagnant après {self.nombre_tour} tours. "