---
Title: PONG final
hidden: true
---

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
    if xb+vx > 512 or xb+vx<0:
        vx = -vx
    if yb+vy > 512 or yb+vy<0:
        vy = -vy
    xb+=vx
    yb+=vy
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
