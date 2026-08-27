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

# Suite

##### {{% button href="../page1" icon="bullhorn" style="caution" %}}Cours{{% /button %}} 
##### {{% button href="../page2" icon="palette" style="tip" %}}TP2a{{% /button %}} conditions
#### {{% button href="../page3_D" icon="palette" style="tip" %}}TP2b{{% /button %}} conditions et algorithmes


* [cours: ](../page1) structures conditionnelles
* [TP1](../../conditions/page2/) sur les structures conditionnelles et boucles while
* [TP2](../../conditions/page3_D/) sur les structures conditionnelles et fonctions
