---
Title: TP mise au point
description: carre magique, exercice sur les tableaux, matrices, et les tests unitaires avec doctest
hidden: true
weight: 32
---

# Carré magique 
exercice issu du site [zonensi](https://www.zonensi.fr/NSI/Premiere/C04/Tableaux2D/)

Un carré magique d'ordre n est une matrice carrée n*n  telle que que la somme des nombres sur chaque ligne, sur chaque colonne et sur chaque diagonale principale soient égales.

1. Vérifier que la matrice M  est bien un carré magique.:

```python
M = [(4,9,2), (3,5,7), (8,1,6)]
```
 
2. On se propose de construire une fonction vérifiant qu'une matrice de taille n*n  est bien un carré magique:

* Créer une fonction `estCarre(M)` qui vérifie que la matrice est bien carrée (son nombre de ligne est égal à son nombre de colonne). Cette fonction renverra `True` dans ce cas, et `False` sinon.
* Créer une fonction `sommeLigne(M,i)` qui renvoie la somme des nombres de la ligne de la matrice M
* Créer une fonction `sommeColonne(M,i)` qui renvoie la somme des nombres de la colonne 
 de la matrice M
* Créer une fonction `sommeDiagPrincipale(M)` qui renvoie la somme des nombres de la diagonale principale de M. (diagonale dont les éléments ont le même numéro de ligne et de colonne).
* Créer une fonction `sommeDiagSecondaire(M)` qui renvoie la somme des nombres de la diagonale non principale de M
* En utilisant les fonctions précédentes, créer une fonction `estMagique(M)` qui renvoie `True` si la matrice 
 est magique, et `False` sinon.

# Ajouter des tests avec le module `doctest`

Nous allons ajouter à nos fonctions des informations pour limiter les risques d'erreurs de programmation.

Ainsi, dans la fonction `sommeLigne(M,i)`, on ajoutera les lignes dans le docstring:

```
def sommeLigne(M,i):
	"""
	>>> M = [(4,9,2),(3,5,7),(8,1,6)]
	>>> sommeLigne(M,0)
	15
	"""
	# script de la fonction
```

Puis, à la fin du programme:

```python
if __name__ == "__main__":
    import doctest
    doctest.testmod()
```

Maintenant, lorsque vous executez le fichier, le module `doctest` va rechercher tous les tests simulés dans les docstrings, et vérifier les résultats. Un message affichera alors le nombre de tests reussis ou manqués.
    

> Ajouter un test avec son resultat dans chacune des fonctions programmées plus haut.

# Créer un carré magique par tirage aléatoire
> Au debut du programme, placer l'appel du module `random.randint`:

```python
from random import randint
```

La fonction `randint` fait le tirage aléatoire d'un entier compris entre les 2 bornes placées entre paramètres.

*Exemple d'utilisation:*

```python
> M = []
> for j in range(3):
> M.append((randint(1,9),randint(1,9),randint(1,9)))
> M
[(5, 1, 8)]
```

> Utiliser une boucle non bornée sur un nombre d'essais inférieur ou egal à 10000.

```python
while essai < 10000:
```

> A chaque essai:

* remplir une nouvelle fois la matrice `M` avec 3 tuples de 3 valeurs, choisies aléatoirement.
* tester si la matrice `M` est un carré magique.
* s'il s'agit d'un carré magique: sortir de la boucle (on peut utiliser la commande `break`)
* sinon, recommencer

> A la fin (sortie de la boucle):

* Afficher la matrice `M` s'il s'agit d'un carré magique.
* Afficher un autre message sinon. Par exemple: 'non trouvé'

> Testez votre programme. Si celui-ci ne génère pas facilement un carré magique, augmentez le nombre d'essais possible dans la condition d'execution de la boucle.

# Autre sujet: Le repertoire
Enoncé du TP sur la page [levavasseur.xyz](https://www.levavasseur.xyz/NSI_T/TAD/Dictionnaire/nsi_t_dictionnaires.html)

> Utilisez un Notebook sur *CAPYTALE* dans votre session ATRIUM.

