---
Title: fonctions et Turtle
linkTitle: dessiner avec Turtle
weight: 12
---

Le module Turtle ![](../images/t1.png) permet d’avoir un environnement simple muni d’une interface graphique. 

La [page suivante](https://perso.limsi.fr/pointal/_media/python:turtle:turtleref.pdf) présente un aide-mémoire avec les principales instructions.

Il est conseillé d'avoir bien lu et traité les exemples des pages:

* [TP boucles et fonctions](/docs/NSI_1/donnees/page5/)
* [Cours sur les fonctions](../page2)

# Premiers tracés
**Script initial**
Ces exemples utilisent une *boucle bornée* pour *répéter* des consignes (`for .. in range`)

Se rendre sur le notebook [Turtle](https://capytale2.ac-paris.fr/web/c/04df-2206914)

> Dans une nouvelle cellule: *Copier-coller* le script ci-dessous. *Executer et analyser* celui-ci.

```python
import turtle

t = turtle.Turtle('turtle')
t.speed(8)
t.width(2)

def carre(largeur):
    t.pendown()
    t.color('red')
    t.forward(largeur)
    t.left(90)
    t.forward(largeur)
    t.left(90)
    t.forward(largeur)
    t.left(90)
    t.forward(largeur)
    t.left(90)
    t.penup()
          
largeur = int(input('entrer la largeur'))
carre(largeur)
turtle.done()
```

Un script Python devra suivre une certaine structure pour la position de l'import des modules, déclaration de variables, des fonctions, et enfin le programme principal:

{{< img src="../images/t2.png" caption="premier script avec le module turtle" >}}

Le programme principal finira par `turtle.done()`, ce qui execute le tracé.

## Modifier la fonction `carre`: utiliser une boucle bornée
> Modifier pour avoir un script qui utilise le *moins de lignes possibles* pour cette fonction. (Rassembler les instructions `t.left + t.forward` dans une boucle)

Utiliser pour cela une boucle bornée `for`.

**question 1:** recopier le script de votre fonction

## Une variante du programme: dessiner un rectangle
> Definir et utiliser une fonction `rectangle` pour tracer un rectangle. On définira une nouvelle variable `longueur` qui sera utile comme paramètre de la fonction. 

La valeur de cette variable sera introduite par une fonction `input`, comme dans le script précédent.

**question 2:** recopier le script de votre fonction

## Dessiner des rectangles
> Reproduire, à l'aide de votre fonction, le dessin ci-dessous. Celui-ci forme 3 rectangles colorés de dimension $80x100$.

{{< img src="../images/t6.png" caption="rectangles côte à côte" >}}

**question 3:** recopier le script de votre programme (ne pas préciser les `import` et les definitions de fonctions)

# Utiliser un variant de boucle
On utilisera maintenant la valeur de `i` dans l'instruction `for i in range(N):`

Pour dessiner la figure suivante, on utilisera une *boucle bornée*, qui répète plusieurs fois le bloc de code:

* calculer la valeur de x
* dessiner un carré de largeur x
* lever le stylo
* avancer jusqu'à la prochaine position.

{{< img src="../images/t7.png" >}}

La valeur du paramètre x, dans la fonction `carre(x)`, dependra du variant `i`. 

> Ecrire un programme qui réalise ce dessin, à partir d'une fonction mathématique $x = a.i + b$

**question 4:** recopier le script de votre programme.

# Dessiner des spirales
## Avec des carrés emboités
Dans un carré de côté 100, on trace un carré dont les sommets sont situés au tiers des côtés du carré initial, et on répète *indéfiniment* l’opération.

{{< img src="../images/t5.png" >}}


On utilisera une [boucle non bornée](/docs/python/pages/conditions/page2_D/) `while` avec le **variant** `largeur`. La condition d'execution pourrait être par exemple, `largeur>20`:

```python
while largeur > 20:
	# instructions
```

A chaque itération: 

* dessiner un carré avec la fonction `carre` et le paramètre `largeur`.
* avancer de $1/3 \times largeur$ 
* tourner de 26.565 degrés
* reduire la largeur d'un facteur 0.745: `largeur = largeur * 0.745`

**question 5:** recopier le script de votre programme principal

## Avec des segments
Ecrire une fonction `spirale` qui devra reproduire une figure sur le modèle de la suivante:

{{< img src="../images/t4.png" >}}

* La fonction utilisera un paramètres: la `longueur` du segment initial
* le nombre d'itérations `N` voulues

Dans la fonction  `spirale`: utiliser une boucle (`for` ou `while`) pour executer un certain nombre de traits.

**question 6:** recopier le script de votre fonction

# Liens
* Editeur en ligne: [https://pythonandturtle.com/turtle](https://pythonandturtle.com/turtle)
