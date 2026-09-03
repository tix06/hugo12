---
Title : types simples
description: int, float, str, methodes de chaines string, slice
weight: 4
---




# Les variables et les types natifs en Python

*Cette page apporte des informations sur les types de base, sur les fonctions de la librairie `math`, sur les références, et les méthodes de chaines.*

Cette rubrique contient 4 pages : 

* page 1 : [Cours](../page1/)
* page 2 : [TP1](../page6/)
* page 3 : [TD1](../page8/)


Les types natifs de base, ce sont les types numériques `int` et `float`, le type booléen `bool`, les chaines de caractères `str`, mais aussi le type `None`.

## le type de « rien » : `None`
`None` est la valeur unique du type `NoneType`. Elle représente l'absence de valeur.

```python
type(None)
# affiche <class 'NoneType'>
```

`None` est utile par exemple lorsque l'on veut terminer une fonction sans valeur de retour, ou lorsqu'une fonction ne contient pas d'instruction `return` (c'est alors la valeur de retour implicite) :

```python
def f(x):
  # instructions
  return None
``` 

## le type booléen : `bool`
`bool` est le type des valeurs de vérité : `True` et `False`. C'est le résultat des comparaisons (`==`, `<`, `>=`, ...) et des expressions logiques.

```python
type(True)
# affiche <class 'bool'>
```

*À noter :* en Python, `bool` est un sous-type de `int` : `True` vaut `1` et `False` vaut `0`. C'est pourquoi `True + True` donne `2`.

## Transformer le type des données
Pour consulter le type d'une donnée : fonction `type`:

```python
a = 3
# Créé un objet de type int et lui associe le nom 'a'
type(a) 
# affiche int
``` 

Pour transformer vers un autre type de base, on utilise les fonctions `int`, `float`, `str`:

| transformer x en ... | fonction |
|--- |--- |
| integer | `int(x)` |
| float | `float(x)` |
| string | `str(x)` |

* Exemple: tranformer en `float`:

```python
float(3)
# affiche 3.0
float('3.8')
# affiche 3.8
```

* transformer en `int`
convertit par exemple un flottant en entier en **tronquant** la partie décimale du nombre (attention, ce n'est pas un arrondi) : 

```python
int(3.5)
# affiche 3
int(-3.5)
# affiche -3 (et non -4 : la troncature se fait vers 0)
``` 

ou une chaine de caractères en un entier :

```python
int("3")
# affiche 3
int("3.5")
# ValueError : int() ne convertit que des chaines représentant un entier
```

# Opérations sur les types numériques
Les opérateurs sur les nombres ont été vus dans le cours *Python les bases*.

* Certaines fonctions natives vont enrichir les possibilités de calcul:

*Exemple:* **arrondir** : fonction `round(nombre,decimales)`

    `round(3.1415926,2)` donne `3.14`

* La [bibliothèque **math**](https://docs.python.org/fr/3.5/library/math.html) contient de nombreuses fonctions utiles au calcul scientifique: 

```python
import math
math.sqrt(9)
# affiche 3.0
PI = math.pi
PI
# affiche 3.141592653589793
math.sin(PI/2)
# affiche 1.0
# le sinus de l'angle en radians
math.fabs(-101)
# affiche 101.0
# Renvoie la valeur absolue de (-101), toujours sous forme de float
math.isnan(PI)
# affiche False
math.isnan(float('nan'))
# affiche True
# Renvoie True si x est NaN (Not a Number)
```

*Remarque:* les nombres flottants ont une précision limitée. Par exemple `0.1 + 0.2` n'affiche pas exactement `0.3` mais `0.30000000000000004`, à cause de la façon dont les flottants sont représentés en mémoire (norme IEEE 754). Il faut garder ceci en tête avant de comparer deux flottants avec `==`.

# Opérations sur les booléens - rappels
| operateur | symbole | exemple d'expression | resultat |
| --- | --- |--- | --- |
| intersection | and | True and False | False |
| reunion | or | True or False | True |
| negation | not | not False | True |
| est égal à | == | True == False | False |
| est différent de | != | True != False | True |



# Opérations avec les chaines de caractères
Les opérateurs `+` et `*` sont autorisés dans les expressions avec les chaines de caractère.

Le `+` réalise une *concaténation* de 2 chaines. Le `*` répète et concatène la chaine : 

```python
a, b = 'Alan', 'Turing'
a + b 
# affiche AlanTuring
a * 3
# affiche AlanAlanAlan
```

Les caractères sont *placés* dans une chaine. On peut donc y accéder avec leur *index*, comme pour les Listes:

```python
chaine = 'Hello World'
chaine[0]
# affiche 'H'
chaine[1:4]
# affiche 'ell'
``` 

On peut aussi utiliser des index négatifs (qui comptent depuis la fin de la chaine) et un pas (*step*) dans le slice :

```python
chaine[-1]
# affiche 'd' (dernier caractère)
chaine[::-1]
# affiche 'dlroW olleH' (la chaine inversée)
chaine[0:11:2]
# affiche 'HloWrd' (un caractère sur deux)
```

Mais, contrairement aux Listes, on ne pourra pas modifier un caractère par son index:

```python
chaine[0] = 'P'
# TypeError: 'str' object does not support item assignment
```

En fait, comme `int` et `float`, le type `str` est **immuable** (*immutable*) : une fois créée, une chaine ne peut plus être modifiée en place. Toute méthode qui semble « transformer » une chaine (`upper()`, `replace()`, ...) renvoie en réalité une **nouvelle** chaine.

Une chaine de caractères est *itérable*: On peut la parcourir avec une boucle bornée. Par exemple, le script suivant élimine tous les espaces dans la chaine:

```python
s = "Il fait beau."
res = ""
for carac in s:
  if carac != ' ':
    res = res + carac
print(res)
# affiche Ilfaitbeau.
```

## méthodes de chaines
Les chaines sont des objets qui possèdent leurs méthodes. il est difficile de se souvenir de toutes les méthodes travaillant sur les chaînes de caractères. Aussi il est toujours utile de recourir à la documentation embarquée


```python
help(str)
```

Ce qui donne:

```
Help on class str in module builtins:

class str(object)
 |  str(object='') -> str
 |  str(bytes_or_buffer[, encoding[, errors]]) -> str
 |  
 |  Methods defined here:
 | ...
 |  format(...)
 |      S.format(*args, **kwargs) -> str
 |      
 |      Return a formatted version of S, using substitutions from args and kwargs.
 |      The substitutions are identified by braces ('{' and '}').
 |  ...
 |  join(self, iterable, /)
 |      Concatenate any number of strings.
 |      
 |      The string whose method is called is inserted in between each given string.
 |      The result is returned as a new string.
 |      
 |      Example: '.'.join(['ab', 'pq', 'rs']) -> 'ab.pq.rs'
 | ...
``` 

*Remarque:* pour construire une chaine à partir de valeurs de variables, la syntaxe moderne et recommandée est la **f-string**, plus lisible que `format` ou la concaténation avec `+` :

```python
nom, age = 'Ada', 36
f"{nom} a {age} ans"
# affiche 'Ada a 36 ans'
```


### Découpage - assemblage: `split` et `join`

Les méthodes `split` et `join` permettent de découper une chaîne selon un séparateur pour obtenir une liste, et à l'inverse de reconstruire une chaîne à partir d'une liste.

`split` permet donc de découper :


```python
'abc=:=def=:=ghi=:=jkl'.split('=:=')
# affiche ['abc', 'def', 'ghi', 'jkl']
```

Et à l'inverse :


```python
"=:=".join(['abc', 'def', 'ghi', 'jkl'])
# affiche abc=:=def=:=ghi=:=jkl
```

*Remarque:* Si le séparateur est un terminateur, comme par exemple `;,` ou`\n`, il conviendra d'utiliser d'abord la méthode `strip`. Voir *Compléments* en bas de page.


### Remplacement: `replace`

`replace` est très pratique pour remplacer une sous-chaîne par une autre, avec une limite éventuelle sur le nombre de remplacements :


```python
"abcdefabcdefabcdef".replace("abc", "zoo")
# affiche zoodefzoodefzoodef
"abcdefabcdefabcdef".replace("abc", "zoo", 1)
# affiche zoodefabcdefabcdef (un seul remplacement grâce au 3e argument)
```


### modifier la casse d'une chaine
utiliser les méthodes `title()` (titre), `upper()` (mise en majuscule), `lower()` (minuscule).

```python
nom = 'charles babbage'
nom.title()
# affiche Charles Babbage
nom.upper()
# affiche CHARLES BABBAGE
```

Les méthodes `lstrip()` (à gauche), `rstrip()` (droite), et `strip()` (à droite et à gauche) suppriment les espaces en trop dans les chaines.

> à tester vous-même : 

```python
nom = 'charles babbage'
nom.strip()
```


# Compléments sur les variables et types

## Valeur et référence
Les **variables** en Python sont des **références nommées**.


Une variable est donc une **étiquette** associée à une **valeur**. Ce nom est à peu près quelconque, mais pour l’ordinateur il s’agit d’une **référence** désignant une **adresse mémoire**, c’est-à-dire un emplacement précis dans la mémoire vive.

À cet emplacement est stockée une **valeur typée** bien déterminée.

{{< img src="../images/var_normalesup1.png" link="http://www.normalesup.org/~doulcier/teaching/python/01_variables.html" width="300" caption="image issue du cours sur http://www.normalesup.org/" >}}
Cette valeur peut être en fait à peu près n’importe quel « objet » susceptible d’être placé dans la mémoire d’un ordinateur, par exemple : un nombre entier, un nombre réel, un nombre complexe, un vecteur, une chaîne de caractères, un tableau, une fonction, etc.

Le programme suivant permet de consulter l'adresse mémoire d'une variable:

```python
a = 3
# Créer un objet de type int et lui associe le nom 'a'
type(a) #=> int
# Cet objet se trouve dans la mémoire de l'ordinateur
# à un endroit que l'on peut obtenir avec `id`:
id(a) #=> La position de l'objet nommé a dans la mémoire de l'ordinateur.
# Affiche
94875962855936
```

*Pour aller plus loin :* deux noms peuvent référencer le **même** objet en mémoire. L'opérateur `==` compare les **valeurs**, alors que l'opérateur `is` compare les **références** (l'identité, donc le résultat de `id`) :

```python
a = [1, 2, 3]
b = [1, 2, 3]
a == b   # True : mêmes valeurs
a is b   # False : deux objets distincts en mémoire
c = a
c is a   # True : c et a référencent le même objet
```

## Typage dynamique
Python est un langage à typage dynamique, ce qui signifie qu'il n'est pas necessaire de déclarer le type de donnée que représentera une variable (c'est la différence avec le typage *statique*). C'est l'interpréteur qui examine la donnée tout au long de la vie du programme et choisit le type.



## Affectation simple et multiple
**Affectation simple :**

Les termes « affecter une valeur » ou « assigner une valeur » à une variable sont équivalents. Ils désignent l’opération par laquelle on établit un lien entre le nom de la variable et sa valeur (son contenu).

*Exemple :* `a = 2` 

Lorsque l'ordinateur execute cette instruction, il va : 

* créer et mémoriser un nom de variable ;
* lui attribuer un type bien déterminé (ce point sera explicité à la page suivante);
* créer et mémoriser une valeur particulière;
* établir un lien (par un système interne de pointeurs) entre le nom de la variable et l’emplacement mémoire de la valeur correspondante.

Le nom d'une variable est une référence, mémorisée dans une zone particulière de la mémoire que l’on appelle espace de noms, alors que la valeur correspondante est située ailleurs.

**Affectation multiple :**

Il est possible de réaliser une affectation pour plusieurs variables d'un seul coup : 
```python
a, b, c = 3, True, 'hello'
b
# affiche True
```



# Compléments sur les strings
## `strip` ou `split` 
Si le séparateur est un terminateur, comme par exemple `;,` ou`\n`, la liste résultat contient alors une dernière chaîne vide. En pratique, on utilisera la méthode `strip`, que nous allons voir ci-dessous, avant la méthode `split` pour éviter ce problème.


```python
"abc;def;ghi;jkl;".split(';')
# retourne ['abc', 'def', 'ghi', 'jkl', '']
# le dernier element de la liste est ''
```

alors que:

```python
"abc;def;ghi;jkl;".strip(';')
# retourne abc;def;ghi;jkl
# on a supprime le dernier ';'
# on peut alors utiliser la methode split:
"abc;def;ghi;jkl;".strip(';').split(';')
# retourne ['abc', 'def', 'ghi', 'jkl']
```

## PARSER une chaine de caractères
"Parser" signifie analyser et convertir un script en un format interne que l'environnement d'exécution peut interpréter. Il s'agit d'une [analyse syntaxique](https://developer.mozilla.org/fr/docs/Glossary/Parse).

Soit la chaine de caractères suivante, issue d'une requête HTTP:

```
'GET /search ville=nice UTC=12'
```

On souhaite stocker dans 4 variables différentes les informations séparées chacune par des espaces ' '.

### méthode utilisant un slide

```python
c = 'GET /search ville=nice UTC=12'
C1 = c[:3]
print(C1)
# GET
C2 = c[4:11]
print(C2)
# /search
C3 = c[12:22]
print(C3)
# ville=nice
C4 = c[23:]
print(C4)
# UTC=12
```

### méthode utilisant une boucle non bornée
On ne connait pas à priori les positions des séparateurs dans la chaine (les espaces ' '). On peut faire une recherche en parcourant la chaine du premier au dernier caractère avec l'instruction `while i < len(c):
    caract = c[i] ...`
    
```python
i=0
caract = c[i]

# recherche des espaces dans la chaine c
while i < len(c):
    caract = c[i]
    if caract == ' ':
        print(i)
    i = i + 1
# affiche les index tels que c[i] == ' '
# 3
# 11
# 22
```

Les séparateurs se trouvent aux indices 3, 11, et 22. On sait alors que les 4 informations de la chaines sont:

```python
C1 = c[:3]
C2 = c[4:11]
C3 = c[12:22]
C4 = c[23:]
```

### méthode split
La méthode la plus adaptée pour réaliser le *parsing* d'une chaine, c'est:

```python
c.split(' ')
# retourne les elements dans une liste
# ['GET', '/search', 'ville=nice', 'UTC=12']
```

# Suite

##### {{% button href="../page1" icon="bullhorn" style="caution" %}}Cours{{% /button %}} 
##### {{% button href="../page6" icon="palette" style="tip" %}}TP1{{% /button %}} Types simples
##### {{% button href="../page8" icon="palette" style="important" %}}TD1{{% /button %}} Variables et types natifs


# Liens
<!--* Lien vers les [Flash cards](../ex1) sur les variables et séquences-->
* Compléments: valeur, references, espace de nom: [Lien vers le cours de normalesup](http://www.normalesup.org/~doulcier/teaching/python/01_variables.html)
