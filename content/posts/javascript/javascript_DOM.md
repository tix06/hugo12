---
author: "Eric Tixidor"
date: 07-28-2020
linktitle: javascript_DOM
menu:
  main:
    parent: javascript
next: 
prev: 
title: Javascript le DOM
weight: 20
---

# Le DOM
le DOM ou Document Object Model, une interface qui fait partie du BOM (Browser Object Model) et grâce à laquelle nous allons pouvoir manipuler le contenu HTML et les styles de nos pages.

Le DOM est ainsi une représentation structurée du document sous forme « d’arbre » crée automatiquement par le navigateur, à partir de sa lecture du document HTML. 

Chaque branche de cet arbre se termine par ce qu’on appelle un nœud, contenant les éléments HTML. On va finalement pouvoir utiliser ces objets, leurs propriétés et leurs méthodes en JavaScript.

Le DOM fournit le squelette du document

Inspecter le DOM se fait avec le navigateur

<figure>
<img src="../images/browserDOM.png" width = "80%" alt="inspecter le DOM">
<figcaption>inspecter le DOM dans le navigateur</figcaption>
</figure>


C'est en particulier l’interface `Document` que nous allons utiliser pour parcourir le DOM : Toute opération sur le DOM commence avec l’objet document : 

<figure>
<img src="../images/arbreDOM.png" width = "80%" alt="arbre du DOM">
<figcaption>arbre du DOM</figcaption>
</figure>

Trois noeuds du DOM sont disponibles directement comme des propriétés de l’objet DOM :

*  document.documentElement
*  document.body
*  document.head

On verra plus loin les méthodes de parcours de l'arbre du DOM (## parcourir l'arbre du DOM).

# Manipuler les éléments de la page
## accéder à un élément à l'aide d'un sélecteur
Pour manipuler les éléments d'une page affichée dans le navigateur, on doit *accéder* à cet élément.

Or, il n'y a pas de lien direct entre html et javascript :
En Javascript, on peut récupérer une instance de HTMLElement correspondant à un élément de la page.

Cela peut se faire à l'aide des *ancres* laissées sur ces éléments. On peut les sélectionner, comme en CSS avec leur classe, leur ID ou le nom de la balise. Pour réaliser ceci, on utilise les fonctions suivantes:

- `document.getElementById()` permet de sélectionner un élément html à partir de son id.
- `document.querySelector()` un sélecteur plus générique qui sélectionne les éléments à la manière des sélecteurs css.

### Un premier exemple : afficher du texte
lorsque l’on souhaite injecter du texte dans un paragraphe dont l'attribut `id="ancre"`, un élément que l'on aura défini dans la partie `html` du code avec :

`<p id = "ancre"></p>`

on utilisera dans la partie javascript:  

`document.getElementById('ancre').innerHTML = "nouveau texte à afficher"`.

### Exemple 2 : modifier l'attribut style de l'élément
soit un élement avec attribut id='elem' de la page :
On cherche à atteindre cet élément et en modifier la couleur : 

*(écrire le code suivant dans un fichier que vous nommerez `exemple1.html`)*
```html-css
<body>
  <h1 id="elem">Un titre qui n'a pas de couleur</h1>
<script>
let elem = document.getElementById('elem');
elem.style.background = 'red';
</script>
</body>
```
On met cet élément dans une variable `elem`. Puis on peut modifier ses attributs, comme par exemple celui `style` pour la couleur.

Ouvrir le fichier avec un navigateur. La couleur du titre devrait apparaitre ... en rouge !

### Exemple 3 : utilisation de querySelector
Cette méthode associée à *document* permet d'utiliser les mêmes règles de selection que lorsque l'on utilise le CSS. On peut donc utiliser comme paramètre : le nom de la balise 'p', la classe de l'élément '.maclasse', l'identifiant '#elem', ...

voir la [page consacrée sur w3schools](https://www.w3schools.com/jsref/met_document_queryselector.asp)

## parcourir l'arbre du DOM
La propriété `childNodes` de l'interface `Node` renvoie une liste sous forme de tableau des nœuds enfants de l’élément donné. Le premier nœud enfant reçoit l’indice 0 comme pour tout tableau.

Et pour obtenir l'élément parent d'un noeud, on utilise la propriété `parentElement`.

*Exemple  :* 
Vous pouvez tester cet exemple en enregistrant le code  suivant dans un fichier que vous nommerez `exemple3.html`: 

```html
<body>
<div>
  <p id="myP">Un peu de texte, <a>un lien</a> et <strong>une portion en emphase</strong></p>
</div>
</body>
``` 

Ouvrir alors la page pour l'afficher dans le navigateur.

Cette page a alors l'arbre de DOM suivant qui lui est associé : 

<figure>
<img src="../images/dom.png" width = "80%" alt="arbre du DOM">
<figcaption>arbre du DOM</figcaption>
</figure>

Le premier enfant de `<p>` est un nœud textuel, alors que le dernier enfant est un élément `<strong>`. Cet élément `<strong>` possède pour noeud enfant un noeud textuel dont le contenu et *une portion en emphase*

Dans la console, saisir une à une les instructions suivantes : (sans les commentaires)
```javascript
> let paragraph = document.getElementById('myP'); // pour stocker le noeud parent.
> let first = paragraph.firstChild; // parcours de l'arbre jusqu'au 1er enfant
> alert(first.nodeValue); // pour récuperer le contenu du noeud textuel
```

<figure>
<img src="../images/dom1.png" width = "600px" alt="arbre du DOM">
<figcaption>contenu textuel du premier enfant</figcaption>
</figure>

Puis :
```javascript
> let last = paragraph.lastChild;
> alert(last.firstChild.data); // pour recuperer le contenu textuel de la balise
```

<figure>
<img src="../images/dom2.png" width = "600px" alt="arbre du DOM">
<figcaption>contenu textuel du dernier enfant</figcaption>
</figure>

On peut réaliser cette dernière manipulation en ayant recours à la liste de tous les enfants de `paragraph`: en écrivant dans la console : 

`> paragraph.childNodes` 

<figure>
<img src="../images/dom3.png" width = "600px" alt="arbre du DOM">
<figcaption>liste de tous les enfants du noeud parent</figcaption>
</figure>

On peut lire dans la console que le noeud textuel (`<strong>Une portion avec emphase</strong>`) est au rang 3 dans la liste des noeuds enfants (`childNodes`).

On affiche alors son contenu textuel : dans la console, écrire : 

```javascript
> let last = paragraph.childNodes[3]
> alert(last.firstChild.data)
```


<figure>
<img src="../images/dom4.png" width = "600px" alt="arbre du DOM">
<figcaption>contenu textuel de last</figcaption>
</figure>

Pour finir, on peut modifier à volonté les éléments textuels en modifiant la valeur renvoyée par `.data` ou `.nodeValue` : 

Dans la console : 
```javascript
> last.firstChild.data = 'un autre texte'
```
<figure>
<img src="../images/dom5.png" width = "600px" alt="arbre du DOM">
<figcaption>modification du contenu textuel de last</figcaption>
</figure>

# Ajouter un paragraphe dans la page
Pour créer un nouvel élément dans la page :

* créer un nouveau noeud an appelant la fonction `creatElement` associée à `document` 
* ajouter la balise textuelle associée à ce noeud s'il y en a une
* ajouter eventuellement des attributs à cet élément: `setAttribute(attribut,valeur)`
* ajouter cet élement directement à son noeud parent: `appenChild`

*Exemple :*

```html-css
<head>
<meta charset="utf-8" />
<script>
      var x = 10;

      /*
      Affiche la valeur de la variable x. Puis incrémente de 1 la valeur de la variable x
       */
      function addXToThePage() {
        let newP = document.createElement('p');
        newP.innerHTML = "<p>La valeur de x = " + x + "</p>";
        newP.setAttribute('style', 'color : red;');
        document.getElementById("newPar").appendChild(newP);
        x = x + 1;
      }
    </script>
  </head>
<body>
    <button onclick="addXToThePage();">
      Clique ici pour afficher la valeur de la variable x
    </button>
    <div id="newPar"></div>
</body>
```

*Résultat : (cliquer sur le bouton pour tester le programme)*

<button onclick="addXToThePage();">
      Clique ici pour afficher la valeur de la variable x
</button>
<div id="newPar"></div>


<script>
      var x = 10;
      function addXToThePage() {
        let newP = document.createElement('p');
        newP.innerHTML = "<p>La valeur de x = " + x + "</p>";
        newP.setAttribute('style', 'color : red;');
        document.getElementById("newPar").appendChild(newP);
        x = x + 1;
      }
      
        function buildTable(){
          let prenom = document.getElementById("prenom").value;
          let nom = document.getElementById("nom").value;
          let email = document.getElementById("email").value;

          // champ prenom
          let contenu =document.querySelector('.client1>.first');
          contenu.textContent=prenom;
      
          // champ nom
        
          // champ email
      }
    
 </script>


    
# Lire et modifier un tableau
Le programme suivant montre l'utilisation d'un formulaire. Lors du clic sur le bouton, on accède aux valeurs des champs du formulaire avec la propriété `.value` associée à l'élément du formulaire.

On recopie alors chacune des colonnes du tableau avec ces valeurs.

Pour accéder à chaque élément de la page, on utilise les règles de selection vues plus haut, avec `document.getElementById` et `document.querySelector`.

L'exemple présenté ici est incomplet et ne renvoie dans le tableau que le champ `prenom`. Il faudra completer le script pour renvoyer aussi les noms et email.

<table>
      <thead>
        <tr>
          <th>Prénom</th>
          <th>Nom</th>
          <th>email</th>
        </tr>
      </thead>
      <tbody>
      	<tr class="client1">
      		<td class="first"></td><td class="last"></td><td class="mail"></td>
      	</tr>
      </tbody>
</table>
    
<form>
      <fieldset>
        <legend>Nom complet</legend>
        <ol>
          <li>
            <label for="prenom">Saisir le prénom</label>
            <input id="prenom"  type="textarea" name="prenom" placeholder="prenom"/>
          </li>
          <li>
            <label for="nom">Saisir le nom</label>
            <input id="nom" type="textarea" name="nom" placeholder="nom" />
          </li>
          <li>
            <label for="email">E-mail</label>
            <input
              id="email"
              type="email"
              name="email"
              placeholder="exemple@domaine.com"
              required
            />
          </li>
        </ol>
      </fieldset>
</form> 
 
<button onclick="buildTable();">  Soumettre </button>



 ```html-css
<body>
<table>
      <thead>
        <tr>
          <th>Prénom</th>
          <th>Nom</th>
          <th>email</th>
        </tr>
      </thead>
      <tbody>
        <tr class="client1">
          <td class="first"></td><td class="last"></td><td class="mail"></td>
        </tr>
      </tbody>
</table>
    
<form>
      <fieldset>
        <legend>Nom complet</legend>
        <ol>
          <li>
            <label for="prenom">Saisir le prénom</label>
            <input id="prenom"  type="textarea" name="prenom" placeholder="prenom"/>
          </li>
          <li>
            <label for="nom">Saisir le nom</label>
            <input id="nom" type="textarea" name="nom" placeholder="nom" />
          </li>
          <li>
            <label for="email">E-mail</label>
            <input
              id="email"
              type="email"
              name="email"
              placeholder="exemple@domaine.com"
              required
            />
          </li>
        </ol>
      </fieldset>
</form> 
 
<button onclick="buildTable();">  Soumettre </button>
<script>
      function buildTable(){
          let prenom = document.getElementById("prenom").value;
          let nom = document.getElementById("nom").value;
          let email = document.getElementById("email").value;

          // champ prenom
          let contenu =document.querySelector('.client1>.first');
          contenu.textContent=prenom;
      
          // champ nom
        
          // champ email
      }
</script>
</body>
```

# concevoir une page avec tableau en 100% javascript

Dans l'exemple suivant, on va voir la création d'un tableau d'une seule rangée, mais avec de nombreuses cellules. On va donc utiliser une boucle bornée, pour sa création, mais aussi pour relever les valeurs.

Une table en HTML est réalisée à partir d'éléments qui ont la hierarchie suivante : 

L'élément *form* est parent d'un élément *table*, lui même parent de *tbody*, parent de *tr* (le ou les rangs) qui possède, lui plusieurs enfant *td*, un par cellule : 

<figure>
<img src="../images/DOM-tab.png" width = "60%" alt="arbre du DOM">
<figcaption>arbre du DOM pour le tableau</figcaption>
</figure>

On commence par selectionner le noeud de l'élément *form* : 

```javascript
let form = document.getElementsByTagName("form")[0];
```

Au début du script on créé les différents noeuds pour ces éléments. Par exemple : 

```javascript
let tbl = document.createElement("table");
```

On créé un noeud pour l'élément `input` qui sera mis dans chaque cellule. Ce noeud est affecté à la variable *cellText*.

On créé les attributs de cet élément. On utilise la méthode `setAttribute(attribut,valeur)` : 

```javascript
cellText.setAttribute("type", "text");
```

On ajoute alors le noeud au DOM avec : 

```javascript
 document.body.appendChild(cellText);
 ``` 

 L'élément créé est alors : `<input type="text">` 

Pour chaque cellule `td` du tableau, on ajoute l'élément `input` : 

```javascript
cell.appendChild(cellText);
```

Puis on ajoute l'élément *td* au noeud *tr* : 

```javascript
row.appendChild(cell);
```

Puis l'élément *tr* à *tbody*, lui même à *table*, et *table* à *form*.

<figure>
<img src="../images/dom-console.png" width = "40%" alt="arbre du DOM">
<figcaption>inspecteur web : console</figcaption>
</figure>

<p class="codepen" data-height="265" data-theme-id="dark" data-default-tab="js,result" data-user="tix06" data-slug-hash="PoPVgEq" style="height: 265px; box-sizing: border-box; display: flex; align-items: center; justify-content: center; border: 2px solid; margin: 1em 0; padding: 1em;" data-pen-title="DOM tableau">
  <span>See the Pen <a href="https://codepen.io/tix06/pen/PoPVgEq">
  DOM tableau</a> by tixidor (<a href="https://codepen.io/tix06">@tix06</a>)
  on <a href="https://codepen.io">CodePen</a>.</span>
</p>
<script async src="https://static.codepen.io/assets/embed/ei.js"></script>

# Liens

* introduction au DOM W3school : [https://www.w3schools.com/js/js_htmldom_methods.asp](https://www.w3schools.com/js/js_htmldom_methods.asp)
* DOM et javascript : [https://developer.mozilla.org/fr/docs/Web/API/Document_Object_Model/Introduction](https://developer.mozilla.org/fr/docs/Web/API/Document_Object_Model/Introduction)
* textContent pour écrire du texte dans un élément textuel : [https://developer.mozilla.org/fr/docs/Web/API/Node/textContent](https://developer.mozilla.org/fr/docs/Web/API/Node/textContent)
