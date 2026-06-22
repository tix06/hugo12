---
Title: boucles
description: cours sur les boucles, bornées et non bornées, notion d'itérable, fonctions natives
weight: 8
---

<!--
fiche reponse: [Lien vers pdf](/pdf/NSI_1/python2_TP_boucle_et_fct.pdf)
-->

# Boucles bornées en Python
## Definition
Une **boucle bornée**  est un système d’instructions qui permet de répéter un certain nombre de fois toute une série d’opérations.

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

On peut représenter ce script avec des modules à assembler type *scratch* ou *blocky*):

{{< img src="../images/bloc1.png" caption="analogie avec des briques de construction du programme" >}}

## Remarque
**Construction de la boucle bornée**

  * Le bloc d'instruction sera executé n fois. Celui-ci peut contenir une ou plusieurs instructions, du moment qu'elles sont bien positionnées dans le bloc.
  * En *Python*, le **bloc** est identifié par une **indentation**: un retrait par rapport au bord gauche, comprenant 2 espaces (ou 4).
  * Pour sortir du bloc, on élimine l'indentation (on revient sur le bord gauche)

  {{< img src="../images/bloc2.png" caption="bloc de retour à la fin de la boucle" >}}

  * La fonction `range(n)` renvoie la liste des entiers de 0 à n-1. C’est un principe général en informatique, on commence toujours à compter à partir de 0, et il faut donc s’arrêter à **n-1 pour effectuer n fois** la boucle.
  * Pour chaque itération, le variant `i` prend une nouvelle valeur de l'ensemble `{0,1,2,... n-1}`, et peut être utilisé dans le bloc d'instructions. 
  * On peut choisir n'importe quel nom pour le variant, pas seulement `i`.
  * Contrairement à la boucle non bornée `while`, le programmeur ne s’occupe pas de faire varier i à chaque itération. Cela ce fait tout seul.

## Boucle bornée et séquence
L'instruction utilisant le mot-clé `for` suit la construction suivante:

```
for variant in iterable:
    # bloc de code à repeter
```

Ce que l'on appelle *iterable*, c'est un ensemble de valeurs que prend successivement le *variant*.

> A tester vous-même (python): Exemple 1: utiliser la fonction `range` 

**iterable = `range(5)`**

Dans ce premier cas, le variant prend successivement le valeurs de l'ensemble `{0,1,2,3,4}`. Le variant vaut 0 lors le premiere itération, puis 1 à la deuxieme, etc ...

```python
for i in range(3):
    print(i)
# affiche
0
1
2
```

> A tester vous-même (python): Exemple 2: utiliser une séquence de type str

**iterable = `"abc"`**

Dans ce deuxieme cas, le variant `i` prend successivement le valeurs de l'ensemble `{"a","b","c"}`. Le variant vaut "a" lors le premiere itération, puis "b" à la deuxieme, etc ...

```python
for i in "abc":
    print(i)
# affiche
"a"
"b"
"c"
```

> A tester vous-même (python): Exemple 3: utiliser une séquence de type list

**iterable = `[1998,2018]`**

Les listes en python sont des sequences qui placent les valeurs entre crochets `[...]`. Les valeurs sont séparées par des virgules `,`

```python
L = [1998, 2018]

for annee in L:
    print('La France a gagné la coupe du monde en ', annee)
```

le variant `annee` prend successivement le valeurs de l'ensemble `{1998,2018}`

On peut placer autant de valeurs que l'on souhaite dans une liste.





# Boucle bornée et non bornée
Pour la boucle bornée `for`, il n'est pas necessaire d'ajouter une instruction dans le bloc pour que le variant change de valeur à chaque itération. Cela se fait tout seul, à chaque fois que le programme revient sur l'instruction `for`.

{{< img src="../images/bloc3.png" caption="modification du variant i à chaque itération" >}}

## Exemples
* *Exemple 1*: afficher le variant de boucle `i`

```python
for i in range(3):
  print(i)
# affiche
0
1
2
```



*Remarque: la fonction `range(3)` va créer une liste itérable constituée des valeurs 0, 1, 2. Ce sont les valeurs prises successivement par le variant `i` dans `for i in range(3)`*

* *Exemple 2*: Ce variant peut être utilisé pour une formule arithmétique, à l'intérieur de la boucle:

```python
for i in range(3):
  x = i**2 + 1
  print(x)
# affiche
1
2
5
```


## Exercices:
Pour chaque exercice **résolu**, **recopier** le script dans votre cahier.

1. **Sélection des valeurs paires**

Placer les 5 instructions suivantes, dans le bon ordre, et avec la bonne indentation pour afficher tous les nombres pairs entre 0 et 100:


```python
if i % 2 == 0:
range(100):
for i 
in 
print(i)
```

Le programme devra afficher les valeurs:

```
0
2
...
100
```



2. **Table de 7**

* version a: Réaliser un programme utilisant une boucel bornée `for`, qui affiche (fonction `print`) les 10 premières valeurs de la table de 7

* version b: Ecrire un nouveau programme, utilisant cette fois une boucle non bornée `while` pour afficher  les 10 premières valeurs de la table de 7:

<!--
{{< img src="../images/tableau1.png" caption="**Sur document-reponse**" >}}
-->

*Rappel:*

> La construction en bloc vous est déjà familière si vous avez utilisé un langage de blocs comme scratch ou blocky.  L’instruction while montre cette même disposition avec l'indentation.


{{< img src="../images/bloc4.png" caption="blocs python à compléter" >}}

> Pensez à ...:

* Utiliser un variant `i`, et une condition d'execution `while i<11:`
* Dans la boucle, augmenter la valeur du variant `i`, avec `i = i+1` 


3. **Parcourir des éléments de liste**

L'équipe de France a remporté aussi les trophées suivants: Coupe des Confédérations (2001, 2003), Jeux olympiques (1984), son championnat continental (1984, 2000)

Ecrire un script python qui utilise des listes et des boucles bornées pour afficher tous les trophées remportés par l'équipe de France:

```
l'equipe de France a remporté la Coupe de Confédérations en 2001
...
l'equipe de France a remporté le championnat continental en 2000
```

4. **Division euclidienne**

*On rappelle que l'utilisation d'une boucle bornée `for` nécessite de connaitre le nombre d'itérations (`for .. in range(n)`). Si ce nombre d'itérations n'est pas connu, il faudra utiliser une boucle `while`*.

Le quotient de la division de a par b est égal au nombre de fois N qu'il faut soustraire b à a jusqu'à ce que l'on ait a < b.

a. D'après cet énoncé, va t-on utiliser une boucle bornée, ou bien un boucle non bornée?

b. Compléter le script de la division euclidienne de a par b

```python
a = int(input('entrer la valeur de a :'))
b = int(input('entrer la valeur de b :'))
N = 0
while a >=b:
  ...
  ...
print(a)
``` 

c. Quel est le quotient entier de la division de 2024 par 7?

# Les fonctions natives du langage python
Tous les langages de programmation fournissent un large ensemble de fonctions prêtes à être utilisées. Nous avons déjà rencontré diverses fonctions prédéfinies, de la librairie standart : `print`, `input`, `range`.

> Tester dans un notebook, ou en console les fonctions natives suivantes:

```python
> bin(129)
..
> int('0b10000001',2)
..
```

Dans ces 2 exemples, on a utilisé un ou plusieurs arguments, positionnés entre les parenthèses.

* pour `bin(129)`, c'est l'argument 129 qui est passé à la fonction, afin que celle-ci réalise la conversion de 129 en binaire.
* pour `int('0b10000001',2)`, ce sont 2 arguments qui sont passés à la fonction `int`: Le binaire '0b10000001', ainsi que l'argument 2 précisant qu'il s'agit d'un code binaire à convertir en entier.

*Remarquer que ces arguments sont séparés par une virgule.*

## Exercices
1. **Convertir en binaire**

Utiliser la fonction `bin` pour convertir les nombres suivants: 65400, 31654, 1026

*Astuce pour **automatiser** le calcul*: On pourra placer ces valeurs dans une liste et utiliser une boucle bornée `for`:

```python
L = [65400, 31654, 1026]
for nombre in L:
    print(..)
```

2. **Convertir en ascii**

La fonction `chr` retourne le caractère ascii correspondant à l'entier (0..127) placé en argument:

```python
> chr(97)
'a'
```

> Utiliser cette fonction `chr` pour décoder le message, et trouver le tresor derrière l'une de ces portes...

{{< img src="../images/miniature.png" link="/pdf/NSI_1/D1_les_3_portes_ascii.pdf" caption="cliquer pour agrandir" >}}

On pourra s'aider du script suivant:

```python
L = [110, 39, 111]
for n in L:
    print(...)
```

# Suite
Les fonctions programmées en python: [Lien](../../fonctions/page51)





