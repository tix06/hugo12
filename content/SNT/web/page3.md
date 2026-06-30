---
title : HTML
description: langage HTML, balises
weight: 11
---

{{< img src="../images/web_evolution.png" link="https://youtu.be/XYTwYmOjqQs?si=Gocy9dPHaZCJM26F" caption="video - evolution des pages web 1990-2019" >}}

# Document Web: HTML
## Contenu et Structure
Le contenu des documents Web est rédigé en langage HTML (acronyme de Hypertext Markup Language). HTML est un langage interprété (par le navigateur). C'est un langage de description qui gère le contenu (le texte et les images), en ajoutant des éléments de structure, comme par exemple:

* mettre le texte dans un paragraphe
* mettre du texte en relief
* insérer un hyperlien sur le texte
* mettre un titre à la page, au paragraphe
* ...

{{< img src="../images/contenustructure.png" link="https://vimeo.com/138623721" caption="Lire la video depuis 20' => 1min40'" >}}

Cette combinaison de contenu et de structure a été vue avec la création d'un document sous LibreOffice Writer. Ces documents ne peuvent toutefois pas servir à la navigation sur internet. Leur poids est trop important, et le code de la page n'est pas normalisé. On utilise pour la redaction de ces pages une combinaison de langages (html, css, js) qui seront rédigés de manière normalisée (recommandations du w3c), et interprétés de la même manière ou presque par tous les logiciels navigateurs.

## Les éléments en HTML
### Balises
Les élements sont décrits par des *balises*, comme par exemple, l'élément paragraphe `p`, est déclaré à l'aide d'une balise `<p>`. Toute balise ouverte doit être refermée, ici avec `</p>`. Et le contenu (souvent textuel), est mis entre ces deux balises:

{{< img src="../images/balises.png" caption="exemple d'une balise paragraphe" >}}
Ces balises s'utilisent comme des *parenthèses* et peuvent être imbriquées. Une mauvaise imbrication de balises constitue une erreur.

Par exemple: Une imbrication **correcte**:

```html
<body>
    <div>  
      <h1>Wanted!</h1>
    </div>
</body>
```

Une imbrication **non correcte**:

```html
<body>
    <div>  
      <h1>Wanted!</h1>
    
</body>
</div>
```



## Les balises principale
**Les balises sont les instructions en langage HTML des éléments structurants de la page web.**

Les balises se distinguent entre celles qui n'ont pas d'attribut obligatoire, et celles qui en ont. Un attribut va ajouter des fonctionnalités à l'élément HTML, et modifier son allure ou son fonctionnement.

Voir l'[exercice 1](/pdf/SNT/html_snt.pdf)

### Balises sans attribut
Les principales balises structurantes sont:

* h1, h2, h3, ... h6
* div
* p
* span
* ...

Elles s'utilisent de la manière suivante:

```html
<h1>Texte</h1>
<p>Texte</p>
```

Il existe aussi des balises qui doivent être combinées, comme celles de listes:

* ul (parent) => li (enfants) pour une liste à puces
* ol (parent) => li (enfants) pour une liste ordonnée (numérotée)

*exemple:*

```html
<ul>
<li>ligne1</li>
<li>ligne2</li>
</ul>
```

### balises avec attribut obligatoire

#### image
Il s'agit d'une balise *orpheline*.

```html
<img src="lien_vers_la_ressource.jpg">
```

#### lien
Voir l'[exercice 1](/pdf/SNT/html_snt.pdf)

```html
<a href="lien_vers_la_ressource.html">texte cliquable</a>
```


On peut ajouter des attributs à une balise. Cela permet de modifier son comportement. Par exemple, la balise de lien `a` prend un argument obligatoire qui est `href`, et qui pointe vers la ressource. Lorsque l'on clique sur le contenu (ce qui est affiché par la balise), on est dirigé vers cette ressource.

*Exemple:* En reprenant l'exemple initial, on souhaite maintenant créer un lien hypertexte sur l'un des mots affichés. On inclue la balise suivante dans le paragraphe:

{{< a link="http://fr.wikipedia.org/restauration_1814" caption="Restauration" >}}
Le lien{{< a caption="Restauration" >}}
Et cela va rediriger sur la page de wikipedia: restauration française de 1814, lorsque l'on clique sur{{< a link="https://fr.wikipedia.org/wiki/Portail:Restauration_française_1814-1830" caption="Restauration" >}}
{{< img src="../images/balises_liens.png" alt="rendu navigateur html avec lien" caption="exemple de liens dans un paragraphe" >}}


## Structure du document
### La premiere page de l'histoire du Web
Voir l'article sur [Lumni.fr](https://www.lumni.fr/article/le-premier-site-web-de-l-histoire#:~:text=Lumniz%20%C3%A0%20remporter.-,En%201990%20par%20Tim%20Berners%2DLee%2C%20l'inventeur%20du,%C3%A9t%C3%A9%20r%C3%A9guli%C3%A8rement%20mis%20%C3%A0%20jour.)

Cette page ne présentait pas de mise en forme particulière. Le code ne contenait pas de balises *fermantes*. Les pages n'étaient pas hierarchisées.

### Mise en boîte
Avec la norme actuelle du HTML, les pages présentent un structure qui propose un parcours de lecture, un design. L'idée est de capter l'attention du lecteur le plus longtemps possible, de transmettre une information dans un certain ordre.

Et pour mettre en forme des éléments à différentes positions, il faut insérer les éléments HTML dans des "boîtes".

D'où l'usage de balises dite "container", qui vont permettre ces structures en lignes et colonnes, comme `div`, `section`, `article`, ...

La boite principale sera l'élément `body`, qui contiendra toutes les autres.

### Une représentation en *arbre*
Observons 2 exemples. 

Dans le premier, les éléments de la page se mettent l'un sous l'autre. Ici, les balises ne présentent pas de hierarchie entre elles. Elles sont toutes au même niveau.

{{< img src="../images/dom1.png" >}}

Dans ce deuxieme exemple: l'élément `h1` est au même niveau de hierarchie que l'ensemble suivant, constitué de 2 colonnes. Tout cet ensemble sera mis dans un container `div`.

Les 2 colonnes contiennent pour la premiere, les éléments `h2` et `p`, et pour la deuxieme, une image.

Chacune de ces 2 colonnes devront être mises dans un élément parent, un autre container `div` par exemple. Cela va amener la descrition suivante:

{{< img src="../images/dom2.png" >}}

Le schéma suivant montre la position de ces *boîtes* dans la fenêtre:

{{< img src="../images/dom4.png" >}}

L'image en forme d'arbre, montre la hierarchie (généalogie) entre ces éléments.

{{< img src="../images/dom3.png" >}}

### Exercice 
Voir l'[exercice 2](/pdf/SNT/html_snt.pdf)

Dans l'exemple qui suit, on peut lire dans le script html que la balise `html` contient celles `head` et `body`. `html` est donc une balise parente de `head` et `body`. On peut représenter ces liens de parentée avec le diagramme suivant:

{{< img src="../images/squelette.png" >}}
**Script complet:**

```html
<html>
  
  <head>
    <link rel="stylesheet" href="style.css">
  </head>
  
  <body>
  
    <div>  
      <h1>Wanted!</h1>
      <h3>Have you seen this robot?</h3>
      <img src="robot.png">
      <p>Description: Height: 30cm, Colour: purple and orange, Arms: 4</p>
      <p>If you have any information, please contact 6207 332 2310</p>
    </div>
    
  </body>
  
</html>
```

> **Exercice:** A l'aide du script complet, poursuivre le diagramme représentant la hierarchie entre ces balises.

# Lien vers la suite du TP

* {{< a link="../web2" caption="le TP HTML" >}}

* {{< a link="../web5" caption="Le cours sur CSS" >}}

* {{< a link="../web6" caption="Le TP sur CSS" >}}  
      
* {{< a link="../web3/" caption="créer une animation en Javascript" >}}  


