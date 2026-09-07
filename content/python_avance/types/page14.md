---
Title : TP2 - types construits (corrigé)
titleHidden: true
description: corrigé du TP2 sur listes, tuples, dictionnaires, mutabilité
weight: 9
hidden: true
---

# Corrigé — TD : Types construits en Python

*Ce corrigé est destiné à l'enseignant.*

---

## Script 1 — Listes et aliasing

**Q1.**
```
[12, 14, 9, 18]
[12, 14, 9, 18]
```
Les deux `print` affichent le même contenu.

**Q2.** `classe_B = classe_A` ne copie pas la liste : les deux noms `classe_A` et `classe_B` référencent le **même objet** en mémoire (aliasing). Comme les listes sont **mutables**, `notes.append(valeur)` modifie cet objet unique en place, ce qui se répercute sur les deux noms qui y font référence.

**Q3.** Version attendue :
```python
def ajouter_note(notes, valeur):
    notes.append(valeur)
    return notes

classe_A = [12, 14, 9]
classe_B = classe_A[:]     # ou : list(classe_A)
ajouter_note(classe_B, 18)

print(classe_A)  # [12, 14, 9]
print(classe_B)  # [12, 14, 9, 18]
```
Point clé à valoriser : utilisation d'une **copie par valeur** (`[:]` ou `list(...)`) plutôt qu'une simple affectation, pour obtenir deux objets indépendants en mémoire.

---

## Script 2 — Tuples et éléments mutables

**Q1.** Avant la dernière ligne :
```
('Dupont', [15, 12, 18, 20])
```
La dernière ligne (`eleve[1] = [0]`) provoque une erreur :
```
TypeError: 'tuple' object does not support item assignment
```

**Q2.** Le tuple est **non mutable** : on ne peut pas réaffecter l'un de ses éléments (`eleve[1] = ...`). En revanche, l'élément à l'indice 1 est lui-même une **liste**, qui est mutable : on peut donc modifier son *contenu* (ici avec `append`) sans jamais réaffecter l'élément du tuple. L'immuabilité du tuple porte sur ses références, pas sur les objets référencés.

**Q3.** Il faut modifier le contenu de la liste en place, sans réaffecter `eleve[1]` :
```python
eleve[1].clear()
# ou, équivalent :
eleve[1][:] = []
```
Point clé à valoriser : toute solution du type `eleve[1] = []` doit être rejetée, car elle réaffecte l'élément du tuple et lève la même `TypeError` qu'à la question précédente.

---

## Script 3 — Dictionnaires et portée des variables

**Q1.**
```
{'pommes': 7, 'poires': 5}
{'pommes': 7, 'poires': 5}
```
Le second `print` affiche le **même** dictionnaire qu'avant l'appel à `reinitialiser()` : le stock n'a pas été vidé.

**Q2.** Dans `vendre`, l'instruction `stock[fruit] -= quantite` **modifie en place** un élément du dictionnaire global : aucune réaffectation du nom `stock` n'a lieu, donc pas besoin de `global`. Dans `reinitialiser`, l'instruction `stock = {}` **réaffecte** le nom `stock` : Python crée alors une variable **locale** à la fonction (qui masque la variable globale le temps de l'appel), sans toucher au dictionnaire global. C'est exactement la distinction faite dans le cours entre lire/modifier en place une variable globale et la réaffecter.

**Q3.** Deux corrections possibles :
```python
# Solution 1 : déclarer explicitement la variable comme globale
def reinitialiser():
    global stock
    stock = {}

# Solution 2 : modifier le dictionnaire en place, sans le réaffecter
def reinitialiser():
    stock.clear()
```
Point clé à valoriser : la solution 2 n'a pas besoin de `global`, car `clear()` modifie l'objet existant plutôt que d'en créer un nouveau — à mettre en parallèle avec la question 1 (aliasing) et la question 2 du script 2 (modifier vs réaffecter).

---

## Grille de correction indicative

| Question | Compétence évaluée | Barème indicatif |
|---|---|---|
| Q1 (×3) | Lire du code et prédire un résultat / une erreur sans exécuter | 1 pt chacune |
| Q2 (×3) | Mobiliser la notion exacte du cours pour expliquer | 2 pts chacune |
| Q3 (×3) | Modifier le code en respectant une contrainte précise | 3 pts chacune |

Total : 18 points.
