# 1. Écrivez un programme Python qui accepte une chaîne de caractères de
# l'utilisateur et affiche le nombre de majuscules et de minuscules

def compter_majmin(chaine):
    majuscules = 0
    minuscules = 0
    for symbole in chaine:
        if 'A' <= symbole <= 'Z':
            majuscules += 1
        elif 'a' <= symbole <= 'z':
            minuscules += 1
    return majuscules, minuscules


chaine_user = input("ecrire une chaîne de caractères:")
maj, min = compter_majmin(chaine_user)

print("Nombre de maj:", maj)
print("Nombre de min:", min)

"""Vous disposez de la chaîne de caractères suivante :
"Python est un langage de programmation puissant et facile à apprendre."
Extraction simple : Extraire le mot "Python" de la chaîne."""

chaine = "Python est un langage de programmation puissant et facile à apprendre."
python = ""
espace_trouve = False
for caractere in chaine:
    if caractere != " " and not espace_trouve:
        python += caractere
    else:
        espace_trouve = True
print(python)

"""Extraction par indices négatifs: Extraire
le mot "apprendre" en utilisant des indices négatifs."""
apprendre = ""
i = -2
while chaine[i] != " ":
    apprendre = chaine[i] + apprendre
    i -= 1
print(apprendre)

# Slicing:Extraire la phrase "langage de programmation" en utilisant le slicing
phrase = chaine[chaine.find("langage"):chaine.find("puissant") + len("puissant")]
print(phrase)

# Challenge : Inversez la chaîne de caractères entière.
inverse = ""
a = len(chaine) - 1   # a est index
while a >= 0:
    inverse += chaine[a]
    a -= 1
print(inverse)

""" 3.Écrire un programme qui demande à l'utilisateur
# de saisir deux nombres sous forme
# de chaînes de caractères, les convertit en entiers,
# effectue la somme de ces deux nombres,
# puis affiche le résultat sous différentes formes."""

nombre1 = input("écrire le premier nombre : ")
nombre2 = input("écrire le deuxième nombre : ")
nombre1 = int(nombre1)
nombre2 = int(nombre2)
somme = nombre1 + nombre2
print("La somme est :", somme)
print("La somme est :", nombre1, "+", nombre2, "=", somme)
