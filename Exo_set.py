# Écrivez un programme qui trouve l'intersection de deux ensembles.
# Importation du module pour utiliser les ensembles
from typing import Set

# Définition de la fonction qui trouve l'intersection de deux ensembles
def intersection(ensemble1: Set[int], ensemble2: Set[int]) -> Set[int]:
    """
    Cette fonction prend deux ensembles en entrée et renvoie leur intersection.
    
    Args:
        ensemble1 (set): Le premier ensemble.
        ensemble2 (set): Le deuxième ensemble.
        
    Returns:
        set: L'intersection des deux ensembles.
    """
    return ensemble1.intersection(ensemble2)

# Exemple d'utilisation
if __name__ == "__main__":
    # Déclaration des deux ensembles
    ensemble1 = {1, 2, 3, 4, 5}
    ensemble2 = {4, 5, 6, 7, 8}
    
    # Appel de la fonction intersection avec les ensembles comme arguments
    resultat = intersection(ensemble1, ensemble2)
    
    # Affichage du résultat
    print("Intersection des ensembles :", resultat)