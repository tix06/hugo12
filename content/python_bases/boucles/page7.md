---
Title: TP 6b Fonctions et boucles
titleHidden: false
description: Partie C de la feuille d'exercices (fonctions et boucles) et Partie D (code / décode)
hidden: true
weight: 12
---

## Partie C de la feuille d'exercices — Fonctions et boucles

## Exercice 11 — Traitements automatisés sur des listes

*Rappels : `chr(110)` donne le caractère de rang 110 dans la table ASCII, `ord("n")` donne le rang du caractère `"n"`. `L.append(x)` ajoute `x` à la fin de la liste `L`.*

Compléter les fonctions suivantes :

```python
def somme(L):
    s = 0
    for valeur in L:
        s += ..........
    return ..........

def decode(L):
    chaine = ""
    for rang in L:
        chaine += chr(..........)
    return chaine

def encode(message):
    L = []
    for c in message:
        L.append(..........)
    return L
```

Compléter ce qu'affiche le shell :

```python
>>> somme([65400, 31654, 1026])
..........
>>> decode([110, 99, 111])
..........
>>> encode("abacab")
..........
```

## Exercice 12 — Multiplication par additions successives

Multiplier `a` par `b` revient à calculer `a + a + … + a` (`b` fois). La variable `produit` stocke les additions successives et `b` sert de compteur : on le diminue de 1 à chaque itération.

**1.** Compléter la fonction (seuls `+` et `-` sont autorisés).

```python
def multiplier(a, b):
    produit = 0
    while b > .....:
        produit = produit + a
        b = b - .....
    return produit
```

```python
>>> multiplier(3, 8)
..........
```

**2.** Compléter le tableau de suivi des variables pour l'appel `multiplier(3, 8)`.

| `b` avant le test | 8 |   |   |   |   |   |   |   |   |
|---|---|---|---|---|---|---|---|---|---|
| test `b > 0` |   |   |   |   |   |   |   |   |   |
| `produit` après le tour |   |   |   |   |   |   |   |   |   |

**3.** Justifier que la fonction se termine, à l'aide du tableau.

..............................................................................................

..............................................................................................

## Exercice 13 — Division entière par soustractions successives

Écrire la fonction `division(a, b)` qui renvoie le quotient entier de `a` par `b`, en n'utilisant que l'opérateur `-` (et `+` pour compter).

```python
def division(a, b):
    ...
```

```python
>>> division(17, 5)
3
>>> division(20, 4)
..........
>>> division(3, 7)
..........
```

## Partie D — Code / Décode

Dans la partie C, la fonction `decode` transformait **une liste de rangs** en **une chaîne de caractères**, et `encode` faisait l'inverse. On va maintenant coder et décoder des **images** en ASCII-art : une image est une suite de lignes, et chaque ligne est une suite de caractères.

## Exercice 14 — Une image, c'est une liste de lignes

Une image peut être stockée dans une liste de chaînes de caractères : chaque élément de la liste est une ligne de l'image.

Compléter le script pour afficher l'image, ligne par ligne :

```python
L1 = [' ^___^', '" o o "', '===X===', '   "  ']
for ligne in L1:
    print(..........)
```

```python
>>> (exécution du script)
 ^___^
" o o "
===X===
   "
```

**a.** Combien de tours fait la boucle ? ..........

**b.** Quelle valeur prend la variable `ligne` au 2e tour ? ..........

## Exercice 15 — Une liste de listes

Cette fois, chaque ligne de l'image n'est plus une chaîne, mais une **liste de caractères**. `L2` est donc une **liste de listes** :

```python
L2 = [[' ', '^', '_', '_', '_', '^'],
      ['"', ' ', 'o', ' ', 'o', ' ', '"'],
      ['=', '=', '=', 'X', '=', '=', '='],
      [' ', ' ', ' ', '"', ' ', ' ']]
```

**1. Lire une liste de listes.** `L2[1]` est la 2e ligne (une liste), et `L2[1][2]` est le 3e caractère de cette ligne. Compléter :

```python
>>> len(L2)
..........
>>> L2[2]
..........
>>> L2[2][3]
..........
>>> len(L2[1])
..........
```

**2. Une ligne à la fois, avec une fonction.** Compléter la fonction `assemble` qui transforme une liste de caractères en chaîne (même principe que `decode` dans l'exercice 11) :

```python
def assemble(l):
    s = ''
    for c in l:
        s += ..........
    return s
```

```python
>>> assemble(['o', 'k'])
'ok'
>>> assemble(L2[0])
..........
```

Utiliser `assemble` dans une boucle pour afficher toute l'image :

```python
for l in L2:
    print(..........)
```

**3. Deux boucles imbriquées.** On remplace l'appel `assemble(l)` par le corps de la fonction : on obtient une boucle **à l'intérieur** d'une autre boucle. Compléter :

```python
for l in L2:              # boucle externe : parcourt les lignes
    s = ''
    for c in l:           # boucle interne : parcourt les caractères de la ligne l
        s += ..........
    print(..........)
```

**a.** Pourquoi faut-il écrire `s = ''` **dans** la boucle externe, et pas avant ?

..............................................................................................

**b.** Combien de tours fait la boucle externe ? .......... Combien de tours fait la boucle interne lors du 1er tour de la boucle externe ? .......... Au total, combien de caractères sont ajoutés à `s` ? ..........

## Exercice 16 — L'image cachée

Une image a été codée : chaque caractère a été remplacé par son rang dans la table ASCII, écrit en **hexadécimal**.

```python
M = [['20', '2F', '5C', '5F', '2F', '5C', '20'],
     ['28', '20', '2E', '20', '2E', '20', '29'],
     ['3D', '5C', '5F', '76', '5F', '2F', '3D']]
```

*Rappels :*

* *conversion hexadécimal → décimal : `int(valeur, 16)`*
* *conversion décimal → caractère ASCII : `chr`*

**1.** Compléter le shell :

```python
>>> int('41', 16)
..........
>>> chr(65)
..........
>>> chr(int('2F', 16))
..........
```

**2.** Compléter la fonction `hex_vers_car` qui convertit un code hexadécimal en caractère :

```python
def hex_vers_car(h):
    return chr(..........)
```

```python
>>> hex_vers_car('41')
'A'
```

**3.** Compléter le script qui décode l'image avec deux boucles imbriquées :

```python
for l in M:
    s = ''
    for r in l:
        s += ..........
    print(..........)
```

**4.** Dessiner l'image cachée :

```
..........
..........
..........
```

## Exercice 17 (bonus) — Coder une image

On fait maintenant l'opération inverse : transformer une image (liste de chaînes) en liste de listes de rangs ASCII, en réutilisant la fonction `encode` de l'exercice 11.

```python
def encode_image(image):
    M = []
    for ligne in image:
        M.append(..........)
    return M
```

```python
>>> encode_image(['^_^', 'o o'])
..........
```

Écrire ensuite une fonction `decode_image(M)` qui affiche l'image codée par `encode_image`, à l'aide de deux boucles imbriquées.

```python
def decode_image(M):
    ...
```

# Liens
##### {{% button href="../page2" icon="bullhorn" style="caution" %}}Cours{{% /button %}} 
##### {{% button href="../page3" icon="palette" style="tip" %}}TP6a{{% /button %}} Listes
##### {{% button href="../page7" icon="palette" style="tip" %}}TP6b{{% /button %}} Listes et codage/decodage ascii
##### {{% button href="../../TP/TP_shifumi" icon="palette" style="tip" %}}TP6c{{% /button %}} jeu du Shifumi
