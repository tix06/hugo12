---
Title: balle rebondissante
hidden: true
---

# Suite du jeu PONG (pygame)
## Dessiner la balle, prevoir les variables
Nous allons nous interesser au dessin et au deplacement de la balle. Celle-ci doit normalement rebondir sur les murs gauche, haut et bas. Par contre, vous devrez l'empêcher d'atteindre le bord droit à l'aide de votre raquette. Sinon, vous perdrez la partie (ou vous perdrez 1 point).

Pour dessiner la balle, ajouter les variables suivantes:

* les coordonnées de son centre: `xb`, `yb`
* le rayon de la balle: `r_balle`
* sa vitesse dans la direction horizontale: `vx`
* sa vitesse dans la direction verticale: `vy`
* sa couleur: `couleur`, un tuple constitué des intensités des 3 couleurs primaires.

Pour ajouter de la variété dans le jeu, la balle pourrait apparaitre à une position (légèrement) aléatoire, et avec une vitesse plus ou moins élevée.

Ces variables seront initialisées avec les valeurs suivantes (*ajuster au besoin, et selon la difficulté voulue*):

```python
from random import randint
r_balle = 16
xb = 50
yb = 256 + randint(0,100)-50
vx = 2 + randint(0,2)
vy = 2
couleur = (45, 170, 250)
```

Pour dessiner la balle, utilisons la fonction `draw.circle`:

```python
pygame.draw.circle(fenetre, couleur, (xb, yb), r_balle)
```

<!--
Cette ligne est à placer avant le rafraichissement de la page: `pygame.display.update()`

A ce niveau, votre programme devrait ressembler à ceci:

```python
import pygame
from pygame.locals import *
from random import randint

pygame.init()
pygame.key.set_repeat(1,20)
fenetre = pygame.display.set_mode((512,512))
fenetre.fill([0, 0, 0])

r1_y = 232
largeur = 16
hauteur = 128
r_balle = 16
xb = 50
yb = 256 + randint(0,100)-50
vx = 2 + randint(0,2)
vy = 2
couleur = (45, 170, 250)

continuer = True


while continuer :
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = False
        if event.type == KEYDOWN:
            if event.key == K_UP:
                r1_y = r1_y - 8
            else: 
                r1_y += 8
    
    fenetre.fill([0,0,0])
    pygame.draw.rect(fenetre,(255,255,255),(450,r1_y,largeur,hauteur))
    pygame.draw.circle(fenetre, couleur, (xb, yb), r_balle)
    pygame.display.update()
    pygame.time.wait(10)

pygame.quit()

```
-->


## Deplacer la balle
La balle se deplace en modifiant `xb` et `yb` à chaque itération (boucle `while`). Il faudra ajouter la vitesse à chacune de coordonnées:


```python
xb = xb+vx
yb = yb+vy
```

## Prevoir les rebonds
Un rebond, c'est inverser le signe de la vitesse.
Par exemple, lorsque la balle rebondit sur la paroie de gauche, ou bien celle de droite, c'est le signe de `vx`, la vitesse horizontale qui change:

`vx = -vx`

Par contre, la vitesse verticale reste la même. (*Faites-vous un schéma pour visualiser la situation*).

On peut programmer ces conditions dans une fonction, et appeler celle-ci à l'interieur de la boucle principale `while`:

```python
...
def rebond(xb,yb,vx,vy):
	...
	return xb,yb,vx,vy

while continuer:
	...
	xb,yb,vx,vy = rebond(xb,yb,vx,vy)
	fenetre.fill([0,0,0])
	...

```

<!--
# Programme final

```python
import pygame
from pygame.locals import *
from random import randint

pygame.init()
pygame.key.set_repeat(1,20)
fenetre = pygame.display.set_mode((512,512))
fenetre.fill([0, 0, 0])

r1_y = 232
largeur = 16
hauteur = 128
r_balle = 16
xb = 50
yb = 256 + randint(0,100)-50
vx = 2 + randint(0,2)
vy = 2
couleur = (45, 170, 250)

continuer = True

def rebond(xb,yb,vx,vy):
	...
    return xb,yb,vx,vy

while continuer :
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = False
        if event.type == KEYDOWN:
            if event.key == K_UP:
                r1_y = r1_y - 8
            else: 
                r1_y += 8
    
    xb,yb,vx,vy = rebond(xb,yb,vx,vy)
    
    fenetre.fill([0,0,0])
    pygame.draw.rect(fenetre,(255,255,255),(450,r1_y,largeur,hauteur))
    pygame.draw.circle(fenetre, couleur, (xb, yb), r_balle)
    pygame.display.update()
    pygame.time.wait(10)

pygame.quit()

```
-->

## Que reste t-il à faire?
* Les rebonds sur la raquette
* La gestion du score et de la fin de la partie

Pour l'écriture de texte dans la fenêtre pygame, consulter la page suivante sur [stackoverflow](https://stackoverflow.com/questions/20842801/how-to-display-text-in-pygame)

## Retour sur la page 1
[Lien vers le debut du projet](../pygame_pong) 
