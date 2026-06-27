---
Title: html et design web
hidden: true
weight: 11
---

* introduction au html/css: activité version [guidée](../html_page11) ou version [autonome](../html_page1)
* page du site vers le [HTML](../html_page3/)
* page du site vers le [CSS](../css_page1/)
* page du site vers le [CSS display et position](../css_page2/)

# Design d'une page Web
## Rappels sur l'encodage des caracteres et header en html
Dans un fichier, les données sont écrites en binaire. Même les caractères sont exprimés sous forme numérique. Il existe plusieurs tables de correspondance lettre - chiffre. La plus ancienne est celle appelée ASCII. Mais la plus utile sera celle *utf-8*.


### Code ASCII
Le code ASCII définit la correspondance entre symboles et nombres jusqu'au nombre 127. Les caractères sont représentés par une série de 7 chiffres, en binaire. Les mots ont alors une longueur multiple de 7 chiffres binaires, puisque chaque lettre a une longueur fixe. 

Cette longueur de 7 bits est suffisante pour repésenter de manière unique chaque caractère latin.
Le problème de l'encodage ASCII est qu'il ne permet pas de représenter assez de caractères pour les besoins des différentes langues. Le e accent aigû **é** sera ainsi représenté par 16 chiffres binaires, et son affichage en format ASCII donnera **Ã©**. 

Dans un document HTML, on pourra tout de même afficher correctement ces caractères, mais il faudra utiliser une *entité* HTML, c'est à dire une combinaison de symboles connus par le navigateur comme par exemple: `&eacute;` pour la lettre `é`.

### Unicode
L'UNICODE est une format d'encodage qui permet de représenter **tous les caractères** des différentes langues. Il est compatible avec les codes ASCII, les caractères latins étant représentés par les mêmes codes binaires. Les autres caractères vont s'ajouter avec des codes plus longs.

L'Unicode se décline en utf-8, utf-16 et utf-32.

L'utf-32 est un encodage des caractères avec une longueur fixe de 32 bits. Cela fait beaucoup de types de caractères différents. (plus de 4 milliards).

L’inconvenient d'un encodage à largeur fixe (utf-32) est qu’il va générer des fichiers de poids plus important, inutilement dans la plupart des cas. Alors que bien souvent, la plupart des caractères utilisés pour un document texte sont ceux de l’alphabet ASCII, avec quelques caractères spéciaux.

Pour l'utf-8 et l'utf-16, le code est de longueur variables, de 2 à 4 octets (16 à 32 bits).


# Activité: Définir le bon encodage en HTML
Utiliser le logiciel Notepad++ ou tout autre éditeur de script. Créer un nouveau fichier et commencer par l'entête suivant:

```html
<!DOCTYPE html>
<html>
<head>
	<meta charset="ISO-8859-1">
	<title>page principale</title>
</head>
```

La balise `<meta charset="ISO-8859-1">` va donner l'information au navigateur que l'encodage des caractères se fait en ASCII.

Ajouter alors les lignes suivantes:

```html
<body>
<section>
<h3>La bataille de Marignan, une date restée gravée</h3>

<p>La bataille de Marignan (Marignano en Italie, aujourd’hui Melegnano, ville à 16 km au sud-est de Milan) eut lieu les 13 et 14 septembre 1515 et opposa le roi de France François Ier et ses alliés vénitiens aux mercenaires suisses qui défendaient le duché de Milan.</p>

<p>Il s'agit de la première victoire du jeune roi François Ier, acquise dès la première année de son règne. Celle-ci fit environ 16 000 morts en seize heures de combat.</p>

<p>François Ier, né sous le nom de François d’Angoulême le 12 septembre 1494 à Cognac et mort le 31 mars 1547 à Rambouillet, est un <a href="https://fr.wikipedia.org/wiki/Liste_des_monarques_de_France">roi de France</a> ayant régné du 25 janvier 1515, jour de son sacre, à sa mort en 1547. Fils de <a href="https://fr.wikipedia.org/wiki/Charles_d%27Orl%C3%A9ans_(1459-1496)" title="Charles d'Orléans (1459-1496)">Charles d'Orléans</a> et de <a href="https://fr.wikipedia.org/wiki/Louise_de_Savoie">Louise de Savoie</a>, il appartient à la branche de Valois-Angoulême de la dynastie capétienne.</p>
</section>
</body>
</html>
```

Le contenu de la page se trouve entre les balise `<body>` et `</body>`.  La balise `<section>` va créer un container et sera utile pour segmenter le document.

**Question a:**  Sauvegarder le document avec le nom: `marignan.html` Puis ouvrir le document avec le navigateur. Que constatez-vous? Pourquoi?

Ajouter mantenant la partie suivante au contenu de la page (à placer avant la balise de fermeture `</body>`:

```html
<section>
<h3>La bataille de Marignan, une date rest&eacute;e grav&eacute;e</h3>

<p>La bataille de Marignan (Marignano en Italie, aujourd&rsquo;hui Melegnano, ville &agrave; 16 km au sud-est de Milan) eut lieu les 13 et 14 septembre 1515 et opposa le roi de France Fran&ccedil;ois Ier et ses alli&eacute;s v&eacute;nitiens aux mercenaires suisses qui d&eacute;fendaient le duch&eacute; de Milan.</p>

<p>Il s&#39;agit de la premi&egrave;re victoire du jeune roi Fran&ccedil;ois Ier, acquise d&egrave;s la premi&egrave;re ann&eacute;e de son r&egrave;gne. Celle-ci&nbsp; fit environ 16 000 morts en seize heures de combat.</p>

<p>Fran&ccedil;ois&nbsp;Ier, n&eacute; sous le nom de&nbsp;Fran&ccedil;ois d&rsquo;Angoul&ecirc;me&nbsp;le 12 septembre 1494 &agrave;&nbsp;Cognac et mort le 31 mars 1547 &agrave; Rambouillet, est un&nbsp;<a href="https://fr.wikipedia.org/wiki/Liste_des_monarques_de_France" title="Liste des monarques de France">roi de France</a>&nbsp;ayant r&eacute;gn&eacute; du 25 janvier 1515, jour de son sacre, &agrave; sa mort en&nbsp;1547. Fils de&nbsp;<a href="https://fr.wikipedia.org/wiki/Charles_d%27Orl%C3%A9ans_(1459-1496)">Charles d&#39;Orl&eacute;ans</a>&nbsp;et de&nbsp;<a href="https://fr.wikipedia.org/wiki/Louise_de_Savoie">Louise de Savoie</a>, il appartient &agrave; la branche de&nbsp;Valois-Angoul&ecirc;me de la dynastie cap&eacute;tienne.</p>
</section>
```

**Question b:** Recharger le document dans le navigateur. Que constatez-vous? Pourquoi?

Vous allez maintenant modifier l'information sur l'encodage en remplaçant la balise `<meta charset="ISO-8859-1">` par balise `<meta charset="utf-8">`. Revenir sur la première version du texte (celui avec les accents é, à, ...).

**Question c:** Recharger le document dans le navigateur. Que constatez-vous? Pourquoi?

# introduction au CSS
Les instructions de style se mettent entre les balises `<style>`. Ces balises seront placées après la fermeture `</head>` et avant l'ouverture du contenu `<body>`

```html
</head>

<style>
  instructions de style en langage css
</style>

<body>
.. contenu ..
``` 

Les instructions de style, en langage CSS, vont déclarer:

* l'élément HTML auquel on fait référence (un selecteur p, h1, ...)
* la propriété que l'on veut styliser
* la valeur que l'on veut mettre pour cette propriété

**Question d:**: Ecrire une règle CSS complète en identifiant: le *sélecteur, la propriété, la valeur*.

## Police, coloration, alignement
Les principales règles de **style pour le texte** sont [color](https://developer.mozilla.org/fr/docs/Web/CSS/color), [font-size](https://developer.mozilla.org/fr/docs/Web/CSS/font-size), [text-align](https://developer.mozilla.org/fr/docs/Web/CSS/text-align), ainsi que [font-family](https://developer.mozilla.org/fr/docs/Web/CSS/font-family).

Vous pouvez tester les effets de certaines de ces instructions en les plaçant entre les balises `<style>` de votre document. Par exemple:

```html
<style>
h3 {
  color: blue;
  font-size: 60px;
  text-align: center;
}

p {
  font-family: Georgia, serif;
  font-size: 16px;
  line-height: 2;
  letter-spacing: 1px;
}
</style>
```

Pour approfondir, suivre le tutoriel à la page [developper.mozilla](https://developer.mozilla.org/fr/docs/Learn/Getting_started_with_the_web/CSS_basics) sur le CSS niveau débutant.

## Containers de type block
Dans le document `marignan.html`, les éléments HTML ont une certaine hierarchie: Les balises `<h3>` et `<p>` sont à l'intérieur de la balise `<section>`. Si on veut encadrer le contenu, il faudra appliquer les règles à l'élément `section`:

```css
section {
	...
}
```

Les règles peuvent permettre de 

* fixer la largeur: [width](https://developer.mozilla.org/fr/docs/Web/CSS/width)
* mettre une marge entre les éléments: [margin](https://developer.mozilla.org/fr/docs/Web/CSS/margin)
* mettre une marge à l'intérieur de l'élément: [padding](https://developer.mozilla.org/fr/docs/Web/CSS/padding)
* mettre une couleur de fond: [background-color](https://developer.mozilla.org/fr/docs/Web/CSS/background-color)
* dessiner une bordure: [border](https://developer.mozilla.org/fr/docs/Web/CSS/border)
* bordure avec coins arrondis: [border-radius](https://developer.mozilla.org/fr/docs/Web/CSS/border-radius)

On rappelle qu'il n'est pas possible de fixer la hauteur des éléments dont le display est *block*, mais que l'on peut fixer leur largeur.



> travaux pratiques: écrire les règles de style CSS qui vont permettre d'obtenir la mise en forme suivante:

{{< img src="../images/css1.png" >}}

**Question e:** faire un tableau avec 3 colonnes: *nom de la propriété*, *effet de style*, *exemple*. Mettre dans ce tableau au moins 3 propriétés prévues pour styliser le texte, et 3 propriétés pour styliser le container de ce texte.

## Positionnement des éléments
Les éléments `section` se placent naturellement l'un sous l'autre. Ce qui donne, pour la page avec 2 éléments `section`:


{{< img src="../images/css2.png" >}}

Pour modifier cette mise en page, et mettre les 2 éléments côte à côte, il faut appliquer la règle de positionnement à **l'élément PARENT** des 2 éléments `section`. Ici, cet élément parent, c'est `body`.

La règle à appliquer, c'est:

```css
display: flex;
```

> Ajouter cette règle CSS pour obtenir la disposition suivante:

{{< img src="../images/css3.png" >}}

**Question f:** Ecrire la règle complète que vous avez utilisée (sélecteur, propriété, valeur).

*Approfondir: [developper.mozilla](https://developer.mozilla.org/fr/docs/Learn/CSS/CSS_layout/Flexbox)*

## Eviter les dépassements
Dans une nouvelle page, que vous appelerez `page2.html`, écrire le script suivant:

```html
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<title>page secondaire</title>
</head>
<style>
	div {
  		width:50%;
  		border: solid 2px;
  		margin:20px;
  		padding: 20px;
		}
</style>
<body>
    <div>
    <img src="marignan.jpeg">
    </div>
</body>
</html>
```

Mettre le fichier [marignan.jpeg](../images/marignan.jpeg) dans le même dossier. Ouvrir la page avec le navigateur.

{{< img src="../images/css9.png" >}}

Vous devriez constater un dépassement de la boîte par l'image.

Pour que l'image rentre complètement dans le cadre, il faudra lui donner la propriété `width: 100%;`

Elle va alors occuper toute la largeur de la boite `div`, son élément parent.

## Agencer les éléments
Vous savez maintenant positionner les éléments dans le flux vertical, horizontal, mettre une image dans un container sans que celle-ci déborde, et utiliser des règles CSS pour personnaliser les styles.

Vous allez assembler ces connaissances pour concevoir une page comme celle donnée ci-dessous:

{{< img src="../images/css10.png" caption="Page complète, avec paragraphes, image et colonnes" >}}

## Placer un bandeau de navigation
Vous allez ajouter un bandeau à gauche de `section` pour naviguer entre les différentes pages de votre dossier.

On peut utiliser une nouvelle balise *container* qui s'appelera `aside`. Il faudra placer cette balise, ainsi que celle appelée `section` dans un container parent, par exemple `div class="principale">`.

L'élément `aside` contiendra les liens vers les différentes pages HTML de votre projet:

```html
  <aside>
    <ul>
      <li><a href="/">page 1</a></li>
      <li><a href="/">page 2</a></li>
      <li><a href="/">page 3</a></li>
    </ul>
  </aside>
```

Les 2 éléments `aside` et `section` vont alors se placer côte à côte avec la règle CSS:

```css
.principale {
  display: flex;
}
```

{{< img src="../images/marignan3.png" caption="page complète avec bandeau de navigation" >}}

La structure du document devrait être alors:

```
body -|
      |-main-|-header
             |-div class="principale"-|
                                      |-aside
                                      |-section-|
                                                |-h3
                                                |-p
                                                |-p
                                                |-div class="colonnes"-|
                                                                       |-p
                                                                       |-figure
```

Analyser la structure de la page:

{{< img src="../images/marignan4.png" >}}

> Question 1:
> * Quels sont les éléments correspondants à chacune de ces boites?
> * Quel est l'élément directement parent des boites 2 et 3?
> * Quel est le parent qui contient l'ensemble de ces boites? (mais qui n'est pas `body`)?

*Aide pour le code CSS:* 

* Pour centrer l'élément `main`, qui est le fils direct de `body`, placer les règles css suivantes:

```css
body{
  display:flex;
  justify-content: center;
  color: #4e5140;
  text-align:justify;
}
main{
  width: 80%;
}
```

* Pour le bandeau supérieur, il s'agit de l'élément `header`, pour lequel il faudra ajouter:

```css
header {
  border-radius: 15px 15px 0 0;
  background-color: #e35f10;
  margin: 0;
  border:solid 0.5px;
  text-align:center;
}
```

* Pour les 2 containers `div`, ajouter la règle suivante:

```css
.principal, .colonnes {
  display:flex;
}
```


## Outil d'exploration du navigateur
Ouvrir l'outil d'exploration (inspecteur). 

> Question 2: Relever les règles CSS qui sont appliquées au paragraphe de la boite 4 (voir plus haut). Faire un tableau en 3 colonnes repondant aux questions suivantes:
> * Quelles règles lui sont directement appliquées, 
> * quelles règles sont héritées (et de quel élément vient cet héritage), 
> * quelles règles ne sont pas appliquées.

Puis repondez à la question:

> Question 3: Même travail, mais cette fois pour les lien `<a>` de ce même paragraphe.

# Approfondir
* cours: les bases en CSS: [Lien](/docs/NSI/CSS/page1/)
* compléments: [positionnement en CSS](/docs/NSI/CSS/page2/) avec display inline block

