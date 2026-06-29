---
Title: html css
---

# Encodage des caracteres et header en html
Dans un fichier, les données sont écrites en binaire. Même les caractères sont exprimés sous forme numérique. Il existe plusieurs tables de correspondance lettre - chiffre. La plus ancienne est celle appelée ASCII. Mais la plus utile sera celle *utf-8*.

*Pour approfondir: page https://sebsauvage.net/comprendre/ascii/*

## Code ASCII
Le code ASCII définit la correspondance entre symboles et nombres jusqu'au nombre 127. Les caractères sont représentés par une série de 7 chiffres, en binaire. Les mots ont alors une longueur multiple de 7 chiffres binaires, puisque chaque lettre a une longueur fixe. 

Cette longueur de 7 bits est suffisante pour repésenter de manière unique chaque caractère latin.
Le problème de l'encodage ASCII est qu'il ne permet pas de représenter assez de caractères pour les besoins des différentes langues. Le e accent aigû **é** sera ainsi représenté par 16 chiffres binaires, et son affichage en format ASCII donnera **Ã©**. 

Dans un document HTML, on pourra tout de même afficher correctement ces caractères, mais il faudra utiliser une *entité* HTML, c'est à dire une combinaison de symboles connus par le navigateur comme par exemple: `&eacute;` pour la lettre `é`. Ou, mieux, utiliser l'encodage utf-8.

## Unicode
Le répertoire Unicode se décline en utf-8, utf-16 et utf-32, qui sont de largeur variable ou fixe (pour utf32) 
Le code UNICODE permet de représenter tous les caractères spécifiques aux différentes langues.



L’inconvenient des encodages à largeur fixe (utf-32) est qu’ils vont générer des fichiers de poids important (poids compté en kilo octets). Bien plus lourd que l’encodage ASCII. Alors que bien souvent, la plupart des caractères utilisés pour un document texte sont ceux de l’alphabet ASCII, avec quelques caractères spéciaux.


## Code à largeur variable utf-8 et utf-16
* Cet encodage utilise l'ASCII pour les caractères dont le point de code est inférieur ou égal à 127.

* Chaque caractère dont le point de code est supérieur à 127 (0x7F) (caractère non ASCII) se code sur 2 à 4 octets.

La *longueur* du nombre binaire est alors *variable*. Un caractère peut nécessiter 8 bits (ascii), 16 bits, ou plus(jusqu'à 32 bits). Une information dans le code numérique va préciser cette longueur (correspond à un caractère spécial comme le Ã). Cela va permettre d'afficher tous les caractères. Cela génère un fichier dont le poids sera inférieur à l'utf-32.

Pour le système d'exploitation Windows, l'encodage par defaut est l'utf-16. MacOs utilise un encodage utf-8.

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

Ajouter maintenant une DEUXIEME section avec la partie suivante: (à placer avant la balise de fermeture `</body>`:

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
Vous avez découvert le *langage HTML (Hypertext Markup Langage)* dans le TP précédent. Celui-ci gère la **structure ET le contenu** du document. La mise en forme dépend alors de votre navigateur, à partir des règles de mise en page standart qu'il va appliquer.

Mais pour maitriser et personnaliser cette mise en forme, il faut utiliser un langage prévu pour **gérer les *styles***. C'est le langage *CSS (Cascading Style Sheet)*.

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

Vous pouvez consulter le tuto à l'adresse suivante: [MDN Mozilla: le CSS](https://developer.mozilla.org/fr/docs/Learn/Getting_started_with_the_web/CSS_basics)

**Question d:**: Ecrire une règle CSS complète en identifiant: le *sélecteur, la propriété, la valeur*.

## Police, coloration, alignement
Les principales règles de style pour le texte sont `color`, `font-size`, `text-align`, ainsi que `font-family`.

Vous pouvez tester les effets de certaines de ces instructions en les plaçant entre les balises `<style>` de votre document. Par exemple:

```html
<style>
h3 {
  color: blue;
  font-size: 60px;
  text-align: center;
}

p {
  font-size: 16px;
  line-height: 2;
  letter-spacing: 1px;
}
</style>
```

Pour approfondir, suivre le tutoriel à la page [developper.mozilla](https://developer.mozilla.org/fr/docs/Learn/Getting_started_with_the_web/CSS_basics) sur le CSS niveau débutant.

## Hierarchie des éléments html, bordures
Dans le document `marignan.html`, les éléments HTML ont une certaine hierarchie: Les balises `<h3>` et `<p>` sont à l'intérieur de la balise `<section>`. Si on veut encadrer le contenu, il faudra appliquer les règles à l'élément `section`:

```css
section {
	...
}
```

Les règles peuvent permettre de 

* fixer la largeur
* mettre une marge entre les éléments
* mettre une couleur de fond
* dessiner une bordure

Suivre maintenant le tutoriel [developper.mozilla](https://developer.mozilla.org/fr/docs/Learn_web_development/Getting_started/Your_first_website/Styling_the_content#css_cest_avant_tout_des_bo%C3%AEtes) pour voir un exemple d'application de ces règles.

> travaux pratiques: écrire les règles de style CSS qui vont permettre d'obtenir la mise en forme suivante:

{{< img src="../images/css1.png" >}}

**Question e:** faire un tableau avec 3 colonnes: *nom de la propriété*, *effet de style*, *exemple de valeur*. Mettre dans ce tableau au moins 3 propriétés prévues pour styliser le texte, et 3 propriétés pour styliser le container de ce texte.

## Positionnement des éléments
Les éléments `section` se placent naturellement l'un sous l'autre. Ce qui donne, pour la page avec 2 éléments `section`:


{{< img src="../images/css2.png" >}}

Pour modifier cette mise en page, et mettre les 2 éléments côte à côte, il faut appliquer la règle de positionnement à l'élément PARENT des 2 éléments `section`. Ici, cet élément parent, c'est `body`.

La règle à appliquer, c'est:

```css
display: flex;
```

> Ajouter cette règle CSS pour obtenir la disposition suivante:

{{< img src="../images/css3.png" >}}

**Question f:**: Ecrire la règle complète que vous avez utilisée.

*Approfondir: [developper.mozilla](https://developer.mozilla.org/fr/docs/Learn/CSS/CSS_layout/Flexbox)*

## Agencer les éléments
Vous savez maintenant positionner les éléments dans le flux vertical, horizontal, mettre une image dans un container sans que celle-ci déborde, et utiliser des règles CSS pour personnaliser les styles. Vous pouvez peut-être, s'il vous reste du temps, revenir sur le [TP précédent](../page51) et personnaliser l'affichage de votre page...



