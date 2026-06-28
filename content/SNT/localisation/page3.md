---
Title: introduction aux graphes et internet
description: modelisation d'une carte numerique par un graphe
titleHidden: true
weight: 15
---

* {{% badge color="green" icon="heart" %}}culture numer{{% /badge %}} Introduction a la sequence sur la geolocalisation: [Lien](../page1)
* {{% badge color="red" icon="angle-double-up" %}}modelisation{{% /badge %}} Methode d'echolocation et trilateralisation: [Lien](../page2)
* {{% badge color="red" icon="angle-double-up" %}}modelisation{{% /badge %}} Modelisation par un graphe: [Lien](../page3)
* {{% badge color="orange" icon="star" %}}competences{{% /badge %}} TP itineraire d'une croisiere: [Lien](../page4)
* {{% badge color="orange" icon="star" %}}competences{{% /badge %}} TP geoportail: [Lien](../page5)

# Les graphes et internet
{{% badge color="red" icon="angle-double-up" %}}modelisation{{% /badge %}}

Les graphes sont utilisés en mathématiques appliquées pour simplifier la compréhension de tous types de réseaux.

Ce sont des représentations visuelles permettant de relier des objets entre eux.  

Cette théorie regroupe un ensemble de théorèmes et d’algorithmes visant à résoudre divers problèmes liés aux réseaux.

## Relier des noeuds avec des arêtes
Soit un reseau constitué de 6 machines, que l'on symbolisera par 6 ronds A, B ,C ,D, E et F.


{{< img src="../images/ABC.png" alt="sommets" caption="sommets d'un graphe" >}}
Sur une feuille, relier ses sommets ( pour que le graphe soit "connexe"). Imaginez plusieurs types de figures. 

Selon le reseau dessiné entre ces machines, plusieurs scénarios peuvent être envisagés. Il peut y avoir une coupure de l'une des liaisons, ce qui risque d'isoler une partie du reseau, et entrainer des problèmes de fiabilité.

On peut aussi considérer le coût que représente le cablage des machines, qui augmente avec le nombre d'arêtes et leur longueur...

> Questions:

1. Quels sont les avantages et inconvénients de chacun des graphes constuits sur le cahier (complets, en étoile, circulaires en particulier) en termes de fiabilité du reseau, et de coût?

2. Quel graphe montre la connexion la plus solide entre ces différentes machines?
3. Avec un graphe complet ( tous les sommets reliés à toutes les arêtes): 

* exprimer le nombre d'arêtes en fonction du nombre de sommets
* calculer ainsi le nombre d’arêtes d’un graphe complet de 10, puis 20 sommets à l’aide d’un tableau .
* calculer le nombre de connections qu'il faudrait pour relier directement chacun des 3 milliards d'internautes(chiffrede2015) )

**Definitions et remarques:**

* Un graphe est un **ensemble d'arêtes et de sommets**. Ces sommets peuvent constituer des *noeuds* s'ils sont reliés à d'autres sommets par une arête.
* Deux sommets sont **voisins** s’ils sont reliés par une arête.
* Le **degré** d’un sommet dans un graphe est son nombre de voisins.
* Un graphe est dit *connexe* s’il est en *un seul morceau*.
* Un graphe **complet** est un graphe simple dont tous les sommets sont adjacents deux à deux.
* Un **chemin** entre 2 sommets d’un graphe est le **parcours** qui relie ces 2 sommets. On peut présenter le parcours en énonçant les sommets traversés, ou bien les arêtes empruntées.
* La **longueur du chemin** est égale au nombre d’arêtes empruntées.
* il est illusoire d'imaginer que toutes les machines sur internet sont reliées 2 à 2 selon un graphe complet.
* Les données echangées doivent donc transiter selon un chemin avec de nombreux *sauts*, de routeur en routeur.
 
## Enoncé du premier problème sur les graphes
Le problème des sept ponts de Königsberg est connu pour être à l'**origine de la topologie et de la théorie des graphes**. Résolu par Leonhard Euler en 1735, ce problème mathématique se présente de la façon suivante :

il y a une île appelée le Kneiphof, entourée d’un fleuve qui se partage en 2 bras. Les bras de ce fleuve sont garnis de 7 ponts


{{< img src="../images/euler1.png" alt="les ponts de Konigsberg" caption="les ponts de Konigsberg" >}}
Le problème consiste à déterminer s'il existe ou non une promenade dans les rues de Königsberg permettant, à partir d'un point de départ au choix, de passer une et une seule fois par chaque pont, et de revenir à son point de départ.

 Il est possible de vérifier, de manière intuitive, que la promenade demandée n'existe pas. Ce sont au moins deux ponts, bien choisis, qu'il faudrait ajouter ou retirer pour permettre la promenade avec retour initialement cherchée.
 
> Questions:

> * Que modélisent les noeuds du graphe?
* Que modélisent les arêtes du graphe?
* Vérifier que cette *promenade* n'existe pas. 
* Modifier le plan des ponts (avec un nombre minimum de ponts ajoutés) pour rendre cette balade possible.
* Que remarque t-on alors sur la parité du nombre d'arêtes pour chacun des noeuds?


## Modélisation
Euler propose une modélisation qui consiste à désigner chacune des berges par une lettre majuscule, les ponts par une lettre minuscule et à étudier l’existence de listes d’une taille donnée de lettres majuscules. Par exemple, sur la figure précédente, la liste CABD peut correspondre à un parcours de la berge C à la berge A par le pont e, puis de A vers B par le pont a, puis de B vers D par f.

L’impossibilité de passer deux fois par le même pont se traduit par l’impossibilité qu’une liste comporte plus de fois la séquence XY ou Y X qu’il n’existe de ponts entre les berges X et Y.

Pour Euler, une solution est une liste comportant exactement une lettre de plus qu’il n’y a de ponts, et répondant aux contraintes précédentes.

> Testez le vous-même:

> * Repérer les berges par des noms de sommet (A, B, C, D). Et représenter les parcours possibles comme une liste de sommets atteints, en n'empruntant qu'une seule fois chaque pont. 
* Constater alors que la liste-solution n'existe pas.

Euler propose ensuite une règle pour répondre au problème général de promenades sur des ponts :

*Un parcours eulérien est possible si, et seulement si, deux régions au plus ont un nombre impair de ponts y conduisant. Si deux régions ont un nombre impair de ponts y conduisant, le parcours commencera par l’une de ces deux régions.*

## Utilité des graphes
### Implémentation
Les algorithmes développés par les mathématiciens discrets se prêtent bien à l’implémentation informatique, dans la mesure où le graphe est un objet discret aisément représentable de façon **matricielle** ou par **listes chaînées** par exemple:

* Les *réseaux routiers* : les villes sont alors considérées comme des sommets, et les routes comme des arêtes ou des arcs.
* Le *web* : les pages sont considérées comme les sommets, et les liens hypertextes sont les arêtes. 
* Les *réseaux sociaux* : les individus sont les sommets, et leurs connexions sont les arêtes. 
* Les *bases de données*, dans le modèle entité-relation, peuvent être représentées par un *graphe orienté*.

### Résolution de problèmes
La théorie des graphes a donné naissance à une multitude de théorèmes et d’algorithmes.  Chacun d’entre eux a pour objectif de résoudre un problème pratique.

> *Théorème pour la résolution du problème d'Euler: un graphe connexe admet un parcours eulérien si et seulement si ses sommets sont tous de degré pair sauf éventuellement deux d'entre eux.*

Si le graphe modélise un *réseau urbain* (les sommets représentant les sites et les arêtes les liens de communication): par exemple, un *plan de métro*:

* quel est le nombre minimal de changements entre deux stations données ?
* quelles sont les stations que l’on peut rejoindre à partir d’une station donnée, avec un changement au plus ?

## La recherche en mathématiques
La théorie des graphes a connu un essor important et a permis de modéliser de nombreux problèmes:

* Le problème hamiltonien, qui peut paraître proche du problème eulérien. Il s’énonce ainsi : Existe-t-il un chemin ou un circuit passant par tous les sommets d’un graphe une et une seule fois ? Ce problème n’a pas de solution générale aujourd’hui.
* Le [théorème des 4 couleurs](https://www.mathemathieu.fr/art/articles-maths/23-le-theoreme-des-quatre-couleurs#:~:text=Le%20th%C3%A9or%C3%A8me%20des%20quatre%20couleurs,(ayant%20une%20fronti%C3%A8re%20commune).) : Énoncé en 1852 par Francis Guthrie, ce problème a été résolu à la fin du vingtième siècle. Dans sa première forme, il s’énonçait ainsi : peut- on colorier avec quatre couleurs une carte géographique de telle façon que deux régions limitrophes aient une couleur différente? Voir resolution [ici: villemin.gerard.free.fr](http://villemin.gerard.free.fr/Wwwgvmm/Geometri/TopoQGra.htm#:~:text=Th%C3%A9or%C3%A8me%20des%20quatre%20couleurs%20via%20les%20graphes&text=Une%20carte%20color%C3%A9e%20est%20%C3%A9quivalente,ar%C3%AAte%20%C3%A9tant%20de%20couleurs%20diff%C3%A9rentes.)


## Quels problèmes peuvent resoudre les graphes pour *Internet*
La modélisation en graphe du reseau internet peut répondre aux questions:

* tous les noeuds du graphe sont-ils accessibles? deux sites donnés peuvent-ils communiquer ?
* Quels sont les chemins possibles pour relier 2 noeuds A et B?
* Si l'un des chemins est rompu, existe t-il un autre chemin?
* Quel est le plus court chemin pour relier 2 noeuds A et B?

Toutes ces questions peuvent être résolues grâce à un *algorithme* de parcours de ce graphe, dont un exemple sur cette [page, avec le parcours en largeur](../page2/).


