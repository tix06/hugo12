---
Title: de Writer a HTML
---

# Découverte du langage HTML
## docx, odt, txt et html: différents documents textuels
Les fichiers aux extensions docx et odt permettent d'écrire et présenter du texte. La structure du document se fait à l'aide de boutons d'options proposés par le logiciel. Le rendu visuel de la page est présenté par le logiciel au fur et à mesure de sa construction.

{{< img src="../images/word.png" >}}

Pour la creation d'une page web, c'est différent. On utilise un editeur HTML, comme notepad++. 

Dans l'editeur, pour structurer le contenu textuel, il n'y a pas de *boutons* pour choisir les *propriétés des éléments*. Il faut ajouter DANS LE DOCUMENT des *métadonnées*. Cela se fait d'une manière très speciale avec le html, à l'aide de BALISES. C'est ce que nous allons voir ici.

{{< img src="../images/balises.png" >}}

Pour afficher la page, il faudra retrouver la page à l'aide de l'explorateur, sur votre disque dur, et l'ouvrir avec un 2e outil, le navigateur.

{{< img src="../images/navigateurs.png" >}}

## Le HTML : Document pour le Web
Un document pour le Web est constitué d’un ou plusieurs fichiers de type texte. Le fichier aura pour extension `.html`. Un fichier `.html` doit être ouvert avec un **navigateur**.

La manière avec laquelle vous allez construire ce document suit les même étapes que la rédaction d’un document textuel. Mais ici, les instructions de **mise en page** seront ajoutées au **contenu**, dans le même fichier.

Le langage HTML s'occupe de la **structure du document**, grâce à des **balises** qui intègrent le **contenu**.

## Format de document
> **A vous de jouer:** Télecharger et ouvrir le document textuel sur {{< a link="/pdf/competences/plastiques.txt" caption="les plastiques" >}}. Copiez l'ensemble du texte (CTRL + a, CTRL + c)

> **Dans un editeur de texte**: Rechercher parmi les logiciels installés: **Bloc notes, Notepad**, ou mieux, **Notepad++** (ajoute la coloration syntaxique): coller le texte. Sauvegarder dans vos *Documents* avec le nom `plastiques.html`

> **Ouvrir à l'aide d'un navigateur**: Double clic sur le document depuis l'*explorateur windows*, ou bien, depuis le menu fichier du *navigateur*: `Ouvrir..` et rechercher le document.

**Problèmes:** 

* On obtient alors un document qui n'a aucune structure
* De plus, avec *certains navigateurs*, certains caractères ne sont pas reconnus et cela peut donner le rendu suivant:

{{< img src="../images/html3.png" caption="fichier texte non formaté ouvert avec un navigateur" >}}

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
<section>
Le plastique, une « antiquité » !
Plusieurs siècles av. J.C, les hommes utilisaient déjà ...
```


* Ajouter aussi les lignes suivantes en FIN de document:

```html
</section>
</body>
</html>
```

> **Navigateur:** 
> * Recharger la page (CTRL + r). Que remarquez vous?
> * Dans le fichier *html*. Remplacer `<meta charset="utf-8">` par `<meta charset="us-ascii">`. Recharger la page. Que remarquez vous? Lequel des 2 encodages, *us-ascii* ou *utf-8* est le plus adapté pour présenter les caractères. 
> * Sélectionner le bon encodage pour la suite de votre travail.


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

{{< img src="../images/html1.png" caption="" >}}

### ajouter les balises `h2` pour les titres des chapitres

{{< img src="../images/html2.png" caption="" >}}

### ajouter les balises `p` pour les paragraphes

### ajouter les balises `a` pour les liens: Le lien se trouve en fin de document dans cet exemple. 
Il s'agit du texte: `Article issu de la page histoire du plastique de cabriolice.com https://www.carbiolice.com/blog/lhistoire-du-plastique-en-15-dates-cle/`

* Identifier l'URL de redirection (l'adresse du lien): `https:/ ... dates-cle/`
* Identifier la cible du lien (le mot sur lequel vous devez cliquer): *histoire du plastique*
* Remplacer le texte non formaté par le mélange de texte et de balises suivant:

`Article issu de la page <a href="https://www.carbiolice.com/blog/lhistoire-du-plastique-en-15-dates-cle/">histoire du plastique</a> de cabriolice.com`

> **Questions**: Dans les instructions de la balise `<a>`:
* où se place la cible du lien?
* où se place l'adresse du lien?

### 5. Ajouter un autre lien
Placer après cette dernière ligne un autre lien, vers la page de wikipedia sur les matières plastiques par exemple.



> **Navigateur:** Recharger la page (CTRL + r). Que remarquez vous? Les liens sont-ils actifs lorsque l'on clique dessus?

## Ajouter une image
L'ajout d'image diffère de la procédure d'un logiciel d'edition de texte comme *Word* ou *Writer*. Ici, on n'insère pas l'image elle-même, mais on indique son adresse sur le net. La syntaxe est la suivante:

```html
<img src="https://adresse_sur_le_net.jpg">
```

On choisira une image libre d'être diffusée, comme par exemple celle sur le site *wikipedia* d'adresse:

```
https://upload.wikimedia.org/wikipedia/commons/8/80/Compounding.png
```



Faites référence à l'auteur de l'image si vous l'identifiez, ou bien la page dont est issue l'image, à l'aide d'un élément `html` qui suivra l'image. On peut utiliser une balise `<figcaption> ... légende ... </figcaption>`.

{{< img src="https://upload.wikimedia.org/wikipedia/commons/8/80/Compounding.png" caption="production de granulés de polymères - image de la page *Matières plastiques* (wikipedia)" >}}

# Modifier les styles des éléments
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

Suivre le tutoriel à la page [developper.mozilla](https://developer.mozilla.org/fr/docs/Learn/Getting_started_with_the_web/CSS_basics) sur le CSS niveau débutant.

Vous pouvez tester les effets de certaines de ces instructions en les plaçant entre les balises `<style>` de votre document. Par exemple:

```html
<style>
h1 {
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

# Ajouter une deuxième page
Votre site web va être constitué de 2 pages, sur le recyclage des plastiques. Le contenu textuel se trouve dans ce fichier: [recyclage_plastiques.txt](/pdf/competences/recyclage_plastiques.txt)

Le texte est extrait de la ressource: [rapport du sénat sur le traitement des plastiques](https://www.senat.fr/fileadmin/Office_et_delegations/OPECST/Notes_scientifiques/OPECST_note39.pdf)

* Créer une 2e page HTML à partir de ce contenu
* Créer un lien depuis la page 1 vers la page 2, puis de la page 2 vers la page 1.

Cette fois-ci, vous allez créer des *liens internes* (entre documents d'un même site internet). Vous allez utiliser des *adresses relatives* entre les pages. Deux possibilités:

* Supposons que  `page1.html` et `page2.html` sont dans le **même dossier**: Pour créer un lien de la page 1 vers la page 2, la balise lien s'écrira: `<a href="page2.html">Lien vers la page 2</a>`
* Si les `page1.html` et `page2.html` ne **sont pas dans** le même dossier, il faudra utiliser le chemin relatif: `<a href="chemin/page2.html">Lien vers la page 2</a>`

Chemin relatif: explication [ici](https://www.alsacreations.com/astuce/lire/78-quelle-est-la-diffrence-entre-les-chemins-relatifs-et-absolus.html)

