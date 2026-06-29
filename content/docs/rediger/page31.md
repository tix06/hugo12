---
Title: Writer et Word
description: elements, proprietes, styles, similitudes dans l'utilisation des logiciels de traitement de texte
weight: 18
---



Ce TP montre les similitudes de conception d'un document:
1. Textuel avec Word/LibreOffice Writer
2. Pour le Web, en langage HTML



**Formater le texte d’un document**

Mettre en forme un document *textuel* demande une certaine maitrise du logiciel, mais surtout, connaitre le nom des objets et des fonctions utilisés:

* feuille de Style
* Objets *paragraphes, Titre 1, Titre 2, ..., listes*.

Ainsi que le nom des *propriétés* de ces objets:

* Police, taille de la police, couleur
* indentation, surlignage, encadré
* ...

*Remarque*: Le logiciel appelle ces éléments et objets des *Styles*. Nous préférons conserver les termes *objets* ou *éléments* pour désigner les *paragraphes, Titre 1, ...*, comme il est d'usage en HTML (voir partie 2).

# Microsoft Word
> **A vous de jouer:** Télecharger et ouvrir le document textuel sur {{< a link="/pdf/competences/plastiques.txt" caption="les plastiques" >}}. Copiez l'ensemble du texte (CTRL + a, CTRL + c) et collez-le dans un nouveau document Word CTRL + V)

En vous inspirant de la video suivante, mettre en forme le document en suivant la méthode proposée.

{{< img src="../images/contenu_structure.png" link="https://youtu.be/BqY3_6egjuI?si=RxR-cx2_wM8AyTHr" caption="video - youtube - separation contenu, structure, forme" >}}

Ci-dessous, certains travaux d'élèves sont proposés en exemple:

{{< img src="../images/plastics1.png" >}}

Pour modifier plus grandement la structure, il faut utiliser des *sections*.

L'editeur de texte Word permet aussi de placer une partie du contenu sur plusieurs colonnes. Le logiciel place alors des *sections* dans le document, comme expliqué dans le tuto suivant: [tuto unilim.fr](https://www.unilim.fr/scd/formation/word-creer-des-sections-differentes-dans-un-document/).

{{< img src="../images/plastics2.png" >}}

# Libre Office Writer
**Modifier le style d’un élément ou en créer un nouveau**
## Méthode 1:
Depuis la fenêtre des Styles (à droite), sélectionner l’un des élements, comme par exemple `Style de paragraphe` par défaut. Choisir dans le menu: `Nouveau` ou `Modifier`

{{< img src="../images/text1.png" >}}

* `Nouveau`: cela créé un nouvel objet fils de celui sélectionné, qui s’ajoute à la liste des Styles

* `Modifier`: cela ouvre la fenêtre de modification du Style, que l’on peut aussi atteindre depuis la barre de menu du haut (Styles > choisir `Editer le Style`). La nouvelle fenêtre contient alors toutes les propriétés modifiables pour ce Style, classées par onglet.

{{< img src="../images/text5.png" >}}

## Méthode 2: 
Sélectionner dans la page l’un des éléments dont vous souhaitez modifier le style. Modifier avec les boutons de la barre d’icones (en haut). 

{{< img src="../images/text2.png" >}}

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

## Créer un élément pour insérer des scripts
Les scripts sont des programmes informatiques. Leur format suit des règles précises, et ceux-ci ne doivent pas être reformatés par le logiciel Writer. Leur indentation doit être conservée, la casse (minuscule / majuscule) aussi.

Cela peut nécéssiter la création d'un nouvel élément dans Writer. Cela permettra d'avoir un format personnalisé, comme une nouvelle *police de caractères*. Souvent, celle utilisée pour les scripts est *Courier New*, en *gras*.

On peut aussi faire un collage du script avec la coloration syntaxique *highlight*). Le logiciel en ligne [highlight.hohli.com](https://highlight.hohli.com/index.php) permet de faire cela. Coller le script dans la fenêtre, choisir le langage, et copier le texte mis en couleur avant de la coller dans Writer. Puis utiliser le nouveau Style personnalisé pour le formater (script).

{{< img src="../images/text8.png" >}}

## Ajouter une numérotation
Si vous souhaitez ajouter un numéro aux éléments de type `Titre 4`:

Ouvrir le menu *Outils* de la barre des menus et choisir numérotation des chapitres:

{{< img src="../images/tools.png" >}}

Dans la fenêtre, choisir l'onglet *numérotation* et paramétrer pour démarrer une numérotation *1,2,3* pour les titres de niveau 4:

{{< img src="../images/numbering.png" >}}


Voir pour plus de détails les explications ici: [pdf de lyceedupaysdesoule.fr](http://www.lyceedupaysdesoule.fr/ressources/libreoffice/libreoffice_writer_6_numerotation_titres.pdf)

# Liens
* Notice sur les styles et modèles: [wiki.documentfoundation.org](https://wiki.documentfoundation.org/images/9/94/GS6003FR-Styles_et_mod%C3%A8les.pdf)