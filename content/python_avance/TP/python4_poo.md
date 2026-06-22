---
Title : TP Python4 POO
BookShowToc : False
hidden: true
---

<!--
Vous pouvez utiliser un notebook colab de votre Google Drive pour rediger le script de l'exercice 3:

* [tuto bref en anglais](https://www.tutorialspoint.com/google_colab/your_first_colab_notebook.htm) 
* et [tuto ici en français](https://ledatascientist.com/google-colab-le-guide-ultime/) 
-->

# Projet labyrinthe
## Principe
Vous allez programmer un jeu de parcours d'un labyrinthe, case après case, en partant du repère **D**. Le joueur devra cliquer dans une case adjacente à celle de sa position, selon les ouvertures possible. 

Le jeu fournit un bouton *retour en arrière*: ![](../images/retour.png) 

Celui-ci permet de retirer la dernière case du parcours du joueur, c'est à dire, ...*revenir en arrière d'une case*.

Le parcours du joueur sera donc stocké dans une *Pile*, qui sera définie à partir de la classe `Pile`.

Voici le résultat attendu: [https://trinket.io/embed/python/26f37880fa](https://trinket.io/embed/python/26f37880fa)

<iframe src="trinket.io/embed/python/26f37880fa" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

## Interface graphique
L'interface graphique est fournie par la librairie `Processing`.  Cette librairie apporte des fonctions utiles pour dessiner dans la fenêtre graphique, mais aussi interragir: On pourra ainsi cliquer dans les cases du labyrinthe, et avoir en retour les coordonnées en pixel, avec pg.mouse.x et pg.mouse.y. La fenêtre graphique est automatiquement mise à jour. Il faudra mettre dans une fonction `draw` toutes les instructions de tracé. Et finir le programme par l'instruction `pg.run()`.

La partie graphique du jeu est programmée dans le fichier `laby.py`. Celui-ci contient la classe `Laby` qui offre les méthodes de classe `__init__`, `contour`, `case_2_xy`, et `x,y_2_case`

* `__init__` qui prend en paramètres les dimensions du labyrinthe: largeur, hauteur, et la liste `murs`.
* `contour`: (sans paramètre) qui trace les murs du labyrinthe dans la fenêtre graphique
* `case_2_xy`: de paramètres `case_x` et `case_y`, les coordonnées d'une case du labyrinthe. Retourne les coordonnées en pixels du centre de la case en fonction de ses coordonnées.
* `x,y_2_case` : de paramètres x,y (en pixels) et retourne les valeurs `case_x`, `case_y`. Cette fonction fait l'inverse de la précédente.

La coordonnée de la case départ vaut par exemple (0,0), celle du dessous, (0,1),... comme illustré sur l'image suivante:

{{< img src="../images/depart.png" caption="repérage des cases du labyrinthe" >}}

Ainsi, lorsque l'on clique dans une case du labyrinthe: les fonctions `pg.mouse.x` et `pg.mouse.y` renvoient la position en pixels du clic dans la fenêtre graphique. Si l'on souhaite connaitre la coordonnée de case correspondante, on utilisera la fonction `xy_2_case`.

Supposons que l'instance de classe Laby soit `mon_laby`, on fait:

```
mon_laby.case_2_case(pg.mouse.x,pg.mouse.y)
```

## Travail pratique
Les instances de classes seront:

* `mon_laby` pour l'objet *labyrinthe* (ligne 38)
* `mon_parcours` pour la pile des cases empruntées. (ligne 29)

L'editeur se situe à la page [https://trinket.io/embed/python/26f37880fa](https://trinket.io/embed/python/26f37880fa)

### Programmer la classe `Pile`
> A vous de joueur:

> **activité 1:** compléter le script de la classe `Pile` avec les fonctions prévues par son interface: `push`, `pop`, et `head`. Ces méthodes ont été vues en cours.

### Programmation du jeu
> A vous de joueur:

> **activité 2:** Dans la fonction `mousePressed`: 

> **1.** affecter à une variable `choix` les coordonnées de cases retournées par la methode `direction` de l'objet `mon_laby`. Cette méthode prend en paramètre le dernier élément de la pile des cases visitées: `mon_parcours.head()`:

```
choix = mon_laby.directions(...)
```

Pour une case donnée, `choix` est la liste des cases accessibles, par exemple, lorsque l'on se trouve en (0,1), la liste choix contient: `[(1,1), (0,2)]`, montrant que l'on peut aller vers l'Est (1,1), et vers le Sud (0,2).

> **2.** affecter aux variables `colonne, ligne` les coordonnées de cases retournées par la méthode `xy_2_case` de l'objet `mon_laby`. Mettre en paramètre `pg.mouse.x,pg.mouse.y`.

```
colonne,ligne = mon_laby.xy_2_case(...)
```

> **3.** ajouter une instruction conditionnelle pour ajouter la case cliquée (colonne,ligne):

> si le tuple (colonne,ligne) est dans la liste `choix`, et s'il ne fait pas partie des cases déjà parcourues (`not mon_parcours.include((colonne,ligne))`), alors ajouter (`push`) le tuple dans `mon_parcours`.

> **4.** ajouter une instruction conditionnelle pour retirer la dernière case lorsque l'on clique sur *Retour*:

```
if pg.mouse.x > 10 and pg.mouse.x < 30 and pg.mouse.y > mon_laby.get_hauteur() :
```

> Ce bloc conditionnel devra contenir une nouvelle instruction conditionnelle, qui retire le dernier élément de `mon_parcours` si celui-ci contient plus d'un élément (on ne veut pas retirer la premiere case (0,0). Utiliser la méthode de classe `Pile` appelée `pop()`.

> Testez alors votre jeu. Vérifiez que vous pouvez bien revenir en arrière lorsque vous prenez une mauvaise direction...

# Extension du TP: projet pour term NSI
* Programmez une première méthode de résolution du labyrinthe par l'ordinateur, en utilisant la structure de données en pile. On pourra adapter la méthode de parcours d'un [graphe en largeur ou bien en profondeur](/docs/SNT_2nde/pages/pages_algo/graphes/page2/). La pile permettra de revenir en arrière dans l'exploration du labyrinthe.
* Le jeu pourrait proposer plusieurs labyrinthes. Et comparer la résolution du joueur avec celle de l'ordinateur.
* On peut programmer plusieurs méthodes de résolution du labyrinthe. Et comparer leur efficacité pour un labyrinthe donné.

<iframe src="https://trinket.io/embed/python/0b360ad25a" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>