"""Écrivez un programme Python qui prend
une liste de tuples et affiche le tuple avec le plus d'éléments"""


def tuple_plus_grand(liste_tuples):

    plus_grand_tuple = ()

    for tup in liste_tuples:
        if len(tup) > len(plus_grand_tuple):
            plus_grand_tuple = tup

    return plus_grand_tuple


liste_tuples = [(8, 5), ('a', 'b', 'c'), (6,), (4, 3, 9, 1)]
tuple_resultat = tuple_plus_grand(liste_tuples)
print(liste_tuples)
print(tuple_resultat)


"""Écrivez un programme qui inverse l'ordre des
éléments dans chaque tuple d'une liste de tuples."""

liste_tup = [('a', 'b', 'c'), (4, 5, 6, 'a'), (1, 2, 3)]


def invert_tuples(liste_tup):
    inverted_tuples = []
    for tup in liste_tup:
        inverted_tuple = tuple(reversed(tup))
        inverted_tuples.append(inverted_tuple)

    return inverted_tuples


inverted_tuples = invert_tuples(liste_tup)
print(inverted_tuples)
