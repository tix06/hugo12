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



**iterable = `range(5)`**

Dans ce premier cas, le variant prend successivement le valeurs de l'ensemble `{0,1,2,3,4}`. Le variant vaut 0 lors le premiere itération, puis 1 à la deuxieme, etc ...

```python
for i in range(5):
    print(i)
# affiche
0
1
2
3
4
```

> A tester vous-même (python): Exemple 1: utiliser la fonction `range` 



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

> A tester vous-même (python): Exemple 2: utiliser une séquence de type str



**iterable = `[1998,2018]`**

Les listes en python sont des sequences qui placent les valeurs entre crochets `[...]`. Les valeurs sont séparées par des virgules `,`

```python
L = [1998, 2018]

for annee in L:
    print('La France a gagné la coupe du monde en ', annee)
```

> A tester vous-même (python): Exemple 3: utiliser une séquence de type list

le variant `annee` prend successivement le valeurs de l'ensemble `{1998,2018}`

On peut placer autant de valeurs que l'on souhaite dans une liste.





# Boucle bornée et non bornée
Pour la boucle bornée `for`, il n'est pas necessaire d'ajouter une instruction dans le bloc pour que le *variant* change de valeur à chaque itération. Cela se fait *tout seul*, à chaque fois que le programme revient sur l'instruction `for`.

{{< img src="../images/bloc3.png" caption="modification du variant i à chaque itération" >}}

## Exemples
* *Exemple 1*: afficher le variant de boucle `i`

```python
# Boucle bornée
for i in range(3):
  print(i)
# affiche
0
1
2
```


*Remarque: la fonction `range(3)` va créer une liste itérable constituée des valeurs 0, 1, 2. Ce sont les valeurs prises successivement par le variant `i` dans `for i in range(3)`*

```python
# Boucle non bornée
i = 0
while i<3:
    print(i)
    i = i + 1
# affiche
0
1
2
```

*Remarque: Avec une boucle non bornée, il faut:*

* *déclarer la valeur initiale du variant*: `i = 0`
* *écrire la condition d'execution après le `while`, `i<3`*
* *faire varier le variant dans la boucle `while`*, `i = i+1`


* *Exemple 2*: Ce variant peut être utilisé pour une formule arithmétique, à l'intérieur de la boucle:

```python
# boucle bornée
for i in range(3):
  x = i*7
  print(x)
# affiche la table de 7
0
7
14
```

```python
# boucle non bornée
i = 0
while i < 3:
  x = i*7
  print(x)
  i = i + 1
# affiche la table de 7
0
7
14
```




# Suite

##### {{% button href="../page5" icon="bullhorn" style="caution" %}}Cours{{% /button %}} 
##### {{% button href="../page6" icon="palette" style="tip" %}}TP3{{% /button %}} Boucles bornées et non bornées







