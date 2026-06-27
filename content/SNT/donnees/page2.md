---
Title : memoire des machines
description: numerisation des donnees, stockage sur un disque dur ou memoire flash, binaire
weight: 10
---

{{% badge color="green" icon="heart" %}}culture numer{{% /badge %}}

## Numérisation - video du site du CEA
{{< img src="../images/ordinateur.png" link="https://www.cea.fr/multimedia/Pages/videos/culture-scientifique/technologies/fonctionnement-ordinateur.aspx"  caption="introduction à l'architecture de l'ordinateur" >}} 



Les machines ne comprennent que les chiffres ! Et pas n’importe lesquels : 0 et 1 sont ses préférés... Pourtant, une machine comme celle qui vous sert à afficher cette page n'est pas (seulement) une calculatrice:

*Comment peut-on travailler avec du texte ou des images sur une machine, qui ne manipule que du binaire?*

# Mémoire d'une machine
Une machine manipule des données numériques BINAIRES. Ce sont des nombres constitués de chiffres ne pouvant prendre que 2 valeurs, 0 ou 1 : des bits.

Le stockage des bits s’est fait autrefois sur support papier (avec/sans trou):

{{< img src="../images/carte.png" link="https://fr.wikipedia.org/wiki/Codage_des_caract%C3%A8res_sur_carte_perfor%C3%A9e" caption="carte perforée IBM - source wikipedia" >}}

{{<img src="../images/ibm.png" caption="source - courstechinfo.be/Techno/Historique2.html" >}}

*Une machine comme l’IBM 1401 lisait les cartes (a) pour en recopier le code sur une bande magnétique (b). Un gros calculateur lisait cette bande (c), exécutait les jobs (d) puis transcrivait les résultats sur une autre bande (e) postposant ainsi l’impression des résultats (impression off-line) faite ensuite par un ordinateur plus léger (f).*

On devine en quoi les machines ont grandement evolué: aujourd’hui, le processeur gère tout seul l’accès aux données et aux programmes. Il n’y a plus besoin d’un personnel humain…

Mais alors, comment représenter et organiser les données sur un support (mémoire) pour qu’elles soient accessibles (lecture/ecriture) par le processeur ?


Aujourd’hui, le support mémoire est constitué de milliards de transistors, possédant 2 niveaux de tension : **5V** ou **0V**.

C’est donc le transistor qui permet la représentation d’un bit de donnée, en ajustant la tension électrique au niveau **haut** ou au niveau **bas**.

{{< img src="../images/transistor.png" caption="Le transistor: un composant électronique à 2 états" >}}
*Un transistor est un morceau de conducteur, dont la conductivité est contrôlée par sa troisième broche/borne. - Source: [Fonctionnement d'un ordinateur/Les transistors et portes logiques](https://fr.wikibooks.org/wiki/Fonctionnement_d%27un_ordinateur/Les_transistors_et_portes_logiques)* 

# Loi de Moore
voir la presentation:

{{< img src="/pdf/NSI_1/C1_presentation_machines.png" link="/pdf/NSI_1/C1_presentation_perf_machines.pdf" >}}

Le nombre de transistors sur une puce électronique devrait être doublé tous les 2 ans, pour le même prix de fabrication. Les transistors deviennent donc de plus en plus petits.

La figure suivante montre l'évolution du nombre de transistors pour un même élement de surface:

{{< img src="../images/mem-moore.png" caption="illustration de la loi de Moore - source wikipedia" >}}

[Lien page wikipedia](https://fr.wikipedia.org/wiki/Loi_de_Moore)

Cette miniaturisation a un effet sur d'autres caracteristiques. Voir l'article ci-dessous.

{{< img src="../images/Moore_law_2.png" caption="evolution des caracteristiques des machines - source wikibooks" >}}

[Lien page wikibooks](https://fr.wikibooks.org/wiki/Fonctionnement_d%27un_ordinateur/La_loi_de_Moore_et_les_tendances_technologiques)

# Coder et manipuler de plus grandes valeurs
Les transistors sont gravés sur circuits intégrés, ce qui a permi d'atteindre des fortes densités par unité de surface. La finesse de gravure est actuellement de 10 nm environ (Intel).

{{< img src="../images/memory.png" caption="Le transistor: un composant électronique à 2 états" >}}

Une machine va traiter des informations qui vont être à l’origine très diverses, plus ou moins structurées, mais toujours en binaire : 

Ce sont des nombres, des caractères, des mots, des images, des sons, des bruits, la température, la quantité d'argent qu'on a dans notre porte-monnaie, notre âge, des dates, etc. 

La quantité de mémoire, même importante, n’est pas infinie dans une machine. C’est pourquoi on doit reserver un certain nombre de bit à chaque donnée, et ce nombre doit être ajusté au mieux.


<!--
{{< img src="../images/mem-bits.png" caption="Le transistor: un composant électronique à 2 états" >}}
-->

Pour coder une information qui peut prendre plus de 2 valeurs, il faudra utiliser plusieurs *bits*. Ceux-ci sont souvent rassemblés par 8, formant un mot-octet. Celui-ci peut prendre 256 valeurs.


# Stocker de manière durable: Disque dur
Les mémoires se partagent en 2 familles: Les mémoires volatiles, comme la RAM: les données stockées vont s'éffacer lorsque l'on coupe l'alimentation de la machine. Et les mémoire persistantes, pour lesquelles les données ne s'effacent pas lors de la mise hors tension.

Le disque dur est du 2e type. Il utilise des pistes magnétiques sur un plateau pour écrire et lire avec une tête magnétique.

{{< img src="../images/Harddrive.svg" link="https://fr.wikipedia.org/wiki/Disque_dur" caption="disque dur - Wikipedia" >}}

Actuellement, les disques durs vendus dans le commerce contiennent 1 à plusieurs To (teraoctets: 10<sup>15</sup> octets)

# Numériser des données - les standards internationaux
Dès l’invention de l’informatique, les ordinateurs ont pu manipuler des textes composés de caractères, que ce soit pour la saisie des commandes sur un clavier ou pour l’impression des résultats sur le papier. Il a donc fallu adopter une convention commune qui soit utilisée par tous les ordinateurs. Ainsi, est né en 1961 le **code ASCII** (American Standard Code for Information Interchange) qui associe une valeur numérique à chaque caractère de l’alphabet : 65 pour A, 66 pour B…

{{< img src="../images/ascii.png" link="https://www.lookuptables.com/text/ascii-table" caption="table ascii, source: lookuptable.com" >}}
Avec la taille des mémoires, et les performances des machines qui ont progressé, il a été possible de coder des données de plus en plus complexes. Il a fallu trouver un moyen de structurer ces données, c’est à dire de les mettre en forme et en lien dans un format approprié.

# Sources et compléménts
* Image du disque dur: [Par I, Surachit, CC BY-SA 3.0](https://commons.wikimedia.org/w/index.php?curid=2537310)
* Cours Licence sur les mémoires [de Jean-Michel Richer](https://leria-info.univ-angers.fr/~jeanmichel.richer/ensl3i_crs4.php)
* Fonctionnement d'un ordinateur: [wikibooks](https://fr.wikibooks.org/wiki/Fonctionnement_d%27un_ordinateur/La_carte_m%C3%A8re,_chipset_et_BIOS)

