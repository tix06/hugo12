---
Title: conditions
Description: TP conditions, boucles non bornées, compteur, jeu de devinettes
hidden: true
weight : 6
---


# Les structures conditionnelles
## Editeur Python
Pour tester les scripts python, vous pouvez:

* Soit utiliser un **notebook**. (*Atrium>Capytale*)

{{< img src="/images/notebook.png" >}}

Dans une même cellule: Saisir une ou plusieurs lignes de code Python, puis appuyer simultanement sur *Majuscule(Shift)* + *Entrée* pour **executer le code**.

* Soit utiliser l'editeur Pyzo:

Mettre `##` avant chaque script pour créer une *cellule*. Executer la cellule et passer à la suivante avec *MAJ+CTRL+ENTREE*.

* Soit utiliser l'editeur Spyder:

Mettre `#%%` avant chaque script pour créer une *cellule*. Executer la cellule et passer à la suivante avec *MAJ+ENTREE*.

{{< img src="../images/cell.png" >}}
  


# Condition sur une valeur entrée (`INPUT`)
La fonction `input` permet d'ouvrir une boite de dialogue, d'attendre la saisie, et de récupérer une information donnée par l'utilisateur.

On utilisera une variable pour stocker l'information saisie:

```python
prenom = input('Comment vous appelez-vous? ')
print('Bonjour ' + prenom)
```

{{< img src="../images/input1.png" alt="boite dialogue input" caption="demarrage du programme" >}}

{{< img src="../images/input2.png" alt="boite dialogue input" caption="saisie dans la boite de dialogue" >}}

{{< img src="../images/input3.png" alt="boite dialogue input" caption="utilisation de la variable prenom" >}}

*Remarquer* que le type retourné par la fonction `input` est toujours de format `str`. Pour modifier en un format numérique, et réaliser des opérations, il faudra utiliser l'une des fonctions `int` (pour obtenir un entier) ou `float` (pour un décimal):

```python
celcius = input('Entrer la température en degrés Celcius: T = ')
kelvin = float(celcius) + 273
print('En degrés absolus T = ' + str(kelvin))
```

{{< img src="../images/input4.png" alt="boite dialogue input" caption="conversion de 23°C en °K" >}}

**Autre exemple**:

*Un boulanger veut créer un programme qui demande à l'utilisateur le nombre de baguettes qu'il désire, qui calcule le prix total (sachant qu'une baguette coûte 1.10 €) et qui affiche le prix que l'utilisateur doit payer.*



```python
nombre=input("Combien de baguettes désirez-vous ?")
prix = nombre * 1.1
print("Vous avez à payer",prix,"euros.")
```

> **Question a**: Testez ce programme. Quel message d'erreur obtenez-vous ?



Testez maintenant le script suivant :

```python
nombre=int(input("Combien de baguettes désirez-vous ?"))
prix = nombre * 1.1
print("Vous avez à payer",prix,"euros.")
```

> **Question b**: Quelle est la différence avec le code précédent de cet exemple ?

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
print("Donner les prénoms des 3 neveux de Donald Duck")
i = 1
while i <= 3:
  nom = input("neveu n°"+str(i)+": ")
  i = i + 1
print("c'est fini")
```

* à la première itération, i vaut 0, donc la condition `i <= 3` est évaluée à `True` et le bloc est executé. l'utilisateur est invité à entrer le premier nom, (*il va certainement entrer Riri*), et i finit avec la valeur 1 (`i = i + 1`)
* La boucle se poursuit jusqu'à ce que i soit égal à 4. Alors `i <= 3` est évaluée à `False` et le programme poursuit APRES la boucle, avec la dernière instruction: affiche `"c'est fini"`

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


**3. Le jeu de devinette**
On veut créer un jeu qui questionne le joueur jusqu'à ce que celui-ci trouve le nombre choisi au hasard par l'ordinateur.

```python
from random import randint
N_aleatoire = randint(1,10)
choix_joueur = 100
while choix_joueur != N_aleatoire:
    choix_joueur = int(input('Choisir un nombre entre 1 et 10 :'))
    if choix_joueur != N_aleatoire:
      print('Recommencez')
print('Bravo vous avez gagné')
``` 

{{< img src="../images/input5.png" alt="boite dialogue input et jeu de hasard" caption="Trouve au bout de 3 essais" >}}

A chaque fois que la condition `choix_joueur != N_aleatoire` est `True`, c'est à dire que le nombre `choix_joueur` est différent de `N_aleatoire`, alors le bloc de la boucle `while` est exécutée. 

Lorsque les valeurs `choix_joueur` et `N_aleatoire` sont identiques, le programme passe à la ligne `print('Bravo vous avez gagné')` 

> **Question c:** A votre avis: à quoi sert la 3e ligne `choix_joueur = 100`?

> Testez ce programme. Modifiez la condition d'arrêt de la boucle pour que l'on puisse sortir du jeu lorsque l'on saisit la valeur 0. Cela doit arrêter la partie.

> Ajouter aussi un compteur du nombre d'essais. Afficher ce nombre à la fin du jeu.

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

# Portfolio
* Quelle est l'instruction python qui génère une *sortie*? Donner un exemple.
* Quelle instruction python permet de saisir une *entrée*? Donner un exemple. Quel est le type systématiquement retourné par cette instruction? Comment obtenir une valeur entière à partir de la saisie par l'utilisateur?
* Quelle est l'instruction conditionnelle avec *alternative* en python? `if .. else` ou bien `if .. elif .. else`?
* Quelle est l'instruction conditionnelle avec *différents cas*? `if .. else` ou bien `if .. elif .. else`?
* Quelle instruction génère une boucle infinie avec `while`?
* Boucle non bornée: pourquoi faut-il initialiser la variable `i` avant d'écrire `while i <= 3:`?
* Boucle non bornée: Comment **réaliser un compteur simple**, utlisant une boucle bornée, avec une condition d'arrêt lorsque la variable atteint la valeur 10? Ecrire le script complet. Votre programme doit être fonctionnel.
* Compléter la phrase: Le quotient d'une division euclidienne de a par b (`a//b`) est égal au nombre de fois qu'il faut executer `a = a - b` pour que l'on obtienne `a ... b`. 
* Dans quel cas peut-on faire l'économie d'un opérateur lors de l'écriture d'une opération logique? (voir paragraphe sur 0 et None)

<!--
* *Algorithme essentiel*: Ecrire le script complet du calcul de **la division euclidienne** entre 2 entiers `a` et `b`. Le programme affiche le quotient et le reste de la division de `a` par `b`. *Vous devrez initialiser les variables a et b avec des valeurs*. Vous ne pouvez utiliser que l'opérateur soustraction `-`.
-->

# Suite

Travaux pratiques: [TP conditions](../page3_D/)
<!--
* *Algorithme essentiel*: Ecrire le script complet du calcul de **la division euclidienne** entre 2 entiers `a` et `b`. Le programme affiche le quotient et le reste de la division de `a` par `b`. *Vous devrez initialiser les variables a et b avec des valeurs*. Vous ne pouvez utiliser que l'opérateur soustraction `-`.
-->

# Liens
* [TP1 sur les opérations et types de base](../../generalites/page2_D) *(NSI_1)*
* [TP1 sur les opérations et types de base](../../generalites/page2) *(Term NSI)*
* [TP2 sur les variables](../../variables/page4/)
* [cours: structures conditionnelles](../page1)
* [TP1 sur les opérations et types de base](../../generalites/page2_D)
* [TP2 sur les variables](../../variables/page4_D/)
* [TP3 structures conditionnelles et fonctions](../../conditions/page3_D/)