---
Title: Traitement des données en table
description: donnees structurees, table, filtrer, trier, calculer
weight: 14
---

{{% badgetable %}}
| | |
|---|---|
| {{% badge color="green" icon="heart" %}}culture numer{{% /badge %}} | D1 Format des données : [Lien](../page4) |
| {{% badge color="green" icon="heart" %}}culture numer{{% /badge %}} | D2 Collecte des données personnelles : [Lien](../page5) |
| {{% badge color="red" icon="angle-double-up" %}}modelisation{{% /badge %}} | D3 Données en table [Lien](../page8) |
| {{% badge color="green" icon="heart" %}}culture numer{{% /badge %}} | D4 RGPD [Lien](page5) et [videos](page6), recherche documentaire [Lien](../page7) |
| {{% badge color="orange" icon="star" %}}competences{{% /badge %}} | TP1 Enquete de police [Lien](../page12) |
| {{% badge color="red" icon="angle-double-up" %}}modelisation{{% /badge %}} | TP2 Pommes [Lien](../page9) |
| {{% badge color="orange" icon="star" %}}competences{{% /badge %}} | TP3 Traitement de données data.gouv [Lien](../page11) |
| {{% badge color="orange" icon="star" %}}competences{{% /badge %}} | TP4 Formulaire d'[enquête](/docs/publier/page1/) et traitement [Lien](/pdf/SNT/page7.html) |
{{% /badgetable %}}

## Activité 1: Trouver une information
Lea, une jeune mère de famille a accepté l’enregistrement de ses données de géolocalisation par le service Google.

Elle se renseigne sur les données enregistrées et obtient le tableau suivant pour les jours 15/09 et 16/09:

{{< img src="../images/lea.png" width="400px" >}}


1. Quelle est la référence de la case contenant la valeur 08:45 ? …

2. Quelle est la valeur de la case E4 ? …

Compléter la formule de calcul de la distance parcourue le 15/09:

= E4 + … 

3. Compléter la formule utilisant la fonction somme pour calculer la distance totale parcourue pendant ces 2 jours:

= SOMME(E4 : …

4. D’après les données de ce tableau: 

* Quelle a été la journée de Lea le Dimanche 15/09?


* Où est le lieu de travail de Léa?

## Activité 2: Données en plusieurs tables
L’agence de voyage Globe Trotteur enregistre les données de ses clients sous la forme de plusieurs tables: CLIENTS, VOYAGES et VOLS:


{{< img src="../images/agence.png" width="600px" >}}

1. Quel est l’identifiant de Julien Dumas dans le fichier CLIENTS?
2. Quelles étaient les destinations de Francoise Dargent au cours du mois d’octobre 2024?
3. Combien de miles cela lui-a-t-il rapporté dans son programme de fidélité?

Chaque traitement sur la base de données s’exprime de la manière suivante:
* Rechercher dans la colonne … de la table … la valeur … et retourner la valeur de la colonne …
ou bien:
* Filtrer les lignes de la table … en conservant celles où la colonne … vaut …
* Dans la table … faire la somme des valeurs de la colonne …
On peut aussi réaliser une combinaison de ces 3 opérations: par exemple, faire la somme sur les colonnes d’un tableau filtré.

4. Pour chacune des 3 premières questions, énoncer le traitement qui est réalisé.
5. Trouver une information à laquelle la base de données peut répondre. Formuler la question, comme vu dans les questions 1. à 3.

# Cours
## Recherche et tri
Le traitement sur des données structurées peut consister à:
* rechercher une donnée (critère)
* filtrer sur les données selon un critère

La formule exprime alors une idée du type: sur le tableau de données T, je cherche la valeur couleur correspondant à la fréquence 4,19

## Calculer
Pour copier une donnée dans une nouvelle cellule, on peut faire une copie par référence en indiquant sa coordonnées, après le signe =

Le traitement peut aussi consister à réaliser des calculs:

```
= somme(E4:E11)
= E4 + E5 + E6
```

On peut aussi combiner les méthodes: somme et filtre:

```
=SOMME.SI(C3:C18;”David";E3:E18)
```

Cette formule calcule uniquement la somme des valeurs de la plage C2:C5, dans laquelle les cellules correspondantes de la plage B2:B5 contiennent le mot « Jean ».

## Base de données à plusieurs tables




Pour représenter les données, on peut utiliser un simple fichier texte. Pour séparer ces données, le plus courant est d’utiliser un séparateur par virgule (comma en anglais) : comma separated values (csv). Ce format convient bien pour des petites collections de données. Pour de plus grosses quantités, on utilisera des ensembles de tables, reliées entre elles par des règles et constituants des « bases de données » (database).
Pour une base de données à plusieurs tables, on utilise des clefs d’indexation permettant d’identifier rapidement chaque ensemble de données (comme un numéro d’article ou un numéro de client)

Exemple: voici un ensemble de données. Placer celles-ci comme nouvelles entrées dans les tableaux proposés.

Dupond Kevin, 21 ans, habite à Nice, voyage à Berlin le 06/12/24, son code client est le 756A
Pour son voyage à Berlin, la compagnie était Lufthansa, le vol était LF 231, à 7h01 et son numéro de siege le 31D.
Le passager voyageait seul et avait un bagage en soute de poids 14,6 kg, dont la reference bagage était 1234.

*[source: www.cours.jlrichter.fr](https://www.cours.jlrichter.fr/lycee/snt-sciences-numeriques-et-technologie/2snt-d-les-donnees-structurees-et-leur-traitement/)*
