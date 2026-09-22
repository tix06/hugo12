---
Title: algorithmes avancés
titleHidden: true
description: algorithme glouton et de recherche des K plus proches voisins
weight: 16
---

# Algorithmes avancés
---
## Algorithme glouton

A chaque étape, on fait le choix qui semble le meilleur *sur le moment*, sans revenir en arrière. Ne donne pas toujours la solution optimale, mais est simple et rapide.

*Exemple classique : le rendu de monnaie.* On utilise toujours la plus grande pièce/billet possible.

```python
def rendu_monnaie(a_rendre, pieces):
    pieces.sort(reverse=True)  # du plus grand au plus petit
    resultat = []
    for p in pieces:
        while a_rendre >= p:
            resultat.append(p)
            a_rendre -= p
    return resultat
```

*Exemple :* `rendu_monnaie(78, [50, 20, 10, 5, 2, 1])` &rarr; `[50, 20, 5, 2, 1]`

*Limite :* avec un système de pièces mal choisi, le glouton peut ne pas être optimal (ex. rendre `6` avec `[4, 3, 1]` donne `4+1+1` au lieu de `3+3`).

## Recherche des K plus proches voisins

Pour classer une nouvelle donnée, on calcule sa distance à toutes les données connues, puis on regarde les `k` voisins les plus proches : la classe majoritaire parmi eux devient la prédiction.

```python
from math import sqrt

def distance(p1, p2):
    return sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def k_plus_proches_voisins(donnees, nouveau_point, k):
    # donnees : liste de (point, classe)
    distances = []
    for point, classe in donnees:
        distances.append((distance(point, nouveau_point), classe))
    distances.sort()
    k_voisins = distances[:k]
    classes = [classe for _, classe in k_voisins]
    return max(classes, key=classes.count)  # classe majoritaire
```

*Exemple :* `donnees = [((1,1), "A"), ((2,1), "A"), ((5,5), "B")]` puis `k_plus_proches_voisins(donnees, (1,2), 2)` &rarr; `"A"` (les 2 voisins les plus proches sont de classe A)

*A retenir :* le choix de `k` est important — trop petit, sensible au bruit ; trop grand, mélange des classes éloignées.
