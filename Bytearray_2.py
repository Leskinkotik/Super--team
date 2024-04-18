# Enoncé :Écrivez un programme qui parcourt un bytearray.
# Affiche chaque élément, puis ajoute 1 à chaque élément.
# je Crée un bytearray avec la variable 'ba'
# en utilisant le type de données intégré 'bytearray'.
ba = bytearray([10, 20, 30, 40, 50])
print(ba)

# Démarre une boucle 'for' en utilisant 'enumerate' pour obtenir à la fois
# l'indice 'i' et l'élément 'byte'. 'enumerate' est une fonction intégrée.
for i, byte in enumerate(ba):
    # Affiche l'élément actuel en utilisant 'print', une fonction intégrée.
    print(f"Élément original à l'indice {i}: {byte}")
    # Ajoute 1 à l'élément actuel du bytearray.
    # L'opérateur '+=' est utilisé pour ajouter et assigner.
    ba[i] += 1

# Affiche le bytearray complet après l'ajout.
# Utilise 'print' pour afficher le contenu du 'bytearray'modifié.
print("Bytearray après ajout de 1 à chaque élément:", ba)
