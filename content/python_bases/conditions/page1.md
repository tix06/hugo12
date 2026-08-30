---
Title : structures conditionnelles
titleHidden: true
description: cours sur les structures conditionnelles
weight: 5
---

# Structures conditionnelles simples et avec alternative
## Conditions
**1. Définition :** Une *instruction conditionnelle* vérifie si une certaine condition est vraie avant d'executer son code : 

```
if instruction_conditionnelle : 
  code_à_executer
``` 

*Exemple :*

```python
if prix_essence > 1.8:
  print('Trop cher')
```

*Remarquer que l'instruction `if .. condition ..:` finit par 2 points `:`, et que la ligne suivante est **indentée***

**Toute portion de code** associée à une **structure de contrôle** (finissant par 2 points `:`) nécéssite une **indentation**.

**2. Les blocs du programme**
En Python, on utilise l'indentation (le retrait de la ligne) pour rendre compte des blocs de code.

{{< img src="../images/pybloc1.png" alt="pybloc et indentation" caption="de pybloc au script python" >}}
Le bloc de code à executer peut contenir plusieurs lignes, à condition de respecter **l'indentation**. (2 ou 4 espaces, ou touche *TAB*).

**3. L'alternative `if - else`**
Une instruction `if - else` contient une instruction `if` qui s'execute si la condition est `True` et une clause `else` qui s'execute si la condition est `False`.

```python
if hauteur_plant < 3 : 
  print('laisser le plant dans la serre')
else : 
  print('le mettre dehors')
```

**4. Conditions multiples `if - elif - else`**
Un bloc `if - elif - else` comprend une premiere instruction `if`, puis une suite de conditions de tests `elif` si le premier test echoue, puis un bloc `else` qui s'execute si tous les autres tests échouent.

Même s'il n'est pas obligatoire, il est fortement recommandé de finir une série de conditions `elif` par le bloc `else`.

```python
if hauteur_plant < 3 : 
  print('laisser le plant dans la serre')
elif hauteur_plant < 10 : 
  print('le sortir le jour')
elif hauteur_plant < 15 : 
  print('le mettre dehors')
else : 
  print('Pret pour la recolte')
```

*Rappelez vous:*

* `elif` est **toujours** suivi d'une condition
* `else` n'est **pas** suivi d'une condition. C'est l'alternative, dont le bloc est executé lorsqu'aucune des conditions precedentes n'est *vraie*.

# Tests logiques
Il s'agit d'une expression booléenne qui est évaluée est qui renvoie `True` si elle est vrai, `False` sinon.

## Opérateurs de comparaison

*Quelques exemples de tests logiques :*

```python
age == 18   # egalité
age != 18   # inegalité
age <= 18   # inferieur ou egal
nom == 'John' # egalité de chaines
```

## Opérateurs et combinaisons logiques
L'expression peut aussi contenir les opérateurs logiques de combinaisons: `and`, `or`, `not`.

L'expression suivante, `A and B` est evaluée à `True` si `A` vaut `True`, et `B` vaut `True`. Dans tous les autres cas, (`A` vaut `False`, ou `B` vaut `False`, ou `A` et `B` valent `False`),  `A and B` est evaluée à `False`. On peut résumer tous les cas dans une table logique:

| A | B | A and B |
| --- | --- | --- |
| `False` | `False` | `False` |
| `False` | `True` | `False` |
| `True` | `False` | `False` |
| `True` | `True` | `True` |


Pour l'opérateur logique `or`:

| A | B | A or B |
| --- | --- | --- |
| `False` | `False` | `False` |
| `False` | `True` | `True` |
| `True` | `False` | `True` |
| `True` | `True` | `True` |

et pour l'opérateur `not`

| A | not A |
| --- | --- |
| `False` | `True` |
| `True` | `False` |

*Exemple:*

```python
n = int(input('entrer un nombre entier: '))
if n%2 == 0 and n > 0:
    print('vous avez entré un entier pair et positif')
```

Une instruction `if` peut également tester une valeur booléenne et exécuter son code si cette valeur vaut `True`, comme par exemple, ci-dessous, avec `if jeu_actif:`

Il n'est pas nécéssaire d'écrire `== True` comme ici avec `if jeu_actif == True:`

```python
if jeu_actif : 
  print('jouons !')
```

## Test sur une liste
On peut aussi vérifier si un élement existe dans une liste : 

```python
capitales = ['Paris', 'Berlin', 'Rome', 'Londres', 'Madrid']
'Paris' in capitales  
# retourne
# True car 'Paris' est dans la liste capitales
```



## Test sur un dictionnaire
Le mot-clé `in` permet de tester si une clé est présente dans le dictonnaire:

```python
dico = {'cle1':'val1','cle2':'val2','cle3':'val3'}

print('cle1' in dico)
# affiche True

print('val1' in dico)
# affiche False car `'val1'` est une valeur et non une clé.
```






# Remarque : 0 et None 
Dans le test logique, 0 et None se comportent comme s'il s'agissait de `False`:

```python
ch = input('Entrez un nombre entier quelconque')
n =eval(ch)
if n:
 print("vrai")
else:
 print("faux")
```

Ce petit script, lorsqu'il est executé, renvoie toujours `True` quel que soit le nombre saisi, mais `False` dans les cas suivants. Si on saisit 

* 0     # zero
* None  # le type Rien

**A savoir:** dans certains cas, on peut *faire l'économie* de l'*opérateur logique*. Dans l'instruction conditionnelle `if n`, la condition vaut `True` dès que `n` est différent de `0` ou de `None`, ou bien n vaut `True`.

Ainsi, les scripts suivants sont équivalents

```python
# script 1
# sortir = True ou bien sortir = False
if sortir:
  print('Vous pouvez sortir')

if sortir==True:
  print('Vous pouvez sortir')
```

```python
# script 2
# n est un entier
if n != 0:
  print('n est different de 0')

if n:
  print('n est different de 0')
```


# Boucles non bornées: `while`
**1. Definition:** Une *boucle non bornée* permet de répéter un élément de code un nombre à priori inconnu de fois.

On écrit l'instruction:  `while <condition d execution>:`

Le bloc de code est *indenté* sous cette première ligne:

```python
while <condition d execution>:
  instruction 1
  instruction 2
instruction suivante # suite du programme
``` 

Cette boucle repète l'execution d'un bloc de code (*instruction 1, instruction 2*), *tant que* la `<condition>` est evaluée à `True`. Le test sur la `<condition>` est réalisé à chaque *itération*.

Lorsque cette `<condition>` n'est plus réalisée, le programme passe à l'*instruction suivante*.

Souvent, il sera nécessaire de démarrer le programme par initier une variable *(celle utile pour la condition d'execution)*. De sorte que cette condition d'execution soit évaluée à `True`, et que le bloc de cette boucel s'execute au moins une fois.

*Exemple 1: Réaliser un compteur*

```python
print("Jeu du cache-cache: compte jusqu'à 10")
i = 1
while i <= 10:
  print(i)
  i = i + 1
print("c'est fini, j'arrive")
```

* à la première itération, i vaut 0, donc la condition `i <= 10` est évaluée à `True` et le bloc est executé. Le programme affiche **1** et i finit avec la valeur 2 (`i = i + 1`)
* La boucle se poursuit jusqu'à ce que i soit égal à 11. Alors `i <= 10` est évaluée à `False` et le programme poursuit APRES la boucle, avec la dernière instruction: affiche `"c'est fini"`

*Exemple 2: reste de la division euclidienne de 40 par 3* 

```python
r = 40
while r >= 3:
  r = r - 3
print('à la fin du programme, r vaut ' + str(r))
```
* A la première itération, `r` vaut 40 donc la `<condition>` r > 3 est `True`. r est diminué de 3 et prend la valeur 37.
* A la dernière itération, `4 >= 3` est evalué à `True`. `r` est diminué de 3 et prend la valeur 1
* Puis `r >= 3` est evalué à `False`. Le bloc n'est pas executé et le programme s'arrête s'il n'y a pas d'autres instructions (ou poursuit le script sinon).

**2. Le problème de l'arrêt**
Pour le script précédent, si l'on avait remplacé la condition `r >= 3` par `r == 3` le programme aurait pu executer le bloc `r = r - 3` indefiniment. `r` aurait pris successivement les valeurs 40, 37, ... 4, 1, -2, -5, ... etc, sans jamais prendre la valeur 0.

C'est le problème avec les boucles non bornées. Celles-ci peuvent ne pas finir, ce qui peut bloquer la machine.

Cet effet de boucle *infini* peut être recherché, par exemple en robotique, où l'on veut que le programme se poursuive indéfiniment. Ainsi, la structure d'un programme *python* sur carte microbit commence par la structure suivante:

```python
from microbit import *

while True:
  # instructions
  # ...
``` 

Mais dans le cas général, il faudra veiller à ce que la boucle finisse à un moment donné. Par exemple, dans le script suivant, on met l'instruction `break` qui a pour effet d'interrompre la boucle lorsque `break` est executée : 

```python
while True : # boucle qui à priori ne finit jamais
  nom = input('Quel est votre nom ?')
  if nom == 'quitter':
    break
  print('Bonjour, {}'.format(nom))
print('sortie de la boucle')
```

**Exemple**:

```
Quel est votre nom ? John
Bonjour, John!
Quel est votre nom ? quitter
sortie de la boucle
```



# Suite

##### {{% button href="../page1" icon="bullhorn" style="caution" %}}Cours{{% /button %}} 
##### {{% button href="../page2" icon="palette" style="tip" %}}TP2a{{% /button %}} conditions
##### {{% button href="../page3_D" icon="palette" style="tip" %}}TP2b{{% /button %}} conditions et algorithmes



