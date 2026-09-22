---
Title: calculer
description: multiplier, diviser, recherche du PGCD
weight: 13
---

# multiplier sans le signe `*`

Addition répétée : on ajoute `a` à un total, `b` fois.

```python
def multiplier(a, b):
    resultat = 0
    for _ in range(b):
        resultat += a
    return resultat
```

*Exemple :* `multiplier(6, 4)` &rarr; `6+6+6+6` &rarr; `24`

# diviser sans le signe `/`

Soustractions répétées : on retire `b` à `a` tant que c'est possible (division euclidienne : quotient et reste).

```python
def diviser(a, b):
    quotient = 0
    reste = a
    while reste >= b:
        reste -= b
        quotient += 1
    return quotient, reste
```

*Exemple :* `diviser(17, 5)` &rarr; `(3, 2)` car `17 = 5×3 + 2`

# PGCD euclide

Le PGCD de `a` et `b` est égal au PGCD de `b` et `a % b`. On répète jusqu'à obtenir un reste nul.

```python
def pgcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
```

*Exemple :* `pgcd(48, 18)` &rarr; `48%18=12` &rarr; `18%12=6` &rarr; `12%6=0` &rarr; PGCD = `6`

# Lien
* [TP](../page5)
