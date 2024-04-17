import random

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
    afficher_pyramide(hauteur)


# Troisieme exercice

def trouver_plus_grand_nombre():
    # Demander à l'utilisateur d'entrer trois nombres
    nombre1 = float(input("Entrez le premier nombre : "))
    nombre2 = float(input("Entrez le deuxième nombre : "))
    nombre3 = float(input("Entrez le troisième nombre : "))

    if nombre1 >= nombre2 and nombre1 >= nombre3:
        plus_grand_nombre = nombre1
    elif nombre2 >= nombre1 and nombre2 >= nombre3:
        plus_grand_nombre = nombre2
    else:
        plus_grand_nombre = nombre3

    print("Le plus grand nombre est :", plus_grand_nombre)


trouver_plus_grand_nombre()


# Quatrieme exercice

def decode_message(message):
    # Diviser la chaîne de nombres en une liste de nombres
    nombres = message.split()

    # Initialiser une chaîne vide pour stocker le message décodé
    message_decode = ""

    # Convertir chaque nombre selon la table ASCII
    for nombre in nombres:
        message_decode += chr(int(nombre))

    return message_decode


message_code = "72 101 108 108 111 44 32 87 111 114 108 100"

message_decode = decode_message(message_code)

print("Le message décodé est :", message_decode)

# Cinquieme exercice


def est_palindrome(mot):
    return mot == mot[::-1]


def compter_palindromes(liste_mots):
    nb_palindromes = 0

    for mot in liste_mots:
        if est_palindrome(mot):
            nb_palindromes += 1

    return nb_palindromes


liste_mots = ["radar", "level", "python", "stats", "racecar"]
nb_palindromes = compter_palindromes(liste_mots)

print("Nombre de palindromes dans la liste :", nb_palindromes)
