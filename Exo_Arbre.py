from graphviz import Digraph
import networkx as nx
# jimportmodule NetworkX renomme nx facilitersonutilisation
import matplotlib.pyplot as plt
# j'mport module pyplot de Matplotlib,renommer pltprfaciliterutilisation
G = nx.Graph()
class Person:
    def __init__(self, name):
        self.name = name
        self.parents = []
# Création des personnes
child1 = Person("Enfant 1")
child2 = Person("Enfant 2")
parent1 = Person("Parent 1")
parent2 = Person("Parent 2")
grandparent1 = Person("Grand-parent 1")
grandparent2 = Person("Grand-parent 2")

# Définir les relations familiales
child1.parents = [parent1, parent2]
child2.parents = [parent1, parent2]
parent1.parents = [grandparent1]
parent2.parents = [grandparent2]

# Créer un graphique à l'aide de Graphviz
dot = Digraph(comment='Arbre Généalogique')

# Fonction pour ajouter des nœuds et des liens au graphique
def add_to_graph(person, graph):
    graph.node(person.name)
    for parent in person.parents:
        graph.node(parent.name)
        graph.edge(parent.name, person.name)
        add_to_graph(parent, graph)

# Ajouter la famille à la visualisation
add_to_graph(child1, dot)
add_to_graph(child2, dot)

# Enregistrer et afficher le graphique
dot.render('family_tree.gv', view=True)