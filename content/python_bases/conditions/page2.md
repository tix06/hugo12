---
Title: TP2a conditions
Description: TP conditions, boucles non bornées, compteur, jeu de devinettes
titleHidden: true
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
  

## Branchements et conditions simples
1. Un robot est en mouvement lorsque son état `avancer` est mis à `True`. Sinon, il reste au repos. Compléter le programme suivant pour mettre en mouvement le robot s'il n'y a pas d'obstacle devant lui.

```python
obstacle = False
batterie = True
avancer = False
if not obstacle:
  ...
```

2. Ajouter une deuxième condition sur l'état de la batterie: le robot n'avance que s'il n'y a pas d'obstacle ET que la batterie n'est pas vide:


```python
obstacle = False
batterie = True
avancer = False
if not obstacle:
  if ... : 
    ...
```

3. Ecrire à nouveau le programme, mais avec une combinaison d'opération, et un seul `if`

```python
obstacle = False
batterie = True
avancer = False
if ... and ...:
  ...
```

4. Le comportement du robot depend maintenant de la jauge de la batterie. La variable `batterie` prend une valeur entre 0 (vide) et 100 (max). Le robot avance dans le cas où:

* le niveau de batterie est supérieur à 80 (même s'il y a un obstacle)
* il n'y a pas d'obstacle, et la batterie a un niveau supérieur à 40.

Dans les autres cas, le robot n'avance pas. Ecrire ce nouveau programme.

**Question a:** Quelles sont toutes les possibilités d'écriture de cette structure conditionnelle?

## Condition sur une valeur entrée (`INPUT`)
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

> **Question b**: Testez ce programme. Quel message d'erreur obtenez-vous ?



Testez maintenant le script suivant :

```python
nombre=int(input("Combien de baguettes désirez-vous ?"))
prix = nombre * 1.1
print("Vous avez à payer",prix,"euros.")
```

> **Question c**: Quelle est la différence avec le code précédent de cet exemple ?

# Boucles non bornées: `while`
## Réaliser un compteur
Le programme suivant (à compléter) compte jusqu'à 4. 

```python
i = 1
print("Début")
while ... :
  print(...)
  i = i + ...
print("Fin")
```

1. Compléter le programme pour qu'il affiche les valeurs du compteur, et termine lorsque `i` depasse 4.
2. Ajouter des instructions pour qu'il n'affiche les valeurs du compteur que si celles-ci sont PAIRES (divisibles par 2).



## Soustractions multiples
Le programme suivant va **soustraire 3** à la valeur saisie par l'utilisateur. Le programmeur ne connait pas cette valeur, aussi utilise t-il une boucle non bornée, `while`, qui s'execute tant que la valeur est supérieure à 3. On affiche à la fin le nombre de soustractions réalisées.

```python
valeur = int(input("entrer une valeur entière: "))
i = 0
while valeur ...:
  valeur = ...
  i = ...
print("il a fallu {i} soustractions")
```


## Le jeu de devinette
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

> **Question d:** 

> d1. A votre avis: 
* à quoi sert ce jeu?
  * à compter le nombre de fois où l'ordinateur tire aléatoirement le nombre 100?
  * à compter le nombre de fois où l'ordinateur tire aléatoirement le nombre 10?  
  * à deviner le nombre tiré aléatoirement (1 à 10) par l'ordinateur, en ayant droit à un seul essai.
  * à deviner le nombre tiré aléatoirement par l'ordinateur (1 à 10), avec un nombre d'essais à priori infini, jusqu'à ce que l'on trouve.
* à quoi sert la 3e ligne `choix_joueur = 100`?

> d2. Testez ce programme. Modifiez la condition d'arrêt de la boucle pour que l'on puisse sortir du jeu lorsque l'on saisit la valeur 0. Cela doit arrêter la partie.

> d3. Ajouter un compteur du nombre d'essais. Afficher ce nombre à la fin du jeu.

> d4. Ecrire un programme qui aide à mémoriser les tables de multiplication. Ce programme propose 2 entiers à multiplier. Le joueur doit donner le resultat de leur multiplication. Le jeu s'arrête lorsque le joueur commet une erreur. On affiche alors le nombre de reussites. Il faudra utiliser une boucle `while` et s'inspirer du programme précédent.

*Aide* Tirage aleatoire. Débuter le programme par l'import de la fonction `randint` de la librairie `random`. Puis utiliser la fonction `randint` avec 2 arguments qui limitent la plage de choix aleatoire entre ces deux bornes.

*Exemple:*

```python
from random import randint
x = randint(0,10)
print(x)
# Affiche une valeur aléatoire entre 0 et 10
```



# Fiche de synthèse
## structure conditionnelle
* A quoi sert l'indentation en python sous une instruction conditionnelle?
* Quelle est l'instruction conditionnelle avec *alternative* en python? `if .. else` ou bien `if .. elif .. else`?
* Quelle est l'instruction conditionnelle avec *différents cas*? `if .. else` ou bien `if .. elif .. else`?
* Dans une structure conditionnelle avec alternative, tous les cas sont-ils toujours examinés par le programme? Expliquez.
* Quelle est l'instruction python qui génère une *sortie*? Donner un exemple.
* Quelle instruction python permet de saisir une *entrée*? Donner un exemple. Quel est le type systématiquement retourné par cette instruction? Comment obtenir une valeur entière à partir de la saisie par l'utilisateur?
## boucle while
* Quelle instruction génère une boucle infinie avec `while`?
* Que faut-il contrôler dans une boucle non bornée (`while`) pour s'assurer que celle-ci finira toujours?
* Boucle non bornée: pourquoi faut-il initialiser la variable `i` avant d'écrire `while i <= 3:`?
* Boucle non bornée: Comment **réaliser un compteur simple**, utlisant une boucle bornée, avec une condition d'arrêt lorsque la variable atteint la valeur 10? Ecrire le script complet. Votre programme doit être fonctionnel.
* Compléter la phrase: Le quotient d'une division euclidienne de a par b (`a//b`) est égal au nombre de fois qu'il faut executer `a = a - b` pour que l'on obtienne `a ... b`. 
* Dans quel cas peut-on faire l'économie d'un opérateur lors de l'écriture d'une opération logique? (voir paragraphe sur 0 et None)



# Suite

##### {{% button href="../page1" icon="bullhorn" style="caution" %}}Cours{{% /button %}} 
##### {{% button href="../page2" icon="palette" style="tip" %}}TP2a{{% /button %}} conditions
#### {{% button href="../page3_D" icon="palette" style="tip" %}}TP2b{{% /button %}} conditions et algorithmes

