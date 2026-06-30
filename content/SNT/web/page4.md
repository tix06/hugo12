---
Title: introduction à CSS
description: declaration css, selecteur, propriete, valeur, heritage, arbre du DOM
weight: 12
---


# Bases en css
les fondamentaux du css: cascade et héritage: [MDN](https://developer.mozilla.org/fr/docs/Learn/CSS/Building_blocks/Cascade_and_inheritance)

Les sigles « CSS » sont l’abréviation de « Cascading StyleSheets » ou « feuilles de styles en cascade » en français.

Le CSS vient résoudre un problème bien différent du HTML : en effet, le HTML sert à définir le *contenu et la structure* d’une page, à leur donner du sens. 

Le CSS, lui, va servir à mettre en forme les différents contenus définis par le HTML en leur appliquant des styles.

Si votre navigateur affiche par défaut les contenus textuels que vous avez déclaré comme des titres en HTML en grand et en gras et à l’inverse les paragraphes en plus petit c’est justement parce que chaque navigateur possède sa propre feuille de styles. En fournissant nos styles CSS pour les différents contenus de notre page, nous allons donc pouvoir définir l’apparence de ceux-ci puisque les styles que nous allons fournir vont être considérés comme prioritaires par rapport à ceux du navigateur. C'est le principe du style en cascade (CSS)

## Une déclaration CSS
Une déclaration typique est composée de trois parties :

- un **sélecteur**,
- une **propriété**,
- une **valeur**



<div style="text-align:center; font-weight: bold;">selecteur { propriete: valeur; }</div>

La **valeur** de la propriété se met après le séparateur `:`.

Ces règles deviennent des *déclarations* lorsque celles-ci comprennent plusieurs couples propriété-valeur :Les règles sont alors séparées par un point-virgule `;`, dans la même accolade:

```css
selecteur {
  propriete 1: valeur;
  propriete 2: valeur;
}
```
*Exemple:*

{{< img src="../images/css.png" caption="règles CSS associées à tous les éléments p de la page: caractères mis en gras (font-weight: bold) et entourés d'une bordure rouge (border: 2px solid red)" >}}

Le selecteur fait référence à un ou plusieurs éléments du document.

## Selecteurs
Pour pouvoir appliquer un style à un contenu, il va déjà falloir le cibler, c’est-à-dire trouver un moyen d’indiquer qu’on souhaite appliquer tel style à un contenu en particulier.

En classe de SNT, le sélecteur, c'est l'élement HTML que l'on veut cibler.

## Où met-on les déclarations CSS?
On cherche à créer le style suivant:

{{< img src="../images/texte.png" >}}

Il y a 3 possibilités pour écrire les règles CSS:

* Soit directement dans la balise, avec l'attribut `style`. Exemple:

```html
<div style="border:solid;">
 <p style ="color:#26b72b;>Le texte suivant sera affiché en VERT, qui est codée en hexadécimal avec #26b72b.</p></div>
 ```

Dans ce cas, seule la règle `propriete:valeur;` est écrite, pas le *sélecteur*.

* Soit directement dans la page HTML, entre les balises `style`:

L'élément `<style>` peut être inclus dans l'élément `<head>` ou dans l'élément `<body>` du document et les styles seront appliqués. Toutefois, il est recommandé de placer les styles dans l'élément `<head>` afin de clairement séparer la présentation du contenu autant que possible. 

*Exemple:*

```HTML
<head>
  <style>
    p {
        color: #26b72b;
        border: solid 2px;
      }
  </style>
</head>

<body>
  <p>Le texte suivant sera affiché en VERT, qui est codée en hexadécimal avec #26b72b.</p>
</body>
``` 


* La méthode idéale consiste toutefois à utiliser des feuilles de style dans des fichiers externes et de les appliquer au document grâce à des éléments `<link>`: 

```html
<head>
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <p>Le texte suivant sera affiché en VERT, qui est codée en hexadécimal avec #26b72b.</p>
</body>
```

C'est dans le fichier `style.css` que l'on mettra alors les déclarations css.

Le choix de la position du CSS est déterminé par l'ampleur du projet à définir, doit-on par exemple appliquer ces déclarations à toute la page, aux autres pages du site, ...

{{< img src="../images/alphorm.png" link="https://www.youtube.com/watch?v=vXGNjxOYxaM"  caption="introduction au CSS, video de la chaine Alphorm" >}}

# Héritage
Comme vu dans le cours sur [HTML](../web1/), les éléments ont une hierarchie selon l'imbrication de leurs balises.

Par exemple, avec l'extrait de page HTML suivant:

```html
<section>
  <h1>Titre de la section</h1>
  <div>  
    <p>Paragraphe 1</p>
    <img src="photo.jpg">
  </div>
  <div>
    <p>Paragraphe 2</p>
  </div >
 </section>
```

On a l'arbre du DOM: 

{{< img src="../images/arbreDOM.png" caption="arbre du DOM d'après l'extrait HTML" >}}

> Les éléments enfants héritent les règles CSS de leur parent, à condition que ces règles leurs soient applicables.

Pour selectionner un élément particulier, il faudra le selectionner à partir de sa *classe*, un attribut qu'il faut rajouter à la balise de l'élément.

Ceci oblige à co-construire le fichier *HTML* et le fichier *CSS*, ce qui peut être parfois un vrai casse-tête...

{{< img src="../images/cssutilityfirst.png" caption="Youtube - Mon probleme avec le CSS" >}}

Avec un *attribut classe*, le selecteur CSS fait reference à la valeur de *classe*. Le sélecteur utilise une notation avec un *point* devant la valeur de *classe*.

Exemple:

| balise HTML | déclaration CSS |
|--- |--- |
| `<p class="paragraphe_stylé">Mon paragraphe</p>` | `.paragraphe_stylé {font-family: arial; }` |

* Dans le code HTML, la balise `p` que l'on veut styliser a l'attribut *class*. Et la valeur `paragraphe_stylé` pour valeur de la classe. Ce nom est librement choisi par le programmeur.
* Dans le code CSS, le sélecteur est alors `.paragraphe_stylé`, avec un point devant le nom. La règle ne concerne alors QUE ce paragraphe. Si la déclaration avait été : `p {font-family: arial; }`, cela aurait concerné TOUT les paragraphes `p` de la page.


# Règles principales
## Règles appliquées aux textes
Tutoriel complet: [developer.mozilla.org](https://developer.mozilla.org/fr/docs/Learn/CSS/Styling_text/Fundamentals)

Quelques propriétés CSS relatives aux textes


| paramètre | valeurs possibles | effet |
|--- |--- |--- |
| color | blue, yellow, red, ... | colorie le texte selon le nom *anglais* de la couleur |
| color | rgb(0..255, 0..255, 0..255) | selon le code RGB sur un octet chacun |
| color | #0..F0..F0..F | selon le code RGB exprimé en hexadecimal, sans separateur |
| background-color | idem color | couleur de fond |
| font-family | arial, courier new... | choix de la police de caractères |
| font | italic 12 pt sans-serif | informations complémentaires pour la police |
| text-align | center, left, right, justify | alignement du texte |
| font-weight | bold | mettre en gras |

## Règles relatives aux listes

Voici un exemple de page qui liste les différentes missions de la NASA:

```HTML
<head>
  <style>

  </style>
</head>

<body>
  <h2>NASA Notable Missions</h2>
  <ul>
    <li>Apollo</li>
    <li>Hubble</li>
    <li>Chandra</li>
  </ul>
</body>
```

<div style="width:70%; border:solid;">
<h2>NASA Notable Missions</h2>
<ul>
    <li>Apollo</li>
    <li>Hubble</li>
    <li>Chandra</li>
  </ul>
</div>

On peut ajouter une déclaration CSS dans le début du fichier. Par exemple pour enlever les marqueurs de liste de la manière suivante:

```HTML
<head>
  <style>
    li {list-style: none;}
  </style>
</head>
```

<div style="width:70%; border:solid;">
<h2>NASA Notable Missions</h2>
<ul>
    <li style="list-style: none;">Apollo</li>
    <li style="list-style: none;">Hubble</li>
    <li style="list-style: none;">Chandra</li>
  </ul>
</div>

*Résumé*

| paramètre | exemples de valeurs possibles | effet |
|--- |--- |--- |
| list-style | square | ![puces carres](../images/listes1.png) |
| list-style | none | ![pas de puces](../images/listes2.png) |



# Liens
* complements sur les listes [developer.mozilla.org](https://developer.mozilla.org/fr/docs/Web/CSS/list-style)
* [exemple de TP css](/docs/SNT_2nde/pages/page4/web6/)
