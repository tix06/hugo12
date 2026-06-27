---
Title : mini projet web
description: creation d'un mini site web avec plusieurs pages et un formulaire, html, css, javascript
hidden: true
weight: 20
---


# TP creation d'un mini site Web
Au cours de cette séance, vous allez créer 3 pages Web, formant un mini site Web. 

Commencez par créer un dossier dans vos *Documents* appelé *siteWeb*.<br>
Créez également 2 sous dossiers, *images* et *static*.<br>
A l'aide d'un editeur de texte, comme VisualCode ou bien Notepad++, créez 3 fichiers: page1.html, page2.html, page3.html, que vous mettrez à la racine de votre projet.

Voici l'arborescence des fichiers proposée pour ce projet, dans ce dossier *siteWeb*:


```
- page1.html
- page2.html
- page3.html  
- page4.html 
- static|
        |- style.css
- images|
        |- xxx.png
```


Ces pages, page1.html, page2.html, page3.html et page4.html devront posséder chacune des **liens de navigation** vers l'ensemble des pages du site. 

Il est souhaitable que ces liens se situent dans le bandeau de navigation *(voir plus loin)*.

Par exemple, pour la page 1:

{{< img src="../images/form.png" caption="Exemple de page avec formulaire" >}}
Commencer par intégrer le squelette HTML pour chacune des pages comme vu en cours:{{< a link="/docs/NSI/HTML/page3/#le-html-et-la-page-web" caption="Lien" >}}
# Page 1: Le formulaire d'accès

Pour la mise en forme de la page, il est fortement suggéré de lire:

* la page sur le `display` des éléments HTML: [CSS positionnement et display](https://developer.mozilla.org/fr/docs/Web/CSS/Layout_cookbook/Split_Navigation)
* la page sur les *bonnes pratiques* à propos de l'usage des *labels*: [MDN](https://developer.mozilla.org/fr/docs/Web/HTML/Element/Label)
* La page du site sur le positionnement des label, et input: [Lien vers la page](/docs/NSI/CSS/page2/)

Un formulaire peut posséder plusieurs éléments comme: 

* des éléments `input` de type `text`
* des éléments `input` de type `radio`
* des éléments `input` de type `button`
* des `textarea`

La liste complète, ainsi que quelques exemples sont donnés à la page: [MDN](https://developer.mozilla.org/fr/docs/Web/HTML/Element/Input)

# Pages 2 et 3: les travaux pratiques
Vous allez ajouter les pages de vos précédents travaux pratiques sur les thèmes:

* page2: [le plastique](/docs/competences/texte/page5/)
* page3: [Marignan 1515](/docs/NSI/HTML/page11/)

# Page 4: Page thématique
Vous aimez le vélo? Et bien présentez votre passion dans cette page thématique.

Cette deuxieme page appelée `velo.html` présentera un **court texte**, et une **image libre de droit**, comme par exemple: [https://pixabay.com/fr/photos/vélo-enfants-graffiti-art-3045580/](https://pixabay.com/fr/photos/vélo-enfants-graffiti-art-3045580/)

Pour respecter les droits d'auteur, vous pouvez ajouter un lien vers la page de l'auteur de l'image lorsque l'on clique sur l'image.

Le court texte peut être celui du Poëme de Ernest Pérochon:

```
Si j'avais une bicyclette,
J'irais dès le soleil levant,
Par les routes blanches et nettes
J'irais plus vite que le vent.

Si j'avais une automobile
Je roulerais au clair matin,
Je roulerais de ville en ville
Jusqu'aux murailles de Pékin.
``` 

*Conseil: Utiliser la balise `<pre>` pour conserver les retours à la ligne du poëme.*
  
Vous pourrez également ajouter un lien textuel vers la biographie de l'auteur.

# Uniformiser les styles
Vous avez probablement écrit les règles de style directement dans la page HTML, entre balises `<style>`. Le problème avec cette pratique, est que votre site manque d'uniformité graphique. La bonne méthode est d'utiliser une feuille de style externe:

* [Déclarez dans l'en-tête](https://developer.mozilla.org/fr/docs/Web/HTML/Element/link) le lien vers votre feuille de style avec la balise `<link>`:

`<link href="chemin_vers_fichier/style.css" rel="stylesheet" />`

* Mettez vos règles CSS dans un fichier externe appelé `style.css`




