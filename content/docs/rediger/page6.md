---
Title : histoire informatique et reseaux
description: recherche documentaire, LibreOffice Writer
weight: 14
---

# Partie 1: Histoire de l'informatique et des reseaux


> Dans ce TP nous allons créer une petite chronologie de l'informatique à l'aide du traitement de textes **LibreOffice Writer**.

En utilisant l'article Wikipédia sur la
[chronologie de l'informatique](https://fr.wikipedia.org/wiki/Chronologie_de_l%27informatique), ainsi que la page sur l'architecture des ordinateurs [site allophysique](/docs/NSI_1/architecture/page1/):

> **créer un document texte** qui rassemble **3 à 6 dates** par période de **l'histoire de l'informatique et d'internet**. Faites un choix pertinent pour chacune des **dates et descriptions**. Choisir ce qui selon vous, résume le mieux **chaque période**.

**Consignes**

- Le document ne doit pas excéder DEUX pages A4.
- Vous utiliserez des styles pour le mettre en forme:
  
  - `Titre principal` pour le titre du document: «Chronologie de l'informatique»
  - `Titre 1` pour chacune des phases de l'histoire de l'informatique:
    - «L'époque des pionniers»
    - «Les débuts de la micro-informatique»
    - «L'ère d'Internet et du World Wide Web»
    - «L'ère de la mobilité et des données partagées»
  - Les dates et leur description sont écrites sous forme d'une liste non-ordonnée avec le `Style de paragraphe par défaut`.
  - Sauvegarder votre fichier sous le titre `histoire_informatique_reseaux` dans le dossier `Documents/Devoirs/tixidor/`


*Remarque: Vous pouvez coller du texte issu d'une page en supprimant sa mise en forme grâce au collage spécial `<CTRL+MAJ+V>`(ou bien clic droit: coller sans Formatage)*

Il est nécessaire de séparer l'écriture du contenu du document (Partie 1) de celui de sa mise en forme (Partie 2).

# Partie 2: mise en forme du document
Pour être lisible, un texte doit comporter une certaine hiérarchie.

## Définir les éléments, structurer le document
Utiliser des niveaux de titres pour structurer votre document (Titre1, Titre2, Titre3...).

{{< img src="../images/exemple0.png" caption="Le document initial" >}}

* Choisir *Titre 1* pour le titre principal
* Choisir *Titre 2* pour chacune des phases de l'histoire de l'informatique: *Les prémices de l'informatique*, ...
* Choisir le Style *Titre 3* pour les dates relatives aux machines et leurs systèmes d'exploitation.

{{< img src="../images/exemple1.png" caption="Le document devrait maintenant ressembler à ceci" >}}

* Créer ensuite DEUX nouveaux Styles *enfants* de *Titre 3*, comme sur l'image ci-dessous. 
  * L'un des ces nouveaux Style servira à mettre en relief les Algorithmes
  * L'autre pour les reseaux et les programmes relatifs à ces reseaux.

{{< img src="../images/hierarchie_heading.png" >}}

Seule la propriété couleurs des Styles *enfants* diffèrent de *Titre 3*. Les autres propriétés sont héritées.

* Ajouter une numérotation aux chapitres (phases de l'histoire)


## Créer un épigraphe pour chaque phase de l'histoire

*L’épigraphe est une courte citation placée au début d’un ouvrage ou d’un chapitre, et qui permet d’en indiquer l’esprit, de résumer son contenu.*


## Personnaliser le style
Vous allez personnaliser les Styles utilisés dans votre document. Vous modifierez les propriétés des différents éléments. Un exemple de document stylisé est donné ci-dessous:



{{< img src="../images/elements_page.png" caption="personnalisation des propriétés couleur, alignement, police, ..." >}}






## Styliser le document de manière personnelle
Voici un modèle utilisé pour un mémoire (document long), pour sciences politiques Lille:

{{< img src="../images/document.png" link="https://www.sciencespo-lille.eu/sites/default/files/guide_preparer_et_rediger_un_memoire_de_recherche.pdf"  caption="Exemple de document - rediger un mémoire - sciencespo-lille.eu" >}} 


Les manières de mettre en forme un document sont très variés, les choix de design sont personnels. Dans tous les cas, il sera nécessaire de modifier les **propriétés** des Styles en modifiant leurs **valeurs**. 

Utiliser les tutoriels ci-dessous.

# Modifier le style d’un élément ou en créer un nouveau


## Méthode 1:
Depuis la fenêtre des Styles (à droite), sélectionner l’un des élements, comme par exemple `Style de paragraphe` par défaut. Choisir dans le menu: `Nouveau` ou `Modifier`

{{< img src="../images/text1.png" >}}

* `Nouveau`: cela créé un nouvel objet fils de celui sélectionné, qui s’ajoute à la liste des Styles

* `Modifier`: cela ouvre la fenêtre de modification du Style, que l’on peut aussi atteindre depuis la barre de menu du haut (Styles > choisir `Editer le Style`). La nouvelle fenêtre contient alors toutes les propriétés modifiables pour ce Style, classées par onglet.

{{< img src="../images/text5.png" >}}

## Méthode 2: 
Sélectionner dans la page l’un des éléments dont vous souhaitez modifier le style. Modifier avec les boutons de la barre d’icones (en haut), ou bien celle des proriétés de style (à droite).

{{< img src="../images/text2.png" caption="barre d'icones" >}}

Puis cliquer sur le bouton `Mettre à jour le Style sélectionné`. ![](../images/text3.png)

{{< img src="../images/text4.png" caption="Ce bouton se trouve près du menu des styles de la barre d'icones" >}}


## Modifier l'une des propriétés de Titre 1
Si vous souhaitez modifier la couleur des `Titre 1`

Dans la partie Style (fenêtre à droite), dérouler le sous menu `Titre`


{{< img src="../images/text6.png" >}}


* Choisir `Titre 1` , puis `Modifier`. Cela ouvre la fenêtre d’Edition.

Le but est alors de retrouver la bonne Propriété.

* Choisir l’onglet `Effets de caractère`. Puis la propriété `Couleur de Police`, dont vous pouvez modifier la valeur.

{{< img src="../images/text7.png" >}}

## Aide en video

On s'aidera des tutoriels pour LibreOffice Writer à l'adresse suivante: {{< a link="https://www.youtube.com/watch?v=ekh2Q1DU8Mw" caption="Youtube - LibreOffice Writer 1/11 : Mettre en forme le style principal " >}}




