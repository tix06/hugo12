---
Title: conditions
description: TP comparer des valeurs, input, boucle while
weight : 4
hidden : true
---


# Editeur Python
Au choix:

* Utiliser un **notebook**. 

{{< img src="/images/notebook.png" >}}

Dans une même cellule: Saisir une ou plusieurs lignes de code Python, puis appuyer simultanement sur *Majuscule(Shift)* + *Entrée* pour **executer le code**.

* Utiliser l'editeur **Pyzo**:

Mettre `##` avant chaque script pour créer une *cellule*. Executer la cellule et passer à la suivante avec *MAJ+CTRL+ENTREE*.

* Utiliser l'editeur **Spyder**:

Mettre `#%%` avant chaque script pour créer une *cellule*. Executer la cellule et passer à la suivante avec *MAJ+ENTREE*.

{{< img src="../images/cell.png" >}}
  
# Conditions et boucles non bornées
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

**2. Les blocs du programme**
En Python, on utilise l'indentation (le retrait de la ligne) pour rendre compte des blocs de code.

{{< img src="../images/pybloc1.png" alt="pybloc et indentation" caption="de pybloc au script python" >}}
Le bloc de code à executer peut contenir plusieurs lignes, à condition de respecter **l'indentation**. (2 ou 4 espaces, ou touche *TAB*).

**3. L'alternative `if - else`**
Une instruction `if - else` contient une instruction `if` qui s'execute si la condition est `True` et une clause `else` qui s'execute si la condition est `False`.

La *condition* est une opération logique, utilisant un opérateur de comparaison, (!=, ==, >, ... in) et retournant un booléen `True/False`.

`else` est ce que l'on appelle *l'alternative*.

```python
if hauteur_plant < 3 : 
  print('laisser le plant dans la serre')
else : 
  print('le mettre dehors')
```

*Remarque:* Observez bien l'alignement vertical qui distingue les instructions `if` et `else` des lignes qui sont executées de manière conditionnelle.

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

* `elif` est *toujours suivi d'une condition*
* `else` n'est pas suivi d'une condition. C'est l'alternative, dont le bloc est executé lorsqu'aucune des conditions precedentes n'est *vraie*.

## Condition sur une valeur **entrée** (`INPUT`)
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

*Un boulanger désire un programme qui demande à l'utilisateur le nombre de baguettes qu'il désire, qui calcule le prix total (sachant qu'une baguette coûte 1.10 €) et qui affiche le prix que l'utilisateur doit payer.*



```python
nombre=input("Combien de baguettes désirez-vous ?")
prix = nombre * 1.1
print("Vous avez à payer",prix,"euros.")
```

> Testez ce programme. Quel message d'erreur obtenez-vous ?



Testez maintenant le script suivant :

```python
nombre=int(input("Combien de baguettes désirez-vous ?"))
prix = nombre * 1.1
print("Vous avez à payer",prix,"euros.")
```

> Quelle est la différence avec le code précédent de cet exemple ?

## Boucles non bornées
**1. Definition:** Une *boucle non bornée* permet de répéter un élément de code un nombre à priori inconnu de fois.

On écrit l'instruction:  `while <condition d execution>:`

Le bloc de code est indenté sous cette première ligne:

```python
while <condition d execution>:
  instruction 1
  instruction 2
instruction suivante # suite du programme
``` 

Cette boucle repète l'execution d'un bloc de code (*instruction 1, instruction 2*), *tant que* la `<condition>` est evaluée à `True`. Lorsque le programme arrive à la dernière ligne de l'indentation, il revient à l'instruction `while`. Il réalise alors une *itération*.

Le test sur la `<condition>` est réalisé à chaque *itération*.

Lorsque cette `<condition>` n'est plus réalisée, le programme passe à l'*instruction* qui suit le bloc. *(sortie de la boucle)*

Souvent, il sera nécessaire de commencer le programme par initier une variable *(celle utile pour la condition d'execution)*. De sorte que cette condition d'execution soit évaluée à `True`, et que le bloc de cette boucle s'execute au moins une fois.

*Exemple 1: Réaliser un compteur*

> Tester le programme suivant:

```python
print("Donner les prénoms des 3 neveux de Donald Duck")
i = 1
while i <= 3:
  nom = input("Donner le nom du neveu n°"+str(i)+": ")
  i = i + 1
print("c'est fini")
```

* à la première itération, i vaut 0, donc la condition `i <= 3` est évaluée à `True` et le bloc est executé. l'utilisateur est invité à entrer le premier nom, (*il va certainement entrer Riri*), et i finit avec la valeur 1 (`i = i + 1`)
* Entrer ensuite les noms *Fifi* et *Loulou*.
* La boucle se poursuit jusqu'à ce que i soit égal à 4. Alors `i <= 3` est évaluée à `False` et le programme poursuit APRES la boucle, avec la dernière instruction: affiche `"c'est fini"`

> Vérifier dans la console: afficher le contenu de `nom`. Vous devriez avoir `Loulou`. Et la valeur du compteur `i`. (4)

*Exemple 2: Soustractions multiples* 

```python
r = 40
while r >= 3:
  r = r - 3
print('à la fin du programme, r vaut ' + str(r))
```

* A la première itération, `r` vaut 40 donc la `<condition>` r > 3 est `True`. r est diminué de 3 et prend la valeur 37.
* A la dernière itération, `4 > 3` est evalué à `True`. `r` est diminué de 3 et prend la valeur 1
* Puis `r > 3` est evalué à `False`. Le bloc n'est pas executé et le programme s'arrête s'il n'y a pas d'autres instructions (ou poursuit le script sinon).

> Executer ce programme. Comparer la valeur de `r` avec `40%3`. Conclure.

**2. Le problème de l'arrêt**
Pour le script précédent, remarquer que la variable testée est `r`, dans la condition d'execution `r > 3`. Le bloc executé à chaque itération doit alors modifier la valeur de `r`, et rapprocher sa valeur de la condition d'arrêt, `r<3`

C'est le problème avec les boucles non bornées. Celles-ci peuvent ne pas finir, ce qui peut bloquer la machine.

Cet effet de boucle *infini* peut être recherché, par exemple en robotique, où l'on veut que le programme se poursuive indéfiniment. Ainsi, la structure d'un programme *python* sur carte microbit commence par la structure suivante:

```python
from microbit import *

while True:
  # instructions
  # ...
``` 


**3. Le jeu de devinette**
Voici le script d'un jeu de hasard:

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

*Exemple:*

{{< img src="../images/input5.png" alt="boite dialogue input et jeu de hasard" caption="Trouve au bout de 3 essais" >}}

A chaque fois que la condition `choix_joueur != N_aleatoire` est `True`, c'est à dire que le nombre `choix_joueur` est différent de `N_aleatoire`, alors le bloc de la boucle `while` est exécutée. 

Lorsque les valeurs `choix_joueur` et `N_aleatoire` sont identiques, le programme passe à la ligne `print('Bravo vous avez gagné')` 

> A votre avis: 
* à quoi sert ce jeu?
  * à compter le nombre de fois où l'ordinateur tire aléatoirement le nombre 100?
  * à compter le nombre de fois où l'ordinateur tire aléatoirement le nombre 10?  
  * à deviner le nombre tiré aléatoirement (1 à 10) par l'ordinateur, en ayant droit à un seul essai.
  * à deviner le nombre tiré aléatoirement par l'ordinateur (1 à 10), avec un nombre d'essais à priori infini, jusqu'à ce que l'on trouve.
* à quoi sert la 3e ligne `choix_joueur = 100`?

> Testez ce programme. 

> Ajouter un compteur du nombre d'essais. Afficher ce nombre à la fin du jeu.


# Portfolio
* Quelle est l'instruction python qui génère une *sortie* (un affichage)? 
* Quelle instruction python permet de saisir une *entrée*? Donner un exemple. Quel est le type systématiquement retourné par cette instruction? Comment obtenir une valeur entière à partir de la saisie par l'utilisateur?
* Quelle est la différence entre l'instruction `elif` et l'instruction `else`?
* Quelle instruction génère une boucle infinie avec `while`?
* Boucle non bornée: Comment **réaliser un compteur simple**, utlisant une boucle bornée, avec une condition d'arrêt lorsque la variable atteint la valeur 10? Ecrire le script complet. Votre programme doit être fonctionnel.
 
# Suite
Travaux pratiques: [TP conditions](../page3_D/)
<!--
* *Algorithme essentiel*: Ecrire le script complet du calcul de **la division euclidienne** entre 2 entiers `a` et `b`. Le programme affiche le quotient et le reste de la division de `a` par `b`. *Vous devrez initialiser les variables a et b avec des valeurs*. Vous ne pouvez utiliser que l'opérateur soustraction `-`.
-->

# Liens
* [cours: ](../page1) structures conditionnelles
* [TP1](../../conditions/page3_D/) sur les structures conditionnelles et boucles while
* [TP2](../../conditions/page3_D/) sur les structures conditionnelles et fonctions

