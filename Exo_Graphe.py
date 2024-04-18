import networkx as nx
# jimportmodule NetworkX renomme nx facilitersonutilisation
import matplotlib.pyplot as plt
# j'mport module pyplot de Matplotlib,renommer pltprfaciliterutilisation

# Créer un graphe vide
G = nx.Graph()

# Ajouter des nœuds au graphe
G.add_node("A")  # Ajouter le nœud "A" au graphe
G.add_node("B")  # Ajouter le nœud "B" au graphe
G.add_node("C")  # Ajouter le nœud "C" au graphe

# Ajouter des arêtes entre les nœuds
G.add_edge("A", "B")  # Ajouter une arête entre le nœud "A" et le nœud "B"
G.add_edge("B", "C")  # Ajouter une arête entre le nœud "B" et le nœud "C"
G.add_edge("C", "A")  # Ajouter une arête entre le nœud "C" et le nœud "A"

# Dessiner le graphe
nx.draw(G, with_labels=True)
# Dessiner le graphe avec les étiquettes des nœuds affichées
plt.show()  # Afficher le graphe à l'écran
