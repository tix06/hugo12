---
Title: TP conditions
description: prevoir l'arrêt, realiser un compteur, multiplier sans le signe produit, fonctions
weight: 5
hidden : true
---



# TP3: Structures conditionnelles
## Editeur Python
Au choix, utilisez:

* un **notebook**. 

{{< img src="/images/notebook.png" >}}

Dans une même **cellule**: Saisir une ou plusieurs lignes de code Python, puis appuyer simultanement sur *Majuscule(Shift)* + *Entrée* pour **executer le code**.

* l'editeur **Pyzo**:

Mettre **`##`** avant chaque script pour créer une *cellule*. Executer la cellule et passer à la suivante avec *MAJ+CTRL+ENTREE*.

* l'editeur **Spyder**:

Mettre **`#%%`** avant chaque script pour créer une *cellule*. Executer la cellule et passer à la suivante avec *MAJ+ENTREE*.

{{< img src="../images/cell.png" >}}

## Exemple
Le programme suivant demande de renseigner votre age (à la premiere ligne), et vous laisse entrer en discothèque, seulement si vous avez plus de 18 ans. La fonction `input` est ce que l'on appelle une **entrée**. Elle permet se saisir une valeur qui sera *utilisée par le programme*. La valeur saisie par l'utilisateur sera TOUJOURS de type **str**.

```python
age = input('Quel age avez-vous? ')
age = int(age)
if age >18:
    print('Vous pouvez entrer')
elif age == 18:
    print('Montrez moi votre carte d identite SVP')
else:
    print('Desole, ca ne va pas etre possible')
```

Cette structure servira pour les prochains scripts.

# Enoncé des exercices
## Ex 1: test sur un nombre divisible
Le script suivant permet de tester la parité d'un nombre `n`. Saisir dans l'editeur Python le script suivant.

```python
n = 33
if n%2 == 0:
  print("n est pair")
else: 
  print("n est impair")
```

> Tester puis adapter ce script, pour demander à l’utilisateur un entier, puis afficher si cet entier pair.

*Aide:* Vous devrez utiliser la fonction de conversion `int` pour transformer la valeur saisie par l'utilisateur en un entier: `n = int(input(' ... '))` 

* **Question a1:** Recopier ce nouveau programme.

> Tester puis adapter ce script, pour demander à l’utilisateur un entier, puis afficher si cet entier est divisible par 11.

* **Question a2:** Recopier ce nouveau programme.

## Ex 2: Comparer 2 nombres
> Completer (et tester avec plusieurs valeurs de a et de b) le programme suivant qui compare a et b et retourne un message selon leur ordre ou leur egalité.

```python 
a = float(input("entrer la valeur de a: "))
b = float(input("entrer la valeur de b: "))
if a ... :
  print("a est plus grand que b")
elif ... :
  print("a et b sont égaux")
else:
  print(...)
```

* **Question b:** Qui a la plus grande valeur parmi `a` et `b` après le `else`?

## Ex 3: Comparer 3 nombres
### version 1
> Completer (et tester avec plusieurs valeurs de a de b et de c) le programme suivant qui compare a, b et c, et retourne un message précisant le plus grand des 3.

On suppose que les 3 nombres a, b et c ne sont jamais égaux. On utilisera l'opérateur `and` qui retourne `True` si les 2 conditions (à gauche et à droite de `and`) sont toutes les 2 évaluées à `True`, `False` sinon.

```python
a = 10
b = 20
c = 11
if a > b and a > c:
  print("a est le plus grand")
elif ...
```

* **Question c:** Combien de `elif` faut-il utiliser au minimum?

### version 2
> Completer (et tester avec plusieurs valeurs de a de b et de c) le programme suivant (version 2) qui compare a et b et retourne un message selon leur ordre.

Cette fois, on **n'utilisera pas** l'opérateur `and`, ce qui oblige à utiliser 2 structures conditionnelles imbriquées.

```python
a = 10
b = 20
c = 11
if a > b:
  if a > c:
    print("a est le plus grand")
  ...
...
```

* **Question d:** Traduire en langage naturel la double condition pour laquelle `a` est le plus grand: *si a est supérieur à b alors si ... ... ... alors ...*

## Ex 3: IMC
L'Indice de Masse Corporelle (IMC) est un indicateur chiffré utilisé en médecine. L'IMC d'une personne est donné par la formule:

$$IMC = \tfrac{masse}{taille^2}$$

où la masse est en **kg** et la taille en **mètres**.

Proposez un algorithme qui demande à l'utilisateur sa taille et sa masse puis qui affiche l'IMC de la personne.

*Pensez à écrire un texte clair à destination de l'utilisateur pour qu'il sache quoi saisir.*

Utilisez le tableau suivant pour fournir une information à la personne en fonction de son IMC:

{{< img src="../images/imc.png" alt="classification de l'IMC" caption="classification de l'IMC - source: has-sante.fr" >}}

* **Question e:** Recopier la série d'instructions conditionnelles qui affichent une information sur l'IMC.


* **Question f:** *(après avoir lu le cours sur les fonctions). IMC à l'aide d'une fonction: 
Créer une fonction que vous nommerez `IMC` à partir de votre script. Testez la dans le shell de votre editeur.

## Ex 4: Compter les ballons 
On utilise un programme pour compter le nombre de ballons touchés lors d'un jeu de fête foraine.

{{< img src="../images/ballons.jpg" caption="tir aux ballons" >}}

source image: {{< a link="https://fr.vecteezy.com/membres/stockgiu" caption="vecteezy - Giuseppe Ramos" >}}

Lorsqu'un ballon est touché, il faut saisir "O". Lorsque le ballon est manqué, saisir un "X". Le jeu termine lorsque le nombre total de tirs est égal à 6.

Les variables utilisées seront: 

* `n`: compteur du nombre total de tirs
* `touches`: nombre de ballons touchés
* `manques`: nombre de ballons manqués
* `choix`: caractère saisi par le joueur ("O" ou "X")

> Ecrire et tester le script du programme. Afficher le score à la fin du jeu.

```python
n = 0
touches = 0
manques = 0
while ...:
  choix = input("X pour manqué ou O pour touché: ")
  ...
  if ...
...
```

* **Question f**: Dans votre programme, quel est le variant de boucle? 

* **Question g**: Supposons que l'utilisateur entre la série: "X", "O", "O", "O", "X", "O". Comment évoluent les différentes variables? Recopier et compléter le tableau de suivi.

| `n` *avant itération* | `touches` *avant iteration* | `manques` *avant iteration* | condition d'execution `True/False` | `choix` |
| --- | --- | --- | --- | --- |
|   |   |   |   |   |

* **Question h**: Etes-vous sûr que le programme finira, quelles que soient les entrées saisies par l'utilisateur?

## Ex 5: Multiplier sans utiliser `*`
La multiplication de `x` par `a` revient à additionner `x + x + x ...` un nombre `a` de fois.

Par exemple, `x + x + x` correspond à `3 * x`.

On peut alors utiliser `a` comme variant dans une boucle `while`avec pour condition d'arrêt, `a == 0`. 

Dans le bloc executé par la boucle, il faudra ajouter à la variable `produit`, la valeur de `x`. Et diminuer `a` d'une unité.

Compléter le programme afin de réaliser le produit de `x` par `a`, sans utiliser l'opérateur `*`.

```python
x = int(input('entrer la valeur de x: '))
a = int(input('entrer la valeur de a: '))
produit = 0
while ...:
  ...
  ...
print('le produit x * a vaut: ' + ...)
```

* **Question i:** Précisez combien d'itérations ont lieu, en fonction de la valeur de `a`.








# Portfolio
## structure conditionnelle
* A quoi sert l'indentation en python sous une instruction conditionnelle?
* Que faut-il contrôler dans une boucle non bornée (`while`) pour s'assurer que celle-ci finira toujours?
* Montrer qu'il est possible de déterminer le nombre d'itérations du bloc conditionnel en fonction du variant. Prenez un exemple.
## fonctions 
* Rappeler comment s'écrit une structure conditionnelle avec alternative (if ... elif ... else). Placer les conditions, indentations, et les `:`
* Dans une structure conditionnelle avec alternative, tous les cas sont-ils toujours examinés par le programme? Expliquez.
* Expliquer la différence entre une variable (déclarée dans le *main*), et un paramètre (déclaré avec une fonction). Définir leur *portée*
* Dans une fonction, quel est le rôle du mot-clé `return`?
* Ecrire les fonctions pour les scripts: `parite`, `est_divisible`, `compare_2_nombres`, `IMC`.
* Compléter le tableau suivant avec le nom et les paramètres que vous avez choisis pour les fonctions précédentes.

| nom de la fonction | paramètre-s | affichage ou valeur de retour |
|--- |--- |--- |
| `parite`  | `N`  |   |
|  ... |   |   |


# Liens
* [cours: ](../page1) structures conditionnelles
* [TP1](../../conditions/page3_D/) sur les structures conditionnelles et boucles while
* [TP2](../../conditions/page3_D/) sur les structures conditionnelles et fonctions



