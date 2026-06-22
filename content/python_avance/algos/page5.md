---
Title: TP algos de recherche
weight: 15
hidden: true
---

## Revision d'algorithmes fondamentaux

Nous allons revoir les algorithmes classiques suivants:

- Recherche du maximum
- Recherche du minimum
- Calculer la moyenne d'un tableau
- La recherche en table

On va commencer par créer une liste de nombre aléatoires pour y appliquer nos algorithmes.


```python
# ceci est une cellule de code
# Rappel: appuyez sur CTRL+ENTER pour l'éxecuter

import random

# On crée une liste de 51 entiers entre 0 et 50
ma_liste = [i for i in range(51)]

# On la mélange
random.shuffle(ma_liste)
ma_liste
```

Vous allez maintenant implémenter les algorithmes suivants. Utilisez les spécifications de ces algorithmes lorsqu'elles sont indiquées.

Si la spécification de l'algorithme n'est pas donnée, vous la complèterez vous-même.

Aide : 

* [page python sur les boucles](https://numerix.netlify.app/docs/python/pages/boucles/page1/index.html)
* [page python sur les structures conditionnelles](https://numerix.netlify.app/docs/python/pages/conditions/page1/index.html)
* [page python sur la mise au point d'un script et les specifications](https://numerix.netlify.app/docs/nsi/langages/page5/index.html)


```python
# script get_maximum
"""
L'algorithme recherche la valeur maximale dans la liste.
variables en entrée : 
------------------
ma_liste : list, une liste de valeurs entieres, uniques, mises dans un ordre aléatoires.
max : int, stocke la valeur maximale actuelle. Initialisé à 0.
Sortie :
------
max : int, prend la valeur de l'élément le plus grand de la liste
Principe : 
--------
on parcourt la liste avec une boucle bornée.
si la valeur la valeur de max est inferieure à la valeur courante, max est actualisée avec cette valeur courante
"""
# programme à écrire ici

```


```python
# script get_minimum
"""
L'algorithme recherche la valeur minimale dans la liste.
variables en entrée : 
------------------
ma_liste : list, une liste de valeurs entieres, uniques, mises dans un ordre aléatoires.

** à compléter **

"""
```


```python
# script moyenne
"""
L'algorithme calcule la moyenne des valeurs d'une liste
variables en entrée : 
--------
somme : int, initialisé à 0, stocke la somme des élements de la liste
ma_liste : list, une liste de valeurs entieres, uniques, mises dans un ordre aléatoires.
Sortie :
--------
moyenne : float, moyenne des valeurs de la liste
Principe : 
--------
on parcourt la liste avec une boucle bornée
on ajoute la valeur de l'element de la liste à somme. 
Une fois la liste parcourue, on affecte à moyenne : somme/len(ma_liste) 
"""
```


```python
# script recherche
"""
l'algorithme recherche une valeur dans une liste et renvoie l'indice
Variables en entrée :
-------------------
val : int, valeur à trouver
ma_liste : list, une liste de valeurs entieres, uniques, mises dans un ordre aléatoires.
Sortie : 
------
i : int, indice de la position de la valeur dans la liste
Principe :
--------
on parcourt la liste avec une boucle non bornée, tant que val n'est pas trouvé dans la liste
on augmente la valeur de i à chaque nouvelle itération
"""
```

## Recherche dans une liste de mots

Télécharger la liste de mots `liste_francais.txt` à partir du dépôt suivant: https://github.com/Sicilat/dictionnary-f _(ou utilisez la liste fournie si présente dans votre dossier)_.

**Importer** la liste de mots sous forme de liste et afficher les 13 premiers éléments de la liste (executer la cellule suivante)


```python
# initialisation de la liste vide
mots = []

# Lecture du fichier txt et remplissage de la liste
with open('liste_francais.txt', encoding='iso-8859-1') as f:
    for mot in f.read().splitlines():
        mots.append(mot)
        
# Affichage des 13 premiers mots
print(len(mots))
mots[:13]
```

**Afficher** la longueur de la liste (le nombre d'éléments) : 


```python

```

Sur votre **cahier de labo**, rédiger la spécification de l'algorithme séquentiel d'un mot dans la liste. Puis vous réaliserez l'implementation de cet algorithme. Recherchez le mot *'tracts'* par exemple.


```python

```

