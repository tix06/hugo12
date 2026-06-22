---
Title : modularité
weight: 30
---

Ce chapitre comprend 2 pages de cours et une page exercices:

* La mise au point d'un programme: [Lien 1](../page5)
* Création et utilisation de modules: [Lien 2](../page3)

La liste des projets se trouve [ici](/docs/NSI/NSI_TP_algo/)

# Modularité
## Qu'est ce qu'un module ?
Un module est un fichier python (d'extension .py) contenant des fonctions.
En principe, il n'est pas prévu pour être executé. Pour faire référence aux fonctions de ce module, il faut l'*importer* depuis le script principal (ìmport module.py`).

## Quand utiliser un module ?
Lorsque vous réalisez un projet en python, votre script s'agrandit, et vous aurez certainement le besoin de séparer votre code dans plusieurs fichiers. 

Ainsi, il vous est facile de réutiliser des fonctions écrites pour un programme dans un autre sans avoir à les copier.

## Mettre son programme sous forme de modules
On a vu la différentes manières d'importer un module dans le cours [Python > Fonctions](/docs/python/pages/fonctions/page1/#importer-des-fonctions)

On peut souhaiter, par exemple, créer une représentation graphique des nombres premiers dans une fenêtre `turtle`. On souhaite diviser les fonctions dans 2 fichiers:

* le fichier executable (appelé le fichier *main*): imaginons que vous lui donniez le nom `nombresPrem.py`. Ce fichier ne contiendra que les fonctions relatives au calcul des nombres premiers. On y mettre aussi l'instruction qui appelera la fonction de dessin du module. C'est elle qui construira et dessinera dans la fenêtre graphique.
* le fichier module de nom `fcts_turtle.py` qui contiendra toutes les fonctions utiles pour la représentation graphique. On supposera que ce fichier contient la fonction `ulam` qu'il faudra appeler pour declencher le tracé.

Le dossier contient alors:
  
{{< img src="../images/page3/modules.png" >}}
Le fichier principal `nombresPrem.py` sera organisé comme ceci:


```python
#####partie import des modules############
import fcts_turtle

#####variables globales####################
# declaration des variables globales

#######definition des fonctions############
# def des fonctions du fichier main
# pour le calcul des nombres premiers

######corps du programme : ################
### à executer si fichier main ############
if __name__=='__main__':
    # calcul d'une liste de nombres premiers
    # appel de la fonction de dessin du module:
    fcts_turtle.ulam(liste_premiers,N)
###########################################
```

Il est recommandé de mettre les instructions du programme principal dans un bloc avec le test `if __name__=='__main__':` 

Ceci permet d'importer le contenu du fichier sans déclencher son execution; et permettre de realiser des tests sur les fonctions. Voir{{< a link="/docs/NSI/langages/page5/#créer-un-module-de-test-avec-unittest" caption="tests sur les modules avec unittest" >}}


Le module `fcts_turtle.py` : 

```python
"""
    DOCSTRING
"""
#####partie import des modules externes###
import turtle

#######definition des fonctions du module#
# fonction de dessin de la fenêtre
# fonction ulam(liste_premiers,N)
##########################################
```

**Remarque :** Il est essentiel que le module comprenne un docstring BIEN documenté.

# Gérer les modules
## depuis le shell python
Il est possible de parcourir les dossiers du disque dur, travailler sur les fichiers, etc, comme avec un shell Unix. Depuis le notebook ou bien depuis un shell python, il faut commencer par importer le module `os`. Les instructions utiles sont :

* `listdir()` pour lister 
* `getcwd()` pour obtenir le chemin (CWD = « Current Working Directory »)
* `chdir()` pour changer de dossier

```python
import os
os.listdir() 
# renvoie la liste des fichiers et dossiers:
['fenDestroy.py',
 'fcts_turtle.py',
 'tk_turtle.py',
 '__pycache__',
 'spirale_ulam.py',
 'nombresPrem.py']
```

```python
os.getcwd()
# donne le chemin du dossier courant
'/Users/nom_user/Applications/python/dessins'
```

```python
os.chdir('..') # permet de remonter au dossier parent
os.getcwd()
# affiche '/Users/nom_user/Applications/python`
os.chdir(`dessin/turtle`) # se deplacer dans un sous dossier
os.getcwd()
# affiche '/Users/nom_user/Applications/python/dessins/turtle`
```

Une différence avec le shell Unix est le traitement des noms de fichiers et dossiers qui sont mis entre guillemets. Ce sont des chaines de caracteres pour python.

## Afficher le contenu et l'aide d'un module
depuis le shell python, se placer dans le repertoire contenant le module ou adapter le chemin, puis: 

* importer le module
* lister les fonctions contenues dans le module avec `dir(nom_du_module)`

*Exemple avec le module `fcts_python.py`:*

```python
import fcts_turtle
dir(fcts_turtle)
# affiche
['fenDestroy.py',
 'fcts_turtle.py',
 'tk_turtle.py',
 '__pycache__',
 'spirale_ulam.py',
 'nombresPrem.py']
```

Afficher les fonctions et le *Docstring* du module et des fonctions: `help(nom_du_module)`:

```python
import fcts_turtle
help(fcts_turtle)
# affiche :
Help on module fcts_turtle:

NAME
    fcts_turtle

FUNCTIONS
    close_window()
    
    ulam(premiers, N, L=220, h=220)
```


*Rq:*  Notez que le fichier est bien enregistré avec une extension `.py` et pourtant on ne la précise pas lorsqu'on importe le module.

Et si le *Docstring* du module est présent:

```python
import fcts_turtle
help(fcts_turtle)
# affiche:
Help on module fcts_turtle:

Help on module fcts_turtle:

NAME
    fcts_turtle - module pour visualiser les nombres premiers

DESCRIPTION
    fonctions utiles pour tracer une spirale avec turtle.

FUNCTIONS
    close_window()
    
    ulam(premiers, N, L=220, h=220)
        represente la spirale de Ulam
        
        Params
        ------
        premiers: list
            les nombres premiers
        N: int
            derniere valeur de la spirale
        L: int
            dimension du rectangle en largeur. 220px par defaut
        h: int
            dimension du rectangle en hauteur. 220 px par defaut
        
        Principe
        --------
        Les nombres sont ecrits sur la spirale. En rouge si le nombre est premier, en noir sinon.
        
        Appel
        -----
        ulam(premiers,100) # tracé de la spirale avec la liste de nombres premiers mis en argument, jusqu'à N=100.
```


## Créer le Docstring d'un module
Un *docstring* est un commentaire multi-lignes utilisé pour documenter des modules, des classes, des fonctions et des méthodes. Il doit s'agir de la première déclaration du composant qu'il décrit.

Une bonne docstring de fonction doit contenir tout ce dont un utilisateur a besoin pour utiliser cette fonction. Une liste minimale et non exhaustive serait :

* ce que fait la fonction,
* ce qu'elle prend en argument,
* ce qu'elle renvoie.

> En pratique

* démarrer le fichier par un commentaire multi-lignes qui documente le module
* ajouter le prototype de chaque fonction selon la méthode vu dans le cours [langage/mise au point](/docs/NSI/langages/page5/#prototypage-d-une-fonction)

Voici un exemple de commentaire multi-lignes pour présenter le module (mis à la premiere ligne du fichier):

```
"""module pour visualiser les nombres premiers

fonctions utiles pour tracer une spirale avec turtle.
"""
```
ce qui renvoie à l'aide de la commande `help(module)`:

```
Help on module fcts_turtle:

NAME
    fcts_turtle - module pour visualiser les nombres premiers

DESCRIPTION
    fonctions utiles pour tracer une spirale avec turtle.

FUNCTIONS
    (prototype de chaque fonction)
```


# Liens
* Modularité - document source : [python.org](https://docs.python.org/fr/3/tutorial/modules.html)
* Fiche recapitulative des instructions du module `os` : [Github YannBouyeron](https://gist.github.com/YannBouyeron/941817d79b83a4b87c5a63580229cbbd)
* conventions d'écriture des Docstrings [RIPtutorial](https://riptutorial.com/fr/python/example/30002/ecrire-de-la-documentation-a-l-aide-de-docstrings)


