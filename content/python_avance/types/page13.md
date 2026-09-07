---
Title : TD1 - types simples (corrigé)
titleHidden: true
description: corrigé du TD1 sur int, float, str, bool
hidden: true
weight: 7
---



# Corrigé du TD1 : variables et types natifs

## Exercice 1 — `None`
```
None
<class 'NoneType'>
```
`verifier_age` ne contient pas de `return` sur le chemin où `age < 18` : la fonction renvoie donc implicitement `None`.

## Exercice 2 — `bool`
```python
True + True    # 2
False + 10     # 10
True == 1      # True
True * 5       # 5
```
`bool` est un sous-type de `int` (`True` = 1, `False` = 0), donc ces valeurs se comportent comme des entiers dans les calculs.

## Exercice 3 — `math`
```python
math.sqrt(16)   # 4.0
math.floor(7.9) # 7   (arrondi à l'entier inférieur)
math.ceil(7.1)  # 8   (arrondi à l'entier supérieur)
math.pow(2, 10) # 1024.0 (toujours un float, contrairement à 2**10)
```

## Exercice 4 — `round`
```python
round(2.5)        # 2  (arrondi au pair le plus proche : "banker's rounding")
round(3.5)        # 4  (4 est le pair le plus proche)
round(3.14159, 3) # 3.142
```
Ce comportement (arrondi au pair) est une spécificité de Python à signaler : il évite un biais systématique vers le haut lors d'arrondis répétés sur de grandes quantités de données.

## Exercice 5 — typage dynamique / affectation chaînée
1.
```
<class 'int'>
<class 'str'>
```
Le même nom `a` a désigné successivement un `int` puis un `str` : c'est le typage dynamique (le type est attaché à la valeur, pas au nom).

2. `x, y = y, x = 1, 2` . Alors `print(x,y)` affiche :

```
2 1
```

Python évalue l'expression `1, 2` (le tuple `(1, 2)`) **une seule fois**, puis l'affecte à chaque cible de gauche à droite :
- `x, y = (1, 2)` → `x = 1`, `y = 2`
- `y, x = (1, 2)` → `y = 1`, `x = 2`
Le résultat final est donc `x = 2`, `y = 1`.

3. En deux lignes:

```python
x,y=1,2
x,y = y,x
print(x,y)
# Affiche 2 1
```

## Exercice 6 — références, `is`, `==`
1.
```
True
True (le plus souvent, voir remarque)
```
2. `==` compare les **valeurs** ; `is` compare les **références** (même emplacement mémoire, donné par `id`).
3. *Remarque pour l'enseignant :* CPython "interne" (met en cache) certaines chaînes courtes et simples, donc `a is b` peut afficher `True` même sans lien explicite entre `a` et `b` — c'est un détail d'implémentation, pas une garantie du langage. En revanche, `a is c` est **toujours** `True` ici puisque `c = a` fait explicitement référence au même objet. C'est l'occasion de préciser que seul `c = a` garantit `is`, pas l'égalité de contenu.

## Exercice 7 — méthodes de chaînes
```python
phrase = "  Les Chaines De Caracteres En Python  "
p1 = phrase.strip()
p2 = p1.lower()
p3 = p2.replace("python", "nsi")
mots = p3.split(" ")
resultat = "-".join(mots)
# resultat : 'les-chaines-de-caracteres-en-nsi'
```

## Exercice 8 — f-strings
```python
nom = "Turing"
annee = 1912
print(f"Nom : {nom}, né en {annee}")
print(f"{nom} a {2024 - annee} ans")
```

## Exercice 9 — parser une date
```python
d = "2024-09-02"

# 1. slicing
annee = d[0:4]
mois = d[5:7]
jour = d[8:10]

# 2. split
annee, mois, jour = d.split("-")
```
3. La méthode `split` est plus robuste : elle ne dépend pas de positions fixes. Si le jour ou le mois avait un seul chiffre (format non normalisé), le slicing donnerait des résultats faux, alors que `split("-")` fonctionne tant que le séparateur `-` reste présent.
