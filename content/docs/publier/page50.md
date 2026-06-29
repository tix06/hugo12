---
Title: HTML de zero
---


# Rédiger un document pour le Web
## Le HTML : Structurer le document
Le HTML s'occupe de la **structure du document**, grâce à des **balises** qui intègrent le **contenu**.

## Formats de document

```
Démocratie athénienne
Les origines de la démocratie athénienne

Au vie siècle av. J.-C., les cités du monde grec sont confrontées à une grave crise politique. Pour répondre à cette crise, de nombreuses cités modifient radicalement leur organisation politique. À Athènes, un ensemble de réformes amorce un processus débouchant au ve siècle av. J.-C. sur l'apparition d'un régime politique inédit : une sorte de démocratie pour les hommes libres mais avec la continuation de l'esclavage.

La démocratie athénienne

La démocratie athénienne désigne le régime politique de démocratie directe mis en place progressivement dans la cité d'Athènes durant l'Antiquité et réputée pour être l'ancêtre des démocraties modernes. Le terme démocratie vient des mots grecs δῆμος / dêmos («le peuple») et κράτος / krátos («la puissance, le pouvoir»). Il s'agit donc d'un régime où les décisions sont prises par le peuple.

La cité

Athènes est fondée formellement vers 750 av. J.-C. par synœcisme de plusieurs agglomérations partiellement préservées de l'invasion des Doriens.

Le site est choisi pour la forteresse naturelle que représente l'Acropole ; les habitants peuvent résister aux hordes de pillards qui menacent la région, augmentant avec les années sa fortification. À partir de 510 av. J.-C., cette fonction défensive est abandonnée, le lieu étant consacré aux cultes et notamment celui d'Athéna, déesse protectrice d'Athènes. Des remparts encerclent à partir de 478 av. J.-C. la ville et son port, le Pirée.

Quelques gymnases et écoles de philosophie s'excentrent pour que leurs élèves profitent de la tranquillité et soient totalement isolés pendant les deux années de leur éphébie.

L'agora devient le centre social et politique de la cité avec l'installation des institutions démocratiques sur cette place. En été de nombreux débats houleux ou amicaux se tiennent à l'ombre du portique sud et de la Stoa Poikilè, on discute politique et philosophie. Des joutes oratoires d'un autre genre se déroulent sur la Pnyx, colline sur laquelle sont votées toutes les lois athéniennes. La cité est donc le cœur de la démocratie.
Sitographie
Article issu de la page (consultée le 01 dec 2023) Démocratie Athénienne sur wikipedia.org: https://fr.wikipedia.org/wiki/D%C3%A9mocratie_ath%C3%A9nienne
```

Le contenu doit être mis dans un document avec l'extension `.html`.

> **A vous de jouer:** Copiez l'ensemble du texte. **Dans un editeur de texte**: Rechercher parmi les logiciels installés: **Notepad++**: coller le texte. Sauvegarder dans vos *Documents* avec le nom `athenes.html`

> **Ouvrir à l'aide d'un navigateur**: Double clic sur le document depuis l'*explorateur windows*, ou bien, depuis le menu fichier du *navigateur*: `Ouvrir..` et rechercher le document.

**Problèmes:** 

* On obtient alors un document qui n'a aucune structure
* De plus, avec certains navigateurs, certains caractères ne sont pas reconnus et cela peut donner le rendu suivant:

{{< img src="../images/html5.png" caption="fichier texte non formaté ouvert avec un navigateur" >}}

On va résoudre certains de ces problèmes en déclarant le format d'encodage des caractères. Cette information est très importante pour le navigateur.

> **Au début du document `html`**: Ajouter avec l'editeur les lignes suivantes:

```html
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<title>page principale</title>
</head>
<body>
<main>
Démocratie athénienne
Les origines de la démocratie athénienne

Au vie siècle av. J.-C., ...
```

* Ajouter aussi les lignes suivantes en FIN de document:

```html
</main>
</body>
</html>
```

> **Navigateur:** Recharger la page (CTRL + r). Que remarquez vous?


## Définir des éléments dans la page
Pour créer un paragraphe, le contenu devra être inséré entre une balise de début `<p>` et une balise de fin `</p>`.

Les autres balises principales sont:

* Titre 1: `<h1> ... </h1>`
* Titre 2: `<h2> ... </h2>`
* Titre 3: `<h3> ... </h3>`
* Bloc de citation: `<blockquote> ... </blockquote>`
* liens: `<a> ... </a>`

Où les `...` signifient le contenu.






> **Balises HTML**: modifier la structure du document à l'aide des balises HTML: 

### ajouter la balise `h1` pour le titre principal

{{< img src="../images/html6.png" caption="" >}}

### ajouter les balises `h2` pour les titres des chapitres

{{< img src="../images/html7.png" caption="" >}}

### ajouter les balises `p` pour les paragraphes

{{< img src="../images/html8.png" caption="" >}}

### ajouter les balises `a` pour les liens: Le lien se trouve en fin de document dans cet exemple. 
Il s'agit du texte: `Article issu de la page (consultée le 01 dec 2023) Démocratie Athénienne sur wikipedia.org: https://fr.wikipedia.org/wiki/D%C3%A9mocratie_ath%C3%A9nienne`

* Identifier l'URL de redirection (l'adresse du lien): `https:/ ... dates-cle/`
* Identifier la cible du lien (le mot sur lequel vous devez cliquer): *Démocratie Athénienne sur wikipedia.org*
* Remplacer ce texte par le script suivant:

```html
Article issu de la page (consultée le 01 dec 2023) <a href="https://fr.wikipedia.org/wiki/D%C3%A9mocratie_ath%C3%A9nienne">Démocratie Athénienne sur wikipedia.org</a>
```

> **A savoir**: Dans les instructions de la balise `<a>`:
* la balise `<a>` possède un attribut `href`, à l'intérieur même de la balise: `<a href="">`
* l'URL se place entre les guillemets devant l'attribut `href`
* la cible du lien (le texte à cliquer) se place entre la balise ouvrante `<a>` et fermante `</a>`


> **Navigateur:** Recharger la page (CTRL + r). Que remarquez vous? Le lien est-ils actif lorsque l'on clique dessus?

## Ajouter une image
L'ajout d'image diffère de la procédure d'un logiciel d'edition de texte comme *Word* ou *Writer*. Ici, on n'insère pas l'image elle-même, mais on indique son adresse sur le net. La syntaxe est la suivante:

```html
<img src="chemin vers l'image">
```

On choisira une image libre d'être diffusée, comme par exemple celle sur le site *wikipedia* ci-dessous:

{{< img src="../images/pnyx.jpg" link="../images/pnyx.jpg" caption="Cliquer sur l'image pour télécharger">}}

> Cliquer sur l'image pour l'afficher seule dans une page. 

> Faire alors clic droit: enregister sous...

> enregistrer l'image dans le même dossier que votre fichier athenes.html

> Mettre alors l'image sous le paragraphe qui fait référence au Pnyx avec l'ensemble d'instructions:

```html
<figure>
<img src="pnyx.jpg">
<figcaption>Un texte sous l'image</figcaption>
</figure>
```

> Faites référence à l'auteur...

... si vous l'identifiez, ou bien la page dont est issue l'image, à l'aide d'un élément `html` qui suivra l'image. On peut modifier le texte de la balise `figcaption`.

```html
<figcaption>Plate-forme de la Pnyx d'où parle l'orateur public. En arrière-plan, l'Acropole. (wikipedia)</figcaption>
```

## Modifier la structure du document
Pour placer l'image à droite du pragraphe, on va utiliser un container (`div`) qui va englober les 2 éléments à placer côte à côte:

**Placer la balise `<div style="display:flex;">`** avant le paragraphe:

```html
<div style="display:flex">
<p class="gauche">L'agora devient le centre social ...
le cœur de la démocratie.</p>
```

Et **fermer** la balise `</div>` après l'objet `figure`:

```html
<figcaption>Plate-forme de la Pnyx ... (wikipedia)</figcaption>
</figure>
</div>
```


# Modifier les styles des éléments
Les instructions de style vont modifier les paramètres par défaut du navigateur pour les éléments HTML. L'idée est d'obtenir le rendu suivant pour votre page:

{{< img src="../images/html9.png" link="../images/html9.png" >}}

> Commencer par copier et coller ces nouvelles règles de style fin de document, juste avant la balise de fermeture `</html>`, les lignes suivantes:

```html
<style>
.titre{font-family: Papyrus, Herculanum, Party LET, Curlz MT, Harrington, fantasy;color: blue;font-size: 40px;text-align: center;}
main {width: 80%;margin: 50px;background-color: hsla(0,70%,50%,0.3);padding: 0 20px 20px 20px;border: 5px solid black;}
.gauche{width:50%;}
figure{width:30%;}
img{width:100%;}
figcaption{font-size: 0.8em;font-style: italic;}
a:visited{color: #0000ff;}
</style>
```

> Modifier ensuite le style du titre principal ainsi que la position de l'image avec les manipulations suivantes:

* Ajouter *l'attribut de classe* au titre h1 en modifiant sa balise. Remplacer `<h1` par `<h1 class="titre">`
* Ajouter *l'attribut de classe* au paragraphe qui traite de la partie sur le *Pnyx*. Ce paragraphe devrait alors se placer à gauche de l'image. Remplacer `<p>` par `<p class="gauche">`, seulement pour ce paragraphe.
