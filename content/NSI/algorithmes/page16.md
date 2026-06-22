---
Title: banc de poissons
hidden: true
---

# Projet banc de poissons
Le comportement des poissons, lorsqu'ils sont en grands groupes, montre une forme d'organisation que l'on assimile souvent à une sorte d'intelligence distribuée. On peut la simuler en modélisant le comportement de chaque individu, en prenant des informations sur ses voisins.

Ainsi, la direction et la vitesse de déplacement de chaque individu sont dictées par celles de ses proches voisins, et sont une combinaison de:

* *séparation*: chaque individu essaie de s'éloigner de ses voisins
* *alignement*: chaque individu avance dans la direction moyenne de ses voisins
* *cohésion*: chaque individu avance vers le centre de masse de ses voisins.

{{< img src= "../images/poissons.png" caption="banc de poissons" >}}

Le module suivant, `poisson.py` apporte la fonction `poisson` qui retourne les coordonnées des points qui dessinent un poisson.

> fichier `poisson.py`: {{< a link="/scripts/lib_projets/poisson.py" caption="cliquer pour telecharger" >}}

## Script minimal pour animer un poisson

```python
import numpy as np
import matplotlib.pyplot as plt
from random import randint
from poisson import poisson

plt.axis([0, 200, 0, 160]) 
C1 = (100,100)
angle_dep = 180
r = 30

C2 = (120,90)

for i in range(200):
    C1 = (C1[0]+randint(-8,8),C1[1]+randint(-8,8))
    angle_dep = angle_dep+randint(-15,15)
    x,y = poisson(C1,angle_dep,r)
    if i == 0:
        line, = plt.plot(x, y)
    else:  
        line.set_data(x, y)
    plt.pause(0.05) # pause avec duree en secondes
    
plt.show()
```