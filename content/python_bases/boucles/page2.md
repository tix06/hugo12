---
Title: listes
description: cours, parcours de liste, méthodes de liste, boucles bornées, tracé de graphique
weight: 9
---


  
# Chaines de caractères, Listes et Boucles bornées
## Chaines de caractères
**1. Definition:** Une chaine de caractère est une séquence ordonnée de caractères, mis entre guillements  (simples `'` ou doubles `"`). C'est le type `str` en python. Pour en savoir plus sur les chaines, on pourra consulter la page: [google dev: chaines](https://developers.google.com/edu/python/strings?hl=fr)

On accède à un élément d'une chaine grace à sa position, appelée *indice*. Le premier élément a pour indice zero. 

```python
> voyelles = 'eio'
> voyelles[0]
e
> voyelles[1]
i
> voyelle[2]
o
> voyelles[-1]
o # le dernier element de la liste
> voyelles
'eio'
```

Un indice négatif permet d'identifier les éléments à partir de la fin: -1 pour le dernier caractère, -2 pour l'avant dernier, ...

Illustration avec la chaine de caractères *Hello*:

{{< img src="../images/hello.png" caption="exemple avec les rangs des caractères du mot Hello" link="https://developers.google.com/edu/python/strings?hl=fr" >}}

**2. Modifier une chaine**
Contrairement aux listes, il n'est pas possible de modifier un caractère dans une chaine:

```python
> voyelles = 'eio'
> voyelles[2] = 'y'
TypeError: 'str' object does not support item assignment
```

**3. Une fonction utile aux chaines: `len`**
La fonction `len` va retourner la longueur de la chaine de caractères.

```python
> chaine = 'abc'
> len(chaine)
3
```

## Listes
**1. Definition:** Une **liste** est une collection ordonnée d'objets.
Une **liste** est entourée de **crochets** `[ ]`. C'est le type `list` en python. Pour en savoir plus sur les listes, on pourra consulter la page: [google dev: listes](https://developers.google.com/edu/python/lists?hl=fr)

On accède à un élément d'une liste grace à sa position, appelée *indice*. Le premier élément a pour indice zero. 

{{< img src="../images/liste.png" caption="La liste `voyelles` est une collection contenant les caractères" >}}
Un indice négatif donne accès à la liste à partir du dernier élément.

```python
voyelles = ['e','i','o']
voyelles[0]
# affiche e
voyelles[1]
# affiche i
voyelle[2]
# affiche o
voyelles[-1]
# affiche o
voyelles
# affiche ['e','i','o']
```

**2. Modifier les éléments d'une liste**
On ne peut modifier un élément d'une liste que si celui-ci existe. Par exemple, si l'on veut modifier l'élément "e" au rang zero de la liste `voyelles` par un "a", il faut faire:

```python
voyelles = ['e','i','o']
voyelles[0] = "a"
voyelles
# affiche ["a","i","o"]
``` 

Par contre, la liste ne contenant que 3 éléments, du rang 0 au rang 2, on ne peut pas ajouter l'élément "u" de la manière suivante:

```python
voyelles[3] = "u"
# affiche
IndexError: list assignment index out of range
``` 

> Mais alors, quelle est la bonne méthode pour ajouter un élément à une liste?

**Il faut utiliser une méthode de liste: la méthode** `append`

```python
voyelles = ['e','i','o']
voyelles.append("u")
voyelles
# affiche ["e","i","o","u"]
```

L'écriture de la méthode `append` se fait avec une notation pointée: `liste.append(x)`, où `x` est la valeur à ajouter à la fin de `liste`.

**3. Une fonction utile aux listes: `len`**
La fonction `len` va retourner la longueur de la liste.

```python
> L = ['a','b','c']
> len(L)
3
```

**4. Autres méthodes de liste TRES utiles**

> Retirer un élément de liste: méthode `pop`

```python
voyelles = ["e","i","o","u"]
voyelles.pop()
voyelles
# affiche ["e","i","o"]
```

> Longueur d'une liste: fonction `len`

```python
voyelles = ["e","i","o","u"]
len(voyelles)
# affiche 4 
# car la liste contient 4 éléments
```



**5. Liste de listes** 
Les éléments contenus peuvent aussi être une liste:

```python
positions = [[0,0], [1,2], [2,4]]
```

C'est la représentation d'un tableau, qui sur un tableur peut être représenté sous la forme suivante:

{{< img src="../images/tableau.png" >}}
Les 3 éléments de la liste `positions` sont `[0,0]`, `[1,2]`, et `[2,4]`

Pour accéder au premier élément `[0,0]`, on fait:

```python
positions[0]
# retourne
[0,0]
```

Pour accéder au deuxieme élément `[1,2]`, on fait:

```python
positions[1]
# retourne
[1,2]
```

Et pour acceder au premier élément du 2e élément de `positions`, c'est à dire à la valeur 1, on fait:

```python
positions[1][0]
# retourne
1
```
Cela permet d'afficher ou modifier la valeur 1.

## Boucles bornées
**1. Definition:** Une **boucle bornée**  est un système d’instructions qui permet de répéter un certain nombre de fois toute une série d’opérations.

La syntaxe d'une boucle bornée, en langage algorithmique peut s'écrire:

```python
Pour i allant de 0 a n-1
Faire:
   instruction 1
   instruction 2
FinPour
```

En python, la syntaxe correspondante est:

```python
for i in range(n):
  instruction 1
  instruction 2
``` 

{{< img src="../images/cb_boucle1.png" caption="demonstration avec python_puzzle. La boucle realise 4 itérations." >}}

* **Remarques:**

  * Le bloc d'instruction sera executé n fois. Celui-ci peut contenir une ou plusieurs instructions, du moment qu'elles sont bien positionnées dans le bloc.
  * En *Python*, le **bloc** est identifié par une **indentation**: un retrait par rapport au bord gauche, comprenant 2 espaces (ou 4).
  * Pour sortir du bloc, on élimine l'indentation (on revient sur le bord gauche)
  * La fonction `range(n)` renvoie la liste des entiers de 0 à n-1. C’est un principe général en informatique, on commence toujours à compter à partir de 0, et il faut donc s’arrêter à n-1 pour effectuer n fois la boucle.
  * Pour chaque itération, le variant `i` prend une nouvelle valeur de l'ensemble `{0,1,2,... n-1}`, et peut être utilisé dans le bloc d'instructions. 
  * On peut choisir n'importe quel nom pour le variant, pas seulement `i`.

* *Exemple*

```python
for c in range(3):
  print(c)
# affiche
0
1
2
```

*Remarque:* `range(3)` va créer une liste itérable constituée des valeurs 0, 1, 2. Ce sont les valeurs prises successivement par le variant `c` dans `for c in range(3)`

**2. Parcourir les éléments d'une liste L avec `range(len(L))`**

```python
L = ["a","b","c"]
for i in range(len(L)):
  print(i, L[i])
# affiche
0 a
1 b
2 c
```

*Remarque:* Rappelez-vous que `len(L)` est une fonction qui retourne la longueur de la liste `L`. Si `L` contient 3 éléments, alors `len(L)` vaut 3.

**3. Parcourir les éléments d'une liste L avec `in L`**

```python
L = ["a","b","c"]
for c in L:
  print(c)
# affiche
a
b
c
```

*Ramarque:* Cette fois-ci, le variant `c` prend successivement toutes les valeurs de la liste `L`.

### Conclusion: Itérable et variant de boucle bornée
Les instructions `for i in range(len(L))` et `for c in L` ont à peu près le même objectif: celui de parcourir TOUS les éléments de la liste L. 

* Ce qui est COMMUN: c'est l'utilisation du mot clé `IN`, qui va créer ce que l'on appelle un *itérable*, c'est-à-dire une liste de valeurs qui seront proposées l'une après l'autre pour le variant de boucle.

* Ce qui est DIFFERENT: Dans le premier cas, on utilise la fonction `range`, qui créé un itérable entre 0 et la valeur mise en paramètre (valeur -1 pour être exact). Ce sont par exemple **les indices** de la liste `L`.

```
# exemple 1
for i in range(5):
  # instruction
```

La boucle va s'executer 5 fois. Mais à chaque fois, le variant i prend successivement l'une des valeurs dans `[0,1,2,3,4]` 

```
# exemple 2
L = [0, 10, 20, 30]
for c in L:
  # instruction
```

L'instruction `for c in L` va, elle, créer un itérable constitué des **valeurs** de la liste `L`

Le nombre d'itération sera égal au nombre `len(L)`, soit 4. Au cours des itérations, le variant `c` va prendre successivement chaque valeur de `L`, soit `[0, 10, 20, 30]`

## Tracer un graphique y = f(x)
Pour tracer un graphique `y=f(x)`, il faut disposer de 2 listes de mêmes dimensions `x` et `y`. Les coordonnées des points sont alors:

* (x[0],y[0]) pour le point M0
* (x[1],y[1]) pour le point M1
* ...

On utilise la fonction `plt.scatter` (nuage de points) ou bien `plt.plot` (courbe) du module `matplotlib.pyplot` qui est importé à la premiere ligne du script de la manière suivante: `import matplotlib.pyplot as plt`

Les 2 listes sont positionnées entre parenthèses, dans l'ordre (liste des X, liste des Y). Ce sont les arguments de la fonction `plt.scatter` (ou de `plt.plot`).

```python
import matplotlib.pyplot as plt
temps = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
T = [20, 20, 22, 24, 28, 32, 38, 44, 52, 60]
plt.clf()
plt.grid()
plt.scatter(temps,T)
plt.xlabel('temps(min)')
plt.ylabel('Temperature(°C)')
plt.show()
```


{{< img src="../images/graphique.png" >}}


# Travaux pratiques
<!--
* Lien vers l'énoncé du {{< a link="../page5" caption="TP4: Tableaux Excel et tableaux Python" >}}
-->

* Lien vers l'énoncé du {{< a link="../page3" caption="TP5: Listes" >}}

* Lien vers l'énoncé du {{< a link="../../../python_avance/pages/boucles/page4" caption="TP6: boucles et parcours de listes" >}}