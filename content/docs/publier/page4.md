---
Title: classif vivant
---


# TP HTML/CSS n°2 - La classification du vivant

## Rappels : Balises et règles CSS

### Tableau récapitulatif des balises HTML

| Balise | Utilisation | Syntaxe |
|--------|-------------|---------|
| `<h1>` | Titre principal | `<h1>Mon titre</h1>` |
| `<h2>` | Titre de section | `<h2>Ma section</h2>` |
| `<h3>` | Sous-titre | `<h3>Mon sous-titre</h3>` |
| `<p>` | Paragraphe | `<p>Mon texte...</p>` |
| `<a>` | Lien hypertexte | `<a href="URL">Texte du lien</a>` |
| `<img>` | Image | `<img src="nom_image.jpg">` |
| `<figure>` | Container pour image | `<figure>...</figure>` |
| `<figcaption>` | Légende d'image | `<figcaption>Texte</figcaption>` |
| `<div>` | Container / bloc | `<div>...</div>` |
| `<blockquote>` | Citation | `<blockquote>...</blockquote>` |
| `<strong>` | groupe de mots en gras | `<strong>...</strong>` |

### Principales règles CSS utiles

| Propriété | Effet | Exemple |
|-----------|-------|---------|
| `color` | Couleur du texte | `color: blue;` |
| `background-color` | Couleur de fond | `background-color: lightgreen;` |
| `font-size` | Taille du texte | `font-size: 20px;` |
| `font-family` | Police de caractères | `font-family: Arial, sans-serif;` |
| `text-align` | Alignement du texte | `text-align: center;` |
| `width` | Largeur | `width: 80%;` |
| `margin` | Marges externes | `margin: 20px;` |
| `padding` | Marges internes | `padding: 10px;` |
| `border` | Bordure | `border: 2px solid black;` |
| `display: flex;` | Placer côte à côte | `display: flex;` |

### Structure de base d'un document HTML

```html
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<title>Titre de la page</title>
</head>
<style>
	/* Vos règles CSS ici */
</style>
<body>
	<main>
	<!-- Votre contenu ici -->
	</main>


</body>
</html>
```

---

## Consignes du TP

Vous allez créer une page web sur **la classification du vivant** en utilisant vos connaissances en HTML et CSS.

### Étape 1 : Créer le fichier
1. Ouvrez **Notepad++**
2. Copiez le texte de contenu ci-dessous
3. Enregistrez le fichier sous le nom `classification.html` dans vos Documents

### Étape 2 : Structurer le document
En vous aidant du tableau récapitulatif :
- Ajoutez la structure de base du document HTML (doctype, html, head, body, main)
- Identifiez et ajoutez les balises appropriées pour :
  - Le titre principal
  - Les titres de sections
  - Les paragraphes
  - Le lien en fin de document

### Étape 3 : Ajouter une image
- Téléchargez l'image fournie (arbre phylogénétique)
- Placez-la dans le même dossier que votre fichier HTML
- Insérez l'image dans le document avec une légende appropriée
- Utilisez un container `<div style="display:flex;">` pour placer l'image à droite du paragraphe concernant "Les arbres phylogénétiques"

### Étape 4 : Styliser la page
Créez des règles CSS pour :
- Donner un style particulier au titre principal (police, couleur, taille, centrage)
- Définir une largeur et une couleur de fond pour le `<main>`
- Adapter les dimensions de l'image et de son paragraphe associé
- Personnaliser l'apparence des légendes d'images
- Ajouter des bordures et marges si nécessaire

**Objectif visuel** : Obtenir une page lisible, structurée et esthétique.

---

## Texte de contenu à structurer

```
La classification du vivant
Qu'est-ce que la classification du vivant ?

La classification du vivant est une science qui a pour objet de regrouper les êtres vivants par catégories. Le système actuel repose sur la notion d'évolution et de parenté entre les espèces. On classe ensemble les êtres vivants qui partagent un ancêtre commun récent. Cette approche s'appelle la classification phylogénétique.

Les critères de classification

Pour classer les êtres vivants, les scientifiques comparent leurs caractères, c'est-à-dire leurs caractéristiques observables : présence d'un squelette interne, de plumes, de poils, d'écailles, type de reproduction, etc. Plus deux êtres vivants partagent de caractères en commun, plus ils sont proches sur le plan de l'évolution. Ces caractères partagés sont appelés caractères dérivés et ils témoignent d'une origine commune.

Les arbres phylogénétiques

Les relations de parenté entre les espèces sont représentées sous forme d'arbres phylogénétiques, aussi appelés arbres du vivant. Chaque branche de l'arbre représente un groupe d'êtres vivants partageant des caractères communs. Les nœuds de l'arbre correspondent aux ancêtres communs hypothétiques. Plus on remonte dans l'arbre, plus on retrouve des ancêtres communs à de nombreux groupes d'organismes.

L'importance de la classification

La classification du vivant permet aux scientifiques du monde entier de parler le même langage lorsqu'ils étudient la biodiversité. Elle aide à comprendre l'histoire évolutive de la vie sur Terre et à identifier les relations entre les différentes formes de vie. Cette connaissance est essentielle pour la conservation des espèces et pour mieux comprendre comment la vie s'est diversifiée au cours des temps géologiques.

Sitographie
Article adapté de la page Classification phylogénétique du vivant consultée le 15 janvier 2024 sur Wikipédia : https://fr.wikipedia.org/wiki/Classification_phylog%C3%A9n%C3%A9tique_du_vivant
```

---

## Image à télécharger

Pour ce TP, vous utiliserez une image d'arbre phylogénétique simplifié.

**Recherche de l'image** : 
- Rendez-vous sur Wikimedia Commons ou Wikipedia
- Recherchez "arbre phylogénétique" ou "phylogenetic tree"
- Choisissez une image libre de droits
- Téléchargez-la et enregistrez-la sous le nom `arbre.jpg` dans le même dossier que votre fichier HTML

---

## Critères de réussite

✓ Le document HTML est valide et s'affiche correctement dans le navigateur  
✓ Toutes les balises de structure sont présentes (h1, h2, p)  
✓ Le lien est fonctionnel  
✓ L'image est visible avec sa légende  
✓ L'image est placée à droite d'un paragraphe  
✓ Des règles CSS personnalisées sont appliquées  
✓ La mise en page est cohérente et agréable visuellement  

**Bonus** : Ajoutez une couleur de fond différente pour les titres h2, ou créez une bordure autour des images.

---

**Bon courage !**
