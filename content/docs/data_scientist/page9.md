---
Title: data.gouv maires de France
---

# data.gouv
Le site [data.gouv.fr](https://www.data.gouv.fr/) est la plateforme des données publiques françaises.

Nous allons consulter les données du Répertoire National des Élus (RNE). Celui-ci a pour finalité le suivi des titulaires d’un mandat électoral. Il est renseigné et tenu à jour par les préfectures et les services du ministère de l'intérieur.

{{< img src="../images/datagouv.png" caption="" link="https://www.data.gouv.fr/datasets/repertoire-national-des-elus-1/" >}}

> Rendez vous à la page [de consultation du RNE](https://www.data.gouv.fr/datasets/repertoire-national-des-elus-1/). 

En bas de page, trouver la rubrique *elus-maires-mai.csv*. Cliquer sur le bouton pour telecharger le document.

{{< img src="../images/rne_csv.png" link="https://www.data.gouv.fr/datasets/repertoire-national-des-elus-1/" >}}

> Lancer le logiciel Excel. Ouvrir un nouveau classeur, vide.

L'ouverture du fichier va se faire à partir du bandeau **Données**: Chercher ensuite le bouton *importer un fichier texte ou csv*. Puis selectionner le fichier.

{{< img src="../images/gimp1.png" caption="Exemple d'import d'un fichier .csv depuis le bandeau Données" >}}

A l'ouverture du fichier, dans la boite de dialogue, il faudra paramétrer:

* l'encodage des caractères (page 1)

{{< img src="../images/utf8.png" caption="dans la page 1, rechercher le menu sur l'encodage des caractères" >}}

{{< img src="../images/utf8_2.png" caption="menu deroulant proposant l'encodage des caractères" >}}

* la tabulation avec pour separateur le point virgule `;` (page 2)

Le paramètre *semicolon* (point virgule) précise le caractère séparateur.

{{< img src="../images/excel_import2.png" caption="le format a été correctement renseigné" >}}

# Traitement du fichier
Le fichier contient des informations basiques sur tous les maires des communes de France. Cela fait un très grand nombre de lignes...

> Commençons par reduire l'affichage aux seuls maires du departement 06:


Si la feuille de calcul ne présente pas de filtres en tête de colonnes:

* Commencer par selectionner toutes les colonnes A, B, C, D, E dans laquelles se trouvent les données du tableau.

{{< img src="../images/excel1.png" >}}

* Dans le bandeau *Données*, choisir Filtrer (entonoir).

{{< img src="../images/filter.png" >}}

Il apparait alors des listes de choix au dessus des descripteurs du tableau. Pour filtrer selon l'un des descripteurs, cliquer sur l'une de ces listes de choix. Celle du *Code du departement*... et choisir **6**

{{< img src="../images/filter2.png" >}}

> Calculons alors le nombre de maire de sexe feminin.

Dans le classeur, sous le tableau, utiliser l'une des cellules pour placer le calcul du nombre de maires dont le Code sexe est **"F"**.

Vous allez utiliser pour cela la fonction [NB.SI](https://support.microsoft.com/fr-fr/office/fonction-nb-si-e0de10c6-f885-4e71-abb4-1f464816df34) (voir [Notice](https://support.microsoft.com/fr-fr/office/fonction-nb-si-e0de10c6-f885-4e71-abb4-1f464816df34) sur support.microsoft.com)

Dans une cellule juste dessous, faire de même pour le nombre de maires de sexe **"M"**.

Sélectionner ensuite ces 2 cellules et insérer un diagramme circulaire: (dans le bandeau INSERTION)

{{< img src="../images/camembert.png" caption="diagramme circulaire dans le bandeau INSERTION" >}}

La proportion joue clairement en faveur des maires de sexe masculin...

{{< img src="../images/camembert2.png" caption="un joli camembert" >}}

# Suite
> Rechercher un autre departement pour lequel la parité est mieux respectée...



