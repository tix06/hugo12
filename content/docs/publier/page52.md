---
Title: mon film prefere
---

# Créer une page web sur votre film préféré
Le but de cet exercice est de réaliser une page HTML de présentation de *votre film préféré*. Cette page sera simple. On pourra piocher les informations de votre film sur des bases de données en ligne de films telles que IMDb, AlloCiné, Wikipédia...

L'objectif est de réaliser une page qui pourrait présenter les informations comme ceci:

{{< img src="../images/LeFilm.png" >}}

## Mise en place de l'environnement de travail de notre site web

Dans un premier temps :

* dans votre répertoire personnel: créez un dossier appelé `web`, ou utlisez votre précédent dossier (celui contenant vos autres pages web, réalisées lors des précédentes séances).

*Attention, on prendra soin de ne pas mettre d'espaces et d'accents dans notre arborescence de fichiers et dossiers.*

* Dans le dossier `web`, créez un nouveau dossier, que vous appelerez `pages`
* Dans le dossier `pages`, créez un nouveau fichier à l'aide de l'editeur *Notepad++*. Copiez-collez les lignes suivantes:

```html
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<title>page principale</title>
</head>
<style>
	/* placer ici vos déclarations CSS*/
</style>
<body>
<!-- le contenu de votre page web. 
Ceci est un commentaire et peut être effacé.
-->
</body>
</html>
```

* Sauvegardez le en l'appelant *page1.html*

* Dans le dossier `pages`, créer un nouveau dossier que vous appelerez `images`. Placez dans ce dossier les images du film que vous souhaitez afficher dans votre page.

* Ouvrir le fichier à l'aide d'un navigateur (Mozilla, Edge, ...). Rafraichir la page à chaque modification.

## Contenu du fichier
Rappelez-vous: le contenu de votre document se place entre les balises `<body>` et `</body>`. A chaque modification, vous devrez *Enregistrer* votre document pour que ces modifications soient prises en compte.

Le document contiendra les éléments suivants:

**Ce document a été réalisé par VOTRE NOM ET PRENOM**

**TITRE DU FILM**

**Informations générales:**

* Année de Sortie
* Réalisateur
* Acteurs Principaux
* Genre

**Résumé**

**Bande-Annonce du Film**

**Sources des informations et médias**

> Méthode:

* Ces éléments peuvent être des *titres* (h1), des sous-titres (h2), ... Voir le [TP de découverte du HTML](/docs/competences/texte/page5/).

* On pourra aussi mettre en évidence, avec la balise `<strong>`, les différents items de la partie Informations générales.

* Les éléments de liste peuvent être placés les uns sous les autres, organisés (liste à puce) à l'aide du système d'instructions suivant: (balises ul et li)

```html
<ul>
    <li>Année de sortie: </li>
    <li>Réalisateur: </h1>
    <li>...</li>
</ul>
```

* Modifiez le texte Ce document a été réalisé par VOTRE NOM ET PRENOM et TITRE DU FILM







*Enregistrez votre travail puis faire F5 dans votre navigateur pour rafraîchir la page. Admirez votre premier travail.*

## Compléter les informations
### Des paragraphes
À l'aide des sites web du début de page, renseignez les différentes informations de la page.

> Méthode: Utilisez les balises `<p> ... </p>` pour placer des informations dans un paragraphe (par exemple pour le résumé)

### Créer des liens hypertextes
On l'a vu précédemment, les liens hypertextes sont la base du Web. Voyons comment réaliser ces liens avec du HTML. Un lien permet simplement de se déplacer vers une autre page HTML.

`<a>` désigne une ancre, c'est-à-dire un lien vers une cible de destination. Cette balise entoure généralement un mot (une image, un paragraphe, un titre, ...) qui devient le texte 'support du lien' hypertexte.

La syntaxe est :

`<a href="adresse_du_lien_hypertexte">support_du_lien</a>`

Dans la partie Sources des informations et médias, ajouter le ou les site·s où vous avez pris vos informations et l'affiche en créant un lien vers le ou les site·s en question.

## Ajouter une image

**(1)** Depuis un site web, télécharger le fichier image du film en faisant un clic-droit dessus Enregistrer l'image sous... Enregistrez ce fichier dans le dossier images crée précédemment.

**(2)** Nommez cette image affiche.jpg, ou affiche.png ou encore affiche.webp selon le format initial du fichier image.

Pour ajouter une image dans une page HTML, il faut utiliser la balise 

```html
<img src="image/affiche.png"/>
```

*chemin vers l'image* est le chemin à fournir à partir du fichier HTML:

* si le fichier affiche.png est enregistré dans le dossier `pages`, à côté de page1.html, on met la ligne de code suivante : `<img src="affiche.png"/>`
* Si l'image se trouve dans le dossier `images`, et qu'elle s'appelle `affiche.png`, le chemin est `images/affiche.png`



**(3)** Ajoutez l'affiche à votre page web en ajoutant la balise HTML adéquate. 

Si votre affiche est trop grande, on peut demander au navigateur de réduire sa largeur en pixels (propriété CSS `width:300px;`)

**(4)** Ajouter une déclaration CSS pour les éléments `img` de la manière suivante:

* Entre les balise `<style> ... </style>` du debut du document, ajouter la déclaration:

```css
img {width: 300px;}
```



## Lien vers une bande d'annonces
Nous allons ajouter une image, qui, lorsqu'elle est cliquée, envoie vers la page de la bande d'anonce.

**(1)** Rechercher le lien vers la bande d'annonce (Youtube)

**(2)** Télécharger l'image ci-dessous, [player.png](../images/player.png), ou bien concevoir votre propre image à partir de [celle-ci](../images/play.png)

{{< img src="../images/player.png" link="../images/player.png" >}}

**(3)** Placer l'image dans une balise *lien* `<a>`

Le code ressemble à cela :

```html
<a href="lien_vers_la_video"><img src="lien_vers_image"></a>
```





## Règles css
Et si je veux mettre un peu de couleurs ? Le *style* d'un document est apporté par le langage `CSS`

Ok, le rendu précédent n'est pas très fun, c'est le rendu par défaut des différentes balises ; on va donc ajouter des instructions de *styles* à notre page afin de la personnaliser à notre goût. 

Voici un exemple: copiez le code ci-dessous. Placez le à la fermeture de la balise `</head>` et avant l'ouverture par la balise `<body>`

```
<style>
body {	background-color: pink;	}

h1 { color: blue; }

h2 { font-variant: small-caps;
		color: green;
		}
</style>
```

Vous devriez obtenir quelque chose approchant...

{{< img src="../images/jeu1.png" >}}

Vous pouvez ausi definir des *containers* et deplacer certains éléments comme vu dans la [TP1, la démocratie athénienne](/docs/competences/texte/page5_bis/) ou bien celui-ci: [TP1 bis la bataille de Marignan](/docs/competences/texte/page8/)


{{< img src="../images/jeu2.png" >}}

# Pour aller plus loin...
Associez votre page à celles déjà réalisées ([TP1](/docs/competences/texte/page5/), [TP2](/docs/NSI/HTML/page11/)), afin de créer un site Web complet.

{{< img src="../images/marignan3.png" link="/docs/NSI/HTML/page11/" >}}

* Organisez votre code et vos fichiers et sous-dossiers du projet.
* Essayez autant que possible d'avoir une présentation homogène pour toutes les pages de votre site.
* Utiliser une feuille de style pour rassembler toutes les déclarations CSS du site.
* Ajouter une page pour personnaliser encore plus votre site (vous aimez les voyages, la lecture, la peinture, les jeux videos...), partagez vos goûts ou vos connaissances.


Vous trouverez de nombreuses références sur les styles sur Internet mais le plus simple sera d'utiliser [cette page](https://portail.lyc-la-martiniere-diderot.ac-lyon.fr/srv1/html/cours_html_css_nsi/exo_css_nsi/css_couleurs.html), ou bien celui-ci très complet: [MDN Mozilla](https://developer.mozilla.org/fr/docs/Learn_web_development/Getting_started/Your_first_website/Styling_the_content)

