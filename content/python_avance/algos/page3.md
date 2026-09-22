---
Title: trier
titleHidden: true
description: tri par selection, tri par insertion
weight: 15
---

# algorithmes de tri
---

## tri par insertion

On construit la partie triée au fur et à mesure : chaque nouvel élément est inséré à sa place parmi les précédents.

```python
def tri_insertion(liste):
    for i in range(1, len(liste)):
        valeur = liste[i]
        j = i - 1
        while j >= 0 and liste[j] > valeur:
            liste[j + 1] = liste[j]
            j -= 1
        liste[j + 1] = valeur
    return liste
```

*Exemple :* `[5, 2, 4, 1]` &rarr; `[2, 5, 4, 1]` &rarr; `[2, 4, 5, 1]` &rarr; `[1, 2, 4, 5]`

## tri par selection

A chaque étape, on cherche le minimum du reste de la liste et on l'échange avec le premier élément non trié.

```python
def tri_selection(liste):
    for i in range(len(liste)):
        indice_min = i
        for j in range(i + 1, len(liste)):
            if liste[j] < liste[indice_min]:
                indice_min = j
        liste[i], liste[indice_min] = liste[indice_min], liste[i]
    return liste
```

*Exemple :* `[5, 2, 4, 1]` &rarr; `[1, 2, 4, 5]` (le `1` puis le `2` sont placés successivement en tête)

*A retenir :* les deux algorithmes ont une complexité en O(n²) dans le pire des cas.
