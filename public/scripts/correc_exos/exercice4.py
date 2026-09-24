## Exercice 4: bibliotheque
bibliotheque = {
    '978-2': {'titre': 'Le Petit Prince', 'auteur': 'Saint-Exupéry', 'annee': 1943, 'emprunte': False},
    '978-3': {'titre': '1984', 'auteur': 'Orwell', 'annee': 1949, 'emprunte': True},
    '978-4': {'titre': 'Fondation', 'auteur': 'Asimov', 'annee': 1951, 'emprunte': False}
}

def livres_disponibles(bibliotheque):
    return [info['titre'] for info in bibliotheque.values() if not info['emprunte']]

def emprunter(bibliotheque, isbn):
    if isbn in bibliotheque and not bibliotheque[isbn]['emprunte']:
        bibliotheque[isbn]['emprunte'] = True
        return True
    return False

def livres_par_auteur(bibliotheque):
    resultat = {}
    for info in bibliotheque.values():
        auteur = info['auteur']
        if auteur in resultat:
            resultat[auteur].append(info['titre'])
        else:
            resultat[auteur] = [info['titre']]
    return resultat

def livres_avant(bibliotheque, annee):
    livres = [(info['annee'], info['titre']) for info in bibliotheque.values() if info['annee'] < annee]
    livres.sort()
    return [titre for _, titre in livres]


# Question 1
assert livres_disponibles(bibliotheque) == ['Le Petit Prince', 'Fondation']

# Question 3
assert emprunter(bibliotheque, '978-2') == True
assert bibliotheque['978-2']['emprunte'] == True
assert emprunter(bibliotheque, '978-2') == False
assert livres_disponibles(bibliotheque) == ['Fondation']

# Question 4
# assert livres_par_auteur(bibliotheque) == ... a completer ...
