---
Title: TP POO trajectoires
description: POO, equation cartesienne et parametree, turtle
hidden: true
weight: 17
---

# Simulation du mouvement d'un projectile

Pour simuler la trajectoire d'un projectile qui est soumis à la gravité, on a besoin de connaitre à un instant donné sa position (x,y) et sa vitesse (vx,vy).

{{< img src="../images/balle.png" caption="simulation de trajectoire avec Python" >}}

Alors, après un intervalle de temps `dt`, la position est donnée par:

$$x = x + vx \times dt$$

$$y = y + vy \times dt$$

Et la vitesse `vy` est telle que:

$$vy = vy - g \times dt$$ 
g = 9,81 SI

Pour représenter un projectile, nous allons utiliser une **classe Projectile**.

Les **attributs du projectile** seront:

* x
* y 
* vx
* vy

On utilisera l'editeur [Python + Turtle](https://pythonandturtle.com/turtle/) comme pour le [TP sur les dessins recursifs](/docs/NSI/algorithmes/page10/).

**1.** Ecrire une méthode de la classe Projectile qui s'appelera `translation` et qui modifiera les attributs x, y, et vy après un pas de temps `dt`. (`dt` est un paramètre de la méthode).

**2.** Ecrire un programme qui créé une instance de la classe Projectile, qui s'appelera `balle1`. Le programme appelera de manière répétée la méthode `translation` et affichera la position de `balle1`.

**3.** Modifier le programme pour qu'il affiche la trajectoire de `balle1`, en dessinant un trait depuis sa dernière position. On utilisera la bibliothèque `turtle` et la fonction `goto(x,y)` qui déplace la tortue à la position x,y en traçant un trait selon l'état `up()` ou `down()` de celle-ci.

**4.** Modifier la méthode `translation` pour programmer le rebond au sol: si la coordonnée y du projectile devient négative, on inverse la vitesse verticale `vy`.

**5.** Modifier le programme pour créer plusieurs balles avec des positions et des vitesses initiales différentes et lancer la simulation en appelant régulièrement la méthode `translation` pour chaque *balle*, à tour de rôle.

# Notes
TP inspiré d'un exercice du Hachette Education NSI, Terminale.

**La suite en TP**

* TP Jeu des 7 familles: [Lien](../page34/) *(Sans interface graphique)*
* TP sur trajectoires de projectiles: [Lien](../page31/) 
* TP sur la programmation d'un jeu de Dominos: [Lien](../page33/). *(Sans interface graphique)*
