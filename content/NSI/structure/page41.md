---
Title: Activite arbre couvrant
hidden: true
weight: 51
---

* [cours sur les graphes. Term NSI](../page5/)
* [TP sur l'implementation en python des graphes](../page6/)
* [Arbres](/docs/NSI/structure/page4/)
* [TP](../page41) sur la notion d'arbre couvrant

# Arbre couvrant minimum
**Definition**: Etant donné un graphe *non orienté connexe*, un arbre couvrant est un graphe non cyclique qui relie tous les sommets du graphe.

**Definition**: Si le graphe possède des arêtes pondérées, un arbre couvrant arbre couvrant minimum est un arbre couvrant dont la somme des poids des arêtes est minimale (c'est-à-dire de poids inférieur ou égal à celui de tous les autres arbres couvrants du graphe). [wikipedia](https://fr.wikipedia.org/wiki/Arbre_couvrant_de_poids_minimal)

## Problème
Le graphe ci-dessous représente un réseau électrique où les objets (les habitations) doivent être reliés entre eux. Il existe de nombreuses façons de construire ce reseau. Les poids de chaque arête représentent le coût de la construction de la ligne.

{{< img src="../images/arbre_couvrant.png" caption="Graphe G d'un réseau d'habitations" >}}

L'arbre couvrant minimum est la façon de construire un tel réseau en minimisant les coûts représentés par les poids des arêtes.

> Retrouver cet arbre couvrant minimum pour le graphe G.

## Sitographie
Le premier algorithme découvert pour resoudre ce problème est l'[algorithme de Boruvka](https://fr.wikipedia.org/wiki/Algorithme_de_Borůvka). C'est aussi l'algorithme employé de manière intuitive si vous parcourez le graphe visuellement, en cherchant une solution. C'est un [algorithme glouton](https://fr.wikipedia.org/wiki/Algorithme_glouton). (cad qui suit le principe de réaliser, étape par étape, un choix optimum local, afin d'obtenir un résultat optimum global)





