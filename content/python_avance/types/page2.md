---
Title : types construits
description: listes, dictionnaires, méthodes
weight: 5
---

  


Cette page aborde les notions avancées sur les Listes. Il est nécessaire de consulter auparavant la page sur les Listes: [les notions de base](/docs/python/pages/boucles/page2/).

On pourra également revenir sur la page 1 : [variables natives de base](../page1/)

Après la lecture, on traitera le [TP sur les variables](../page3/) utilisant *Pythontutor*.

# Les structures de données et les types construits
Les *structures de données* définissent la manière avec laquelle sont stockées les données dans un langage.

Les types construits, comme les listes et les dictionnaires sont *contruits* à partir des types de bases que l'on a déjà vus. Ce sont d'autres moyens d'organiser et d'agencer les types de base dans d'autres structures.


# Types séquentiels : les listes et les tuples
Une séquence est une structure de données qui stocke une collection d'éléments dans un ordre déterminé.
## Listes
**Definition:** Une **liste** est une **collection ordonnée d'objets**. Au niveau de la mémoire de l'odinateur, une liste *porte un nom*, et fait *référence à des espaces mémoire* pour chaque *élément* de liste. Ces éléments (espaces mémoires) font eux-même reference aux *emplacement mémoire* qui *stockent les valeurs* ou *objets*.


En python: Une **liste** est entourée de **crochets** `[ ]`

Les éléments contenus peuvent être de tout type.

On accède à un élément d'une liste grace à sa position, appelée *indice*. Le premier élément a pour indice zero. 

{{< img src="../images/liste.png" caption="La liste `voyelles` est une collection contenant les caractères" >}}

Un indice négatif donne accès à la liste à partir du dernier élément.

```python
voyelles = ['e','i','o']
voyelles[0]
# affiche e
voyelles[-1]
# affiche o
voyelles
# affiche ['e','i','o']
```
Les listes sont **mutables** : On peut modifier un seul de ses éléments à partir de son indice : 
```python
voyelles[2] = 'y'
voyelles
# affiche ['e','i','y']
```

Ceci n'est pas possible avec le type natif `str`, qui, lui est un type **non mutable**.

### Construire une liste avec une boucle
Les boucles `while` et`for` permettent d’itérer sur les éléments d’une séquence.

```python
# Boucle while
squares = []
i = 0
while i <= 100:
  squares.append (i ** 2)
  i += 1

# Boucle for
squares = []
for i in range (101) :
  squares.append (i ** 2)
```

### Construire une liste par compréhension
Pour construire une liste par compréhension, on place une boucle bornée à l'INTERIEUR les crochets. Cela créé un éléments dans la matrice pour chaque valeur de l'itérable

```python
# Définition par compréhension
squares = [i ** 2 for i in range (10) ]
squares
# affiche [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```



On peut combiner les expressions entre les crochets, en ajoutant par exemple une condition. Ainsi, si l'on veut uniquement le carré des nombres pairs (`if i % 2 == 0`):

```python
# carre des nombres pairs
squares = [i ** 2 for i in range (101) if i % 2 == 0]
```

Pour un tableau, on peut créer une liste par compréhension à l'intérieur de la première liste:

```python
M = [[0 for j in range(3)] for i in range(3)]
M
# affiche [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
``` 

## Tuples
Un *tuple* est entouré de **parenthèses** `( )`

On accède à l'un des éléments à l'aide de son indice, comme pour les listes.

Par contre, le tuple est **non mutable** : on ne peut pas en modifier l'un de ses éléments. Il faut refaire, au besoin, une affectation complète de tout le tuple.

```python
elementaire = ('CP','CE1','CE2')
elementaire[1]
# affiche CE1
elementaire[2] = 'CM2'
# affiche TypeError
elementaire = ('CP','CE1','CM2')
elementaire
# affiche ('CP','CE1','CM2')
``` 

# Mappages : les dictionnaires
Un *mappage* est une structure de données qui relie 2 informations ou plus, appelées *paires clé : valeur*. Aussi appelée *table de hashage*. En python, cette structure est le dictionnaire.

Un dictionnaire est entouré d'*accolades* `{ }`. Les paires sont séparées par une virgule.

Par exemple, pour créer un dictionnaire non vide, on peut faire : 
```python
capitales = {'France':'Paris','Italie':'Rome','Allemagne':'Berlin'}
``` 
Mais on peut aussi ajouter chaque paire en faisant :
```python
capitales = {} # dictionnaire vide
capitales['France'] = 'Paris'
capitales
# affiche {'France': 'Paris'}
```

Dans cet exemple, les clés du dictionnaire `capitales` sont les pays ("France", "Italie"...) et les valeurs sont les villes ("Paris","Rome",...).

On ne peut placer comme clé d'un dictionnaire que des objets de type **non mutable**.

Pour accéder à une *valeur*, on utilise la clé comme index: `capitales['France'] = 'Paris'`

Pour accéder **aux clés** d'un dictionnaire: on utilisera les méthodes `keys` avec par exemple `capitales.keys()`

```python
for pays in capitales.keys():
  print(pays)
```

Pour accéder **aux valeurs**: on utilise la méthode `value`, avec par exemple `capitales.values()`

```python
for ville in capitales.values():
  print(ville)
```

Pour accéder **aux paires clé-valeurs**: méthode `items`, avec par exemple `capitales.items()`

```python
for pays,ville in capitales.items():
  print(pays,ville)
```


# méthodes de listes


Pour commencer, rappelons comment retrouver la liste des méthodes définies sur le type `list` :

```python
help(list)
```

## append
**append(element)** ajoute un élément en fin de liste
```python
aeroports = ['CDG','ORY','LIS']
aeroports.append('NY')
aeroports
# affiche ['CDG','ORY','LIS','NY']
```
## pop
**pop()** supprime le dernier élément et renvoie sa valeur.
```python
aeroports = ['CDG','ORY','LIS','NY']
aeroports.pop()
# affiche 'NY'
aeroports
# affiche ['CDG','ORY','LIS']
```

## index
**index(element)** retourne la position (index) de cet élément dans la liste (ou du moins la première occurence s'il y en a plusieurs).

```python
aeroports = ['CDG','ORY','LIS','NY']
aeroports.index('ORY')
# retourne 1
```

## insert
**insert(index, element)** insère l'élément à l'index précisé.

```python
aeroports = ['CDG','ORY','LIS','NY']
aeroports.insert(2,'LCY')
# la liste aeroport est alors
# ['CDG','ORY', 'LCY', LIS','NY']
```

## remove et del
**remove(element)** supprime un élément d'une liste. Si l'élément apparait plusieurs fois dans la liste, seule la premiere occurence est supprimée.

**del liste[indice]** supprime l'élément de la liste à partir de son indice.

```python
aeroports = ['CDG','ORY','LIS','NY']
aeroports.remove('LIS')
aeroports
# affiche ['CDG','ORY','NY']
del aeroports[0]
aeroports
# affiche ['ORY','NY']
```
## découpe d'une liste
une *découpe* est une partie de liste, spécifiée à partir des indices : 
```python
etats = ['CH','GB','NL','PL','RO','SK']
etats[2:4]
# affiche ['NL','PL']
etats[:2] # sans specifier le premier indice
# affiche ['CH','GB'] # commence au debut
etats[3:] # sans specifier l'indice de fin
# affiche ['PL','RO','SK'] # jusqu'à la fin
```
## copie d'une liste
Une *copie* d'une liste permet d'utiliser le contenu de la liste copiée sans affecter la liste d'origine (voir [TP sur les variables](../page3/)). C'est une copie par *valeurs*.

Pour copier une liste, on peut : 

* la découper sans mentionner les 2 indices:

```python
etats = ['CH','GB','NL','PL']
mes_etats = etats[:] # liste copiée par valeur dans mes_etats
``` 
* ou bien utiliser la fonction `list`: 

```python
etats = ['CH','GB','NL','PL']
mes_etats = etats[:] # liste copiée par valeur dans mes_etats
mes_etats = list(etats)
```
On peut alors vérifier qu'il s'agit maintenant d'une copie par valeurs :

```python
mes_etats.append('DK')
mes_etats
# affiche ['CH','GB','NL','PL','DK']
etats
# affiche ['CH','GB','NL','PL']
```

Sans cette *astuce*, la copie se ferait par **référence** (*rappelez-vous: Liste = mutable*)

## Trier une liste
Il y a 2 fonctions de tri : 

* La fonction **sorted** renvoie une copie de la liste triée dans l'ordre naturel (alphanumerique) sans modifier la liste d'origine.

```python
L = [9, 5, 1, 3, 4]
sorted(L)
# affiche [1, 3, 4, 5, 9]
```

Puis:

```python
L
# affiche [9, 5, 1, 3, 4]
```

* La méthode **sort** permet de trier la liste en place.

```python
L = [9, 5, 1, 3, 4]
L.sort()
# L est transformee en
# [1, 3, 4, 5, 9]
```


## Choix d'un élément aléatoire dans une liste.

Il faut importer la fonction `choice` de la librairie `random`:

```python
from random import choice
L = [1, 10, 100, 1000]
print(choice(L))
```

Affiche un élément au hasard: 1, 10, 100 ou 1000.

# méthodes de dictionnaires
Les dictionnaires sont présentés à la page sur les [variables](/docs/python/pages/variables/page1/#mappages-les-dictionnaires)

## keys
méthode qui permet d'accéder aux clés d'un dictionnaire (retourne une liste de clés) :
```python
capitales = {'France':'Paris','Italie':'Rome','Allemagne':'Berlin'}
capitales.keys()
# affiche dict_keys(['France', 'Italie', 'Allemagne'])
``` 
## values
méthode pour accéder aux valeurs d'un dictionnaire (retourne une liste de valeurs):
```python
capitales = {'France':'Paris','Italie':'Rome','Allemagne':'Berlin'}
capitales.values()
# affiche dict_values(['Paris', 'Rome', 'Berlin'])
```
## items
méthode pour accéder aux paires clé-valeurs d'un dictionnaire (retourne une liste de tuples):

```python
capitales = {'France':'Paris','Italie':'Rome','Allemagne':'Berlin'}
capitales.items()
# affiche dict_items([('France', 'Paris'), ('Italie', 'Rome'), ('Allemagne', 'Berlin')])
```

## copier un dictionnaire
On peut utiliser la fonction `dict` pour faire une copie par *valeur* d'un dictionnaire : 

```python
mes_capitales = dict(capitales)
```

Sans cette *astuce*, la copie se ferait par **référence** (Dictionnaire = mutable)


# Dataframes
Un Dataframe est un objet qui permet de mieux représenter et travailler sur les tables. C'est un outil puissant, qui necessite un apprentissage supplémentaire, comme une extension du langage python. Voir ici : [towardsdatascience.com](https://towardsdatascience.com/pandas-ground-zero-selection-and-projection-3827f74ae6c5)

# Objets mutables et non mutables
En Python, il existe deux types d’objets: les **mutables** (listes, dictionnaires, sets, objets customisés, etc) et les **non mutables** (string, int, float, tuple, etc).

Les **mutables** sont ceux qu’on peut modifier après leur création. Les non mutables sont ceux qu’on ne peut pas modifier après création.

Lorsque 2 références **pointent sur le même objet**, ce qui est possible avec les mutables, il faut s'attendre à ce que la modification de l'un entraine celle de l'autre (effet de bord).

C'est le mot-clé `IS` qui va permettre de tester si 2 noms pointent vers la même réference en mémoire:

```python
x = ["apple", "banana", "cherry"]
y = ["apple", "banana", "cherry"]
x == y
# affiche True
x is y
# affiche False
``` 

Pour plus de précisions sur ces différences, voir le [TP utilisant Pythontutor](../page3/)

### Portée des variables
Un **effet de bord** est une modification d'une variable qui affecte l'état du programme en dehors de la fonction où elle a lieu. Cela peut arriver avec des variables globales, déclarées en dehors de toute fonction.

Pour une variable `x` non mutable, déclarée dans le corps du programme, celle-ci peut être lue dans une fonction où elle n'a pas été definie. Par contre, pour la modifier dans cette fonction, il faudra la déclarer avec `global x` dans cette fonction.

# Suite
* TP sur les types construits, les copies par valeur et reference sur [Pythontutor](../page3/)

* TP sur le parours de liste, compréhension de liste et tracé graphique: [Lien](../page4/)

* TP sur les tableaux: [Lien](../page6/)



