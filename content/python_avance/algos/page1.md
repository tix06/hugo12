---
Title: calculer
description: multiplier, diviser, recherche du PGCD
weight: 13
---

## multiplier sans le signe `*`

Addition répétée : on ajoute `a` à un total, `b` fois.

```python
def multiplier(a, b):
    resultat = 0
    for _ in range(b):
        resultat += a
    return resultat
```

*Exemple :* `multiplier(6, 4)` &rarr; `6+6+6+6` &rarr; `24`

## diviser sans le signe `/`

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

## PGCD euclide

Le PGCD de `a` et `b` est égal au PGCD de `b` et `a % b`. On répète jusqu'à obtenir un reste nul. Cette méthode repose sur la propriété suivante:

*S'il existe un diviseur commun pour `a` et `b`, alors ce diviseur est aussi commun à `a`, `b` et `a-b`. Donc également à `a%b`:* 

```python
def pgcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
```

*Exemple :* `pgcd(48, 18)` &rarr; `48%18=12` &rarr; `18%12=6` &rarr; `12%6=0` &rarr; PGCD = `6`


## Méthode de Horner
*La factorisation de Horner:*

Supposons que l'on ait à convertir le mot binaire $1110$ en décimal, ou plus généralement $b_0 b_1 b_2 b_3$ en décimal:

\(b_{0}\cdot 2^{3}+b_{1}\cdot 2^{2}+b_{2}\cdot 2^{1}+b_{3}\cdot 2^{0}\)

On peut factoriser par 2 au fur et à mesure :

\(=\left(b_{0}\cdot 2^{2}+b_{1}\cdot 2^{1}+b_{2}\right)\times 2+b_{3}\)
\(=\left(\underline{(b_{0}\times 2+b_{1})}\times 2+b_{2}\right)\times 2+b_{3}\)

On devine la structure de suite recurence pour la suite :
* Le premier bloc souligné \(\underline{(b_{0}\times 2+b_{1})}\), c'est votre étape \(u_{2}\).
* Pour passer à la suite, on prend ce bloc, on le multiplie par 2, et on ajoute le terme suivant. 

C'est exactement la définition de \(u_{n+1} = 2u_n + b_{n+1}\).

On peut alors proposer le programme suivant:

```python
def horner(binaire:str)->int:
    # binaire est un mot binaire du type "1110"
    s = 0
    for bit in binaire:
        s = 2*s + int(bit)
    return s
```

*ou bien*:

```python
def horner_recursif(binaire):
    if binaire=="":
        return 0
    bit = int(binaire[-1])
    return 2*horner_recursif(binaire[:-1]) + bit
```

# Lien
* [TP](../page5)
