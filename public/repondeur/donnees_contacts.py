"""
donnees_contacts.py

Données factices utilisées pour générer des contacts aléatoires.
Ce fichier est fourni : vous n'avez pas besoin de le modifier.
"""

PRENOMS = [
    "Margaret", "Lucas", "Emma", "Nathan", "Chloé", "Hugo", "Léa", "Louis",
    "Manon", "Gabriel", "Camille", "Raphaël", "Sarah", "Jules", "Inès",
    "Adam", "Louise", "Arthur", "Alice", "Mattéo", "Jade", "Noah", "Zoé",
    "Ethan", "Rose", "Liam", "Anna", "Tom", "Julia", "Paul",
    "Léon", "Nina", "Victor", "Lina", "Simon", "Eva", "Marius", "Iris",
    "Théo", "Agathe",
]

# Noms de famille "simples". importer_contact() (dans script.py) en
# combine parfois deux au hasard pour former un nom composé (ex :
# "Costa-Royer"), ce qui multiplie considérablement le nombre de noms
# de famille différents possibles.
NOMS = [
    "Costa", "Royer", "Lefèvre", "Bernard", "Girard", "Dubois", "Moreau",
    "Lambert", "Rousseau", "Fontaine", "Chevalier", "Robin", "Masson",
    "Sanchez", "Lopez", "Fournier", "Andre", "Mercier", "Blanc", "Guerin",
    "Boyer", "Garnier", "Chevallier", "Francois", "Legrand", "Gauthier",
    "Perrin", "Morel", "Faure", "Roux", "Muller", "Simon",
]

RUES = [
    "avenue Bruneau", "rue des Lilas", "rue de la Paix", "boulevard Voltaire",
    "impasse des Peupliers", "allée des Tilleuls", "rue Victor Hugo",
    "chemin des Vignes", "rue de la Gare", "place de la Mairie",
    "quai des Fleurs", "rue du Commerce",
]

# Chaque élément est un couple (ville, code_postal)
VILLES_CP = [
    ("Perrot", "13749"), ("Rochefort", "69002"), ("Vaugirard", "75015"),
    ("Beaumont", "44100"), ("Clermont", "63000"), ("Fontenay", "94120"),
    ("Argentan", "61200"), ("Villeneuve", "31000"), ("Montreuil", "93100"),
    ("Sartrouville", "78500"), ("Chartres", "28000"), ("Vichy", "03200"),
]
