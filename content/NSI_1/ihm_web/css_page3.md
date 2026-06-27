---
Title: direct css
description: TP css en pratique en utilisant un framework comme direct css, bootstrap
hidden: true
weight: 13
---

* page du site vers le [CSS](../css_page1/)
* page du site vers le [CSS display et position](../css_page2/)
* pratique du css: [TP](../css_page3)

# Direct css
La technique de direct-css est une manière originale de styliser le document, qui s'apparente à faire de la stylisation directe en inline.

L'idée est d'ajouter des valeurs à l'attribut class. Ces classes font référence au fichier *framework* en ligne. Voir pour plus d'infos [tailwindcss.com](https://tailwindcss.com/docs/utility-first).

Ainsi, pour réaliser le pop up suivant, le script HTML ne contient que queslques lignes. Sans écriture d'une seule ligne de css. On fait alors référence à des classes définies sur une feuille de style externe, chargée au démarrage:

{{< img src="../images/direct_css.png" >}}


```html
<!-- version courte -->
  <div class="p-6 max-w-sm mx-auto bg-white rounded-xl shadow-lg flex items-center space-x-4">
  <div class="shrink-0">
    <img class="h-12 w-12" src="chat.svg" alt="ChitChat Logo">
  </div>
  <div>
    <div class="text-xl font-medium text-black">ChitChat</div>
    <p class="text-slate-500">You have a new message!</p>
  </div>
```

**Remarque:** les styles sont ajoutés en nommant les classes, dans l'attribut `class`. Il peut y avoir plusieurs classes par balise. Chaque classe ajoutée sera séparée par un espace.

## Démarrer
Pour démarrer, il faudra placer la ligne suivante dans le `<head>`:

```html
<script src="https://cdn.tailwindcss.com"></script>
```

Le squelette du document est alors:

```html
<!doctype html>
<html>
<head>
  <meta charset="UTF-8">
  <script src="https://cdn.tailwindcss.com"></script>
</head>
<body>
``` 


Sous la balise `<body>`, ajouter les lignes suivantes:

```html
<h1 class="text-3xl font-bold underline">
Hello world!
</h1>
</body>
</html>
``` 

Ouvrir ensuite les *developper tools* du navigateur > [inspecteur](https://developer.mozilla.org/fr/docs/Learn/CSS/Building_blocks/Debugging_CSS)

> Puis survoler le script HTML du *dev tools* pour atteindre l'élément `h1`.

**question a:** Quelles sont les propriétés css qui sont ajoutées à partir des classes *text-3xl font-bold et underline*? Faire une liste de ces propriétés.


## Positionner des éléments dans une carte
> Remplacer le contenu de la page (titre h1 *Hello World*) par le script donné plus haut pour le *chat*.

> Telecharger et ajouter le logo *chat.svg* dans le même dossier que celui du fichier html: 

{{< img src="../images/chat.svg" link="../images/chat.svg" caption="cliquer pour telecharger l'image" >}} 


**question b**: Dans la fenêtre *inpecteur du dev tools*: Quelles sont les propriétés css ajoutées pour obtenir chacune des cartes A, B, C?

{{< img src="../images/chitchat.png" >}}

**A, B, C**:

* box-shadow
* padding
* border-radius
* align-items
* max-width
* display-flex
* margin-left
* margin-right

**question c:** même question pour les cartes D, E, F

{{< img src="../images/chitchat3.png" link="../images/chitchat3.png" caption="cliquer pour agrandir" >}}

## Construire un formulaire
Un formulaire contient des balises `form, label et input`. Celles-ci sont imbriquées de la manière suivante:

{{< img src="../images/chitchat4.png" caption="arbre du DOM pour un formulaire à 2 champs de saisie" >}}

En vous inspirant de la carte de *chat* (paragraphe précédent), ainsi que de l'arbre du DOM pour le formulaire, réaliser un formulaire de connexion dans une carte sur le modèle suivant:

{{< img src="../images/chitchat5.png" caption="exemple de formulaire de connexion" >}}

### Choisir les classes:
#### pour les éléments texte `<p>` choisir une combinaison de classes parmi: 


* text-xs, text-sm, text-base, text-lg, text-xl 
* font-medium 
* text-slate-500, text-slate-700 
* text-black
* text-gray-100, text-gray-200, ... text-gray-900
* text-red-100, text-red-200, ... text-red-900
* ...

Plusieurs classes peuvent être ajoutées. Elles doivent être séparées par un espace, entre les guillemets de l'attribut `class`

#### Pour les éléments `<input>`
Ces éléments ont 2 attributs `type` et `value` qui sont obligatoires, précisant le type `text` et la valeur écrite par défaut:


```html
<input type="text" value="tbone" class="mt-1 block w-full px-3 py-2 bg-white border border-slate-300 rounded-md text-sm placeholder-slate-400 text-gray-400
  focus:outline-none focus:border-sky-500 focus:ring-1 focus:ring-sky-500 focus:text-gray-700"/>
```

### Ajouter le bouton
Ajouter le script:

```html
<button class="px-4 py-1 text-sm text-purple-600 font-semibold rounded border border-purple-200 hover:text-white hover:bg-purple-600 hover:border-transparent focus:outline-none focus:ring-2 focus:ring-purple-600 focus:ring-offset-2">Log in</button> 
```

Son positionnement peut être ajusté en le mettant dans un élément `div` et en ajoutant les classes `px-XX` et `py-YY`, où XX et YY sont des valeurs en pixels (1, 2, 3, ...).

**question d:** quelles sont les propriétés css modifiées par ces 2 classes `px-XX` et `py-YY`? Chercher la réponse dans l'inspecteur du *dev tools*.

# Paramètres réseau
## Quels éléments sont chargés par le navigateur?
Ouvrir maintenant le **moniteur réseau** (onglet réseau ou network).
Après le chargement de la page, observer les informations affichées.

{{< img src="../images/chitchat6.png" >}}

Recommencer le chargement de la page, mais cette fois après avoir coché l'option *désactiver les caches* (*disable caches*). *La procédure peut différer selon le navigateur utilisé.*

**question e:** Combien d'éléments sont chargés pour afficher la page? Quels sont ces éléments?

## Analyse de la requête client - serveur
Dans la liste des éléments rechargés par la page, repérer la ligne qui concerne l'échange avec le serveur `cdn.tailwindcss.com/`

Cliquer sur cette ligne et afficher le `header`. Parcourir les informations d'échange entre client (navigateur) et le serveur distant. Les informations précisent les requêtes-reponses entre le client et le serveur. Un code de statut (**statut code**) spécifie cet échange. 


**question f:** combien de serveurs différents sont solicités pour le chargement de votre page?

**question g:** Quel a été ce code lors de la communication client-serveur? Que signifie t-il? 


# Compléments (lecture)
La technique de direct-css est une manière originale de styliser le document, qui s'apparente à faire de la stylisation directe en inline).

L'idée est d'ajouter des valeurs à l'attribut class. Ces classes font référence au fichier *framework* en ligne. Voir pour plus d'infos [tailwindcss.com](https://tailwindcss.com/docs/utility-first).

Ainsi, pour réaliser le pop up suivant, il faudra de nombreuses lignes de script css:

{{< img src="../images/direct_css.png" >}}

```html
<!-- version longue -->
<div class="chat-notification">
  <div class="chat-notification-logo-wrapper">
    <img class="chat-notification-logo" src="/img/logo.svg" alt="ChitChat Logo">
  </div>
  <div class="chat-notification-content">
    <h4 class="chat-notification-title">ChitChat</h4>
    <p class="chat-notification-message">You have a new message!</p>
  </div>
</div>

<style>
  .chat-notification {
    display: flex;
    max-width: 24rem;
    margin: 0 auto;
    padding: 1.5rem;
    border-radius: 0.5rem;
    background-color: #fff;
    box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04);
  }
  .chat-notification-logo-wrapper {
    flex-shrink: 0;
  }
  .chat-notification-logo {
    height: 3rem;
    width: 3rem;
  }
  .chat-notification-content {
    margin-left: 1.5rem;
    padding-top: 0.25rem;
  }
  .chat-notification-title {
    color: #1a202c;
    font-size: 1.25rem;
    line-height: 1.25;
  }
  .chat-notification-message {
    color: #718096;
    font-size: 1rem;
    line-height: 1.5;
  }
</style>
```

Mais cela peut être remplacé par le script HTML minimum suivant. Sans écriture d'une seule ligne de css. On fait alors référence à des classes définies sur une feuille de style externe, chargée au démarrage:

```html
<!-- version courte -->
  <div class="p-6 max-w-sm mx-auto bg-white rounded-xl shadow-lg flex items-center space-x-4">
  <div class="shrink-0">
    <img class="h-12 w-12" src="chat.svg" alt="ChitChat Logo">
  </div>
  <div>
    <div class="text-xl font-medium text-black">ChitChat</div>
    <p class="text-slate-500">You have a new message!</p>
  </div>
```





