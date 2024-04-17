# Définition de la classe 'Node', qui représente un nœud dans un arbre binaire.
class Node:
    # Constructeur de la classe 'Node'. 
    def __init__(self, key):
    # Je définis ici chaque nœud avec trois attributs : left, right, et value.
        self.left = None   
        # Je définis 'left' pour pointer vers le nœud enfant gauche, initialisé à None.
        self.right = None  
        # Je définis 'right' pour pointer vers le nœud enfant droit, initialisé à None.
        self.value = key   # Je stocke la clé (ou la valeur) du nœud.

# Fonction pour insérer une nouvelle clé dans l'arbre binaire de recherche.
def insert(root, key):
    if root is None:
    # Si le nœud actuel est vide, je crée un nouveau nœud avec la clé donnée.
        return Node(key)
    else:
        # Sinon, je compare la clé avec la valeur du nœud actuel pour décider de l'insertion à gauche ou à droite.
        if root.value < key:
            root.right = insert(root.right, key)  # Insertion à droite si la clé est plus grande.
        else:
            root.left = insert(root.left, key)   # Insertion à gauche si la clé est plus petite.
    return root  # Je retourne le nœud actuel après l'insertion.

# Fonction pour effectuer un parcours infixe (Inorder Traversal) de l'arbre.
def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)   # D'abord, je visite le sous-arbre gauche.
        print(root.value, end=' ')     # Ensuite, j'affiche la valeur du nœud courant.
        inorder_traversal(root.right)  # Enfin, je visite le sous-arbre droit.

# Je crée un arbre avec une valeur racine de 50.
r = Node(50)

# Je procède à l'insertion de nouveaux nœuds dans l'arbre.
r = insert(r, 30)
r = insert(r, 20)
r = insert(r, 40)
r = insert(r, 70)
r = insert(r, 60)
r = insert(r, 80)

# J'affiche l'arbre en utilisant le parcours infixe, qui affiche les valeurs dans l'ordre croissant.
inorder_traversal(r)
