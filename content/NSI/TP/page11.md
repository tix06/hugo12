---
Title: ABR applications
description: arbre binaire de recherche, inventaire et rangement
weight: 89
--- 

# ABR: sujet 1
Vous programmez un jeu narratif, ou le personnage peut collecter, gagner ou perdre des objets. Il possède ainsi un (très) grand **sac à dos**. Pour représenter ces objets, vous les numérotez (à l'aide d'une clé) d'une manière qui permettra de facilement les retrouver. Vous placerez ces clés dans un [arbre binaire de recherche](/pdf/NSI/sd6_ABR.pdf) lorsque le personnage gagne l'objet. Et vous retirerez cette clé lorsqu'il perd l'objet.

{{< img src="../images/abr_P2.png" link="index.html" >}}

Vous aurez besoin ainsi de 2 structures de données: 

* l'ABR pour ranger les clés
* un tableau pour placer les couples `clé,nom_de_l_objet`

Pour organiser votre sac à dos, les clés possèderont un code commun ([voir exercice de bac pages 7,8](/pdf/NSI/sd5_arbres.pdf)) lorsqu'il s'agit d'une même famille d'objets. Par exemple, le couteau et le glaive pourraient être codés de la manière suivante:

* `'01100001', 'couteau'`
* `'01100010', 'glaive'`

Les 4 premiers caractères de la clé, `0110` codent alors les *armes de contact*.

On peut imaginer d'autres rubriques, et d'autres codes, pour classer les différents objets.

> Etape 1: Créer un programme qui place les très nombreux objets du sac à dos dans un ABR.

> Etape 2: Programmez les fonctions qui permettent:
> * d'ajouter un nouvel objet
> * de retirer un objet du sac à dos
> * d'afficher la liste des objets du sac à dos, pour une famille d'objets donnée.


# ABR: sujet 2
{{< img src="../images/abr_P3.jpg" caption="vue d'artiste de la bibliothèque de Babel" >}}
*La célèbre bibliothèque infinie de Jorge Luis Borges issue de son récit La bibliothèque de Babel a été récemment modélisée par un certain Jamie Zawinski, d’après la description faite au début du récit.*


Imaginez une **bibliothèque** contenant un extrêmement grand nombre de livres. Cette bibliothèque est organisée de la manière suivante :

Il y a des milliers de pièces différentes.

Chaque pièce est repérée par une suite de trois lettres, et dans cette pièce sont rangés tous les livres dont les titres commencent par ces trois lettres.

Chaque pièce possède **deux** sorties, une à droite et une à gauche.

La sortie de gauche mène soit à une salle dont les trois lettres sont situées avant dans l'ordre alphabétique, soit nulle part.

La sortie de droite mène soit à une salle dont les trois lettres sont situées après dans l'ordre alphabétique, soit nulle part.

Une représentation de cette bibliothèque peut être donnée sous la forme d'un arbre binaire tel que le suivant :

{{< img src="../images/abr_P1.png" caption="exemple de placement des données dans un ABR. Ordre alphabetique" >}}

*Questions:* 

1. Combien de pieces différentes pourrait comporter cette bibliothèque, si celle-ci devait représenter toutes les combinaisons de clés de 3 lettres possible?
2. Où se placerait la salle de clé `KRO`? 

> Etape 1: Le projet pourrait consister à établir une liste de clés, dans un fichier. Chaque ligne sera constituée de la clé, ainsi que d'un mot dont les premières lettres débutent par cette clé. (une table de [hashage](https://fr.wikipedia.org/wiki/Table_de_hachage)). Il n'est pas necessaire d'être exhaustif, et d'envisager toutes les clés existantes. 

> Etape 2: Vous placerez ces clés dans un [arbre binaire de recherche](/pdf/NSI/sd6_ABR.pdf), avec pour information à chaque noeud le couple `(clé,ligne_dans_la_table)`

> Etape 3: Programmez la fonction qui permet de trouver une clé dans l'ABR, puis de retrouver les informations correspondantes dans la table.

# ABR: sujet 3
Programmer un index inversé pour les **mots d'un roman**. 

{{< img src="../images/time_machine.jpg" link="https://www.gutenberg.org/ebooks/35" caption="Lire sur gutenberg.org" >}}

L'énoncé complet se trouve ici: [people.montefiore.uliege.be](https://people.montefiore.uliege.be/geurts/Cours/PA/2014/Projets/projet2.pdf)

> Etape 1: Ouvrir les 10 premières pages du roman *The Time Machine* de H.G. Wells avec les outils python (fonction `open`). Utiliser un compteur de phrases et de mots. Chaque mot sera associé à une position dans le texte du type (`numero_phrase, numero_mot_dans_la_phrase`)

> Etape 2: Placer alors tous les mots dans un ABR au fur et à mesure de leur apparition. La donnée stockée dans le noeud de l'arbre sera constituée d'une paire `(clé,valeur)`, où la clé est le mot, la valeur est la position dans le texte pour sa première occurence.

> Etape 3: Utiliser une table pour placer toutes les occurences de chaque mot. La donnée stockée dans chaque noeud servira maintenant à retrouver la position de cette information dans la table et sera constituée du couple: `(mot,ligne_dans_la_table)`.

# Outils
* Lire les données d'un fichier *csv* ou *txt*: [python - entrées/sorties - lire csv](/docs/python/pages/ES/page1/)
* Ecrire des données (table) dans un fichier: [python - entrées/sorties - ecrire](/docs/python/pages/ES/page1/)
* Sauvegarder une liste/dictionnaire dans un fichier: [python - entrées/sorties, module pickle](/docs/python/pages/ES/page1/)
* Mise au point d'un programme. Modules, tests, docstring: [Lien](/docs/NSI/langages/page5/)

# Liens
* Le sujet 2 est inspiré de la page [zonensi.fr](https://www.zonensi.fr/NSI/Terminale/C05/ABR/), et également Numérique et Sciences Informatiques, 24 leçons avec exercices corrigés, Balabonski, Conchon, Filliâtre, Nguyen, Editions Ellipses
* Le sujet 3 est celui de [Pierre Geurts – Jean-Michel Begon, Université de Liège](https://people.montefiore.uliege.be/geurts/Cours/PA/2014/Projets/projet2.pdf)