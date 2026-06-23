---
Title: algo et recursivite
description: recherche dichotomique, complexité, récursivité
weight: 65
---

# Sujet Métropole Sept 1 : 2021 - Exercice 2

*Principaux thèmes abordés : algorithmique (recherche dichotomique) et langages et programmation (récursivité)*

{{% badge icon="star" %}}dichotomie{{% /badge %}} {{% badge icon="star" %}}récursivité{{% /badge %}} {{% badge icon="star" %}}complexité{{% /badge %}}

On veillera à mettre sur la copie toutes les réponses.

## Partie A : La recherche dichotomique
**1.** La recherche d’un élément dans un tableau avec une méthode dichotomique ne peut se faire que si le tableau est trié.

*a.* Vrai

*b.* Faux

**2.** Le coût d’un algorithme de recherche dichotomique est :

*a.* Constant : Complexité O(1)

*b.* Linéaire : Complexité O(n)

*c.* Logarithmique : Complexité O(log(n))

**3.** Justifier pourquoi l’entier `fin–deb` est un *variant de boucle* qui montre la
terminaison du programme de recherche dichotomique de l’annexe 1 de l’exercice 2.

## Partie B : La recherche dichotomique itérative
Le programme de recherche dichotomique de l’annexe 1 de l’exercice 2 est utilisé pour effectuer des recherches dans une liste.

Dans l’ensemble de cette partie, on considère la liste : 

`Lnoms = ["alice", "bob","etienne", "hector", "lea", "nathan", "paul"]`.

**1.** Expliquer pourquoi en ligne 2, on a «`fin = len(liste)-1`» plutôt que «`fin = 6`».

**2.** En Python, l’opérateur `//` donne le quotient de la division euclidienne de deux nombres entiers. Proposer un algorithme pour obtenir ce quotient.

**3.** Donner la trace complète de l’exécution `rechercheDicho("lea", Lnoms)` en
complétant le tableau ci-dessous sur votre copie :

| Debut | Fin | M | condition  deb <= fin| valeur renvoyée |
|--- |--- |--- |--- |--- |
|  |  |  | |  |

**4.** Sur votre copie, modifier le code du corps de la fonction `rechercheDicho()` pour qu’elle renvoie aussi la position *(indice)* de l’élément cherché ou **-1** si l’élément n’est pas trouvé.

On pourra indiquer sur la copie le numéro des lignes modifiées, à supprimer ou à
insérer s’il y a lieu.

## Partie C : La recherche dichotomique récursive
**1.** Donner la définition d’une fonction récursive en programmation.

**2.** Écrire en langage naturel ou en python, l’algorithme de recherche dichotomique d’un élément dans une liste, triée de façon croissante, en utilisant une méthode récursive.
Il renverra `True` si l’objet a été trouvé, `False` sinon.

## ANNEXE 1
On considère la fonction de recherche dichotomique suivante : 

```python
def rechercheDicho (elem, liste):
  """
  Cette fonction indique si un élément se trouve dans un
  tableau.
  Elle utilise la méthode de recherche dichotomique.
  Elle prend en arguments :
  - elem : élément à rechercher de type string
  - liste : liste d'éléments de type string triée
  par ordre croissant
  Elle renvoie un booléen correspondant à la présence ou
  non de l'élément
  """
  deb = 0
  fin = len(liste)-1
  m = (deb+fin)//2
  while deb <= fin :
    if liste[m] == elem :
      return True
    elif liste[m] > elem :
      fin = m-1
    else :
      deb = m+1
    m = (deb+fin)//2
  return False 
```

# Sujet Métropole Sept 2 2021 Exercice 4
Cet exercice porte sur la programmation en général et la récursivité en particulier.
{{% badge icon="star" %}}tableau{{% /badge %}} {{% badge icon="star" %}}permutation{{% /badge %}} {{% badge icon="star" %}}récursivité{{% /badge %}}

On s’intéresse dans cet exercice à un algorithme de mélange des éléments d’une liste.

1. Pour la suite, il sera utile de disposer d'une fonction echange qui permet d'échanger dans une liste lst les éléments d'indice `i1` et `i2`.
Expliquer pourquoi le code Python ci-dessous ne réalise pas cet échange et en proposer une modification.

```python
def echange(lst, i1, i2):
 lst[i2] = lst[i1]
 lst[i1] = lst[i2]
```

2. La documentation du module random de Python fournit les informations ci-dessous concernant la fonction `randint(a,b)` :

```
Renvoie un entier aléatoire N tel que a <= N <= b. 
```

Parmi les valeurs ci-dessous, quelles sont celles qui peuvent être renvoyées par l'appel `randint(0, 10)` ?

```
0   1   3.5   9   10  11
```

3. Le mélange de Fischer Yates est un algorithme permettant de permuter
aléatoirement les éléments d'une liste. On donne ci-dessous une mise en œuvre récursive de cet algorithme en Python. 

```python
from random import randint

def melange(lst, ind):
  print(lst)
  if ind > 0:
    j = randint(0, ind)
    echange(lst, ind, j)
    melange(lst, ind-1) 
```

a. Expliquer pourquoi la fonction melange se termine toujours.

b. Lors de l’appel de la fonction melange, la valeur du paramètre `ind` doit être égale au plus grand indice possible de la liste `lst`.

Pour une liste de longueur `n`, quel est le nombre d'appels récursifs de la fonction melange effectués, sans compter l’appel initial ?

c. On considère le script ci-dessous :

```python
lst = [v for v in range(5)]
melange(lst, 4)
```

On suppose que les valeurs successivement renvoyées par la fonction
`randint` sont 2, 1, 2 et 0.

Les deux premiers affichages produits par l'instruction `print(lst)` de la fonction melange sont :

```python
[0, 1, 2, 3, 4]
[0, 1, 4, 3, 2]
```

Donner les affichages suivants produits par la fonction melange.

d. Proposer une version itérative du mélange de Fischer Yates. 
