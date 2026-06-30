---
Title: recherche de correlations
weight: 19
---

# Recherche de corrélations
## Principe
La recherche de correlations entre valeur d'un tableau consiste à identifier des colonnes qui semblent être interdépendantes.

On doit commencer par rassembler les données dans une même table, où les réponses d'une même personne sont rassemblées dans une même ligne.

{{< img src="../images/grille.png" >}}

Puis on fait des hypothèses sur ce qui pourrait montrer une interdépendance:

* Exemple: il y a peut être un lien entre la durée du trajet scolaire, et l'avance avant le début des cours.
* Contre exemple: il y a peu de chances de trouver une corrélation entre l'âge et la durée du trajet scolaire. 

On selectionne alors les colonnes de la table qui sont probablement corrélées. On les porte comme axes X et Y dans un graphique. Puis on place les points pour chaque élève:

{{< img src="../images/diag_corre.png" >}}

La corrélation peut montrer un regroupement de points

{{< img src="../images/corre_knn.png" caption="source: appendre le machine learning en une semaine, G. Saint-Cirgue" >}}

Cela peut être aussi un alignement sur une droite, ou une courbe.

{{< img src="../images/corre_regre.png" caption="source: appendre le machine learning en une semaine, G. Saint-Cirgue" >}}

## En pratique
A l'aide du logiciel Excel:
* importer les données à partir des fonctionnalités du logiciel *(faites-vous aider par le professeur)*.
* (1): selectionner les 2 colonnes de données. Celles-ci doivent être côte à côte dans le tableau, sinon, déplacer les colonnes.
* (2): menu INSERTION
* (3): choisir graphique > nuage de points

*Analyser et conclure*
