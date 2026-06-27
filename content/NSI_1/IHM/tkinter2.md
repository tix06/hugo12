---
Title: Tkinter demineur
description: Tkinter demineur
weight: 9
---

# Canvas et Tkinter
## Principe
Le module Tkinter permet de dessiner dans la fenêtre en ajoutant un objet Canvas. Les fonctions de dessin permettent de tracer des figures, afficher une image... Les éléments sont repérés par leur coordonnées (x,y). Le point (0,0) se situant en haut à gauche.

On verra dans une autre seance que le canvas peut aussi relever la position de la souris lors d'un clic. Et que l'on peut ainsi programmer des jeux.

## But de la séance
Vous allez poursuivre votre appentissage des algorithmes sur les listes, en positionnant les images *bombes* sur une grille du canvas.

## Contenu du projet
Le projet{{< a link="/scripts/Tkinter/tkinter_grille.zip" caption="suivant (fichier zip)" >}}
* canvas.py: le fichier principal qui contient les fonctions de dessin. Ce sera ce fichier qui faudra executer pour afficher la fenêtre graphique. 

* utils.py: C'est le fichier qui contient les fonctions de calcul des positions des bombes. Au depart, ce fichier ne contient que la fonction `position_bombes`. Cette fonction génère une liste de listes adaptée à la grille $L*h$:
  * chaque sous-liste positionne les bombes d'une même ligne (L cases)
  * il y a autant de sous-listes que le nombre de cases en hauteur (h lignes)
  * une valeur 1 dans la sous-liste positionne une bombe. 
  * une valeur 0 signifie case vide

Vous devrez modifier le contenu de la fonction `position_bombes` pour réaliser les grilles proposées.

> Pour executer le programme, ouvrir *canvas.py* avec un IDE python, et *Executer le module* (F5: Run module)

## Que génère la fonction `position_bombes`?
Pour tester la fonction, vous pouvez executer le module `utils.py`, puis appeler dans le shell la fonction avec des arguments choisis.

> Ouvrir le ficher `utils.py` avec votre IDE python. Puis *Executer* le module. Dans le shell, faire:

```python
>>> help(position_bombes)
# retourne les informations sur la fonction
# Pour sortir de la fenêtre de l’aide, appuyer sur la touche q
>>> position_bombes(6,6)
# retourne la liste Bombes générée par la fonction
```


## Les grilles à réaliser
Il vous faudra modifier la fonction `position_bombes` pour realiser chacune de ces grilles.

```python
def position_bombes(L,h):
    """
    grille pleine
    :param L: nombre de cases horizontales
    :param h: nombre de cases verticales
    :return Bombes: matrice de dimension L*h
    retourne une liste de binaires avec la position des bombes
    exemple:
    --------
    >>> position_bombes(

    """




```

{{< img src="../images/tkinter_mines0.png" caption="grille 1" >}}
```python
def position_bombes(L,h):
    """
    ligne horizontale de bombes
    :param L: nombre de cases horizontales
    :param h: nombre de cases verticales
    :return Bombes: matrice de dimension L*h
    retourne une liste de binaires avec la position des bombes
    exemple:
    --------
    >>> position_bombes(
    
    """





```
{{< img src="../images/tkinter_mines1.png" caption="grille 2" >}}
```python
def position_bombes(L,h):
    """
    Premiere ligne verticale
    :param L: nombre de cases horizontales
    :param h: nombre de cases verticales
    :return Bombes: matrice de dimension L*h
    retourne une liste de binaires avec la position des bombes
    exemple:
    --------
    >>> position_bombes(
    
    """





```

{{< img src="../images/tkinter_mines3.png" caption="grille 3" >}}

```python
def position_bombes(L,h):
    """
    diagonale vers le bas a droite
    :param L: nombre de cases horizontales
    :param h: nombre de cases verticales
    :return Bombes: matrice de dimension L*h
    retourne une liste de binaires avec la position des bombes
    exemple:
    --------
    >>> position_bombes(
    
    """





```

{{< img src="../images/tkinter_mines4.png" caption="grille 4" >}}
```python
def position_bombes(L,h):
    """
    position aléatoire de bombes
    :param L: nombre de cases horizontales
    :param h: nombre de cases verticales
    :return Bombes: matrice de dimension L*h
    retourne une liste de binaires avec la position des bombes
    exemple:
    --------
    >>> position_bombes(
    
    """





```

{{< img src="../images/tkinter_mines5.png" caption="grille 5" >}}
*Aide:* on pourra utiliser la fonction `randint(0,1)` du module `random`


# Spécifier la fonction et programmer des tests
## Prototypage
Dans chaque cas, compléter le prototypage de la fonction pour:

* spécifier ce qu'elle doit faire (début du prototypage)
* préciser ce qui est attendu lorsqu'elle est executée avec certaines valeurs choisies pour arguments (fin du prototypage). Ajouter par exemple (compléter):

 ```
 >>> position_bombes(...,...)
 [[...,...,...,...],[...,...,...,...]]
 ```

## Programmer un test automatique
Le doctest est un module qui recherche dans le prototypage de la fonction ce qui pourrait s'apparenter à des tests sur la fonction.

Comme par exemple:

```
>>> position_bombes(2,2)
[[0, 0], [0, 0]]
```

Pour réaliser des tests sur la fonction, on ajoutera alors à la suite du script les lignes suivantes:

```python
if __name__ == "__main__":
    import doctest
    doctest.testmod()
```

Et pour réaliser les tests automatiques, il faudra executer le fichier `utils.py`: Depuis le shell, faire:

```python
>>> python utils.py
```

*Remarque:* la sortie de la fonction doit suivre le *guide de style* python, sinon des erreurs peuvent être générées (absence d'espaces,...). Il s'agit de PEP8 sur [https://python.org](https://python.org).