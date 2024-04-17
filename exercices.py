"""import random

# Premier exercice Boucles


def deviner_le_nombre():
    nombre_mystere = random.randint(1, 100)

    print("Devinez le nombre mystère entre 1 et 100. Vous avez 5 tentatives.")

    for tentative in range(1, 6):
        message = "Tentative {}: Entrez votre estimation : ".format(tentative)
        guess = int(input(message))

        if guess == nombre_mystere:
            print("Félicitations ! Vous avez deviné le nombre mystère :",
                  nombre_mystere)
            return
        elif guess < nombre_mystere:
            print("Le nombre mystère est plus grand.")
        else:
            print("Le nombre mystère est plus petit.")

        tentatives_restantes = 5 - tentative
        print("Il vous reste", tentatives_restantes, "tentatives.")

    print("Vous avez épuisé toutes vos tentatives. Le nombre mystère était :",
          nombre_mystere)


deviner_le_nombre()


# Deuxieme exercice


def afficher_pyramide(hauteur):
    for i in range(1, hauteur + 1):
        print(" " * (hauteur - i), end="")
        print("*" * (2 * i - 1))


hauteur = int(input("Entrez la hauteur de la pyramide : "))
if hauteur <= 0:
    print("La hauteur doit être un entier positif.")
else:
    afficher_pyramide(hauteur)"""


# Troisieme exercice

def trouver_plus_grand_nombre():
    # Demander à l'utilisateur d'entrer trois nombres
    nombre1 = float(input("Entrez le premier nombre : "))
    nombre2 = float(input("Entrez le deuxième nombre : "))
    nombre3 = float(input("Entrez le troisième nombre : "))

    # Comparer les nombres pour trouver le plus grand
    if nombre1 >= nombre2 and nombre1 >= nombre3:
        plus_grand_nombre = nombre1
    elif nombre2 >= nombre1 and nombre2 >= nombre3:
        plus_grand_nombre = nombre2
    else:
        plus_grand_nombre = nombre3

    # Afficher le résultat
    print("Le plus grand nombre est :", plus_grand_nombre)


# Appeler la fonction pour exécuter le code
trouver_plus_grand_nombre()
