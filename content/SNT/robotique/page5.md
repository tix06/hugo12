---
Title : Python Turtle
description: dessiner en donnant des ordres
titleHidden: true
weight: 17
---

{{< img src="../images/figuresMath.png" caption="des exemples de figures mathématiques" >}}
# TP Python Turtle
Le module Turtle de Python permet de dessiner à l'écran des formes, à l'aide d'instructions qui tracent des formes géométriques.

Nous nous limiterons aux fonctions:

* up() : lève le crayon
* down() : baisse le crayon
* forward(n) : avance de n
* left(n) : tourne vers la gauche de n degrés
* right(n) : tourne vers la droite de n degrés
* circle(n) : dessine un cercle de rayon n
* write(’texte’) : écrit le texte
* color(’couleur’) : définit la couleur du trait
* fillcolor('couleur') : definit la couleur du remplissage

# Premiers tracés
## L'interface Scratch + Python de Vittascience
* Aller sur le site{{< a link="https://fr.vittascience.com/python/" caption="Vittascience.com" >}}
Le site propose un éditeur Scratch en ligne (avec des blocs de code).

Les blocs de code sont accessibles à partir des *menus*, par genre:

* Affichage
* Turtle
* Logique
* Boucles
* Variables
* Fonctions ...

## Pour commencer: dessiner un triangle simple
### Assembler les blocs
A partir du *menu Turtle*, en utilisant les blocs, vous allez:

{{< img src="../images/bloc1.png" caption="bloc avancer du menu Turtle" >}}
```
avancer de 50
tourner a gauche d'un angle de 120°
avancer de 50
```

Vous voyez sur l'écran de droite le script Python équivalent, qui se construit au fur et à mesure:

```python
import turtle

turtle.forward(50)
turtle.left(120)
turtle.forward(50)
```

Appuyer sur **Executer**: La forme dessinée n'est pas un triangle fermé.

> **Défi 1:** ajouter les blocs manquants pour dessiner complètement le triangle.

{{< img src="../images/triangle.png" >}}
* Recopiez le script python correspondant dans votre cahier.

### Répéter avec une boucle
Si vous observez votre script, vous remarquez qu'il est constitué de 3 répétitions:

{{< img src="../images/bloc2.png" >}}
Vous allez réaliser la même chose, mais en réduisant *AU MAXIMUM* le nombre de lignes.

* Conserver uniquement les 2 premiers blocs, *AVANCER* et *TOURNER*. Supprimer les autres
* Dans le menu *Boucles*, prendre le bloc *répéter ... fois* et insérer dans ce bloc les 2 instructions de dessin. Modifier le paramètre 3.

{{< img src="../images/bloc3.png" >}}
* EXECUTER le programme
* Recopiez le script python correspondant dans votre cahier.

### Créer une spirale de triangles

> **Défi 2:** Vous allez créer une figure originale en modifiant juste les paramètres dans votre script:

> * Répéter 25 fois 
* Faites tourner chaque fois votre *Tortue* d'un angle de 125° et non 120°

Vous voyez ici l'interêt d'utiliser une boucle pour répéter plusieurs fois les même instructions...

### Créer ses propres fonctions
Une fonction permet de mémoriser des blocs de code afin de les organiser et les réutiliser plusieurs fois.

* Remettre les arguments qui dessinent un triangle simple (3 fois, 120°)
* Dans le menu *Fonctions*, prendre le premier bloc *Définir*. Modifier le nom, et renommer cette fonction avec `triangle`.

{{< img src="../images/bloc4.png" >}}
* Mettre alors la boucle entière dans cette fonction. EXECUTER... il ne se passe rien.
* Revenir dans le menu *Fonctions* et:
  * aller chercher le bloc de code appelé `triangle`. 
  * Ajouter ce bloc dans la programme, à la suite
  * et EXECUTER... voilà qui devrait afficher le triangle. Vous venez de programmer votre propre fonction, puis vous l'avez appelé avec son nom,  `triangle()`.
* Recopiez le script python correspondant dans votre cahier.

### Réutiliser une fonction
Voici un extrait de la suite du script qui vous permettra de créer une figurre plus complexe:

{{< img src="../images/bloc5.png" >}}
> **Défi 3:** Vous allez déplacer votre *Tortue* à différentes positions de l'image, afin de dessiner la forme suivante:

{{< img src="../images/triangleFigure.png" >}}
*Remarque: Vous aurez besoin pour cela de réutiliser votre fonction `triangle`.*

Une fois le défi réalisé, recopiez le script dans votre cahier.

> **Défi 4:** Réaliser maintenant l'une des figures ci-dessous:

{{< img src="../images/triangleFigure1.png" caption="figure 1: triangles alignés" >}}
{{< img src="../images/triangleFigure2.png" caption="figure 2: triangles tournants" >}}