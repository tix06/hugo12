---
Title: TP algorithme parcours graphes
description: graphonline, reseaux sociaux, die hard 3 le probleme des transvasements
hidden: true
weight: 44
---

* [introduction aux graphes](/docs/SNT_2nde/pages/pages_algo/graphes/page1/)
* [cours sur les graphes. Term NSI](/docs/NSI/structure/page5/)
* [algorithmes de parcours des graphes](/docs/SNT_2nde/pages/pages_algo/graphes/page2/)
* [TP sur l'implementation en python des graphes](/docs/NSI/structure/page6/)
* [TP sur les algorithmes de parcours des graphes (app en ligne)](/docs/NSI/structure/page61/)
* [TP 2 sur la coloration d'un graphe](/docs/NSI/structure/page63/)
* [algorithme de Dijkstra](/docs/SNT_2nde/pages/pages_algo/graphes/page4/)
* [Protocoles de routage](/docs/NSI/architecture/page3/)
* [Arbres](/docs/NSI/structure/page4/)


# Utiliser un outil en ligne
Ouvrir l'application en ligne [https://graphonline.ru/fr/](https://graphonline.ru/fr/)


# Influenceur 
Vous pouvez créer un premier graphe de type: sous-réseaux en étoile. Ce graphe pourrait être la représentation d'un réseau social, ou bien de 2 sous-réseaux interfacés par un routeur.

{{< img src="../images/g1.png" >}}

Une fois le graphe réalisé, explorer le menu des *Algorithmes*, et sélectionner:

* le degré des sommets
* le rayon du graphe
* la *Recherche du plus court chemin* entre 2 sommets éloignés du graphe. 

**Q.a:** Quelle caractéristique du graphe indique la personne la plus influente de ce reseau social? 

**Q.b:** Quel algorithme sur le graphe permet d'optimiser le chemin d'une information qui circule entre 2 sommets?

# Chemin Eulérien
La page [wikipedia](https://fr.wikipedia.org/wiki/Graphe_eul%C3%A9rien) présente ce qu'est un *chemin eulérien*. 

Représenter chacun des 2 graphes suivants, l'un après l'autre, et chercher la présence (ou non) d'un *chemin eulérien* dans une telle figure.

{{< img src="../images/g2.png" >}}

**Q.c:** Comment modifier (à minima) le graphe 2 pour qu'il présente un chemin eulérien? Quelle est la règle sur les degrés des sommets pour qu'il existe un chemin eulérien?

# Problèmes des vases à transvasement
## Die Hard III
Une partie de l'exercice utilise le notebook sur [Capytale](https://capytale2.ac-paris.fr/web/c/759e-5222738)

Dans le film Die Hard III, Mc Clane (Bruce Willis) et Zeus (Samuel L. Jackson) doivent résoudre un problème de transvasement pour éviter une explosion...

L'idée est de conserver **exactement 4L** dans l'un des bidons. On dispose au départ de 2 bidons vides, l'un de 5L, l'autre de 3L. Ils n'ont pas de graduation. On peut les vider complètement, eventuellement l'un dans l'autre.

{{< img src="../images/die_hard.png" link="https://youtu.be/RFo8JR3hiao?si=XHJit316r3erP6Ra" caption="Die Hard III - extrait de l'enigme des 2 bidons" >}}

**Modélisation**: On peut utiliser un pavage de triangles pour les différents états de remplissage des 2 bidons. La distance d'un point à la ligne horizontale du bas indique le volume du petit bidon, B (celui de 3L). Et la distance au côté gauche, le volume du grand bidon, A. Les points ont 2 coordonnées: A,B

{{< img src="../images/diag_triang1.png" caption="diagramme triangulaire des états de remplissage" >}}

Les états possibles de remplissage des bidons sont les points sur les bords du diagramme. En effet, on arrive forcement à une situation où l'un des 2 récipients est vide, ou l'un des 2 complètement plein.

Entre ces états, on passe de l'un à l'autre en suivant un segment de l'un des sommets vers l'autre, d'un bord à l'autre de la figure (à la manière d'une boule de billard). Ce diagramme nous aide à concevoir un graphe orienté dont voici les sommets:

{{< img src="../images/diag_triang2.png" caption="états numérotés à la manière d'un graphe" >}}

**Les sommets du graphe:** Les états A,B

On peut représenter cette correspondance sommet <-> volume d'eau à l'aide du dictionnaire python: (donné pour les 8 premiers sommets)

```python
tab = {1: (0,0),
       2: (1,0),
       3: (2,0),
       4: (3,0),
       5: (4,0),
       6: (5,0),
       7: (5,1),
       8: (5,2)}
```

**Q.d**: Compléter sur [Capytale](https://capytale2.ac-paris.fr/web/c/759e-5222738) le dictionnaire `tab` des états 1 à 16 du diagramme. *Chercher un peu, puis voir la [Solution](../page62) si vous êtes bloqués.*


**Les arêtes du graphe:** Les transvasements 

Les déplacements possibles seront: 

* robinet=>A (on remplit A)
* robinet=>B (on remplit A)
* A=>B, 
* B=>A, 
* A=>vidange (on vide complètement) 
* B=> vidange

Supposons que l'état initial est (A,B) = (0,0). Il s'agit du point 1. On peut remplir complètement: 

* le bidon A: deplacement du sommet 1 au sommet 6 de coordonnées (5,0), arête 1->6
* le bidon B: deplacement du sommet 1 au sommet 14 de coordonnées (0,3), arête 1->14

Le dictionnaire des *sommets adjacents* est alors:

```python
D = {1: [6,14]}
```

Depuis le sommet 2, on peut:

* revenir à 1 en vidant le recipient A (on perd l'eau)
* aller à 6 en rajoutant de l'eau dans A (on remplit complètement)
* aller à 16 en vidant A dans B, jusqu'à ce que B soit plein.

```python
D = {1: [6,14]
     2: [1,6,16]}
```

**Q.e**: Compléter le dictionnaire D des sommets adjacents d'après les règles énoncées pour les transvasements. *Chercher un peu, puis voir la [Solution](../page62) si vous êtes bloqués.*

Le script suivant permet d'établir la matrice d'adjacence à partir du dictionnaire D placé en paramètre:

```python
D = {1: [6,14]
     2: [1,6,16]
     ...
     }

def matrice(D):
    cles = list(D.keys())
    n = len(cles)
    M = []
    for i in cles:
        line = []
        for j in cles:
            if j in D[i]:
                line.append(1)
            else:
                line.append(0)
        M.append(line)
    return M

>>> M = matrice(D)
```

Et la fonction suivante, d'afficher la matrice sous un format compatible avec le logiciel [graphonline.ru](https://graphonline.ru/fr/)

```python
def affiche(M):
    matrice_texte = ""
    for line in M:
        for elem in line:
            matrice_texte += str(elem)+ ','
        matrice_texte += '\n'
    print(matrice_texte)

>>> affiche(M)
```

Vous pouvez alors **copier** la matrice et créer un nouveau graphe à partir de celle-ci dans [graphonline.ru](https://graphonline.ru/fr/), faire **Graph > Adjacency Matrix** puis **coller**.

Utiliser alors l'algorithme de recherche de chemins (*Find all path*) pour trouver le chemin depuis AB = 0,0 jusqu'à AB = 4,3. Sélectionner le plus court chemin pour résoudre ainsi le problème.

**Q.f**: Représenter ce parcours sur votre diagramme (sur feuille). Recopier le chemin parcouru (1=>...=>...). Décrire les étapes au niveau des volumes (différents état): (0,0) => (6,0) => ...


## Problème à 3 bidons, 8L, 5L, 3L
L'énoncé du problème est issu de la page [EFREI, pdf](https://efrei.poupa.net/Th%C3%A9orie%20des%20graphes/EFREI_1516-TG-TD-Exercices.pdf).

Claude dispose d'une bouteille **pleine contenant huit litres** de vin.
Il a dans sa cave une bouteille vide de **cinq litres**, et une autre tout aussi **vide** de **trois litres**.

Aucune des 3 bouteilles n’est graduée, et leurs formes sont vraiment bizarres. Ceci implique que, partant de la bouteille pleine de 8 litres et de la bouteille vide de 5 litres, il n’est pas possible de verser 4 litres de la première dans la seconde puisqu’on n’a aucun moyen permettant de s’arrêter à 4 litres exactement. 

On ne maîtrise finalement que des transvasements qui consistent à vider entièrement
une bouteille et/ou en remplir complètement une autre.

Claude désire partager le vin en deux parts de quatre litres chacune sans utiliser aucun autre moyen de mesure. Ces deux parts de quatre litres doivent être contenues dans deux bouteilles.

La solution à ce problème peut se formaliser à l'aide d'un diagramme triangulaire, déjà vu dans l'exercice précédent:

{{< img src="../images/diag_triang3.png" caption="diagramme triangulaire adapté au problème à 3 bidons: numérotation des sommets" >}}

Les états correspondent aux volumes ABC et peuvent être disposés sur le contour de la forme à l'interieur du triangle (parallélogramme):

{{< img src="../images/diag_triang4.png" caption="diagramme des états... à compléter" >}}

Indiquez-lui la façon de procéder au moyen d'un graphe.
Vous devez pour cela :

- définir le graphe que vous utilisez de façon formelle (sommets, arcs ou arêtes) ;
- l'implémenter en python
- executer l'algorithme de parcours de ce graphe pour trouver un chemin du sommet initial au sommet final
- énoncer la solution en terme de graphe et de problème que l'on résoud de façon classique sur un graphe.

*Aide et [correction](../page62)*

# Liens
* résolution du problème à 3 vases à l'aide d'un diagramme triangulé: [ilemaths.net](https://www.ilemaths.net/sujet-strategie-des-3-vases-710723.html)
* problème de transvasement illustré: [Gérard Villemin](http://villemin.gerard.free.fr/aJeux1/Mesure/Transvas.htm)
* La sociologie structurale, appelée maintenant analyse de réseaux a développé une grande panoplie de métriques pour caractériser les réseaux sociaux... [Mémoire de maitrise par FRANCK GOUDJO](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwiZoKiDmZyEAxUfQ6QEHZ5kBawQFnoECBcQAQ&url=https%3A%2F%2Farchipel.uqam.ca%2F3672%2F1%2FM11510.pdf&usg=AOvVaw0GqGUBx-QWUzPAEfpdhgfv&opi=89978449) sur la Réalisation d'un outil de simulation de réseaux sociaux 

# Compléments
**Pourquoi un diagramme triangulé pour la résolution?**

Dans ce diagramme, les déplacements se font le long d'un côté d'un triangle equilatéral: la diminution d'une unité pour l'un des récipients se fait avec l'augmentation d'une unité d'un autre récipient. Le volume total reste constant.

Dans ce diagramme, seuls quelques deplacements sont possibles, en rapport avec la règle énoncée au départ (pas de sous-graduations, possibilité ou non de vider l'un des récipients en dehors des autres).

Lorsque l'on vide le récipient A dans un autre (le B), il y a 2 choix:

* Soit on vide complètement le A: Les états tels que A,B => 0,B sont reliés par une arête du graphe, quel que soit B final et quel que soit A initial.
* Soit on remplit complètement B: Les états A,B => A, max(B) sont reliés par une arête quel que soit A final.





