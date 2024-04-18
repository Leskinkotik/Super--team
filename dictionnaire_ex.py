def etudiants_note(dictionnaire_notes):
    etudiants_selectionnes = {}
    for nom, note in dictionnaire_notes.items():
        if note >= 15:
            etudiants_selectionnes[nom] = note
    return etudiants_selectionnes


dictionnaire_notes = {
    "Alice": 18,
    "Bob": 12,
    "Charlie": 16,
    "David": 14,
    "Eva": 19
}


etudiants_selectionnes = etudiants_note(dictionnaire_notes)

# Affichage du nouveau dictionnaire avec les étudiants sélectionnés
print("Étudiants avec une note moyenne supérieure ou égale à 15 :")
print(etudiants_selectionnes)


# Deuxieme exercice

def trier_produits_rupture(base_de_donnees_produits):
    produits_rupture_stock = []

    for produit_id in sorted(base_de_donnees_produits.keys()):
        produit_info = base_de_donnees_produits[produit_id]
        if produit_info["quantite"] == 0:
            produits_rupture_stock.append((produit_info["prix"], produit_id))

    produits_rupture_stock.sort(reverse=True)
    produits_rupture_stock_tries = [
        {"id": produit[1], "prix": produit[0]}
        for produit in produits_rupture_stock
    ]
    return produits_rupture_stock_tries


# Exemple base de données (identifiant: {"prix": prix, "quantite": quantite})
base_de_donnees_produits = {
    1: {"prix": 10, "quantite": 0},
    2: {"prix": 20, "quantite": 3},
    3: {"prix": 15, "quantite": 0},
    4: {"prix": 25, "quantite": 0},
    5: {"prix": 20, "quantite": 1},
    6: {"prix": 15, "quantite": 0}
}

produits_rupture_stock_tries = trier_produits_rupture(base_de_donnees_produits)

print("Produits en rupture de stock triés par prix :")
for produit in produits_rupture_stock_tries:
    print("Produit ID:", produit["id"], "- Prix:", produit["prix"])
