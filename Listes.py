"""Écrivez un programme Python qui prend une liste et
retourne une nouvelle liste contenant uniquement les
éléments uniques de la première liste."""
liste = [2,2, 'g' ,2, 'a' , 'a' ,1,5]
liste_vide = []
for element in liste:
    if element not in liste_vide:
        liste_vide.append(element)
print("Liste des éléments uniques :", liste_vide)

"""Écrivez un programme Python qui effectue une rotation à
droite des éléments d'une liste. La rotation doit être
définie par l'utilisateur"""

liste_initiale = [1,2,3,9]
rotation = int(input("ecrire le nombre de rotations: "))
# Si le nombre de rotations est supérieur à la longueur de la liste, ajuster
if rotation > len(liste_initiale):
    rotation = rotation - len(liste_initiale)
indice_rotation = len(liste_initiale) - rotation

liste_apres_rotation = liste_initiale[indice_rotation:] + liste_initiale[:indice_rotation]

print("Liste après rotation à droite de", rotation, "positions :", liste_apres_rotation)
