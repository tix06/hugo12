---
Title : types construits
description: listes, tuples, dictionnaires, méthodes
weight: 7
---

  


Cette page aborde les notions avancées sur les types construits (listes, tuples, dictionnaires). Il peut être nécessaire de consulter les *notions de base* sur les : [listes](/python_bases/boucles/page2/).


Après la lecture, on traitera le [TP sur les variables](../page3/) utilisant *Pythontutor*.

# Les structures de données et les types construits
Les *structures de données* définissent la manière avec laquelle sont stockées les données dans un langage.

Les types construits, comme les listes et les dictionnaires sont *construits* à partir des types de bases que l'on a déjà vus. Ce sont d'autres moyens d'organiser et d'agencer les types de base dans d'autres structures.

Les types construits peuvent stocker d'autres types construits.


On distingue les **types séquentiels** (liste, tuple et string) des **mappages** (dictionnaires).

Une *séquence* est une structure de données qui stocke une collection d'éléments dans un ordre déterminé. On accède aux éléments par leur indice (leur rang dans la séquence). 

Pour les *mappages*, il s'agit d'une collection de type *clé:valeur*. On accède à une valeur par sa *clé*.

# Listes
**Definition:** Une **liste** est une **collection ordonnée d'objets**. Au niveau de la mémoire de l'ordinateur, une liste *porte un nom*, et fait *référence à des espaces mémoire* pour chaque *élément* de liste. Ces éléments (espaces mémoires) font eux-mêmes référence aux *emplacements mémoire* qui *stockent les valeurs* ou *objets*.


En python: Une **liste** est entourée de **crochets** `[ ]`

Les éléments contenus peuvent être de tout type.

On accède à un élément d'une liste grâce à sa position, appelée *indice*. Le premier élément a pour indice zero. 

{{< img src="../images/liste.png" caption="La liste `voyelles` est une collection contenant les caractères" >}}

Un indice négatif donne accès à la liste à partir du dernier élément.

## Construire une liste
### Construire une liste de manière directe.

```python
voyelles = ['e','i','o']
voyelles[0]
# affiche 'e'
voyelles[-1]
# affiche 'o'
voyelles[-2]
# affiche 'i'
voyelles
# affiche ['e', 'i', 'o']
```

**Modifier un élément de liste**:

Les listes sont **mutables** : On peut modifier un seul de ses éléments à partir de son indice : 
```python
voyelles[2] = 'y'
voyelles
# affiche ['e', 'i', 'y']
```

Ceci n'est pas possible avec le type natif `str`, qui, lui, est un type **non mutable**.

### Construire une liste avec une boucle (accumulation)
Les boucles `while` et`for` permettent d’itérer sur les éléments d’une séquence.

```python
# Boucle while
squares = []
i = 0
while i <= 100:
  squares.append(i ** 2)
  i += 1

# Boucle for
squares = []
for i in range(101):
  squares.append(i ** 2)
```

### Construire une liste par compréhension
Pour construire une liste par compréhension, on place une boucle bornée à l'INTERIEUR des crochets. Cela crée un élément dans la liste pour chaque valeur de l'itérable.

```python
# Définition par compréhension
squares = [i ** 2 for i in range(10)]
squares
# affiche [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```



On peut combiner les expressions entre les crochets, en ajoutant par exemple une condition. Ainsi, si l'on veut uniquement le carré des nombres pairs (`if i % 2 == 0`):

```python
# carre des nombres pairs
squares = [i ** 2 for i in range(101) if i % 2 == 0]
```

Pour construire un tableau à deux dimensions (une liste de listes), on peut imbriquer deux compréhensions de liste:

```python
M = [[0 for j in range(3)] for i in range(3)]
M
# affiche [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
``` 

## Méthodes de listes


Pour commencer, rappelons comment retrouver la liste des méthodes définies sur le type `list` :

```python
help(list)
```

### append
**append(element)** ajoute un élément en fin de liste
```python
aeroports = ['CDG','ORY','LIS']
aeroports.append('NY')
aeroports
# affiche ['CDG', 'ORY', 'LIS', 'NY']
```
### pop
**pop()** supprime le dernier élément et renvoie sa valeur.
```python
aeroports = ['CDG','ORY','LIS','NY']
aeroports.pop()
# affiche 'NY'
aeroports
# affiche ['CDG', 'ORY', 'LIS']
```

### index
**index(element)** retourne la position (index) de cet élément dans la liste (ou du moins la première occurence s'il y en a plusieurs).

```python
aeroports = ['CDG','ORY','LIS','NY']
aeroports.index('ORY')
# retourne 1
```

### insert
**insert(index, element)** insère l'élément à l'index précisé.

```python
aeroports = ['CDG','ORY','LIS','NY']
aeroports.insert(2,'LCY')
# la liste aeroports est alors
# ['CDG', 'ORY', 'LCY', 'LIS', 'NY']
```

### remove et del
**remove(element)** supprime un élément d'une liste. Si l'élément apparait plusieurs fois dans la liste, seule la premiere occurence est supprimée.

**del liste[indice]** supprime l'élément de la liste à partir de son indice.

```python
aeroports = ['CDG','ORY','LIS','NY']
aeroports.remove('LIS')
aeroports
# affiche ['CDG', 'ORY', 'NY']
del aeroports[0]
aeroports
# affiche ['ORY', 'NY']
```

### extend
**extend(list)** est une méthode utile pour ajouter les éléments d'une autre liste, à la fin:

```python
L1 = ['lundi','mardi']
L2 = ['mercredi','jeudi']
L1.extend(L2)
print(L1)
# affiche ['lundi', 'mardi', 'mercredi', 'jeudi']
```

### reverse
**reverse()** est une méthode qui renverse la liste (en place, renvoie None)

```python
L1.reverse()
print(L1)
# affiche ['jeudi', 'mercredi', 'mardi', 'lundi']
```

## Autres manipulations de listes
### découpe d'une liste
une *découpe* est une partie de liste, spécifiée à partir des indices : 

```python
etats = ['CH','GB','NL','PL','RO','SK']
etats[2:4]
# affiche ['NL', 'PL']
etats[:2] # sans specifier le premier indice
# affiche ['CH', 'GB'] # commence au début
etats[3:] # sans specifier l'indice de fin
# affiche ['PL', 'RO', 'SK'] # jusqu'à la fin
```
### copie d'une liste
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
mes_etats = list(etats) # liste copiée par valeur dans mes_etats
```
On peut alors vérifier qu'il s'agit maintenant d'une copie par valeurs :

```python
mes_etats.append('DK')
mes_etats
# affiche ['CH', 'GB', 'NL', 'PL', 'DK']
etats
# affiche ['CH', 'GB', 'NL', 'PL']
```

Sans cette *astuce*, la copie se ferait par **référence** (*rappelez-vous: Liste = mutable*)

### Trier une liste
Il y a 2 fonctions de tri : 

* La fonction **sorted** renvoie une copie de la liste triée dans l'ordre croissant (numérique pour des nombres, alphabétique pour des chaînes) sans modifier la liste d'origine.

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


### Choix d'un élément aléatoire dans une liste.

Il faut importer la fonction `choice` de la librairie `random`:

```python
from random import choice
L = [1, 10, 100, 1000]
print(choice(L))
```

Affiche un élément au hasard: 1, 10, 100 ou 1000.


# Tuples
Un *tuple* est entouré de **parenthèses** `( )`

On accède à l'un des éléments à l'aide de son indice, comme pour les listes.

Par contre, le tuple est **non mutable** : on ne peut pas en modifier l'un de ses éléments. Il faut refaire, au besoin, une affectation complète de tout le tuple.

```python
elementaire = ('CP','CE1','CE2')
elementaire[1]
# affiche 'CE1'
elementaire[2] = 'CM2'
# TypeError: 'tuple' object does not support item assignment
elementaire = ('CP','CE1','CM2')
elementaire
# affiche ('CP', 'CE1', 'CM2')
``` 

**Non mutable** mais avec des éléments **mutables**:

```python
t = (0, [1, 2])
t[1].append(3)
print(t) 
# Affiche (0, [1, 2, 3]) ← le tuple n'a pas changé, mais son contenu change
```

L'immuabilité du tuple garantit que ses références ne changent pas, pas que les objets
référencés sont eux-mêmes figés.

# Mappages : les dictionnaires
Un *mappage* est une structure de données qui relie 2 informations ou plus, appelées *paires clé : valeur*. Aussi appelée *table de hashage*. En python, cette structure est le dictionnaire.

Un dictionnaire est entouré d'*accolades* `{ }`. Les paires sont séparées par une virgule.

## Création d'un dictionnaire

```python
dic = {}     # creer un dictionnaire vide
dic = dict() # Variante
dic = {"nom": "Alice", "âge": 30} # Création d'un dictionnaire déjà peuplé
```

Par exemple, pour créer un dictionnaire non vide, on peut faire : 

```python
capitales = {'France':'Paris','Italie':'Rome','Allemagne':'Berlin'}
``` 
Mais on peut aussi ajouter chaque paire en faisant :

```python
capitales = {} # dictionnaire vide
capitales['France'] = 'Paris' # creation ou ajout du couple 'France':'Paris'
print(capitales)
# affiche {'France': 'Paris'}
capitales['Italie'] = 'Rome'
print(capitales)
# affiche {'France': 'Paris', 'Italie': 'Rome'}
```

Dans cet exemple, les clés du dictionnaire `capitales` sont les pays ("France", "Italie"...) et les valeurs sont les villes ("Paris","Rome",...).

On ne peut placer comme clé d'un dictionnaire que des objets de type **non mutable** (on dit qu'ils doivent être *hashables*).

## Accéder au contenu du dictionnaire
Pour les exemples qui suivent, on part de :

```python
capitales = {'France': 'Paris', 'Italie': 'Rome'}
```

### Une valeur associée à une clé
Pour accéder à une *valeur*, on utilise la clé comme index: 

```python
print(capitales['France'])
# affiche 'Paris'
```

### Toutes les clés
Pour accéder **aux clés** d'un dictionnaire: on utilisera la méthode `keys` avec par exemple `capitales.keys()`

```python
for pays in capitales.keys():
  print(pays)
# affiche
# France
# Italie
print(capitales.keys())
# affiche dict_keys(['France', 'Italie'])
```

ou bien, avec une version plus courte:

```python
for pays in capitales:
  print(pays)
# affiche
# France
# Italie
```

### Toutes les valeurs
Pour accéder **aux valeurs**: on utilise la méthode `values`, avec par exemple `capitales.values()`

```python
for ville in capitales.values():
  print(ville)
# affiche
# Paris
# Rome
print(capitales.values())
# affiche dict_values(['Paris', 'Rome'])
```

### Tous les items clé:valeur
Pour accéder **aux paires clé-valeurs**: méthode `items`, avec par exemple `capitales.items()`

```python
for pays, ville in capitales.items():
  print(pays, ville)
# affiche
# France Paris
# Italie Rome
print(capitales.items())
# affiche dict_items([('France', 'Paris'), ('Italie', 'Rome')])
```

*Dans ce dernier exemple:*

* l'iterable `capitales.items()` donne un nouveau tuple à chaque itération.
* on déclare 2 variables `pays` et `ville`, qui permettent de destructurer le tuple, et récupérer le pays dans `pays` et la ville dans `ville`.

### Modifier le contenu
**Ajouter** puis **modifier** un couple clé:valeur:

*Exemple complet:*

```python
capitales = {'France':'Paris'}
capitales['Italie'] = 'Rome'      # ajouter
capitales['Egypte'] = 'Alexandrie'# ajouter
print(capitales)
# affiche {'France': 'Paris', 'Italie': 'Rome', 'Egypte': 'Alexandrie'}
capitales['Egypte'] = 'Le Caire'  # modifier
print(capitales)
# affiche {'France': 'Paris', 'Italie': 'Rome', 'Egypte': 'Le Caire'}
```

**Supprimer un couple: `del`**

```python
del capitales['Egypte']
print(capitales)
# affiche {'France': 'Paris', 'Italie': 'Rome'}
```

### Appartenance

```python
key in dic # Renvoie True ou False, selon que key est ou non une cle
val in dic.values() # Renvoie True ou False, selon que val est ou non une valeur
```

## Copier un dictionnaire
On peut utiliser la fonction `dict` pour faire une copie par *valeur* d'un dictionnaire : 

```python
mes_capitales = dict(capitales)
```

Sans cette *astuce*, la copie se ferait par **référence** (Dictionnaire = mutable)








# Objets mutables et non mutables
En Python, il existe deux types d’objets: les **mutables** (listes, dictionnaires, sets, objets customisés) et les **non mutables** (string, int, float, bool, tuple, None).

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

*Exemple: lire et essayer de modifier*

```python
vies = 3

def lire():
    print(vies)
    
def modifier():
    vies=vies-1
    print(vies)
    
> lire()
3
> modifier()
UnboundLocalError: local variable 'vies' referenced before assignment
```

*Exemple: lire et modifier en utilisant l'instruction `global`*

```python
vies = 3

def lire():
    print(vies)
    
def modifier():
    global vies
    vies=vies-1
    print(vies)
    
> lire()
3
> modifier()
2
```

# Suite
##### {{% button href="../page2" icon="bullhorn" style="caution" %}}Cours{{% /button %}} 
##### {{% button href="../page9" icon="palette" style="tip" %}}TP2{{% /button %}} decouverte du cours
##### {{% button href="../page3" icon="palette" style="important" %}}TD2a{{% /button %}} les types construits, les copies par valeur et reference sur Pythontutor
##### {{% button href="../page4" icon="palette" style="important" %}}TD2b{{% /button %}} le parcours de liste, compréhension de liste et tracé graphique
##### {{% button href="../page5" icon="palette" style="tip" %}}TP3{{% /button %}} les tableaux