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


# Appel de la fonction principale
deviner_le_nombre()
