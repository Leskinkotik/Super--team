# Ennoncer :Écrivezprogrammequicrée un bytearray..
# à partir d'une liste d'entiers
# Puis modifie un de ses éléments.
# Importe le module 'sys' pour l'encodage (implicite pour 'bytearray').

# Initialise une liste d'entiers dans la variable 'liste_entiers'.
liste_entiers = [10, 20, 30, 40, 50]

# Crée un bytearray 'ba' à partir de 'liste_entiers'.
ba = bytearray(liste_entiers)

# Affiche le 'ba' initial via la fonction 'print'.
print("Bytearray original:", ba)

# Modifie l'élément d'index 2 de 'ba' à la valeur 35.
ba[2] = 35

# Affiche le 'ba' modifié en utilisant la fonction 'print'.
print("Bytearray après modification:", ba)
