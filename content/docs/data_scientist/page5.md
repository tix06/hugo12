---
Title: tableur pommes
description: importer les donnees csv pour filtrer et calculer sur les donnees des ventes dans differentes regions, avec le logiciel Excel
weight: 24
---

# Format des données
Les **données structurées** sont stockées dans des **fichiers** contenant des caractères. Ces fichiers peuvent être utilisés par plusieurs logiciels (**interopérabilité**), à condition que les données y soient mises dans un le bon **format**.

Nous allons voir ici l'un de ces formats: Le **csv**, ou *comma separated values*.

Voici un exemple de données en format *csv*. Il s'agit d'informations sur les vendeurs de fruits d'une compagnie, sur le territoire français.

```
;;;;;
;;;;;
Région;Commercial;Produit;Unités;;
Est;Maurice;Pommes;6380;;
Ouest;Alain;Raisins;5619;;
Nord;Ariane;Poires;4565;;
Sud;Marie;Bananes;5323;;
Est;Claude;Pommes;4394;;
Ouest;Noël;Raisins;7195;;
Nord;Jérôme;Poires;5231;;
Sud;Sébastien;Bananes;2427;;
Est;Maurice;Bananes;4213;;
Ouest;Alain;Poires;3239;;
Nord;Ariane;Raisins;6420;;
Sud;Marie;Pommes;1310;;
Est;Claude;Bananes;6274;;
Ouest;Noël;Poires;4894;;
Nord;Jérome;Raisins;7580;;
```

> Copiez ces données et collez les dans un fichier à l'aide de *Notepad* (du menu Programmes > accessoires de l'ordinateur).

> Sauvegardez le fichier dans votre *dossier* **documents** en le nommant: `fruits.txt`, ou bien `"fruits.csv"`

<!--
> * Soit en écrivant entre guillemets le nom du fichier `"fruits.csv"`
Les guillemets vous permettent de choisir l'extension du fichier et de remplacer celle par defaut choisie par le bloc note (`.txt`)
-->

**Question a:** A partir de vos connaissances, ou bien après une petite recherche sur le *net* que contient un fichier `.txt`? Les données y-sont-elles mises dans un format special (structuré)? 

**Question b:** Même question, mais cette fois pour les fichiers `.csv`. 

# Présenter les données à l'aide d'un tableur
> Démarrer le logiciel Excel (un tableur de la suite bureautique microsoft).

**Une fois le logiciel Excel démarré**, ouvrir le fichier `fruits.txt`

<!--
L'ouverture du fichier peut aussi se faire à partir du bandeau **Données**: Chercher ensuite le bouton *importer un fichier texte ou csv*. Puis selectionner le fichier.

{{< img src="../images/gimp1.png" caption="Exemple d'import d'un fichier .csv depuis le bandeau Données" >}}
-->

A l'ouverture, il vous sera demandé de préciser le séparateur des données (`,` ou bien `;`), puis l'encodage et les caractères.

Selon la version du logiciel Excel, la boite de dialogue peut différer:

{{< img src="../images/excel_import1.png" caption="le format n'a pas été correctement renseigné" >}}

Le paramètre *semicolon* (point virgule) précise le caractère séparateur.

{{< img src="../images/excel_import2.png" caption="le format a été correctement renseigné" >}}

Dans une version plus recente, la boite de dialogue peut ressembler à celle-ci:

{{< img src="../images/gimp2.png" caption="à gauche, les caractères accentués ne sont pas gérés. à droite, en utf-8, les caractères accentués sont pris en charge." >}}

Pour l'encodage des données, choisir **utf-8**. Cela permetra d'afficher aussi les caractères accentués.


Le logiciel Excel sert à PRESENTER les données. C'est à dire à reconstruire le tableau. Le visuel peut être important pour lire les informations contenues. 

> Vous devriez obtenir un tableau (lignes, colonnes, cellules, texte, couleurs) comme celui présenté ci-dessous:



{{< img src="../images/tableau_orig_2.png" caption="exemple de présentation structurée des données en tableau" >}}

**Question c:** Comment le logiciel a-t-il analysé le contenu du fichier pour obtenir cet affichage, en lignes et en colonnes?

Maintenant que la présentation est satisfaisante:

> ajoutez l'information suivante, en renseigant certaines valeurs dans le tableau:

> *le commercial **Sébastien** a vendu **9814 Pommes** dans la région **Sud***

**Question d:** Quelles sont les réferences (coordonnées) des cases dans laquelle vous avez renseigné *Sébastien*, *Pommes*, région *Sud*, *9814*? Comment avez-vous choisi ces différentes colonnes?

# Rechercher et Filtrer 
## Rechercher
Souvent, les tables contiennent de très nombreuses lignes, et ne peuvent pas toutes être présentées à l'écran. Il faut alors utiliser la fonction de recherche (bouton LOUPE à droite). 

> Utiliser le bouton pour *rechercher* le nom **Alain**. Cliquer sur *Suivant*. 

**Question e:** Quelles sont les réferences des cases qui sont sélectionnés lorsque l'on clique plusieurs fois sur *Suivant*?

## Filtrer par critère simple
Le fichier, lorsqu'il est importé depuis le bandeau *Données*, s'ouvre dans un classeur avec *filtres*.

{{< img src="../images/gimp3.png" caption="à gauche: ouverture du classeur AVEC filtres. à droite, ouverture SANS filtres" >}}

Si la feuille de calcul ne présente pas de filtres en tête de colonnes:

* Commencer par selectionner toutes les colonnes A, B, C, D, E dans laquelles se trouvent les données du tableau.

{{< img src="../images/excel1.png" >}}

* Dans le bandeau *Données*, choisir Filtrer (entonoir).

{{< img src="../images/filter.png" >}}

Il apparait alors des listes de choix au dessus des descripteurs du tableau. Pour filtrer selon l'un des descripteurs, cliquer sur l'une de ces listes de choix:

{{< img src="../images/excel2.png" >}}
* Sur le filtre appliqué à la première colonne (étiquette: Région), choisir **Est**.

{{< img src="../images/filtrer.png" caption="menu permettant la sélection par Région" >}}

## Filtrer selon un 2e critère
* Sur le filtre appliqué à la troisième colonne (étiquette: Produits), choisir **Pommes**.

Vous devriez obtenir un tableau ressemblant à celui-ci, mais avec plus de lignes:

{{< img src="../images/tableau_tri_2.png" caption="exemple de tableau filtré par Région ET par Produit (n'affiche que la 1ere ligne)" >}}

**Question f:** Combien de lignes sont affichées dans ce tableau filtré? Qu'ont-elles en commun?

# Les fonctions de calcul

## Somme de toutes les valeurs de la colonne *Unités*
Pour revenir au tableau initial, rappuyer sur Filtre dans le bandeau d'Excel.

Cela retire tous les filtres. 


### Fonction somme
Vous allez maintenant programmer une fonction de calcul sur le tableau: La fonction *SOMME*.

Voici un lien vers le [tuto de microsoft office.](https://support.microsoft.com/fr-fr/office/somme-somme-fonction-043e1c7d-7726-4e80-8f32-07b23e057f89)

> * cliquer dans la cellule juste sous la dernière valeur de la colonne *Unités*. 
* Ecrire debut de la formule: `= SOMME(` 
* puis faire une **sélection étendue** de toutes les valeurs de la colonne. 
* Valider avec la touche *Entrer*

**Question g:** Quel est le resultat du calcul? *Si le resultat est égal à zero, veuillez modifier le format comme expliqué en bas de page (Compléments), puis recommencer.*

**Question h:** Cliquer dans la case. Recopier la formule du calcul généré par le logiciel.

## Somme conditionnelle: SOMME.SI
La fonction SOMME.SI permet de sélectionner certaines cellules d'une selection étendue.

> On va s'aider du *concepteur de formule*: Cliquer dans la cellule dans laquelle vous souhaitez rentrer la formule, sous le tableau, puis:
> * écrire `= SOMME.SI(`

{{< img src="../images/cadre_tab.png" caption="somme conditionnelle " >}}
> * cliquer sur le bouton *fx* de la barre de saisie.
> * Aidez vous des champs suivants pour remplir les plages pour cette formule:
	* Plage: faire une selection étendue des valeurs de la colonne *Produits*
	* Critères: écrire "Pommes", ou bien cliquer sur le mot "Pommes" dans l'une des cellules du tableau (la *C24* dans cet exemple.
	* Somme_plage: selectionner toutes les valeurs numériques de la colonne *Unités*:

{{< img src="../images/sommesi.png" caption="concepteur de formule pour SOMME.SI" >}}
On a alors le nombre de Pommes vendues dans toute la France.

**Question i:** Quel est le résultat? Recopier aussi la formule qui a été générée.

# Conclusion
Un logiciel tableur (Excel, Calc, Number) permet de présenter les données à l'utilisateur en tableau, mais apporte aussi des **fonctions de traitement**. Ce sont les mêmes fonctions que l'on peut programmer avec un langage de traitement sur une Base de Données (SQL).

**Question j:** Quelles sont les *fonctions de traitement*que vous avez utilisées lors de ce TP? Donner leur nom.

# Compléments
## Format numérique
 Lors de l'import des données, le format des cellules est parfois incompatible avec les fonctions de calcul. 

 Il faut alors définir une plage de valeurs numériques.

> Sélectionner toutes les valeurs numériques du tableau. 

{{< img src="../images/gimp4.png" >}}

> Dans le bandeau **Données**, choisir: **Convertir**. Et faire suivant, plusieurs fois, sans changer les options proposées. Les cellules sont maintenant en format NOMBRE.


## Document
Fiche reponse à {{< a link="/pdf/SNT/C21_TP_Excel.pdf" caption="télecharger / remplir" >}}

# Suite
Traitement de données sur Excel à partir d'un fichier de data.gouv: [Lien](../page11)

