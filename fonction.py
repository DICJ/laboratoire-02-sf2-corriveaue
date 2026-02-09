def afficher_menu() :
    """fonction d'affichage de menu

    """
    text = "Menu Principal  \n " 
    text += "(1) : ajouter un personnage  \n " 
    text += "(2) : voir la liste de personnage actuellement dans l'arène \n " 
    text += "(3) : faire combattre deux personnages \n " 
    text += "(4) : afficher historique combats \n"
    text += " (5) : quitter le programme"
    print(text)

def information_personnage(type : int) :
    """fonction d'input utilisateur enregistrant les données d'un personnage

    Args:
        type (int): type de combattant du personnage
    """
    nom = input("quelle est le nom de votre personnage ? ")
    pv = int(input("combien de pv votre personnage possède-t-il ? (0-500) ? "))
    attaquer = int(input("quelle est le montant d'attaque standard du personnage (0-50) ?  "))

    #début du match case séparant les guerrier selon leur type
    match type :

        case 1 :
            force = int(input("quelle est le montant de la force de votre personnage ? (0-50) ? "))
            return nom,pv,attaquer,force

        case 2 : 
            mana = int(input("quelle est le montant total de votre mana. (0-100) ? "))
            return nom,pv,attaquer,mana

        case 3 : 
            dexterite = int(input("quelle est le montant total de votre dexterite (40-70) ? "))
            return nom,pv,attaquer,dexterite
        
        

