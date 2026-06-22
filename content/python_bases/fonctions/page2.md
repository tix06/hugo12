---
Title: fonctions
description: cours et exercices sur les fonctions, paramètres
weight: 10
---




# Les fonctions
## Fonction sans paramètre
**1. Definition:** Une fonction permet d'encapsuler un bloc d'instructions et de lui donnéer un *nom*:

```
def ma_fonction():
    # bloc de code ligne 1
    # bloc de code ligne 2
``` 

La fonction est déclarée après le mot-clé `def`. 

Choisir un nom qui n'appartient pas à Python (aucune autre fonction porte ce nom dans le langage).

Le nom est suivi de parenthèses `()` et deux points `:`

Le bloc de code de la fonction est *indenté* sous la ligne `def ma_fonction`

**Appel de fonction:** On peut ensuite exécuter ce bloc en utilsant ce *nom*. On dit qu'on **appelle** cette fonction en écrivant son nom, suivi de parenthèses `()`.

```
ma_fonction()
``` 

**Valeur de retour:** Une fonction retourne en général une valeur. Après le mot-clé `return`



* *Exemple 1* Dans ce script, on definit une fonction qui retourne `Hi`. Les lignes commençant par le symbole `#` sont des commentaires, et ne sont pas executées par Python. Elles sont optionnelles.

```python
# definition de la fonction
def hello():
  return 'Hi'

# appel de la fonction
hello()
# 'Hi'
```

## Fonction avec paramètre
Une fonction peut avoir un ou plusieurs **paramètres** qui permettent de transmettre des valeurs au bloc d'instructions. A l'interieur de la fonction, ces paramètres sont traités comme des variables, mais **locales**: Elles n'existent pas à l'exterieur du bloc.

Il y a alors une affectation: `paramètre = argument` 

* *Exemple 2* Dans ce script, on definit une fonction qui calcule le carré d'un nombre `x`. 

```python
# definition de la fonction
def carre(x):
  return x**2

# appel de la fonction
carre(5)
# retourne 25
``` 

*Lors de la déclaration de la fonction, le seul paramètre attendu s'appelera `x`. Puis lors de l'appel de la fonction `carre`, l'argument choisi est 5. A l'interieur de la fonction, `x` vaut 5.*

{{< img src="../images/def_carre.png" caption="illustration du passage d'argument lors de l'appel de la fonction" >}}

*La valeur de retour est alors 25: l'intruction `return x**2` évalue `5**2`, soit 25, avant de retourner la valeur.*

Observez comme la *fonction Python* avec paramètre ressemble à la déclaration d'une *fonction* en mathématiques:

```
# en math
f(x) = 10 * x + 20
```

On peut calculer f(x) pour toute valeur de x en remplaçant x dans $10\times x + 20$ par sa valeur. Par exemple, $f(1) = 10\times 1 + 20 = 30$

```
# en python
def f(x):
  return 10 * x + 20
```

En python, on appelle cette fonction avec la valeur  $x=1$ en écrivant:

```
f(1)
# retourne 30
```

Le `return` correspond au signe `=` en langage mathématique.

### Plusieurs paramètres
Lors de l'*appel de la fonction*, le ou les arguments passés doivent correspondre aus paramètres attendus. Ils doivent être placés *dans l'ordre*.

* *Exemple 3*: fonction qui calcule la surface d'un rectangle lorsque l'on divise chacun de ses côtés par un même coefficient `c`. On aura besoin de la longueur de ses côtés `x` et `y` (les 2 premiers paramètres de la fonction). Mais aussi de la valeur `c`:

```python
# definition de la fonction
def calcul_surface(x,y,c):
  S = (x/c) * (y/c)
  return S

# appel de la fonction avec x=20 et y=30, c=1.5
# 20 sera place en premier argument
# 30 sera place en 2e argument
# 1.5 sera placé au niveau du 3e argument

calcul_surface(20,30,1.5)
# retourne 266.667
```

# Importer des fonctions
On peut étendre les fonctions du langage en important des fonctions. Celle-ci sont natives, elles font partie du langage python, mais ne sont pas chargées au démarrage.

L'un des modules très utile est, par exemple, le module `math`. Celui-ci contient de nombreuses fonctions. Pour importer celle qui transforme le angles de degrés en radians, il faut ajouter la ligne suivante au debut du programme:

```python
from math import radians
```

Puis, pour l'utiliser, et transformer 45° en radians, on écrira plus loin dans le programme:

```python
angle = radians(45)
print(angle)
```

# Placer un script dans une fonction
Le programme suivant comporte quelques lignes que l'on peut avoir à répéter. Imaginons un robot, chargé de laisser entrer les personnes dont l'age est supérieur ou egal à 18:

```python
age = input('Quel age avez-vous? ')
age = int(age)
if age >18:
    print('Vous pouvez entrer')
else:
    print('Desole, ca ne va pas etre possible')
```

Il sera plus efficace de placer ces lignes dans une *fonction*.

Les règles pour écrire une fonction à partir de ce script sont les suivantes:

* les entrées et variables sont mises en paramètre: il s'agit de `age`
* Les `print` sont remplacés par `return`
* Il faut choisir un nom à la fonction, écrit après `def`

```python
def entrer_en_discotheque(age):
  if age >=18:
      return 'Vous pouvez entrer'
  else:
      return 'Desole, ca ne va pas etre possible'
```

Lorsque vous executez le programme, ... il ne se passe rien. Vous avez seulement *chargé* la fonction.

Il faut appeler la fonction pour que celle-ci soit executée, par exemple avec:

```python
entrer_en_discotheque(18)
```

Voici un exemple d'execution d'une fonction à partir du shell. 

{{< img src="../images/spyder_fct.png" caption="1:charger la fonction (executer cellule), 2: appel, 3: sortie" >}}

Son execution cesse lorsqu'elle arrive à l'instruction `return`. Le programme reprend alors son cours.

# Travaux pratiques 
## Ex 1: fonction sans paramètre
La fonction suivante va retourner un dessin réalisé à partir de symboles ascii du clavier:

```
def figure_petit_chat():
  fig = "^---^"
  print(fig)
  fig = "_00_"
  print(fig)
  fig = "|-=-|"
  print(fig)
```

* Saisir le script dans une cellule python et executer.
* Dans une nouvelle cellule/interpreteur python: appeler la fonction. Ecrire: `figure_petit_chat()`

```python
>>> figure_petit_chat()
^---^
_00_
|-=-|
```


*La plupart du temps, on evitera d'utiliser la fonction `print` à l'intérieur d'une fonction. Sauf cas particulier comme ci-dessus.*

La fonction suivante va justement utiliser le mot clé `return` prévu pour qu'il y ait une *sortie*.

```python
def dessine():
  n = 3
  dessin = ""
  for i in range(n):
    dessin = dessin + "x*x"
  return dessin
```

* **Question a:** Executer la fonction du 2e script: `>>> print(dessine())` 

Quel est le motif dessiné? Pourquoi?

## Ex 2: fonction avec paramètre

> Ecrire une fonction `salut` qui prend pour paramètre `nom` et qui retourne une chaine de caractères `bonjour + "nom"`. 

Exemples d'appels de la fonction `salut`:

```python
salut("John")
# affiche
bonjour John
salut("Paul")
# affiche
bonjour Paul
salut("Ringo")
# affiche
bonjour Ringo
salut("George")
# affiche
bonjour George
```  

* **Question b:** Citer l'un des avantages d'utiliser une fonction. (répétition)

## Ex 3: fonction pour calculer
1. Écrire une fonction `cube` qui retourne le `cube` de son argument: `x**3`
2. Écrire une fonction `volumeSphere` qui calcule le volume d’une sphère de rayon r fourni en argument et qui utilise la fonction cube.

*Donnée:*

$$V = \tfrac{4}{3}\times\pi\times R^3$$

3. Calculer le volume en $cm^3$ d'une sphere de rayon 10cm (à l'aide de la fonction `volumeSphere`)

## Ex 4: Importer des fonctions
Importer les fonctions `degrees` et `radians` du module `math` et completer le tableau:

| angle degrés | angle radians |
|--- |--- |
| 45 |    |
| 35 |    |
|    | 0.657 |
|    | 0.1 |

## Travaux pratiques
* TP sur les boucles bornées, et les fonctions avec et sans paramètres: [Lien](../page51/)

* Le TP sur les fonctions utiles pour calculer: [Lien](../page52/)

* Le TP d'application des fonctions à Turtle: [Lien](../../dessiner/page3)

