---
Title: spirale d'Ulam
description: alignement des nombres premiers sur la spirale, defauts, doctest
hidden: true
weight: 6
---

Voir la page: [TP sur les nombres premiers](../page11)

# Spirale de Ulam
## Principe
En mathématiques, la spirale d'Ulam, ou spirale des nombres premiers (dans d'autres langues, elle est appelée aussi horloge d'Ulam) est une méthode simple pour la représentation des nombres premiers qui révèle un motif qui n'a jamais été pleinement expliqué. Elle fut découverte par le mathématicien Stanislaw Marcin Ulam, lors d'une conférence scientifique en 1963.

[lien wikipedia](https://fr.wikipedia.org/wiki/Spirale_d%27Ulam)

{{< img src="../images/ulam.gif" >}}
## Enoncé du projet
Vous devrez réaliser la spirale de Ulam dans une fenêtre `turtle` en vous inspirant du modèle proposé plus haut. Le programme sera réalisé en langage python. Le programme sera organisé en modules. On pourra consulter [la page suivante](/docs/NSI/langages/page3/) pour la mise en module du script.

## Démarche de projet
1. Vous commencerez par identifer le cahier des charges: Quelles sont les données initiales pour résoudre le problème? Quel est le résultat attendu?

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

# Extension du TP pour projet en Term NSI
* [Sur la page villemin.gerard.free.fr](http://villemin.gerard.free.fr/Wwwgvmm/Premier/Ulam.htm): En poursuivant cette présentation pour une très grande quantité de nombres, on remarque quantité d'alignements.

Ces alignements correspondent à des polynômes du 2e degré du type:

$$y = a.x^2 + b.x + c$$

Tracer alors les valeurs en spirale données par l'une de ces formules. Vérifier à l'aide de tests que vous aurez programmés que la formule choisie donne bien des *nombres premiers*. 

* Comparez la spirale donnée par une formule $y = a.x^2 + b.x + c$ avec la spirale donnée pour une série *complète* de nombres premiers, sur ce même intervale.

* Certains affirment que la sprirale d'Ulam apporte peu d'information sur les nombres premiers, à preuve, le même dessin avec des nombres aléatoires aurait à peu près la même allure. Vérifiez le.

# Liens
* Les nombres premiers, [podcastsciences](https://www.podcastscience.fm/dossiers/2012/09/26/les-nombres-premiers/)
* Comment les nombres premiers protègent vos données: [loic_demeulenaere](https://www.reflexions.uliege.be/upload/docs/application/pdf/2016-12/loic_demeulenaere.pdf)
