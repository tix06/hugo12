"""
TP - Carnet d'adresses
Nom, prénom : ......................
Classe : ......................

Consigne générale : complétez le code à chaque endroit signalé par
# A COMPLETER, puis exécutez le fichier en entier. Chaque partie est
vérifiée par des instructions assert : si aucun message d'erreur ne
s'affiche, votre code est correct pour cette partie.
"""

import random
import string
import timeit

from donnees_contacts import PRENOMS, NOMS, RUES, VILLES_CP


# ============================================================
# FONCTIONS FOURNIES (à ne pas modifier)
# ============================================================

def importer_contact():
    """Pioche aléatoirement, dans les données du fichier donnees_contacts.py,
    un nom complet, une adresse (rue), une ville et un code postal.
    Renvoie le tuple (nom, rue, ville, code_postal).

    Pour multiplier le nombre de noms de famille possibles (et donc
    limiter les doublons quand on génère beaucoup de contacts), un nom
    composé est formé une fois sur deux en accolant deux noms de la
    liste NOMS (par exemple "Costa-Royer")."""
    prenom = random.choice(PRENOMS)
    if random.random() < 0.5:
        nom_famille = random.choice(NOMS)
    else:
        nom1, nom2 = random.sample(NOMS, 2)
        nom_famille = f"{nom1}-{nom2}"
    nom = f"{prenom} {nom_famille}"
    numero_rue = random.randint(1, 150)
    rue = f"{numero_rue}, {random.choice(RUES)}"
    ville, code_postal = random.choice(VILLES_CP)
    return nom, rue, ville, code_postal


def genere_telephone():
    """Génère un numéro de téléphone factice sous la forme '0X XX XX XX XX'."""
    groupes = [f"0{random.randint(1, 9)}"] + [f"{random.randint(0, 99):02d}" for _ in range(4)]
    return " ".join(groupes)


def genere_date_naissance():
    """Génère une date de naissance factice sous la forme 'JJ/MM/AAAA'."""
    jour = random.randint(1, 28)
    mois = random.randint(1, 12)
    annee = random.randint(1950, 2005)
    return f"{jour:02d}/{mois:02d}/{annee}"


def genere_mot_de_passe(longueur=10):
    """Génère un mot de passe factice de la longueur donnée."""
    caracteres = string.ascii_letters + string.digits + "!@#$%&*"
    return "".join(random.choice(caracteres) for _ in range(longueur))


# ============================================================
# PARTIE 1 - FABRICATION D'UN CONTACT
# ============================================================

# Exercice 1
# Créez un dictionnaire nommé "contact" pour le contact suivant :
#   Margaret Costa-Royer
#   08 06 18 37 28
#   93, avenue Bruneau
#   13749 Perrot
# Les clés attendues sont : nom, tel, rue, code, ville, naissance

# A COMPLETER
contact = {}

assert contact["nom"] == "Margaret Costa-Royer"
assert contact["tel"] == "08 06 18 37 28"
assert contact["ville"] == "Perrot"
print("Exercice 1 : OK")

# Exercice 2
# Ajoutez une nouvelle entrée "passwd" au dictionnaire contact,
# ayant pour valeur 's75JWikE&o'

# A COMPLETER

assert contact["passwd"] == 's75JWikE&o'
print("Exercice 2 : OK")


# ============================================================
# PARTIE 2 - GENERATION AUTOMATIQUE D'UN CONTACT
# ============================================================

# Exercice 3
# Ecrivez une fonction genere_contact() qui :
#  - ne prend aucun paramètre
#  - renvoie un dictionnaire possédant les mêmes clés que le contact
#    de l'exercice 1, y compris "passwd"
# Utilisez pour cela les fonctions fournies plus haut :
# importer_contact(), genere_telephone(), genere_date_naissance()
# et genere_mot_de_passe().

def genere_contact():
    """Fabrique un contact factice et le renvoie sous forme de dictionnaire."""
    # A COMPLETER
    pass


contact1 = genere_contact()
assert type(contact1["nom"]) == str
assert "ville" in contact1
print("Exercice 3 : OK")


# ============================================================
# PARTIE 3 - PREMIERE IMPLEMENTATION DU CARNET (LISTE)
# ============================================================

# Exercice 4
# Ecrivez une fonction genere_carnet1(n) qui renvoie une liste de n
# contacts générés aléatoirement.
# ATTENTION : deux contacts du carnet ne doivent jamais avoir le même
# nom (sinon la recherche par nom n'aurait plus de sens). Utilisez une
# boucle qui régénère un contact tant que son nom est déjà présent
# dans le carnet (on peut mémoriser les noms déjà utilisés dans un set).

def genere_carnet1(n):
    """Renvoie une liste de n contacts aléatoires, tous de noms différents."""
    # A COMPLETER
    pass


carnet1 = genere_carnet1(10)
assert type(carnet1) == list
assert len(carnet1) == 10
assert "nom" in carnet1[3]
noms_carnet1 = [c["nom"] for c in carnet1]
assert len(set(noms_carnet1)) == 10  # tous les noms doivent être différents
print("Exercice 4 : OK")

# Exercice 5
# Ecrivez une fonction est_present(nom, carnet) qui renvoie True si
# nom figure dans le carnet d'adresses (liste), False sinon.

def est_present(nom, carnet):
    """Teste si nom est présent dans le carnet d'adresses (liste)."""
    # A COMPLETER
    pass


carnet1 = genere_carnet1(10)
nom_test = carnet1[-1]["nom"]
assert est_present(nom_test, carnet1)
assert not est_present("Lecluse Olivier", carnet1)
print("Exercice 5 : OK")


# ============================================================
# PARTIE 4 - MESURE DE PERFORMANCE (LISTE)
# ============================================================

# Ne modifiez rien ici : exécutez et observez les temps affichés.

carnet1 = genere_carnet1(100)
nom_test = carnet1[-1]["nom"]
duree = timeit.timeit(lambda: est_present(nom_test, carnet1), number=1000)
print(f"Liste de 100 contacts   : {duree:.5f} s pour 1000 recherches")

carnet1 = genere_carnet1(1000)
nom_test = carnet1[-1]["nom"]
duree = timeit.timeit(lambda: est_present(nom_test, carnet1), number=1000)
print(f"Liste de 1000 contacts  : {duree:.5f} s pour 1000 recherches")

# Question 1 (répondez par un commentaire ci-dessous) :
# Comment le temps de recherche évolue-t-il quand la taille du carnet
# est multipliée par 10 ?
#
# A COMPLETER (réponse en commentaire)


# ============================================================
# PARTIE 5 - SECONDE IMPLEMENTATION DU CARNET (DICTIONNAIRE)
# ============================================================

# Exercice 6
# Ecrivez une fonction genere_carnet2(n) qui renvoie un dictionnaire
# de n contacts aléatoires : les clés sont les noms, les valeurs sont
# les fiches contacts (dictionnaires).
# ATTENTION : si deux contacts générés ont le même nom, le second
# écraserait le premier dans le dictionnaire et le carnet contiendrait
# alors moins de n contacts. Assurez-vous, comme à l'exercice 4, qu'un
# nom n'est ajouté que s'il n'est pas déjà une clé du dictionnaire.

def genere_carnet2(n):
    """Renvoie un dictionnaire de n contacts aléatoires, de noms tous différents."""
    # A COMPLETER
    pass


carnet2 = genere_carnet2(10)
assert type(carnet2) == dict
assert len(carnet2) == 10  # aucun nom ne doit avoir été écrasé
nom_test = list(carnet2.keys())[-1]
assert type(carnet2[nom_test]) == dict
print("Exercice 6 : OK")


# ============================================================
# PARTIE 6 - MESURE DE PERFORMANCE (DICTIONNAIRE)
# ============================================================

# Ne modifiez rien ici : exécutez et observez les temps affichés.

carnet2 = genere_carnet2(100)
nom_test = list(carnet2.keys())[-1]
duree = timeit.timeit(lambda: nom_test in carnet2, number=1000)
print(f"Dictionnaire de 100 contacts    : {duree:.5f} s pour 1000 recherches")

carnet2 = genere_carnet2(10000)
nom_test = list(carnet2.keys())[-1]
duree = timeit.timeit(lambda: nom_test in carnet2, number=1000)
print(f"Dictionnaire de 10000 contacts  : {duree:.5f} s pour 1000 recherches")

# Question 2 (répondez par un commentaire ci-dessous) :
# Comparez l'évolution du temps de recherche dans le dictionnaire à
# celle observée dans la liste. Quelle structure de données est la
# mieux adaptée à la recherche sur les clés, et pourquoi ?
#
# A COMPLETER (réponse en commentaire)
