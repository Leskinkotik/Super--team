# Ennoncée : Écrivezunprogrammeconstruit un arbre binaire et imprime ses éléments en ordre préfixé.
# Import de la classe Digraph du module graphviz
from graphviz import Digraph

# Définition de la classe Noeud pour représenter les nœuds de l'arbre binaire
class Noeud:
    def __init__(self, valeur):
        self.valeur = valeur
        self.gauche = None
        self.droite = None

# Fonction récursive pour imprimer les éléments de l'arbre en ordre préfixé
def imprimer_prefixe(noeud):
    """
    Imprime les éléments de l'arbre en ordre préfixé.

    Args:
        noeud (Noeud): Le nœud à partir duquel commencer l'impression.
    """
    if not noeud:
        return
    print(noeud.valeur)
    imprimer_prefixe(noeud.gauche)
    imprimer_prefixe(noeud.droite)

# Fonction pour construire un arbre binaire à partir d'une liste d'éléments
def construire_arbre(elements):
    """
    Construit un arbre binaire à partir d'une liste d'éléments.

    Args:
        elements (list): La liste des éléments à ajouter à l'arbre.

    Returns:
        Noeud: Le nœud racine de l'arbre construit.
    """
    racine = None
    for element in elements:
        racine = ajouter_noeud(racine, element)
    return racine

# Fonction récursive pour ajouter un nœud à l'arbre
def ajouter_noeud(racine, valeur):
    """
    Ajoute un nœud à l'arbre.

    Args:
        racine (Noeud): La racine de l'arbre actuel.
        valeur: La valeur du nœud à ajouter.

    Returns:
        Noeud: Le nœud racine mis à jour.
    """
    if not racine:
        return Noeud(valeur)
    if valeur < racine.valeur:
        racine.gauche = ajouter_noeud(racine.gauche, valeur)
    else:
        racine.droite = ajouter_noeud(racine.droite, valeur)
    return racine

# Fonction pour générer le graphique de l'arbre binaire
def generer_graphique(arbre, filename):
    """
    Génère le graphique de l'arbre binaire et l'enregistre dans un fichier.

    Args:
        arbre (Noeud): Le nœud racine de l'arbre binaire.
        filename (str): Le nom du fichier dans lequel enregistrer le graphique.
    """
    dot = Digraph(format='png')
    generer_graphique_recursif(dot, arbre)
    dot.render(filename, view=False)

# Fonction récursive pour générer les nœuds et les liens du graphique
def generer_graphique_recursif(dot, noeud):
    """
    Fonction récursive pour générer les nœuds et les liens du graphique.

    Args:
        dot (Digraph): L'objet graphviz pour créer le graphique.
        noeud (Noeud): Le nœud actuel à ajouter au graphique.
    """
    if not noeud:
        return
    dot.node(str(noeud.valeur))
    if noeud.gauche:
        dot.edge(str(noeud.valeur), str(noeud.gauche.valeur))
        generer_graphique_recursif(dot, noeud.gauche)
    if noeud.droite:
        dot.edge(str(noeud.valeur), str(noeud.droite.valeur))
        generer_graphique_recursif(dot, noeud.droite)

# Exemple d'utilisation
elements = [10, 5, 15, 3, 7, 12, 20]
arbre = construire_arbre(elements)
filename = "arbre_binaire"
print("Parcours en ordre préfixe de l'arbre binaire :")
imprimer_prefixe(arbre)
generer_graphique(arbre, filename)
print(f"L'arbre binaire a été généré et le graphique a été enregistré sous le nom '{filename}.png'.")
