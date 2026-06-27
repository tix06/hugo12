---
Title : HTML CSS les bases
hidden: true
weight: 10
---



# Programmation: HTML et CSS
## Rappels de SNT
Si vous débutez complètement en HTML, consultez les ressources de SNT:

* Une introduction à la redaction d'un document en HTML:{{< a link="/SNT_2nde/pages/page4/web1/" caption="Document Web, contenu et structure" >}}* Les balises principales:{{< a link="/SNT_2nde/pages/page4/web2/" caption="Rappels" >}}

## Compléments théoriques
* introduction au html/css: activité version [guidée](../html_page11) ou version [autonome](../html_page1)
* page du site vers le [HTML](../html_page3/)
* page du site vers le [CSS](../css_page1/)
* page du site vers le [CSS display et position](../css_page2/)

## Deux balises pour tout écrire
On pourrait utiliser une ou deux balises uniques pour tous les usages, par exemple :

* la balise `DIV` pour des éléments qui devront s'afficher l'un **sous** l'autre.
* la balise `SPAN` pour des éléments qui devront s'afficher l'un **à côté** de l'autre.

Voici le code HTML utilisé : 

```html
<!DOCTYPE html>

<html>
    <head>
        <meta charset="UTF-8">
        <title>Marignan 1515</title>
    </head>

<body>
<div class="main">
  <div class="titre">La bataille de Marignan</div>
  <div class="contenu">
      <div class="paragraphe">
        La bataille de Marignan (Marignano en Italie, aujourd’hui Melegnano, ville à 16 km au sud-est de Milan) eut lieu les 13 et 14 septembre 1515 et opposa le roi de France <span class="lien" onclick="window.location.href = 'https://fr.wikipedia.org/wiki/François_Ier_(roi_de_France)'">François Ier</span> et ses alliés vénitiens aux mercenaires suisses qui défendaient le duché de Milan.
      </div>
      <div class="paragraphe">
        Première victoire du jeune roi François Ier, acquise dès la première année de son règne, elle fit environ 16 000 morts en seize heures de combat.
      </div>
  </div>
</div>
</body>
```


* Résultat obtenu SANS aucune règle CSS : 

{{< img src="../images/marignan1.png" >}}

*Remarques: le contenu apparait de manière structuré, mais sans aucune mise en forme. Le lien est fonctionnel: cliquer sur le nom François Ier pour vous en apercevoir.*

* Résultat obtenu AVEC les règles CSS : 

{{< img src="../images/marignan2.png" >}}


Les règles CSS utilisées pour ce 2<sup>e</sup> exemple:

```html
<style>
.contenu{
  border:solid;
  margin: 0.5em;
  padding: 0.5em;
}
.titre{
  font-size:1.5em;
  text-decoration: none;
}

.paragraphe{
  text-indent:20px;
  text-align:justify;
}
.lien{
  color:blue;
  cursor: pointer;
}

</style>
```

Les balises `<style>` peuvent être insérées n'importe où dans le document *html*. Mais la bonne pratique est de les mettre dans l'élément *head*. Ou, encore mieux, dans un fichier séparé, comme on le verra plus loin.

**Commentaires :**

* Avec 2 balises seulement, il est possible de segmenter et d'afficher du contenu.
* Ces balises étant génériques, et souvent ré-employées, il faudra pouvoir distinguer les différents éléments et leur ajouter des attributs de classe (voir le pragraphe [indexer](#indexer-les-parties-du-document)).
* En ajoutant des règles de mises en forme, écrites dans la partie CSS, les éléments retrouvent leur rôle spécifique (container, paragraphe, lien...).
* comme vous l'imaginez, ce n'est pas la bonne pratique que d'utiliser seulement 2 balises pour tout le document : le code sera difficile à maintenir. Et vous aurez besoin d'écrire toutes les règles de mise en page CSS pour ces balises. Alors qu'avec des balises bien nommées, le navigateur va pouvoir appliquer les styles par défaut pour ces éléments.

## Quelques notions de CSS
Pour le cours complet sur CSS, voir la{{< a link="/docs/NSI/CSS/page1/" caption="page CSS" >}}
Les règles CSS sont construites de la manière suivante:

```css
selecteur { propriete: valeur; }
``` 

La valeur de la propriété se met après le séparateur `:`.

Le selecteur fait référence à un ou plusieurs éléments du document (sera développé plus tard).

{{< img src="../images/css.png" >}}

*Exemple:* Pour colorier TOUS les titres `h1` en bleu, on utilise la règle CSS que l'on peut mettre entre les balises `<style>`:

```css 
h1 { color: blue;}
``` 

## Activité 1: Construire un premier paragraphe en html et css
> Utiliser un editeur en ligne, comme par exemple{{< a link="https://htmledit.squarefree.com/" caption=" Utiliser un editeur en ligne, comme par exemple " >}}
**1.** La bataille de Marignan avec seulement 2 balises `<div>` et `<span>`

* Copier-coller les instructions html avec le contenu sur la *bataille de Marignan*.
* ajouter les balises `<style>` proposées plus haut et leur contenu CSS.
* Modifier les propriétés CSS et compléter le tableau.

| propriété | valeur | effet |
|--- |--- |--- |
| border | solid |  |
| border | dashed |  |
| font-size | 3em |  |
| font-size | 1em |  |
| text-decoration | underline |  |
| margin | 0 |  |
| margin | 0.5em |  |
| padding | 0em |  |
| padding | 0.5em |  |
| color | blue |  |
| background-color | rgb(230,230,230) |  |
| color | #66FF66  |  |
| cursor | pointer |  |
| text-align | left |  |
| text-align | right |  |
| text-align | justify |  |
| font-weight |  bold |  |

**2.** Remplacer maintenant toutes les balises `<div>` et `<span>` par les balises adequates. On s'aidera du tableau suivant:

| balise à remplacer | balise adequate |
|--- |--- |
| `<div class="main">` | `<main>`|
| `<div class="titre">` | `<h1>` |
| `<div class="contenu">` | `<section>` |
| `<div class="paragraphe">` | `<p>` |
