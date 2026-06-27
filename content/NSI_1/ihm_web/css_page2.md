---
Title: css display et position
description: css, display, position
hidden: true
weight: 11
---


* page du site vers le [CSS](../css_page1/)
* page du site vers le [CSS display et position](../css_page2/)
* pratique du css: [TP](../css_page3)

# Display
## display : block, inline, inline-block, none
*Une difficulté que l'on a souvent lorsque l'on apprend le CSS, c'est de faire la différence entre les propriétés* **display** et **position**.

Chaque navigateur possède une feuille de styles (c’est-à-dire un fichier CSS) qui sera appliquée par défaut pour les différents éléments dont nous ne précisons pas le comportement dans nos propres feuilles de style.

La plupart des navigateurs suivent les recommandations du W3C (l’organisme en charge de l’évolution et des standards des langages Web). Ce W3C spécifie pour chaque élément HTML quelle devrait être la valeur de son display parmi : 

* `display : block` : affichage sous forme d’un bloc ;

* `display : inline` : affichage en ligne ;

* `display : inline-block` :  permet aux éléments inline de suivre des règles de mise en forme ressemblant au block. Pour permettre par exemple à un élément inline d'avoir des marges ou des paddings. C'est la valeur par defaut de l'élément `input`. C’est pour cela que l’utilisation de cet élément est aussi simple : il reste à côté de son label, et on peut en changer sa largeur, sa hauteur, ses marges, etc..

* `display : none` : l’élément n’est pas affiché.

## Eléments de niveau block
Exemples d'éléments block : `p`, `div`, `form`, `header`, `nav`, `ul`, `li`, et `h1`.

Un élément block a les caractéristiques suivantes : 

- Si aucune largeur n'est définie, il prendra toute la largeur de son élément parent.
- Il peut avoir des marges et des paddings.
- Si aucune hauteur n'est définie, il prendra la hauteur de ses éléments enfants (en supposant qu'il n'y a pas de "float" ou de positionnement sur des éléments environnants).
- Il ignore la propriété vertical-align.

Il est donc inutile pour un élément block de définir une largeur ou de lui donner une width: 100%

{{< img src="../images/block.jpg" alt="display : block" caption="display : block" >}}
### Exemple utilisant le display block
{{< img src="../images/a_retenir.png" caption="éléments de display block" >}}
Tous les éléments de cet exemple, `div`, `p`, `ul`, `li` s'empilent grâce à leur display `block`, valeur par defaut. 

<div class="essentiel">
  <p class="entete">
    L'essentiel à retenir
  </p>
  <div class="resume">
    <ul>
    	<li>premier point</li>
    	<li>deuxième point</li>
    </ul>
  </div>
</div>

Voici le code HTML et CSS utilisé : 

```css
<div class="essentiel">
  <p class="entete">
    L'essentiel à retenir
  </p>
  <div class="resume">
    <ul>
    	<li>premier point</li>
    	<li>deuxième point</li>
    </ul>
  </div>
</div>

<style>
	/* creation du container au fond coloré et avec bords arrondis */
/* aucune marge intérieure pour que les éléments soient contre les bords */
/* du container */
.essentiel {
  background:#f0d0a0;
  color:#555;
  border-radius:10px;
  width:80%;
  border:1px solid #ccc;
  padding-top:0; 
}

/* en-tête : boite qui se positionne à l'interieur du container */
/* en position la plus haute */
/* avec un fond coloré plus foncé et une police plus grosse */
.essentiel>.entete {
  margin:0;
  background:#f56611;
  color:#555;
  font-size:1.5em;
  padding:20px;
  border-radius:10px 10px 0 0 ;
}

/* le contenu : se place à la suite de l'entête, au dessous */
/* ajout d'une marge intérieure et police plus petite */
.essentiel>.resume {
  padding:20px;
  font-size:0.8em;
}
</style>
```


**Remarque :**
Pour mettre côte à côte des éléments de display `block`, il faudra utiliser la règle `display:inline` et eventuellement `float` (voir plus loin).

{{< img src="../images/inline.png" caption="disposition des éléments de liste en inline" >}}

## Éléments de niveau Inline
Exemples d'éléments inline : `a`, `span`

Un élément inline s'inscrit dans le flux de texte. On peut l'imaginer comme une boîte qui se comporte comme du texte.
Il ignore le propriétés `width` et `height`, mais accepte `vertical-align`
Il s'inscrit dans le flux du texte.

{{< img src="../images/inline.jpg" alt="display : inline" caption="display : inline" >}}

### inline : application à la barre de menu horizontale
Cette barre de menu est conçue avec des éléments de type `a`, mis dans des éléments de type `li`. La valeur par défaut d'un `<li>` pour la propriété display est `list-item`. Cette valeur est connue pour ses styles par défaut (margin-start plus ou moins élevée, puce de liste de type disc, saut de ligne, etc.).

La valeur par défaut du display de `li` est ressemblant à celui de `block` ce qui va rendre impossible le placement de tous nos liens sur une seule ligne. On va donc le modifier en `inline`

Le display de `a` va être conservé en `inline`.

<ul >
	<li class="demoLi"{{< a link="#" caption="" >}}	<li class="demoLi"{{< a link="#" caption="" >}}	<li class="demoLi"{{< a link="#" caption="" >}}	
</ul>

<style>
  
.demoLi{
	display: inline;
	list-style: none; 
	margin: 1px;
}

.exemple{
	/*display: inline;*/
	list-style: none; /* pour enlever les puces sur IE7 */
	width: 100px;
	padding: 5px 10px;
	text-decoration: none;
	color: #fff;
	font-weight: bold;
	background: #999;
	border-radius: 10px;
}
</style>


```html
<ul>
	<li><a href="page1.html">Lien1</a></li>
	<li><a href="page2.html">Lien2</a></li>
	<li><a href="page3.html">Lien3</a></li>
</ul>

<style>
li {
	display: inline;
	list-style: none; 
	margin: 1px;
}
</style>
```


On pourra alors ajouter des règles CSS aux éléments `a` directement enfants de `li` avec le selecteur `li a`. (pour définir une couleur de fond, une bordure..., ou pour des effets de survol, avec la pseudo classe `a:hover`)


## Eléments de niveau inline-block
Avec Inline-block, l'élément génère une boîte block qui est mise en forme comme s'il s'agissait d'une boîte inline (c'est à dire sur la même ligne que le contenu adjacent).
Cela offre la possibilité de définir une largeur et une hauteur, des marges et paddings top et bottom, etc.

{{< img src="../images/inline-block.jpg" alt="display : inline-block" caption="display : inline-block" >}}
### application aux formulaires
Dans un formulaire, les éléments `label` et `input` se succèdent : un *label* précede un *input* afin d'expliciter la nature du champ *input* à remplir.

On montre ici un exemple de mise en page selon le *display* choisi pour le label. Le display par défaut du *label* a la valeur `inline`. On modifiera celui-ci par `block` puis `inline-block`; 

Le code HTML sera identique dans les 3 cas ci-dessous : 

```html
<form name="my_form" action="#result" method="post">
	<p> <label for="nom">Nom</label> <input type="text" id="nom"> </p>
	<p> <label for="email">E-mail</label> <input type="e-mail" id="email"> </p>
	<p> <label for="sujet">Sujet</label> <input type="text" id="sujet"> </p>
	<p> <label for="message">Message</label> <textarea id="message"></textarea> </p>
</form>
```

* display `inline` (display par defaut) : 
Ici, la règle css `width:100px` que l'on souhaite associer à l'élément `label` est inopérante. Les labels se mettent à côté de l'élément *input*, mais ces derniers ne s'alignent pas car la boite contenant l'élément *label* n'a pas une largeur fixe : 

{{< img src="../images/formulaire-inline.png" alt="display : inline" caption="label avec display : inline" >}}
* display `block` : 
Les éléments se positionnent l'un sous l'autre : 
{{< img src="../images/formulaire-block.png" alt="display : block" caption="label avec display : block" >}}
* display `inline-block` :
c'est le résultat attendu : l'étiquette *label* se met côte à côte avec l'élément *input*. Ceux-ci sont alignés verticalement, et la règle css `width:100px` associée au *label* est opérante. Ce qui aligne alors les éléments *input* :

{{< img src="../images/formulaire-inline-block.png" alt="display : inline-block" caption="label avec display : inline-block" >}}
Le code CSS correspondant : 

```html
<form name="my_form" action="#result" method="post">
	<p> <label for="nom">Nom</label> <input type="text" id="nom"> </p>
	<p> <label for="email">E-mail</label> <input type="e-mail" id="email"> </p>
	<p> <label for="sujet">Sujet</label> <input type="text" id="sujet"> </p>
	<p> <label for="message">Message</label> <textarea id="message"></textarea> </p>
</form>

<style>
input, textarea {
	/*déjà en inline-block*/
	width: 150px;
	padding: 4px;
	vertical-align: top;
}

label {
	display: inline-block;
	width: 100px;
	margin-right: 20px;
	vertical-align: top;
	text-align: left;
}
</style>
``` 

### inline-block : application au design responsive
**design responsive :** mise en page qui s'adapte à la taille de l'écran.
Souvent, lorsque la page s'affiche dans un écran d'ordinateur, les éléments se mettent côte à côte pour profiter de la largeur de cet écran. 
Par contre, lorsque l'écran est plus étroit (tablette ou smartphone), il est d'usage de disposer les éléments l'un sous l'autre.

Dans cet exemple, on va positionner des éléments en 3 **colonnes**. 
On a vu que les élements de type `div` ont un display par défaut qui vaut `block`. Leur disposition naturelle est donc : l'un sous l'autre (mode écran pour smartphone). 

Si on veut que l'affichage s'adapte à un écran large, on va alors modifier le display des éléments `div` en une nouvelle valeur `inline-block`.

**La propriété `float` :** Une fois le comportement des éléments modifié avec la valeur `inline-block`, on souhaitera définir l'élément `div` qui se positionnera à gauche, celui qui se positionnera au centre, et celui qui se positionnera à droite. 
Avec la propriété `float`, un élément va se positionner par rapport à son élément voisin : il va s'empiler sur le bord (droite) de l'élément à gauche (`float:left;`), ou bien sur le bord de l'élément à droite (`float:right;`).


*Méthode : pour placer les éléments côte à côte*  
- **chaque élément div : display: inline-block;**  
- floater à gauche : **float: left;** ou floater à droite : **float: right;**

L'élément `<div class="demoMain">` pour lequel la proriété `float` n'a pas été modifiée, se positionnera au centre.

{{< img src="../images/troisBlocs.png" alt="display : inline-block" caption="display : inline-block" >}}
Ici, le changement de valeur du display se fait lorsque l'écran est assez grand. En CSS, les déclarations sont alors encapsulées dans un bloc conditionnel, comme le montre l'extrait ci-dessous : 

```css
@media screen and (min-width: 800px), handheld and (min-width: 800px) {
div {
	/*concerne tous les elements div*/
	display: inline-block;
	width: 33.33%;
}
.demoA {
	/*pour l'element div qui floatera à gauche*/
	float: left;
}
.demoB {
	/*pour l'element div qui floatera à droite*/
	float: right;
}
}
```
Le code complet est donné en bas de document, avec l'exemple du *Holy Grail*

### inline-block : centrer un élément fils dans son élément parent

* L'élement parent, `conteneur` doit avoir la propriété `text-align: center;` afin de centrer horizontalement l'élément fils `bloc`.

* Pour l'élément fils, `bloc` : centrer celui-ci avec les règles : `display: inline-block;`, et `vertical-align: center;`



```html
<style>
.conteneur {
	background-color:#ccc;
	width:400px;
	height:200px;
	line-height:200px;
	text-align:center; /* centrage horizontal */ }

	.bloc {
	width:100px; /* largeur du bloc */
	padding:10px; /* aération interne du bloc */
	border:1px solid #fff;
	vertical-align:middle;
	display:inline-block;
	line-height:1.2; /* on rétablit le line-height */
	text-align:left; /* ... et l'alignement du texte */ }
	</style>

<div class="conteneur">
	<div class="bloc">
		<h3>Kikoo !</h3>
		<p>Lorem ipsum [...]</p>
	</div>	
</div>
``` 

{{< img src="../images/kikoo.png" >}}


## Display: flex
Noter qu'il est possible d'utiliser la règle `display:flex`. Ce qui a egalement pour rôle de modifier le flux de l'affichage des éléments fils. Cette technique, plus simple, sera traitée en TP: [positionnement des objets](/docs/NSI/HTML/page11/).

Un exemple de positionnement avec éléments placés côte à côte:

{{< img src="/docs/NSI/HTML/images/marignan3.png" caption="page complète avec bandeau de navigation, utilisant display:flex" >}}

Noter que la règle `display:flex` peut aussi faciliter le centrage d'un élément par rapport à son parent. Le script CSS ci-dessous montre la simplicité de la méthode, comparée à celle utilisant le `display: inline-block` vue plus haut:

```css
.conteneur {
	display: flex;
	align-items: center;
	justify-content: center;
}
```

Cette propriété va placer l'élément fils centré par rapport au parent, sans que celle-ci soit héritée, ce qui présente un gros avantage (il n'est plus necessaire de rétablir l'alignement gauche par defaut du fils).

# Position

la propriete position determine de quelle manière les éléments se disposent dans une page les uns par rapport aux autres. Voir le tutoriel à l'adresse : 

[https://developer.mozilla.org/fr/docs/Web/CSS/position](https://developer.mozilla.org/fr/docs/Web/CSS/position)

{{< img src="../images/position.png" alt="position" caption="valeur de position : static (à gauche), relative (centre), absolute (à droite)" >}}
```css
/* image du centre */
.jaune {
	position: relative;
  top: 40px; left: 40px;
}

/* image à droite */
.jaune {
	position: absolute;
	top: 40px; left: 40px;
}
``` 
Par defaut, la valeur est *static* . Les propriétés `top`, `right`, `bottom`, `left`, et `z-index` n'ont aucun effet lorsque le positionnement est `static`.

*  RELATIVE —L'élément est positionné dans le flux normal du document puis décalé, par rapport à lui-même, selon les valeurs fournies par top, right, bottom et left. Le décalage n'a pas d'impact sur la position des autres éléments. Aussi, l'espace fourni à l'élément sur la page est le même que celui fourni avec static.
  Par defaut, right, bottom et left ont pour valeur *auto*

*  ABSOLUTE-L'élément est retiré du flux normal et aucun espace n'est créé pour l'élément sur la page. Il est ensuite positionné par rapport à son élément parent. C'est la valeur choisie pour les objets que l'on veut placer à l'aide de leurs coordonnées : voir les exemples dans les pages{{< a link="../../javascript_avance/page1/index.html" caption="javascript avancé" >}}
*  FIXED — ressemble à `absolute`mais le positionnement se fait relativement à la fenêtre du navigateur. Il reste *fixe* malgré le scrolling de la page.


# Eléments en 3 colonnes : le Holy Grail
Pour des explications détaillés, on pourra se référer à la [page consacrée sur alsacreation](https://www.alsacreations.com/tuto/lire/588-trois-colonnes-float.html)

Le Holy Grail se réfère à une page web qui est constituée de quatre sections — un header, un footer, et une zone principale comportant deux sidebars, un de chaque côté : 

{{< img src="../images/HolyGrail.png" alt="saint graal css" caption="mise en page en 3 colonnes" >}}
La mise en page respecte les règles suivantes :

- Elle comporte une colonne centrale de largeur fluide et des sidebars de largeur fixe.
- La colonne centrale doit apparaître en premier dans le markup, avant les deux sidebars mais après le header.
- Les trois colonnes doivent avoir la même hauteur, indépendamment de leur contenu.
- Le footer doit toujours se trouver en bas du viewport, même si le contenu ne remplit pas la hauteur du viewport.
- Le layout doit être responsif, toutes les sections doivent se retrouver sur une seule colonne sur les viewports de dimension réduite.

Le Saint Graal est bien connu pour être difficile à créer en CSS sans aucun tripatouillage.

Exemple de code html, css respectant la mise en page du saint graal, et de manière *responsive* (avec adaptation à la largeur des écrans, même de type smartphone).

**Exemple :** Vous pourrez voir ici l'effet *responsive* en réduisant ou augmentant la largeur de la fenêtre.


```html
<!doctype html>
<head>
	<meta charset="UTF-8" />
	<title>Une mise en page responsive sur trois colonnes</title>
	
	<style type="text/css">
/*** 3 Columns ***/
.demo * {
	box-sizing: border-box;
	text-align: center;
}
.demo div {
	height: 12em;
}
.demoHeader,
.demoFooter {
	background: #aaa;
}
/*****
Colors
*****/
.demoMain {
	background: #ddd;
}
.demoA {
	background: #abc;
}
.demoB {
	background: #def;
}

li {
	display: inline;
	list-style: none; 
	margin: 1px;
}
/*********************
Media queries examples
**********************/
@media screen and (min-width: 800px), handheld and (min-width: 800px) {
.demo div {
	display: inline-block;
	width: 33.33%;
}
.demoA {
	float: left;
}
.demoB {
	float: right;
}
}
	</style>
</head>
<body>
<main role="main" class="demo">
<h1>Une mise en page <i>responsive</i> sur trois colonnes.</h1>

<header class="demoHeader">HEADER</header>
<div class="demoMain">TOP/CENTER<br>(ex: main content)</div>
<div class="demoA">MIDDLE/LEFT<br>(ex: menu)</div>
<div class="demoB">BOTTOM/RIGHT<br>(ex: aside)</div>
<footer class="demoFooter">FOOTER
<nav>
	<h2>Menu.</h2>
	<ul>
		<li><a hreflang="fr" href="/lab/">lab</a></li>
		<li><a hreflang="fr" href="/">accueil</a></li>
		<li><a class="contact" hreflang="fr" href="/contact">contact</a></li>
	</ul>
</nav>
</footer>

</main>

<footer>


</footer>
</body>
</html>
```

<!--
<div class="essentiel">
  <p class="entete">
    L'essentiel à retenir
  </p>
  <div class="resume">
  	Le positionnement des éléments se fait à l'aide de 4 propriétés importantes :
    <ul>
    	<li>display :
				<ul>
					<li>block : les éléments `block` se placent l'un sous l'autre. <br> On peut leur appliquer des règles pour les dimensionner (width et height). Par défaut, l'élément `block` occupe toute la largeur de l'élément parent (width), et toute la hauteur de son élément enfant (height). Par défaut, c'est la valeur des éléments `p`, `div` ainsi que pour les autres balises de sectionnement (header, footer, section), et les listes (ul, ol, li).<br>La règle `vertical-align` ne fonctionne pas avec des éléments `block` : ils ne peuvent pas être alignés avec le bord supérieur de l'élement parent.<br>On peut lui affecter la règle `text-align : right, left, center, justify;` qui affectera son contenu.<br>
					Un élément block peut contenir un élément inline, mais pas l'inverse.</li>
					<li>inline : positionnement côte à côte, sur la même ligne.<br> Il ignore les propriétés width et height, mais accepte `vertical-align`.<br>Il s’inscrit dans le flux du texte. <br>C'est la valeur par défaut des éléments `a` et `span`.
						<br>Les éléments inline ne peuvent contenir que des éléments inline.</li>
					<li>inline-block : l'élément devient une boîte `block`, mais qui est mise en ligne comme s’il s’agissait d’une boîte inline. On peut alors appliquer les règles de dimension width et height. Mais également celle de positionnement vertical `vertical-align` et pour son contenu celle de `text-align`.<br>C'est la valeur par défaut de l'élément `input`.</li>
				</ul>
    	</li>
    	<li>vertical-align : concerne les éléments dont les display sont inline et inline-block, ainsi que les cellules d'un tableau. L'élément est alors positionné :
    		<ul><li>dans la hauteur de l'élement parent (valeurs possibles : text-top, text-bottom et middle)</li>
    		<li>ou bien par rapport aux éléments de la même ligne (avec les valeurs : top, bottom, sub).</li>
    	  </ul>
    	</li>
    	<li>text-align : concerne les éléments dont le display est block ou inline-block. Permet de mettre le contenu à gauche, au centre, à droite ou de manière justifié (left, right, center, justify).</li>
    	<li>float : concerne les éléments dont le display est inline, ou inline-block. Permet d'inscrire les éléments en ligne dans un flux où ils seront floatés à gauche (left), ou à droite (right).</li>
    	<li>position : les éléments ont tous par défaut la valeur `static` pour la propriété position. Ils se placent dans le flux de construction de la page, selon leur valeur de display. 
				<ul>
					<li>position : relative ;<br>
							Pour décaler un élément : dans le flux normal du document l'élément est décalé, par rapport à lui-même, selon les valeurs fournies par top, right, bottom et left. Cela ne modifie pas les autres éléments qui conservent leur place.<br>
							C'est aussi la valeur que doit posséder un élément parent afin de positionner un de ses éléments fils de manière `absolute`.
					</li>
					<li>position : absolute; <br>
							L’élément est retiré du flux normal. Il peut alors être positionné avec les propriétés top et left, qui placeront l'élément à partir du coin supérieur gauche. (par exemple `top: 100px;` pour placer l'élément 100px sous le bord supérieur du parent).
					</li>
				</ul>
    	</li>
    </ul>
  </div>
</div>
-->

# Liens
* [https://developer.mozilla.org/fr/docs/Web/CSS/display](https://developer.mozilla.org/fr/docs/Web/CSS/display)

* [https://developer.mozilla.org/fr/docs/Web/CSS/position](https://developer.mozilla.org/fr/docs/Web/CSS/position)

* [https://la-cascade.io/la-difference-entre-block-et-inline/](https://la-cascade.io/la-difference-entre-block-et-inline/)

* Cours html css, apprendre à coder: [pierre-giraud.com](https://www.pierre-giraud.com/html-css-apprendre-coder-cours/display/)

* Best practices: optimiser le chargement des pages:  [github.com/cnumr/best-practices](https://github.com/cnumr/best-practices/blob/main/chapters/BP_037_fr.md)

* Tutos, tester et jouer avec flexbox: [believemy.com](https://believemy.com/fr/r/le-guide-complet-sur-flexbox-css)




