"""Écrivez un programme Python qui prend
une liste de tuples et affiche le tuple avec le plus d'éléments"""

liste_tuples = [(1, 2), (3, 4, 5), (6,), (7, 8, 9, 10)]
max_tuple = None
max_length = 0
for tup in liste_tuples:
    current_length = len(tup)
    if current_length > max_length:
        max_tuple = tup
        max_length = current_length
print(max_tuple,max_length)

"""Écrivez un programme qui inverse l'ordre des
éléments dans chaque tuple d'une liste de tuples."""

liste_tup = [('a', 'b', 'c'), (4, 5, 6,'a' ), (1, 2, 3)]
def invert_tuples(liste_tup):
    inverted_tuples = []  
    for tup in liste_tup:
        # Инвертирование порядка элементов в кортеже и добавление его в новый список
        inverted_tuple = tuple(reversed(tup))
        inverted_tuples.append(inverted_tuple)

    return inverted_tuples

# Инвертирование порядка элементов в каждом кортеже с помощью функции invert_tuples
inverted_tuples = invert_tuples(liste_tup)
print(inverted_tuples)t
