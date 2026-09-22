---
Title: rechercher
description: algorithmes de parcours séquentiel et dichotomique
weight: 14
---

La connaissance des algorithmes suivants est exigée pour les étudiants en NSI. Le langage python propose des fonctions pour chacun d'eux. Mais, parfois, il est demandé à l'étudiant d'écrire ou compléter le script pour ces fonctions.

# Parcours séquentiel

On parcourt la structure élément par élément, du début à la fin.

## algorithmes de recherche
Exemple avec une liste, avec un dictionnaire

```python
# liste : renvoie l'indice de la valeur, ou -1 si absente
def recherche_liste(liste, valeur):
    for i in range(len(liste)):
        if liste[i] == valeur:
            return i
    return -1

# dictionnaire : renvoie la clé associée à la valeur
def recherche_dict(d, valeur):
    for cle in d:
        if d[cle] == valeur:
            return cle
    return None
```

## recherche d'occurences

```python
def compter_occurrences(liste, valeur):
    compteur = 0
    for element in liste:
        if element == valeur:
            compteur += 1
    return compteur
```

## calcul d'une somme ou moyenne

```python
def somme(liste):
    total = 0
    for element in liste:
        total += element
    return total

def moyenne(liste):
    return somme(liste) / len(liste)
```

## recherche d'un extremum (min, max)

```python
def maximum(liste):
    m = liste[0]
    for element in liste:
        if element > m:
            m = element
    return m
```

# Recherche dichotomique

S'applique uniquement sur une liste **triée**. On compare la valeur cherchée à l'élément central puis on réduit la zone de recherche de moitié à chaque étape.

```python
def dichotomie(liste, valeur):
    gauche, droite = 0, len(liste) - 1
    while gauche <= droite:
        milieu = (gauche + droite) // 2
        if liste[milieu] == valeur:
            return milieu
        elif liste[milieu] < valeur:
            gauche = milieu + 1
        else:
            droite = milieu - 1
    return -1
```

*A retenir :* recherche séquentielle en O(n), recherche dichotomique en O(log n).

# Liens
* [TP](../page6/)
