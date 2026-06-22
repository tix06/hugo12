---
Title: nombres premiers
hidden: true
weight: 5
---

# Algorithmes des nombres premiers
## Definition
Nombre premier: un nombre premier est un nombre qui accepte DEUX diviseurs : uniquement lui-même et 1.

## Algorithme naïf
Un test de primalité est un algorithme permettant de savoir si un nombre entier est premier.

Le test le plus simple est le suivant : pour tester N , on vérifie s’il est divisible par l’un des entiers compris au sens large entre 2 et N − 1. Si la réponse est **positive (True)**, alors **N est premier**, sinon il est composé (multiple).

Les nombres 0 et 1 ne sont **pas** considérés comme premiers.

> Pseudo code:

```
Fonction prem1(n): 
    Si n = 0 ou n = 1 alors: retourner Faux
    Pour i de 2 à n − 1 faire:
        Si i divise n alors: 
            retourne False
    Fin Pour 
    Retourner Vrai
```

> Questions:

> 1. Implémenter ce pseudo code en python dans un notebook

> 2. Déterminer le nombres d'opérations T(100) réalisées pour n = 100. On considèrera comme opérations significatives les *opérations arithmétiques* et les *comparaisons*. Les comparaisons réalisées dans l'instruction `Pour ... faire:` ne seront pas comptées. Seules les instructions DANS la boucle seront considérées significatives.

<br>

> Amélioration: nous allons modifier la borne supérieure dans la boucle, et diminuer le nombre d'opérations...

Soit n un entier supérieur ou égal à 2.
Si n n’est pas premier, et si d est son plus petit diviseur supérieur ou égal à 2, on peut écrire :
$$n=d\times quotient,~avec~d \leq quotient$$

Imaginons par exemple que l'on recherche les diviseurs de 54:
Les diviseurs sont 2, 3, 6, 9, 18, 27. 

Mais 18 et 27 sont egalement multiples de 2 et de 3. Donc, pour tester si un nombre est premier, il ne sera pas necessaire de tester toutes les valeurs de d. En pratique, il suffira de tester si n est divisible par des valeurs de d telles que: $$d \times d \leq n$$ 
C'est à dire des entiers dont le carré est inférieur ou égal à n.

> Questions:

> 1. Modifier le code dans une nouvelle fonction (que vous renommerez `prem2`) pour que celle-ci execute le moins d'opérations possibles. (soit le plus efficace).

> 2. Déterminer le nombre d'opérations T(100) réalisées pour n = 100.



## Votre fonction, calcule t-elle bien?

1. Programmer une fonction `liste_prime` qui utilise votre fonction `prem2` pour établir la liste des nombres premiers de 0 à 100.
2. Faites une recherche documentaire pour trouver la liste des nombres premiers entre 0 et 100. Appelons cette liste `wiki`
3. Programmer une fonction `compare` qui détermine si tous les nombres de votre liste (donnés par `prem2`) font partie de celle `wiki`.

## L'algorithme le plus efficace
L'algorithme le plus **efficace** est celui qui prend le moins de temps pour effectuer la même tâche.

On peut mesurer le temps d’exécution des programmes à l’aide du module `time`. Après avoir importé le module, il suffit de créer une variable `t = time.time()` que l'on mettra au debut de la fonction `liste_prime`.

Puis avant la sortie, d’afficher en console (print) le temps écoulé avec l’instruction : `print(time.time()-t)`.

> Tester les différentes fonctions prem1, prem2 avec les entiers premiers. Choisir une plus grande valeur pour N (10000 par exemple).

## Créer vos modules de test
Vous allez maintenant realiser un test unitaire sur votre fonction `prem2`.
Pour faire cela, vous allez réorganiser vos fonctions dans différents fichiers, et créer des *modules*.

Suivre l'énoncé du TP à la page [/posts/python/Python_unittest_np/](/posts/python/Python_unittest_np/)

# Suite
* [TP la spirale d'Ulam](../page12)

# Liens
* Les nombres premiers, [podcastsciences](https://www.podcastscience.fm/dossiers/2012/09/26/les-nombres-premiers/)
* Comment les nombres premiers protègent vos données: [loic_demeulenaere](https://www.reflexions.uliege.be/upload/docs/application/pdf/2016-12/loic_demeulenaere.pdf)

<!--
# Spirale de Ulam
## Principe
En mathématiques, la spirale d'Ulam, ou spirale des nombres premiers (dans d'autres langues, elle est appelée aussi horloge d'Ulam) est une méthode simple pour la représentation des nombres premiers qui révèle un motif qui n'a jamais été pleinement expliqué. Elle fut découverte par le mathématicien Stanislaw Marcin Ulam, lors d'une conférence scientifique en 1963.

[lien wikipedia](https://fr.wikipedia.org/wiki/Spirale_d%27Ulam)

{{< img src="../images/ulam.gif" >}}
## Enoncé du projet
Vous devrez réaliser la spirale de Ulam dans une fenêtre `turtle` en vous inspirant du modèle proposé plus haut. Le programme sera réalisé en langage python. Le programme sera organisé en modules. On pourra consulter [la page suivante](/docs/NSI/langages/page3/) pour la mise en module du script.

## Démarche de projet
1. Vous commencerez par identifer le cahier des charges: Quelles sont les données initiales pour résoudrre le problème? Quel est le résultat attendu?

2. Vous ferez une recherche documentaire utile pour déterminer les fonctions et instructions python dont vous aurez besoin.

3. Vous définirez les différentes parties qui constituent le projet.

4. Vous établirez un plan d'action: par quoi allez vous commencer? (une premiere approche du dessin turtle, une fonction qui calcule des nombres premiers...). Comment le programme sera t-il écrit au début? (un IDE en ligne, un notebook, un IDE installé sur votre ordinateur)...

5. Enfin, vous ajouterez des [assertions](http://localhost:1313/docs/NSI/langages/page5/#assertions) ou des tests unitaires à votre projet afin de valider les différentes étapes: voir la page [langage/mise au point](/docs/NSI/langages/page5/#créer-un-module-de-test-avec-unittest)

## IDLE python
L'IDLE python fait partie de l'environnement *Winpython*. L'interêt de cet IDE est sa bonne gestion des fenêtre graphiques que vous allez ouvrir et fermer.

Pour le lancer, aller dans le menu Démarrer du PC, puis choisir IDE python.

Seule la fenêtre d'edition s'ouvre alors. Vous pouvez y taper ou coller votre script python. Pour executer : Touche **F5**.

Deux autres fenêtres s'ouvrent alors: 

* la fenêtre graphique (turtle, Tkinter)
* la console interactive (le shell).

Vous pouvez alors organiser vos fenêtres comme sur l'image suivante.

{{< img src="../images/idlePython.png" caption="A gauche, l'editeur python, à droite les fenêtres graphique et le shell" >}}
-->
