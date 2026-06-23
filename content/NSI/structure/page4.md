---
Title : arbres
description: arbres, binaires, implementations
weight: 50
---

Ce cours comporte plusieurs pages:


* [cours sur les graphes. Term NSI](../page5/)
* [TP sur l'implementation en python des graphes](../page6/)
* [Arbres](/docs/NSI/structure/page4/)
* [TP](../page41) sur la notion d'arbre couvrant



# Arbres
## Définitions
Un arbre est constitué de **noeuds** organisés de manière **hierarchique**: c'est un **graphe non orienté, connexe, sans cycle**, dans lequel on a choisi un noeud particulier appelé la **racine**.

Chaque noeud peut être étiqueté  par une information.

Un arbre est donc un cas particulier des graphes. Voir la [page suivante sur les graphes](/docs/NSI/structure/page5/)

On parle de *descendants* pour les noeuds *fils*.

Des **exemples** d'arbres:

* l'*arbre généalogique* est un bon exemple. Le vocabulaire sur la structure des arbres s'inspire d'ailleurs de la génélogie (père-fils).

{{< img src="../images/family_tree.png" caption="family tree sur freepik.com/genealogie" >}}

*Les noeuds sont ...les couples*.

* L'arbre représentant les sytèmes de dossiers sur ordinateur (dossiers et sous-dossiers puis fichiers)Ci-dessous l'arborescence de fichiers dans un *raspberry-Pi*:

{{< img src="../images/arborescence_linux.jpg" caption="arborescence linux" >}}


* arbre représentant des expressions arithmétiques

{{< img src="../images/arbre2.png" alt="expression arithmetique" caption="Retrouver l'expression arithmetique correspondante" >}}
Les arbres sont très utilisés en informatique, d'abord parce que les données sont souvent hierarchisées, et se prêtent bien à cette structure. Mais aussi parce que l'accès à ces données est alors plus efficace: la recherche d'une valeur se fait en *O(log(n))* dans le cas moyen, où n est la *taille de l'arbre*.

## Caractéristiques d'un arbre

{{< img src="../images/arbre3.png" alt="caracteristiques d" caption="exemple d'arbre binaire et vocabulaire" >}}
* Dans un arbre, chaque **valeur** est stockée dans un nœud. On appelle parfois cette *valeur* une **clé**.
* Les **nœuds** sont connectés par des **arêtes**, ou **branches** qui représentent une relation de type "**parent** (prédécesseur est le terme exact) – **fils**".
* Chaque noeud ne possède qu'**un seul noeud parent** (sauf le noeud racine).
* La **racine** est le seul nœud qui n’a pas de prédécesseur.
* Les nœuds qui n’ont pas de fils sont appelés des **feuilles**.
* Des nœuds qui ont le même père sont appelés des **frères**.
* Un **sous-arbre** c’est une portion de l’arbre. C'est une notion utile pour la recursivité.
* Le **niveau d’un nœud** est la distance qui le sépare de la racine... Sachant que le niveau de la racine est 0 et que le niveau d’un nœud quelconque c’est 1+ le niveau de son père.
* La **hauteur** d'un arbre, ou sa **profondeur** est égale au *niveau* (à la profondeur) du noeud le plus profond. Selon la convention proposée ici (le niveau de la racine vaut 0), la hauteur correspond aussi au **plus grand nombre de branches** depuis la *racine* jusqu'à l'une de ses *feuilles*.
* Le **degré** d'un arbre est egal au plus grand des degrés de ses noeuds.
* Un arbre de **degré** égal à 1 est ... une **liste**.

{{< img src="../images/arbre7.png" alt="degré d" caption="Quel est le degré de cet arbre?" >}}

* La **taille** d'un arbre est son nombre de noeuds.

{{< img src="../images/arbre5.png" alt="dimensions d" caption="dimensions d'un arbre" >}}
## Arbres binaires
* **Arbre binaire:** arbre de degré égal à 2. Chaque noeud a au plus 2 fils: le **fils droit** et le **fils gauche**.
* **Arbre binaire équilibré:** pour chaque noeud interne, les sous-arbres gauche et droit ont une même hauteur (ou qui diffère d'une unité).
* **Arbre binaire complet:** tous les niveaux de l’arbre sont remplis.

La **taille** d'un arbre binaire peut alors se déduire de la formule, qui prend la profondeur `p` en paramètre:

$$T = \sum_{0}^{n-1} 2^p = 2^n-1$$

{{< img src="../images/arbre4.png" alt="sous arbres droit et gauche" caption="definition recursive des arbres binaires" >}}
{{< img src="../images/arbre_complet.png" alt="arbre complet" caption="arbre complet" >}}
# Implémenter en python
On utilisera l'arbre suivant pour l'implémentation en python:

{{< img src="../images/arbre6.png" alt="exemple d" caption="exemple d'arbre binaire de taille 9" >}}
Comme vu pour les graphes, on pourra utiliser des listes imbriquées, un dictionnaire, ou une classe (programmation objet).

## Liste
Un noeud peut être représenté par une liste imbriquée `[clé,fils gauche,fils droit]`.

Et comme les *fils gauche* ou *fils droit* sont des noeuds, on y mettra une nouvelle liste imbriquée `[clé,fils gauche,fils droit]`.

Pour les feuilles, la liste s'écrit: `[clé,None,None]`.

Le petit arbre suivant peut être représenté par `['r'`,['a',None,None],['b',None,None]]` 

{{< img src="../images/arbre8.png" caption="petit arbre de taille 3" >}}
Avec l'arbre de taille 9 donné en exemple:

`arbre9 = [3,[...,..,..],[...,..,..]]`

> Question: compléter cette liste.

## Classe
La classe suivante va permettre d'implémenter les arbres binaires:

```python
class ArbreBinaire:
    def __init__(self, valeur):
        self.valeur = valeur
        self.fils_gauche = None
        self.fils_droit = None
```

On n'a donné ici que le constructeur, mais il est possible d'y ajouter les méthodes qui permettront de retourner une valeur (getter), ou d'ajouter un noeud (setter); ou encore de déterminer les dimensions de l'arbre.

Avec l'arbre de taille 9 vu plus haut, la classe peut s'utiliser de la manière suivante (avec la notation pointée qui n'est pas recommandée):

```python
racine = ArbreBinaire(8)
noeud1 = ArbreBinaire(3)
noeud2 = ArbreBinaire(10)
noeud3 = ArbreBinaire(1)
...
racine.fils_gauche = noeud1
racine.fils_droit = noeud2
noeud1.fils_gauche = noeud3
...
```

Ou bien, en supposant que vous ayez ajouté deux méthodes de classe `ajoute_fils_gauche` et `ajoute_fils_droit`:

```python
racine = ArbreBinaire(8)
noeud1 = ArbreBinaire(3)
noeud2 = ArbreBinaire(10)
noeud3 = ArbreBinaire(1)
...
racine.ajoute_fils_gauche(noeud1)
racine.ajoute_fils_droit(noeud2)
noeud1.ajoute_fils_gauche(noeud3)
```





# Parcours
**Definition:** Un **parcours** est un algorithme qui appelle une fonction, ou un méthode sur tous les noeuds d'un arbre.

L'**ordre** sur les noeuds dans lequel la méthode est appelée doit être fixé. Il y a plusieurs choix, qui diffèrent par la seule position de l'instruction `Afficher clef [ r ]`

L'algorithme opère alors un **traitement** sur chacune des clés de l'arbre, dans un ordre choisi. Ici, on cherche à *Afficher la clef*.

Mais on peut remplacer cette instruction par un traitement sur les valeurs: ajouter 1 pour compter les clés par exemple.

## Parcours postfixe

```
ParcoursPostfixe ( Arbre binaire T de racine r ) 
  ParcoursPostfixe(Arbre de racine fils_gauche[r]) 
  ParcoursPostfixe(Arbre de racine fils_droit[r])
  Afficher clef [ r ]
```

## Parcours préfixe

```
ParcoursPréfixe ( Arbre binaire T de racine r ) 
  Afficher clef [ r ]
  ParcoursPréfixe(Arbre de racine fils_gauche[r]) 
  ParcoursPréfixe(Arbre de racine fils_droit[r])
```

## Parcours infixe

```
ParcoursInfixe ( Arbre binaire T de racine r ) 
  ParcoursInfixe(Arbre de racine fils_gauche[r]) 
  Afficher clef [ r ]
  ParcoursInfixe(Arbre de racine fils_droit[r])
```

{{< img src="../images/arbre10.png" caption="exemples de parcours" >}}

## Parcours en largeur
Les trois algorithmes vus plus haut s'apparent à une exploration de type *parcours en profondeur*. C'est la position de l'instruction de *traitement* qui amène les différences entre ces 3 parcours.

Un arbre est un *graphe*. On peut donc lui appliquer l'algorithme de **parcours en largeur** vu dans une leçon précédente.

*Rappel:*

```python
from collections import deque

def BFS_ite(d,s,visited=[], queue=deque()):
        queue.append(s)
        while queue:
            v = queue.popleft()
            if v not in visited:
                visited.append(v)
                unvisited = [n for n in d[v] if n not in visited]
                queue.extend(unvisited)
                print(queue)
        return visited
```
t
# Travaux pratiques
## Sur Capytale
=> [Lien vers le notebook](https://capytale2.ac-paris.fr/web/c/a443-5846248)

## Sur Google Colab
* telecharger le fichier module [hierarchyP](/pdf/NSI/hierarchyP.py) (faire un clic droit et *enregistrer sous...*)
* utiliser le lien suivant pour acceder au{{< a link="https://colab.research.google.com/drive/1y3GF5m5UI2ilRLX7wYQsFNnw6gzdvvHV?usp=sharing" caption="notebook colab" >}}

## Notebook avec un IDE local
* lien alternatif: télécharger une [version locale](/scripts/notebooks/sd5_notebook.ipynb) du notebook (clic droit et *enregistrer sous...*)
* correction du{{< a link="https://colab.research.google.com/drive/18VUCVjH9u9V3jF7JU2VRy0XZWQwyXtqO?usp=sharing" caption="notebook colab en ligne" >}}

# Liens

* cours de l'Université Paris Sud: [Lien](https://www.lri.fr/~hivert/COURS/CFA-L3/06-Arbres.pdf)
