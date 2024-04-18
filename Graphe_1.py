# Ennoncé : Écrivez un programme pour représenter un graphe 
# en utilisant un dictionnaire en Python
# Crée un dictionnaire pour représenter le graphe
import networkx as nx
import matplotlib.pyplot as plt

# Énoncé: Écrivez un programme pour représenter un graphe en utilisant un dictionnaire en Python.

class Graphe:
    def __init__(self):
        # Initialisation d'un dictionnaire pour stocker les connexions du graphe.
        self.connexions = {}

    def ajouter_noeud(self, noeud):
        # Ajoute un nouveau noeud au graphe s'il n'existe pas déjà.
        if noeud not in self.connexions:
            self.connexions[noeud] = []

    def ajouter_connexion(self, noeud1, noeud2):
        # Ajoute une connexion bidirectionnelle entre noeud1 et noeud2.
        
        # Si noeud1 n'est pas dans le graphe, ajoutez-le avec une liste de connexions vide.
        if noeud1 not in self.connexions:
            self.connexions[noeud1] = []
        # Si noeud2 n'est pas déjà dans la liste des connexions de noeud1, ajoutez-le.
        if noeud2 not in self.connexions[noeud1]:
            self.connexions[noeud1].append(noeud2)

        # Faites de même pour noeud2.
        if noeud2 not in self.connexions:
            self.connexions[noeud2] = []
        # Si noeud1 n'est pas déjà dans la liste des connexions de noeud2, ajoutez-le.
        if noeud1 not in self.connexions[noeud2]:
            self.connexions[noeud2].append(noeud1)

    def afficher_graphe(self):
        # Imprime chaque noeud avec ses voisins.
        for noeud, voisins in self.connexions.items():
            print(f"{noeud}: {voisins}")

# Créer un graphe vide avec networkx pour le dessin
G_nx = nx.Graph()

# Exemple d'utilisation de la classe Graphe
graphe = Graphe()

# Ajout de noeuds et connexions
graphe.ajouter_connexion('A', 'B')
graphe.ajouter_connexion('A', 'C')
graphe.ajouter_connexion('B', 'D')
graphe.ajouter_connexion('C', 'D')
graphe.ajouter_connexion('C', 'E')
graphe.ajouter_connexion('D', 'F')
graphe.ajouter_connexion('E', 'F')

# Affichage du graphe
graphe.afficher_graphe()

# Transférer les connexions de l'objet Graphe à l'objet graphe networkx pour le dessin
for noeud, voisins in graphe.connexions.items():
    for voisin in voisins:
        G_nx.add_edge(noeud, voisin)

# Dessiner le graphe avec networkx et matplotlib
nx.draw(G_nx, with_labels=True, node_color='lightblue', font_weight='bold', node_size=700)
plt.show()  # Affiche le graphe à l'écran
