"""Écrivez un programme Python qui prend une liste et
retourne une nouvelle liste contenant uniquement les
éléments uniques de la première liste."""


def elements_uniques(liste):

    uniques = set()

    for element in liste:
        if element not in uniques:
            uniques.add(element)

    return list(uniques)


liste = [1, 2, 4, 4, 2, 3, 5]
resultat = elements_uniques(liste)
print(liste)
print(resultat)

"""Écrivez un programme Python qui effectue une rotation à
droite des éléments d'une liste. La rotation doit être
définie par l'utilisateur"""


def rotation_droite(liste, rotation):

    if not liste or rotation == 0:
        return liste

    rotation = rotation % len(liste)
    return liste[-rotation:] + liste[:-rotation]


liste = [1, 2, 3, 4, 5]
rotation = int(input("Entrez le nombre de rotations à droite : "))
resultat = rotation_droite(liste, rotation)
print(liste)
print(rotation, "fois :", resultat)
