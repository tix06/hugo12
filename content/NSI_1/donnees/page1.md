---
Title : Denombrer
description: histoire numeration
weight: 5
---

*Données, machines, algorithmes, langages*

# Dénombrer: du comptage au calcul mécanique
## 1. Ecriture des nombres: (Bordas p9)
*mots clés: le statut de nombre, base 10, 2, 16, Leibniz et le binaire*

{{< img src="../images/numeration1.JPG" caption="Systeme de numération égyptien et gréco-romain (source:Bordas NSI)" >}}
Voir la page dédiée dans la partie SNT sur la numération au cours des ages: [Lien](/docs/SNT_2nde/pages/page14/histoire_num)

## 2. Les abaques et le boulier
### Comment additionne t-on deux nombres avec un abaque?
*Un abaque est le nom donné à tout instrument mécanique plan facilitant le calcul.*

Au départ, une opération aussi simple que l'addition demande de la mémoire, d'utiliser les doigts de la main, ou des artefacs (petits cailloux ou des petits jetons en argile) : jusqu'à 3300 ans avant JC, voire plus tard selon les civilisations.

Puis les abaques ont permi d'exploiter la numération de position en base 10 en séparant les unités des dizaines, centaines, et plus, avec des jetons en colonnes.

La colonne la plus à droite étant celle des unités, celle à sa gauche, les dizaines, ...

{{< img src="../images/abaque.jpeg" link="https://fr.wikipedia.org/wiki/Abaque_(calcul)" caption="Reconstitution d'un abaque romain" >}}
La méthode est expliquée ici avec un container de billes, mais elle peut être adaptée facilement à l'usage du boulier...

* On dispose les billes dans chaque colonne (centaine à gauche, puis dizaine et unité à gauche). Les nombres à additionner sont écrits sur 2 rangées, l'une sous l'autre.

{{< img src="../images/addition_1.png" caption="104 + 17 - debut" >}}
* On deplace les billes dans l'une des rangées

{{< img src="../images/addition_2.png" caption="104 + 17 - etape 2" >}}
* On rassemble les billes par 10 lorsqu'il y a un depassement dans l'une des colonnes, et on les remplace par une retenue dans la colonne plus à gauche.

{{< img src="../images/addition_3.png" caption="104 + 17 - etape 3" >}}
* On peut alors exprimer le résultat: 104 + 17 = 121

{{< img src="../images/addition_4.png" caption="104 + 17 - resultat" >}}
**Exercice:**

* Représenter les étapes de la **soustraction** de 15 à 103 à l'aide de ce même abaque.

### Le boulier
*Le boulier est un dispositif mécanique d'aide au calcul. Il est lié au système de numération décimale*.

{{< img src="../images/video_boulier.png" link="https://youtu.be/GnMgHsos7cY" caption="Youtube: Les bouliers - Micmaths" >}}
**Exercice:**

* Représenter les étapes de la multiplication de 6 par 4 avec un boulier à 10 unités.
* Représenter les étapes de la division de 32 par 8 avec ce même boulier.
* Pourquoi l'auteur de la video avance t-il que le disque mécanique est une amélioration importante par rapport aux colonnes droites de billes?
* Quel est le problème qui survient lorsque l'on compte avec le disque numéroté?

## 3. Circuits électroniques à 2 états
* La numération binaire: [Leibnitz](https://fr.wikipedia.org/wiki/Gottfried_Wilhelm_Leibniz) (1646-1716) [archives ouvertes](https://archive.org/details/69LeibnizDiadica/mode/2up)

Ce manuscrit exceptionnel, écrit par Leibniz à 33 ans mais non publié, fait le lien entre deux de ses travaux majeurs, paraissant a priori indépendants : son idée du calcul binaire et son idée de machine à calculer décimale.
Ce manuscrit apparaît à ce jour comme la plus ancienne évocation d'un *calculateur binaire*.

{{< img src="../images/manuscrit_Leib.png" link="https://archive.org/details/69LeibnizDiadica/mode/2up" caption="manuscrit sur la numération binaire - Leibnitz" >}}
* Comprendre la frontière entre le matériel et le logiciel: [blog couleur-science.eu](https://couleur-science.eu/?d=e2e507--comprendre-la-frontiere-entre-le-materiel-et-le-logiciel)


# Cours: Représentation des entiers positifs
## Numération additive
Pour la numération additive, la lecture d'un nombre se fait en additionnant les valeurs de chacun des chiffres-caractères.

{{< img src="../images/exemple-egypt.gif" caption="Exemple: la numération egyptienne" >}}

## Numération de position
La numération de position permet d'écrire un nombre avec les mêmes symboles pour les rangs 0, 1, 2, etc... Le rang zero étant le plus à droite. Le poids d'un chiffre dépend de son rang:

$$Poids = Base^{rang}$$

La numération de position implique d'utiliser un symbole pour le zero.

## Base
Une base est un nombre qui permet de décomposer un nombre entier dans une numération de position:

* **Base 10**: 

{{< img src="../images/vis-division.png" caption="division euclidienne de 4 par 2" >}}
Pour convertir un nombre N décimal dans la base 2, on réalise la **division par 2** de N puis des **quotients** de ses divisions, jusqu'à ce que le quotient arrive à **0**.

Le **resultat** de la conversion en base 2 est la série de valeur obtenues pour les **restes**. Le dernier reste obtenu est celui de poids le plus fort:

{{< img src="../images/vis-euclide.png" caption="conversion: 4" >}}


## Exemples et visuels
*Visuels:*

* principe de gestion mecanique de la retenue

{{< img src="../images/gears.png" link="https://youtu.be/rjWfIiaOFR4?t=40" caption="Youtube: How mechanical counters work, gears" >}}
* Overflow avec un compteur mécanique

{{< img src="../images/mecanical_count.png" link="https://youtu.be/rjWfIiaOFR4?t=154" caption="Youtube: How mechanical counters work, overflow" >}}



## Mémoires
Les différents supports de stokage utilisés pour les ordinateurs modernes sont présentés [ici (wikipedia, mémoires informatiques)(https://fr.wikipedia.org/wiki/M%C3%A9moire_(informatique)#Mat%C3%A9riel_informatique)

Le **codage binaire** (2 états) se fait à l'aide:

* d'une piste pouvant avoir 2 polarités magnétiques (disque dur, disquette)
* un creux ou une bosse sur un support (DVD, CD-ROM)
* materiaux reflechissant ou non reflechissant (CD-ROM à graver)
* condensateur chargé ou déchargé (mémoire RAM, registres)

Les techniques de stockage mécaniques, par exemple par rubans perforés ont été largement utilisés dès le début de l'informatique, puis abandonnés au profit de supports plus pratiques et plus rapides




