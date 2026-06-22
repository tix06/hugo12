---
Title: etude comparée algos de tri
description: TP,  chronometrage time du module time, copie par valeur, melange avec shuffle du module random
hidden: true
weight: 9
---

# Etude comparée des algorithmes de tri
## Explorer le sujet
Les algorithmes de tri sont vus à la page: [rappels sur les algorithmes de tri](../page8/)

Le projet a pour but de faire une étude comparée des 3 algorithmes de tri: insertion, selection et fusion, pour différentes listes d'entiers non rangés.

Le temps de calcul de chaque algorithme dépend de sa complexité. Le graphique suivant (taille de la liste triée en abscisses, temps de calcul en ordonnée), permet ainsi comparer ces différents algorithmes.

{{< img src="../images/DIU_tris_compare.png" caption="comparaison des temps de calculs pour différents algorithmes de tri" >}}

> Vous allez réaliser un programme Python qui permettra de comparer les 3 principaux algorithmes de tri à l'aide d'un graphique. Vous vérifierez ensuite par une étude mathematique si la complexité de chaque algorithme correspond à la courbe obtenue.

## Aides pour la réalisation du projet
### Tracé de courbe de type nuage de points
Le script suivant permet de tracer plusieurs *nuages de points* sur le même graphique.

```python
from matplotlib import pyplot as plt
x = [0, 100, 200, 500, 1000]
y1 = [0, 0.5, 1, 2.5, 5]
y2 = [0, 0.1, 0.4, 2.5, 10]
plt.scatter(x,y1)
plt.scatter(x,y2)
plt.show()
```

### Modélisation
Le script suivant permet de modéliser une courbe à partir de ses points. Le programme permet d'obtenir les coefficients pour un modèle mathématique donné.

```python
import numpy as np
from scipy.optimize import curve_fit

def fit_func(x,a,b,c):
    return a*x**2+b*x+c

x = np.asarray([0, 100, 200, 500, 1000])
y1 = np.asarray([0, 0.4, 1.4, 2.4, 6])

#mise en place de l'outil curve fit (scipy)
params, mcov =curve_fit(fit_func,x,y1,absolute_sigma=True)
# params = coefficients retournés par le calcul de modélisation
# mcov = matrice de covariance, permet de quantifier la variation de chaque variable par rapport à chacune des autres
a = params[0]
b=params[1]
c=params[2]
y_model = [a*n**2 + b*n +c for n in x]
```

On peut alors tracer la courbe `y_model` avec celle de `y1` et juger de la qualité de la modélisation.

## Mesure du temps
Pour mesurer un temps à un moment précis du programme, on utilise la fonction `time` du module `time`.

Pour obtenir la documentation de cette fonction, dans une console Python, faites:

```python
> import time
> help(time.time)
```

*Rappel*: pour mesurer une durée, il faut faire $t=t_2 - t_1$

### Créer une liste non ordonnée de valeurs
Pour mélanger une liste `L0`, utiliser la fonction `shuffle` du module random:

```python
import random
random.shuffle(L0)
```

### Copie par valeur d'une liste

```python
L1 = L0.copy()
```

# Suggestion de projets
L'efficacité d'un algorithme vient aussi de la nature de la liste à trier. Il peut être intéressant de mesurer la durée de tri pour certaines formes de listes particulières (déjà triée, triée en sens inverse, avec des doublons, ...). 

Quel sera l'algorithme le plus *efficace*, le plus *inéfficace*?

Le programme pourrait décider alors du meilleur algorithme en fonction de la nature de la liste.


