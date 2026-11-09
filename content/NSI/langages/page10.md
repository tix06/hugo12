---
Title: turtle fractales
description: dessins recursifs, turtle
hidden: true
weight: 15
---

# Dessins récursifs avec python turtle
Le module Turtle permet d’avoir un environnement simple muni d’une interface graphique. 

La [page suivante](https://perso.limsi.fr/pointal/_media/python:turtle:turtleref.pdf) présente un aide-mémoire avec les principales instructions.

Le langage turtle diffère légèrement selon l'editeur. Avec l'editeur [pythonandturtle.com/turtle](https://pythonandturtle.com/turtle):

* veiller à terminer votre script par la ligne: `turtle.done()`
* il peut être utile de recharger la page à chaque modification du script afin de vider le cache du navigateur.

## Premier tracé
Se rendre sur l'editeur en ligne: [pythonandturtle.com/turtle](https://pythonandturtle.com/turtle)

Copier-coller le script ci-dessous. Executer et analyser celui-ci.

```python
import turtle

t = turtle.Turtle('turtle')
t.speed(5)
t.width(2)

t.pendown()
t.color('red')

def carre(largeur):
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

> A. Remplacer le script de la fonction par une boucle. Utiliser une boucle bornée `for` puis une boucle non bornée `while`.

> B. Remplacer maintenant le script de la fonction par un script recursif:

* La fonction `carre` aura 2 paramètres: `def carre(largeur,n=0):`
* La condition de base sera `if n == 4: return` afin de couper la descente dans la pile d'appels recursifs.
* Dans la partie hérédité: tracer un segment et pivoter. Puis appel recursif avec `carre(largeur,n+1)`

**question 1.1.:** recopier le script de votre programme fonction.

## Dessiner des spirales
... Avec des carrés emboités

Dans un carré de côté 100, on trace un carré dont les sommets sont situés au tiers des côtés du carré initial, et on répète *indéfiniment* l’opération.

{{< img src="../images/t5.png" >}}

Effacer les instructions de la partie *Programme principal*.

On utilisera une boucle non bornée avec le variant `largeur`. La condition d'execution pourrait être par exemple, `largeur>20`:

```python
while largeur > 20:
	# instructions
```

A chaque itération: 

* dessiner un carré avec la fonction `carre` et le paramètre `largeur`.
* avancer de $1/3 \times largeur$ 
* tourner de 26.565 degrés
* reduire la largeur d'un facteur 0.745: `largeur = largeur * 0.745`

**question 2.1.:** recopier le script de votre programme principal

> Créer une nouvelle fonction `spirale_carree` pour remplacer le script du programme principal. Celle-ci sera programmée de manière RECURSIVE. La condition de base sera `largeur < 20` afin d'arrêter la mile d'appel recursifs pour une largeur < 20.

**question 2.2.:** recopier le script de votre fonction


## Des plus petits carrés
On veut réaliser le dessin récursif dont on a mis ci-dessous les premières étapes (profondeur 0,1 et 2):

{{< img src="../images/recur_carre.png" >}}

Voici l'allure de l'arbre des appels de la fonction recursive. On y représente les traits du dessin de la figure. 

{{< img src="../images/recur_directions.png" >}}



**question 3.1:** Recopier la figure. Numéroter les 3 premiers segments dessinés par le programme. (sans le programmer)

> Programme de la fonction `carre`: 

```python
def carre(largeur,n):
  # Base de la fonction recursive
  # n représente le diviseur de la longueur du côté du carré
  if n >= 4:
    return
  # l'instruction return ne retourne rien 
  # mais termine la fonction
  # 
  # --- partie heredite ---
  # 
```

**question 3.2:** A partir de ces observations: Dans quel ordre doit-on placer les instructions de la partie hérédité?

```python
# proposition 1
for i in range(4):
    t.forward(largeur/n)
    t.right(90)
    carre(largeur,n+1)
# proposition 2
for i in range(4):
    t.right(90)
    t.forward(largeur/n)
    carre(largeur,n+1)
# proposition 3
for i in range(4):
    t.forward(largeur/n)
    carre(largeur,n+1)
    t.right(90)
```

**question 3.3:** : Quelles doivent être les instructions à placer dans la fonction pour obtenir l'image suivante:

{{< img src="../images/recur_carre2.png" >}}

**question 3.4:** : Calculer le nombre d'appels recursifs A(n) réalisées par la fonction. Puis estimez la complexité de cette fonction, en considérant comme instructions significatives : chaque deplacement et rotation réalisé par la tortue.



## Des triangles
Adapter ensuite cette fonction pour dessiner la figure:

{{< img src="../images/recur_triangle1.png" >}}
## Chalenge avec d'autres triangles

{{< img src="../images/recur_triangle2.png" >}}

**question 4.:** à partir d'une petite recherche sur le net, retrouver le nom de chacune des figures présentée ci-dessus.

*Prolongement:* Tuto pour dessiner ces figures: [TP sur eskool.gitlab.io](https://eskool.gitlab.io/tnsi/algorithmique/diviser_pour_regner/exercices/fractalesCorrige/)

# Liens
* Les dessins recursifs sont issus de la page [fourier.ujf-grenoble.fr](https://www-fourier.ujf-grenoble.fr/~parisse/giac/doc/fr/casrouge/casrouge019.html)
* La recursivité en term NSI [eduscol, quelques applications](https://eduscol.education.fr/document/10103/download)
* dynamique holomorphe, ensemble de Julia, Mandelbrot, Fractales: [wikipedia](https://fr.wikipedia.org/wiki/Ensemble_de_Mandelbrot)
* Mandelbrot par la pratique: [page de villemin.gerard](http://villemin.gerard.free.fr/Wwwgvmm/Suite/FracPrat.htm)
* Une discussion sur le theme des fractales, autosimilarités exacte et statistique, applications [blog futura-sciences](https://forums.futura-sciences.com/physique/154964-fractal-autosimilarite.html)