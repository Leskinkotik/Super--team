# Importe le module 'sys' (non affiché mais implicite pour 'utf-8')
# Déclare une chaîne (variable 'phrase')
phrase = "Hello World!"
# Convertit la chaîne en 'bytearray' via la bibliothèque 'utf-8'
ba = bytearray(phrase, 'utf-8')

# Imprime le bytearray (utilise la fonction 'print')
print("Bytearray original:", ba)

# Modifie des éléments du bytearray (utilise la fonction 'ord')
ba[1] = ord('e')  # Remplace par 'e'
ba[2] = ord('l')  # Remplace par 'l'
ba[3] = ord('p')  # Remplace par 'p'
ba[4] = ord('!')  # Remplace par '!'

# Affiche le bytearray après modification (utilise 'print')
print("Bytearray modifié:", ba)

# Ajoute un élément au bytearray (utilise 'append')
ba.append(ord('!'))

# Montre le bytearray après ajout (utilise 'print')
print("Bytearray après ajout:", ba)

# Enlève un élément du bytearray (utilise 'del')
del ba[-1]

# Imprime le bytearray après retrait (utilise 'print')
print("Bytearray après suppression:", ba)

# Convertit le bytearray en chaîne (utilise 'decode')
phrase_modifiée = ba.decode('utf-8')
# Affiche la chaîne modifiée (utilise 'print')
print("Phrase modifiée:", phrase_modifiée)
