---
Title : Pile
description: pile, structures lineaires, expression correctement parenthesee
weight: 35
---

*Ce cours comporte:*

* les types abstraits: [Lien](../page1)
* Cours sur les Piles: [Lien](../page2)
* Cours sur les Files et listes: [Lien](../page21)
* exercices en ligne (TP) sur les Piles: [Lien](../page22)







# Structure linéaire : La Pile
## Les structures de données
*Definition:* Une *structure de données* est une manière de stocker, d’accéder à, et de manipuler des données (comme les types list ou dict de Python).

*Definition:* Un *type abstrait* décrit essentiellement une interface, indépendamment du  langage de programmation.

## Un premier exemple
La pile est une manière de ranger les données.

Elle correspond exactement à l’image traditionnelle d’une pile de cartes ou d’assiettes posée sur une table. En particulier, on ne peut accéder qu’au dernier élément ajouté, qu’on appelle le sommet de la pile.

L'illustration suivante montre que c'est la structure de données à adopter si l'on veut sortir d'un labyrinthe...

{{< img src="../images/turt.gif" alt="parcours utilisant une pile" caption="parcours pour sortir d'un labyrinthe" >}}
Le labyrinthe peut être modélisé par les coordonnées de ses noeuds, ainsi qu'une liste de directions possibles (ouvertures) pour chacun de ses noeuds : 

{{< img src="../images/laby.png" alt="labyritnhe modelisation" caption="modelisation d'un labyrinthe" >}}
En observant l'animation de la tortue dans le labyrinthe, on peut supposer que la pile des sommets visités (les cases du labyrinthe) sont, dans l'ordre : 

(4,0), (3,0), (3,1), (3,2), (4,2), (4,1) ...

puis le chemin inverse jusqu'au sommet (3,0) : 

(4,2), (3,2), (3,1), (3,0), ...

Une fois revenu au sommet (3,0), on reprend l'exploration vers (2,0), (2,1),... 

Il s'agit d'une méthode d'exploration du labyrinthe de type *parcours en profondeur*. L'algorithme est expliqué en détail à la page : [SNT algorithmes graphe : parcours en profondeur](/docs/SNT_2nde/pages/pages_algo/graphes/page2/#parcours-d-un-arbre-en-profondeur-dfs)

{{< img src="../images/logott.png" alt="turtle" caption="fil d'ariane" >}}
La tortue suit son chemin jusqu'à arriver à une impasse (ou un sommet déjà visité). Alors, elle doit être capable de *revenir sur ses traces*. C'est pour cela qu'elle mémorise son parcours dans une *pile*, qu'elle pourra remonter (c'est à dire *dépiler*) au besoin. Cette pile de sommets visités correspond au fil d'Ariane, rendu célèbre par la mythologie (Thésée et le Minautore).

Lorsqu'elle s'avance plus en profondeur dans le labyrinthe, vers des sommets encore non explorés, elle *empile*.

Lorsqu'elle revient sur ses traces, elle *dépile* (elle retire des sommets de la pile). 

{{< img src="../images/empile.png" alt="empiler depiler" caption="pile de sommets du labyrinthe" >}}
Lorsque la tortue arrive à la case (4,1), l'impasse, la pile a alors la configuration **pile a** (voir schéma plus bas).

Elle revient jusqu'à (3,0). 

Après avoir *dépilé* (4,1),(4,2),(3,2),(3,1), la pile est alors la **pile b**.

Puis, lorsqu'elle est parvenu à une bifurcation vers une nouvelle direction, elle poursuit son exploration (et *empile* à nouveau) : **pile c**. Qu'il faudra encore prolonger pour atteindre la sortie (en bas à droite).

{{< img src="../images/pileL.png" alt="pile DFS" caption="pile du parcours en profondeur" >}}
## Deuxieme exemple : une expression correctement parenthésée

**Principe :** On lit l'expression de gauche à droite et on empile au fur et à mesure les caractères ouvrants : [, {, (. On dépile lorsqu'on lit le caractère fermant correspondant. A la fin, la pile doit être vide.

Dans l'exemple suivant, on voit que l'expression `[a+(b+c)]` est correctement parenthesée. Ce qui ne serait pas le cas pour `[a+(b+c])`.

{{< img src="../images/parentheses.png" >}}
## Définitions
### La pile: interface
La pile est une structure de données appropriée quand :

* On veut stocker des éléments dont le nombre est variable, et inconnu à l’avance.
*  On peut ou on doit se contenter d’accéder au dernier élément stocké.

Dans d'autres cas, il faudra utiliser une autre structure de données, comme par exemple un tableau.

Une <b>Pile</b> est une structure de données <b>linéaire</b> (les données sont rangées sur un ligne ou une colonne). Le dernier élément entré sera aussi le premier à sortir (<b>L</b>ast <b>I</b>n <b>F</b>irst <b>O</b>ut : LIFO).

Les méthodes (= fonctions) disponibles pour cette structure sont : 

* construction (d'une pile vide)
* test d'une pile vide (renvoie `True` si la pile est vide)
* ajout d'un élément (empiler = `push`), mis au sommet de la pile
* retire le premier élément de la pile, celui au sommet (dépiler = pop) si la pile est non vide et renvoie cet élément.
* lire le sommet de la pile



### Implémenter un pile en Python en langage natif

Le type *List* en Python possède déjà toutes les méthodes d'une pile :

```python
pile = []           # creation d'une pile
pile == []          # tester si la pile est vide
pile.append(valeur) # empile valeur dans la pile
pile.pop()         # depiler l'element au sommet
pile[-1]            # lire l'element au sommet de la pile
```

Lorsque l'on fait référence à une structure de données de type *pile* en traduisant un algorithme en Python, il faudra se contenter de ces 5 instructions.

### Créer une nouvelle Interface


Les types abstraits, comme les piles, sont définis par leur **interface** (comment  on s’en sert) plutôt que par leur **implémentation** (comment ils fonctionnent). Ils permettent d’étudier des algorithmes indépendamment  du langage utilisé.  

Rappels: 

* L’*interface* de la structure de données décrit de quelle manière on peut la  manipuler, par exemple en utilisant `append` pour le type list ou `get` pour le type  dict.

* L’*implémentation* de la structure de données, contient le code de  ces méthodes (comment fait Python). Il n’est pas nécessaire de connaître l’implémentation pour manipuler la structure de données. 
 

On verra ici deux manières d'implémenter la *pile*.


### Implémentation fonctionnelle
Pour traduire un algorithme utilisant cette structure *pile*, il peut être préférable de définir des instructions portant les noms de ces 5 instructions:

```python
def Pile():
  """creation d'une pile vide à l'aide de l'instruction : 
  pile = Pile()
  """
  return []

def est_vide(pile)
  # à compléter

def empile(valeur,pile):
  # à compléter

def depile(pile):
  # à completer

def sommet(pile):
  # à completer
```

### Implémentation en Programmation Objet
On peut créer un type (= une **classe**) `Pile` personnelle en Python. 

Les méthodes (fonctions) déclarées précédemment sont alors associées à l'objet `Pile`. L'appel d'une méthode se fait à l'aide de l'instruction : 

```python
pile = Pile()
pile.est_vide()
pile.empile(valeur)
pile.depile()
pile.sommet()
```

Voir le cours sur la [programmation orientée objet](/docs/NSI/structure/page3/).

**Rappel : Objet = type mutable**. Quelle que soit la façon avec laquelle la pile est implémentée, il faudra se souvenir que celle-ci est un objet *mutable*. Cela a des conséquences sur la manière avec laquelle la pile est passée en argument d'une fonction, et comment cette fonction modifie la pile.

## Pile et recursivité
Tout algorithme récursif peut être mis sous forme d'algorithme itératif avec une structure de données en pile.


Voir le cours sur la [recursivité](/docs/NSI/langages/page2/)

<!--
# Résumé

<div class="essentiel">
 <div class="entete">
  L'essentiel
 </div>
 <div class="resume">
  Une <b>structure de données</b> est une manière de stocker, d’accéder à, et de manipuler des données.<br>
  Une <b>Pile</b> est une <em>structure de données</em> <b>linéaire</b> (les données sont rangées sur un ligne ou une colonne). Le dernier élément entré sera aussi le premier à sortir (<b>L</b>ast <b>I</b>n <b>F</b>irst <b>O</b>ut : LIFO).<br>

  <b>Interface</b><br>
  L’<em>interface</em> d'une structure de données décrit de quelle manière on peut la  manipuler.
  Les méthodes (= fonctions) disponibles pour la <em>Pile</em> sont : 
  <ul>
  <li> <b>construction</b> (d'une pile vide)</li>
  <li> <b>test</b> d'une pile <b>vide</b> (renvoie `True` si la pile est vide)</li>
  <li> ajout d'un élément (<b>empiler</b> = `push`), mis au sommet de la pile</li>
  <li> retire le premier élément de la pile, celui au sommet (<b>dépiler</b> = pop) si la pile est non vide et renvoie cet élément.</li>
  <li> lire le sommet de la pile.</li>
  </ul>

  <b>Implementation</b><br>
  L'<em>implementation</em> contient le code de  ces méthodes (comment fait Python). Il n’est pas nécessaire de connaître l’implémentation pour manipuler la structure de données. Il faut connaitre l'interface.<br>
  Pour <b>implémenter</b> une pile en Python, on utilisera les méthodes déjà existantes pour le type <b>List</b> : 

  <pre><code class=language-python data-lang=python>
  pile = []           # creation d'une pile
  pile == []          # tester si la pile est vide
  pile.append(valeur) # empile valeur dans la pile
  pile.pop()         # depiler l'element au sommet
  pile[-1]            # lire l'element au sommet de la pile
</code></pre>

 </div>
</div>
-->

# Exercices sur les piles
voir la page [exercices](../page22)



# Autres structures linéaires
Lien vers la page{{< a link="../page21/" caption="Listes et Files" >}}

# Liens
* cours sur [info.blaisepascal.fr](https://info.blaisepascal.fr/nsi-pile-file/)