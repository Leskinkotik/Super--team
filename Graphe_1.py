# Enoncé : Écrivez un programme pour représenter un graphe
# en utilisant un dictionnaire en Python.

import networkx as nx
import matplotlib.pyplot as plt


class Graphe:
    def __init__(self):
        # Initialisation d'un dictionnaire prstockerlesconnexions du graphe.
        self.connexions = {}

    def ajouter_noeud(self, noeud):
        # Ajoute un nouveau noeud au graphe s'il n'existe pas déjà.
        if noeud not in self.connexions:
            self.connexions[noeud] = []

    def ajouter_connexion(self, noeud1, noeud2):
        # Ajoute une connexion bidirectionnelle entre noeud1 et noeud2.
        if noeud1 not in self.connexions:
            self.connexions[noeud1] = []
        if noeud2 not in self.connexions[noeud1]:
            self.connexions[noeud1].append(noeud2)

        if noeud2 not in self.connexions:
            self.connexions[noeud2] = []
        if noeud1 not in self.connexions[noeud2]:
            self.connexions[noeud2].append(noeud1)

    def afficher_graphe(self):
        # Imprime chaque noeud avec ses voisins.
        for noeud, voisins in self.connexions.items():
            print(f"{noeud}: {voisins}")


# Exemple d'utilisation de la classe Graphe
graphe = Graphe()
noeuds_et_connexions = [
    ('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'D'),
    ('C', 'E'), ('D', 'F'), ('E', 'F')
]

# Ajout de noeuds et connexions
for noeud1, noeud2 in noeuds_et_connexions:
    graphe.ajouter_connexion(noeud1, noeud2)

# Affichage du graphe
graphe.afficher_graphe()

# Créer un graphe vide avec networkx pour le dessin
G_nx = nx.Graph()

# Transférer les connexions de l'objet Graphe àl'objetgraphenetworkxprle dessin
for noeud, voisins in graphe.connexions.items():
    for voisin in voisins:
        G_nx.add_edge(noeud, voisin)

# Dessiner le graphe avec networkx et matplotlib
nx.draw(G_nx, with_labels=True, node_color='lightblue',
        font_weight='bold', node_size=700)
plt.show()  # Affiche le graphe à l'écran
