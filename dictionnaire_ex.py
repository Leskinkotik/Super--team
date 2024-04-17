def etudiants_note_superieure_ou_egale(dictionnaire_notes):
    """
    Retourne un nouveau dictionnaire contenant les noms des étudiants
    ayant une note moyenne supérieure ou égale à 15.
    """
    etudiants_selectionnes = {}
    for nom, note in dictionnaire_notes.items():
        if note >= 15:
            etudiants_selectionnes[nom] = note
    return etudiants_selectionnes


# Dictionnaire des notes des étudiants (nom: note moyenne)
dictionnaire_notes = {
    "Alice": 18,
    "Bob": 12,
    "Charlie": 16,
    "David": 14,
    "Eva": 19
}


etudiants_selectionnes = etudiants_note_superieure_ou_egale(dictionnaire_notes)

# Affichage du nouveau dictionnaire avec les étudiants sélectionnés
print("Étudiants avec une note moyenne supérieure ou égale à 15 :")
print(etudiants_selectionnes)
