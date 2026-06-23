---
Title: Pygame Snake
description: interface IHM avec pygame, liste chainee
weight: 86
---


# Jeu du Snake avec le module Pygame
*Pygame est une librairie Python apportant la SDL (Simple Directmedia Library), une bibliothèque libre multi-plateformes permettant la gestion du multimédia dans la programmation. Utile pour la programmation de jeux avec graphiques*

Ce projet consiste à realiser (en partie) le jeu *Snake*. Il traite des types abstraits personnalisés.

Le *Snake* est un genre de jeu vidéo dans lequel le joueur dirige un serpent qui grandit et constitue ainsi lui-même un obstacle. Ce jeu est apparu pour la première fois en 1976 (Editeur Gremlin) sous le nom de *Blockade*. Les consoles de jeu à l'époque possédaient un CPU de 8-bit (MOS Technology 6507 @ 1.19 MHz) et une RAM de 128 octets. Depuis, le jeu a connu de nombreux clones.


{{< img src="../images/snake_retro.png" caption="snake retro game" >}}

Le type *serpent* proposera pour interface les fonctions suivantes:

* affiche
* tete
* ajoute_tete
* supprime_queue

Une version de ce projet sur microbit est accessible [ici](/techno/MB/MB_bulles/).

## Editeur
Le module `Pygame` est installé sur votre ordinateur. Utilisez un IDE python comme IDLE ou pyzo.

## Script initial
Le script suivant donne les éléments de base du programme.

```python
import pygame

 
pygame.init()
 
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
 
dis = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

game_over = False
 
x1 = 300
y1 = 300
 
x1_change = 0       
y1_change = 0
 
 
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -10
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = 10
                y1_change = 0
            elif event.key == pygame.K_UP:
                y1_change = -10
                x1_change = 0
            elif event.key == pygame.K_DOWN:
                y1_change = 10
                x1_change = 0
 
    x1 += x1_change
    y1 += y1_change
    dis.fill(white)
    pygame.draw.rect(dis, black, [x1, y1, 10, 10])
 
    pygame.display.update()
    clock.tick(30)
 
 
pygame.quit()
quit()
```

Copier-coller celui-ci dans la fenêtre du fichier `main.py`.



## Creation d'un type abstrait `serpent`
Le *serpent* est un objet qui *stocke les données* d'une certaine manière, et qui propose quelques fonctions utiles pour interragir avec lui (*une interface*). Il s'agit donc d'un *type abstrait*.

Pour représenter le serpent, comme dans le jeu *snake*, les coordonnées des pixels du serpent seront stockées dans une Liste `[(x1,y1),(x2,y2),...]`.

### Interface
Vous allez programmer chaque fonction de l'interface à partir des renseignements suivants. Ces fonctions seront placées dans le proggramme, avant la boucle principale.

* fonction `affiche`

```python
def affiche(S):
    # affiche tous les pixels du serpent
    # a partir de leurs coordonnees dans S
    # utilise une boucle for
```

L'affichage de chaque pixel du serpent necessite une boucle bornée:

```python
for coord in serpent:
    x = coord[0]
    y = coord[1]
    pygame.draw.rect(dis, black, [x, y, 10, 10])
```

* fonction `tete`

 ```python
 def tete(S):
    # retourne les coordonnees x, y de la tete du serpent
    # qui sont stockees dans le dernier element S[-1]
    # sous la forme d'un tuple (x,y)
```

* fonction `ajoute_tete`
Il peut être necessaire d'ajouter un pixel au serpent. Celui-ci s'ajoutera à la fin de la liste de coordonnées:

```
def ajoute_tete(S, x, y):
    # ajoute un tupple (x,y) a la fin de la liste S 
```

* fonction `supprime_queue`

A chaque déplacement, cela ajoute un pixel à la fin de la liste. Il s'agit de la tête du serpent. Il faut alors retirer le premier pixel (`serpent[0]`) si l'on veut que sa longueur reste constante.

{{< img src="../images/depl_snake.png" caption="deplacement du serpent vers le bas" >}}



```python
def supprime_queue(S):
    # decale toutes les valeurs de la liste S vers la gauche:
    # a l'aide d'une boucle bornee sur les indices i:
    # copie toutes les valeurs S[i+1] dans S[i]
    # puis supprime le dernier element
```


### Dans le programme `main.py`

* Définissez une variable qui stocke les coordonnées du *serpent*: `serpent = [(400,200),(400,210), (400,220), (400,230)]`

* Dans la boucle principale:
    * recuperer les coordonnées x1 et y1 de la tête du serpent (utiliser la fonction `tete`)
    * modifier les valeurs de x1 et y1 en fonction de la direction du deplacement
    * Ajoutez des conditions pour que le pixel ne sorte pas de l'écran. On peut faire changer de direction lorsque le bord de l'écran est touché par le pixel: `if x1 > 800 or x1 < 0: ...`
    * Ajouter les coordonnées du pixel x1, y1 à la fin de la liste `serpent` (`ajoute_tete`)
  * Supprimer le premier pixel du serpent, celui placé en `serpent[0]` avec `supprime_queue`
  * Afficher le serpent une fois ses coordonnées recalculées avec la fonction `affiche`.


Le jeu devrait être à present fonctionnel.

## Créer un module
Vous pouvez maintenant améliorer la mise en forme de votre programme: Mettre les fonctions de l'interface dans un nouveau fichier.

Dans le fichier que vous nommerez `utils.py`, déplacer les fonctions: `tete`, `ajoute_tete`, et `supprime_queue`. (Sur *Trinket*, il suffira d'ajouter un nouvel onglet dans l'editeur python et de nommer cet onglet: `utils.py`).

Pour faire référence à ces fonctions, il faudra ajouter la ligne suivante dans le programme `main.py`:

```
from utils import *
```


# Questions

1. Expliquer: Comment le programme gère les déplacements du serpent?
2. Cette gestion des déplacements, est-elle facilitée par l'interface du type *serpent*? Si oui, comment?
3. Quelles fonctionnalités du jeu manque-t-il pour que celui-ci soit complet? 
4. Si vous deviez créer le jeu complet:

* quelles fonctions ajouteriez vous à l'interface serpent?
* Quelle autre structure de données envisageriez-vous?




# Correction fichier main.py
```python
import pygame
from utils import *
 
pygame.init()
 
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
 
dis = pygame.display.set_mode((800, 600))
 
game_over = False
 
x1 = 300
y1 = 300
 
x1_change = 0       
y1_change = 0
 
clock = pygame.time.Clock()

serpent = [(400,200),(400,210), (400,220), (400,230)]

def affiche(S):
    # affiche tous les pixels du serpent
    # a partir de leurs coordonnees dans S
    for coord in S:
      x,y = coord
      pygame.draw.rect(dis, black, [x, y, 10, 10])

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -10
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = 10
                y1_change = 0
            elif event.key == pygame.K_UP:
                y1_change = -10
                x1_change = 0
            elif event.key == pygame.K_DOWN:
                y1_change = 10
                x1_change = 0
    x1, y1 = serpent[-1]
    x1 += x1_change
    y1 += y1_change
    
    if x1 > 800 or x1 < 0: x1_change = -x1_change
    if y1 > 600 or y1 < 0: y1_change = - y1_change
    
    ajoute_tete(serpent,x1,y1)
    supprime_queue(serpent)
    
    dis.fill(white)
    
    affiche(serpent)
    pygame.display.update()
 
    clock.tick(30)


pygame.quit()
quit()
```

# Correction fichier utlis.py
```python
import pygame
def tete(S):
    # recupere les coordonnees x, y de la tete du serpent
    return S[-1][0], S[-1][1]

def ajoute_tete(S, x, y):
    # ajoute un tupple (x,y) a la fin de la liste S
    S.append((x,y))

def supprime_queue(S):
    # decale toutes les valeurs de la liste S vers la gauche:
    # copie toutes les valeurs S[i+1] dans S[i]
    # puis supprime le dernier element
    for i in range(len(S)-1):
        S[i] = S[i+1]
    S.pop()
```

# Microbit: Petit jeu de type Snake en 2D

Se rendre à la page du [TP de term NSI](/techno/MB/MB_bulles/) et approfondir la seance.
# Liens
Ce TP est inspiré de la page [www.edureka.co](https://www.edureka.co/blog/snake-game-with-pygame/)