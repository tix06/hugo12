---
author: "Eric Tixidor"
date: 07-30-2020
linktitle: jeu Space Invader
menu:
  main:
    parent: javascript
next: 
prev: 
title: jeu Space Invader
weight: 21
---

Ce mini projet sera l'occasion de mettre en oeuvre les notions vues dans le cours précédent sur : 

- la définition d'un objet en javascript
- la gestion des évènements
- l'utilisation d'une fonction callback avec un timer

Vous pourrez également suivre ce tutoriel avec la video à l'adresse : 
[lien video ](https://www.youtube.com/watch?v=IXDO5pKA9pY)

# Afficher des éléments en javascript
## Contenu du dossier du projet
D'abord, créer un dossier contenant :

* spaceInvader.html
* jeu.js
* <a href="../images/ship.png">ship.png (sur fond transparent)</a>
* <a href="../images/ufo.png">ufo.png</a>
* <a href="../images/missile.png">missile.png</a>



Pour les images, on pourra faire un clic droit sur les liens proposés et choisir de télécharger le fichier.



## Code minimal HTML
Le code html minimal qui permet de positionner un vaisseau aux coordonnées : 200px horizontal et 100px vertical : 
```
<html>
<head>
	<title>My space invader</title>
	<script src="jeu.js"></script>
<style>
	html,body {margin : 0px; padding: 0px; width : 100%; height: 100%}
	body {background: url('fond.jpg'); background-size: cover; overflow: hidden;}
</style>

</head>
<body>
	<img id="ship" src="ship.png">
	<script type="text/javascript">
		let v = document.getElementById('ship');
		v.style.width = '100px';
		v.style.height = 'auto'; // pour conserver le ratio
		v.style.position = "absolute";
		// regles de positionnement
		// demarrer par la regle de positionnement absolute pour que 
		// l'image soit mise par rapport à l'élément precedent dans le flux
		// de maniere absolute
		v.style.left= '200px';
		v.style.top='100px';

	</script>
</body>
</html>
```

<figure>
<img src="../images/position.png" width = 80% alt="vaisseau">
<figcaption>position du vaisseau à 200px à gauche et 100 px en bas</figcaption>
</figure>

Le problème est que l'on ne veut pas avoir à taper tout ces volumes de code pour positionner un vaisseau un missile ou un alien : on va alors utiliser une librairie que l'on va nous même écrire.

On pourra effacer toutes les lignes écrites entre les balises `<body>` et `</body>`

# le constructeur de Sprites : function Sprite( )
## les propriétés liées aux attributs
Nous allors programmer une librairie javascript qui va nous permettre de concevoir un constructeur pour tous les objets à afficher. Chacun des ces objets aura alors des propriétés de positionnement, et deux options d'affichage : visible ou caché.
Commençons par programmer le constructeur et les attributs dont héritera l'objet. Dans le fichier `jeu.js`, mettre les lignes de code : 

```
function Sprite(filename, left,top){
	this._node = document.createElement("img");
	this._node.src = filename;
	this._node.style.position="absolute";
	this._node.style.height="100px";
	this._node.style.width="auto";
	this._node.style.left=left+"px";
	this._node.style.top=top+"px"
	document.body.appendChild(this._node);
}
```

*Explications:*

- La `function Sprite(filename, left,top){` : C'est une fonction de creation d'objets (contient des this et commence par majuscule)
- `Sprite`  :  l'element à créer
- `this` :  l'objet lui meme et  `_node` , c'est l'élément correspondant, avec tous ses attributs, tel qu'on l'avait défini de maniere statique dans le premier document html.

On peut déjà positionner l'objet à l'écran en écrivant dans la partie `<script>` de la **page html** : (ce sera alors la première ligne mise entre les balises `<script>` et `</script>`

>`let vaisseau = Sprite('ship.png',400,500);`

Ce qui devrait *construire* un objet *vaisseau*, et ajouter un nouvel élément sur la page : l'image du vaisseau à la position 400px,500px.

		
## Les propriétés de (re)positionnement

<div>
    <label for="toggle" class="btn-lg">Cliquer pour plus d'explications</label>
    
    <input type="checkbox" id="toggle" class="visually-hidden">

    <div class="control-me">

      <p>On souhaite maintenant ajouter des méthodes particulières à l'objet, qui permettront de le déplacer facilement (le <span class="ital">repositionner</span>).</p>

      <p>On pourrait le réaliser à l'aide d'une affectation simple, comme on l'a déjà vu dans le cours précédent. Par exemple, avec : 
      <code>Sprite.posX</code></p>

      <p>Ici, on va utiliser la méthode Object.defineProperty(), qui permet de préciser le comportement attendu, potentiellement différent de celui par défaut.</p>

      <p>On veut maintenant que la nouvelle propriété <code>left</code> soit accessible en ecriture ET en lecture de la manière suivante : 
      <ul>
      <li>Ecriture : Avec le signe <code>=</code> d'affectation =>  <code>vaisseau.left = 400;</code> </li>
      <li>Lecture : Sans le signe <code>=</code> pour accéder à la valeur => <code>vaisseau.left</code> </li>
      </ul>
      </p>

    </div>
</div>



Une fois cette nouvelle méthode attachée au constructeur *Sprite*, on peut le représenter avec le schéma suivant : 

<figure>
<img src="../images/objet.png" width = 80% alt="classe sprite">
<figcaption>classe Sprite</figcaption>
</figure>

L'objet que l'on définira à partir de cette classe héritera des propriétés et des méthodes, que l'on appelera avec l'instruction `objet.propriété` ou `objet.methode` 

> Pour ajouter les méthodes : Dans le fichier `jeu.js`, enlever l'accolade finale du constructeur et mettre :

```
Object.defineProperty(this,"left", {
	get: function(){
		return this._left;
	},
	set: function(value){
		this._left=value;
		this._node.style.left=this._left+"px";
	}
});
```

`Object.defineProperty` permet de definir une propriété pour l'objet que l'on a créé : on passe l'objet avec l'argument `this`

> une propriété est un ensemble de 2 *methodes* : 

> * une methode `get` d'acces en lecture.
> * une methode `set` d'acces en ecriture

Remarquer que l'on utilise `_left`pour le nommage d'une prorieté qui reste privée (locale) dans ce constructeur.

Cette *methode*, on va y acceder avec le nom de *proprieté* `left`: 

On fait par exemple dans le script de la page principale : (ligne à écrire à la suite des autres instruction, avant la fermeture `</script>` dans la page **html**) 

> `vaisseau.left = 400;` 

Le signe `=` va indiquer que l'on invoque la propriété `left`en *ecriture* (on dit que l'on invoque le *setter*), et cela va modifier l'attribut css `style avec la nouvelle règle `left : 400px`. 

Rafraichissons la page.	
Dans la console : explorons les attributs de l'élément associé à l'objet `vaisseau` : 
On peut alors vérifier les valeurs prises pour les propriétés CSS des attributs.

Ouvrir la console du navigateur, et saisir : 
```
> vaisseau._node.style
< CSSStyleDeclaration {0: "position", 1: "height", 2: "width", 3: "left", 4: "top", alignContent: "", alignItems: "", alignSelf: "", alignmentBaseline: "", all: "", …}
> vaisseau._node.style["height"]
< "100px"
```

On sait maintenant positionner horizontalement le vaisseau.
Avec de nouvelles déclarations dans le même format, on peut aussi : 

* positionner **verticalement** (propriete CSS `top`)
* modifier la propriete CSS `display` dont les valeurs possibles sont : 
	* `none` : n'affiche pas
	* `block` : affiche

## le script jeu.js
Avec le constructeur Sprite( ) tel qu'il a été défini dans le paragraphe précédent, le script `jeu.js` est alors :  
```
function Sprite(filename, left,top){

	this._node = document.createElement("img");
	this._node.src = filename;
	this._node.style.position="absolute";
	this._node.style.height="100px";
	this._node.style.width="auto";
	//this._node.style.left=left+"px";
	//this._node.style.top=top+"px"
	document.body.appendChild(this._node);

  Object.defineProperty(this,"left", {
   get: function(){
		return this._left;
	},
	set: function(value){
		this._left=value;
		this._node.style.left=this._left+"px";
	}
	});

	Object.defineProperty(this,"top", {
	get: function(){
		return this._top;
	},
	set: function(value){
		this._top=value;
		this._node.style.top=this._top+"px";
	}
	});

	Object.defineProperty(this,"display", {
	get: function(){
		return this._node.style.display;
	},
	set: function(value){
		this._top=value;
		this._node.style.display=value;
	}
	});

	this.left=left;
	this.top = top;
}
```

## Positionner les éléments

Le reste du script sera mis entre les balises `<script>`de la page **html**.
On peut avoir accès à la dimension de l'écran avec un propriété de l'objet : 

*document* : `document.body.clientWidth`

Centrer le vaisseau, au mileu de l'écran, en position basse avec l'instruction : remplacer `let vaisseau = Sprite('ship.png',400,500);` par : 

> `let vaisseau = new Sprite("ship.png", document.body.clientWidth/2, 500);`

*A vous de jouer :* ajouter 3 aliens que vous devrez repartir sur la largeur de l'écran, en position haute. Nommez les : *alien1, alien 2, alien3*.

Et ajoutez le missile, à une position quelconque, mais modifiez immédiatement sa propriété `display`pour qu'il reste caché : 
ajouter : 

> `missile.display="none";` 

<figure>
<img src="../images/positionTous.png" width = 80% alt="éléments">
<figcaption>à gauche : missile visible, à droite : missile caché</figcaption>
</figure>

# Gestionnaires d'évènements
On ajoute un gestionnaire d'evenements lié aux touches appuyées avec : 

`document.onkeydown = function (event) {`

lorsque l'on appuie sur une touche, cela genere un evenement `"event"` et appelle une fonction avec le parametre  l'un des attributs possibles de `event` qui est `keyCode` : comme ici, l'evenement est lié aux touches appuyées, on peut demander le keyCode de ces touches : 

> Mettre les lignes suivantes dans le programme de la page **html** : 

```
document.onkeydown = function (event) {
	console.log(event.keyCode);
	}
```
Cliquer alors dans la fenêtre du navigateur pour lui donner le focus, puis tester en appuyant sur diverses touches du clavier la valeur affichée dans la console : 

* f : 70
* flèche droite : 39
* flèche gauche : 37
* s : 83
* space : 32

Pour faire avancer le vaisseau à droite lorsque l'on appuie sur la touche f ou la flèche droite, il faut alors mettre : 
```
document.onkeydown = function (event) {
    if (event.keyCode==70 || event.keyCode==39 ){
				vaisseau.left+=10;
}
```

A vous de jouer : 
ajouter alors, dans le même bloc de code lié à la gestion d'evenements du clavier, les instructions consitionnelles qui feront : 
* avancer le vaisseau à gauche pour s ou pour flèche gauche
* faire apparaitre le missile juste devant le vaisseau lorsque l'on appuie sur la barre espace.
* limiter le déplacement à gauche et à droite pour ne pas que le vaisseau sorte de l'écran.


# Animer les éléments
On va modifier à intervalle de temps réguliers les aliens et le missile, ce qui donnera l'illusion d'une trajectoire.

## méthode setInterval()
Les méthodes setTimeout et setInterval sont des méthodes de l'objet Window. 
Ce sont des processus indépendants qui, quand ils sont lancés par une instruction, ne bloquent pas l'affichage du reste de la page ni les actions de l'utilisateur.
Elles permettent de placer dans la pile des prochaines fonctions à exécuter une fonction particulière. Javascript exécute cette pile fonction après fonction dans l'ordre de la pile. 
* SetTimeout indique un délai avant exécution
* setInterval déclenche une opération à intervalles réguliers
* ClearTimeout interrompt le décompte de setTimeout et de setInterval

> Syntaxe : 
`var intervalID = scope.setInterval(func ou bloc de code, [delay (en ms)]);`

Ce compteur de temps est identifié de manière unique : `window.setInterval` renvoie une valeur numérique qui permet cette identification.

> Dans le fichier `jeu.js`, en dehors du constructeur Sprite( ) (à la suite), ajouter : 

```
Sprite.prototype.startAnimation = function (fct, interval) {
	if (this._clock) window.clearInterval (this._clock);
	// s'il y a deja un missile qui est envoyé, clearInterval
	// retire le timer qui lui était lié et en met un nouveau
	var _this=this;
	// on demarre un intervalle que l'on associe à l'objet this
	// on déclare une nouvelle variable locale avec l'underscore _this
	// dont la portée sera descendante. Cette variable pourra être utilisée 
	// par la fonction executée par setInterval
	this._clock=window.setInterval(function(){
		fct(_this);
	},interval);
};

Sprite.prototype.stopAnimation = function() {
	window.clearInterval(this._clock);
};
```

Lorsque la touche `barre espace` est appuyée : on appelle la méthode `startAnimation` pour l'objet *missile*. Cette méthode appelle la fonction `setInterval` qui va associer un timer à l'objet lorsque l'on fait `nom_de_l_objet.startAnimation(fct,interval)`. L'un des paramètres de la fonction `setInterval`est justement une fonction, `fct`. On met `moveMissile` comme fonction de *callback*. 
Le timer associé à l'objet, appelle à intervalle de temps régulier cette fonction qui est passée en paramètre (ce que l'on appelle un callback). L'intervalle de temps est donné par la paramètre `interval`. Ce qui modifie la *pile d'appel* des fonctions dans le programme.



<figure>
<img src="../images/pile.png" width = 80% alt="pile d'appel des fonctions">
<figcaption>fonction callback et pile d'appel des fonctions</figcaption>
</figure>




La deuxieme propriété, stopAnimation, permet de retirer le timer avec l'instruction `clearInterval()`.



*Remarques :* voir en annexe en bas du document



## animation du missile
On va alors ajouter la fonction moveMissile(missile) qui sera appelée par setInterval : 
Dans la partie `<script>` du programme de la page **html** : en dehors de la fonction anonyme executée par onkeydown, on ajoute : 

```
function moveMissile(missile){
		missile.top -=10;
		if (missile.top<100) {
		  missile.stopAnimation(); // sortie de l'écran : on retire le timer de l'objet
		  missile.display = "none";
		}
	}
``` 
Lorsque la fonction est appelée, cela modifie la position du missile (on soustrait 10 px à sa position par rapport au haut de la page)

> dans le bloc de code associé à la condition sur l'évenement de la touche appuyée (la n°32), ajouter : `missile.startAnimation(moveMissile,20);` 

Le bloc de code doit maintenant avoir le contenu suivant : 
```
if (event.keyCode == 32){
	if (missile.display=="none"){
	// condition qui permet de ne lancer un missile que 
	// si aucun missile n'est deja en vol
	missile.display="block";
	missile.left = vaisseau.left+vaisseau._node.width/2;
	missile.top = vaisseau.top;
	missile.startAnimation(moveMissile,20);
	}
}
```

## animation des aliens
On créé ensuite l'animation des aliens, avec un déplacement à droite puis à gauche, à l'aide de 2 nouvelles fonctions : 

```
function moveAlienToRight(alien){
		alien.left += 10;
		if (alien.left > document.body.clientWidth-vaisseau._node.width){
			alien.stopAnimation();
			alien.top += 50;
			alien.startAnimation(moveAlienToLeft,40);
		}
	}

	function moveAlienToLeft(alien){
		alien.left -= 10;
		if (alien.left < 0){
			alien.stopAnimation();
			alien.top += 50;
			alien.startAnimation(moveAlienToRight,40);
		}
	}
	
	alien1.startAnimation(moveAlienToRight,40);
```
Puis on lance l'animation pour chacun des autres aliens : 
`alien2.startAnimation(moveAlienToRight,40);` par exemple pour le 2e alien.

Enfin, on va programmer une méthode de verification de collision de sprite, mais au niveau de la librairie de sprites.



# Ajout d'une méthode checkCollision
Dans le fichier `jeu.js`, ajouter les lignes de code suivantes pour vérifier si deux sprites se chevauchent

```
Sprite.prototype.checkCollision = function (other){
	return (( this.top + this._node.height > other.top) && 
		(this.top<(other.top+other._node.height)) &&
		(this.left+this._node.width>other.left) &&
		(this.left<other.left+other._node.width))
}
```

Si on veut savoir si le sprite missile chevauche le sprite alien1, on fait, dans la fonction de déplacement du missile : 
`missile.checkCollision(alien1)`

La fonction retourne alors `true` si les 2 sprites se chevauchent.
L'appel de cette méthode de missile se fera dans la fonction moveMissile(missile). Ajouter les lignes suivantes : 
```
if (alien1.display != "none" && missile.checkCollision(alien1)){
			// on ne fait un test QUE si l'alien est visible
			// sinon le missile traverse l'écran
			missile.display="none";
			missile.stopAnimation();
			alien1.display="none";
			alien1.stopAnimation();
			// on retire l'alien
		}
```

# Prolongement
Il reste maintenant à programmer les conditions de collision du missile avec les autres aliens, et aussi la condition de collision des aliens avec le vaisseau, ce qui amènerait un *Game Over*.

Enfin, pour aller plus loin, on pourrait imaginer d'ajouter encore plus d'aliens, comme expliqué dans la vidéo (lien en début de document), de gérer un *Score*, et de pouvoir recommencer la partie. 


# Annexe
1. Pour comprendre en détail la manière avec laquelle on a programmé ce timer, il faudra revoir, dans le cours précédent ce que sont : **une fonction callback, une fonction lambda, un objet et son prototype**
2. Remarque à propos de la portée des variables : Le problème du **this**

Le code executé par setInterval() se fait dans un contexte séparé de celui de la fonction qui l'appelle. Conséquence : le mot clé `this`ne pointe pas vers l'objet local , mais il est associé au contexte global, window.
En dehors de tout contexte, pour un navigateur, `this` est l'objet window.

C'est la raison pour laquelle on choisit ici de déclarer : 
`var _this = this;` juste avant la fonction anonyme qui fait appel à `_this` 

# Programme complet
## page html
```
<html>
<head>
	<title>My space invader</title>
	<script src="jeu.js"></script>
<style>
	html,body {margin : 0px; padding: 0px; width : 100%; height: 100%}
	body {background: url('fond.jpg'); background-size: cover; overflow: hidden;}
</style>

</head>
<body>
	
	<script type="text/javascript">
		let vaisseau = new Sprite("ship.png",400,500);
		let alien1 = new Sprite("ufo.png",100,100);
		let alien2 = new Sprite("ufo.png",400,100);
		let alien3 = new Sprite("ufo.png",700,100);
		
		let missile = new Sprite("missile.png",100,100);
		missile.display="none";
		
		document.onkeydown = function (event) {
			console.log(event.keyCode);
			// l'un des attributs possibles de event est keyCode : 
			// comme ici, l'evenement est lié aux touches appuyées
			// on peut demander le keyCode de ces touches.
			// f : 70
			// s : 83
			// space : 32
			if (event.keyCode==70 || event.keyCode==39 ){
				vaisseau.left+=10;
			}
			if (event.keyCode==83 || event.keyCode==37 ){
				vaisseau.left-=10;
			}
			


			if (vaisseau.left<=0) vaisseau.left = 0;
			if (vaisseau.left >= document.body.clientWidth-vaisseau._node.width) vaisseau.left=document.body.clientWidth-vaisseau._node.width;
			if (event.keyCode == 32){
				if (missile.display=="none"){
				// condition qui permet de ne lancer un missile que 
				// si aucun missile n'est deja en vol

				missile.display="block";
				missile.left = vaisseau.left+vaisseau._node.width/2;
				missile.top = vaisseau.top;
				missile.startAnimation(moveMissile,20);
				// on appelle la methode startAnimation
				// associée à l'objet missile
				// avec la fonction missile comme premier parametre (callback)
				// et 20 ms comme seconde parametre (mis dans interval
				// par la fonction anonyme executée lorsque l'on appelle 
				// la methode)
				}
			}
			
		}
			
	function moveMissile(missile){
		missile.top -=10;
		if (missile.top<100) {
		missile.stopAnimation(); // sortie de l'écran : on retire le timer de l'objet
		missile.display = "none";
		}
		if (alien1.display != "none" && missile.checkCollision(alien1)){
			// on ne fait un test QUE si l'alien est visible
			// sinon le missile traverse l'écran
			missile.display="none";
			missile.stopAnimation();
			alien1.display="none";
			alien1.stopAnimation();
			// on retire l'alien
		}
	}

	function moveAlienToRight(alien){
		alien.left += 10;
		if (alien.left > document.body.clientWidth-vaisseau._node.width){
			alien.stopAnimation();
			alien.top += 50;
			alien.startAnimation(moveAlienToLeft,40);
		}
	}

	function moveAlienToLeft(alien){
		alien.left -= 10;
		if (alien.left < 0){
			alien.stopAnimation();
			alien.top += 50;
			alien.startAnimation(moveAlienToRight,40);
		}
	}
	
	alien1.startAnimation(moveAlienToRight,40);
	alien2.startAnimation(moveAlienToRight,40);
	alien3.startAnimation(moveAlienToRight,40);

	</script>
</body>
</html>
```

## fichier jeu.js
```
function Sprite(filename, left,top){

	this._node = document.createElement("img");
	this._node.src = filename;
	this._node.style.position="absolute";
	this._node.style.height="100px";
	this._node.style.width="auto";
	//this._node.style.left=left;
	//this._node.style.top=top;
	document.body.appendChild(this._node);



	Object.defineProperty(this,"left", {
	

	get: function(){
		return this._left;
	},
	set: function(value){
		this._left=value;
		this._node.style.left=this._left+"px";
	}
	});

	Object.defineProperty(this,"top", {
	get: function(){
		return this._top;
	},
	set: function(value){
		this._top=value;
		this._node.style.top=this._top+"px";
	}
	});

	Object.defineProperty(this,"display", {
	get: function(){
		return this._node.style.display;
	},
	set: function(value){
		this._top=value;
		this._node.style.display=value;
	}
	});

	this.left=left;
	this.top = top;
}

Sprite.prototype.startAnimation = function (fct, interval) {
	if (this._clock) window.clearInterval (this._clock);
	// s'il y a deja un missile qui est envoyé, clearInterval
	// retire le timer qui lui était lié et en met un nouveau
	var _this=this;
	// on demarre un intervalle que l'on associe à l'objet this
	// on déclare une nouvelle variable locale avec l'underscore _this
	// dont la portée sera descendante. Cette variable pourra être utilisée 
	// par la fonction déclarée  
	this._clock=window.setInterval(function(){
		fct(_this);
	},interval);
};

Sprite.prototype.stopAnimation = function() {
	window.clearInterval(this._clock);
};


Sprite.prototype.checkCollision = function (other){
	return (( this.top + this._node.height > other.top) && 
		(this.top<(other.top+other._node.height)) &&
		(this.left+this._node.width>other.left) &&
		(this.left<other.left+other._node.width))
}

```


# Liens

* [video du tutoriel tutoriel ](https://www.youtube.com/watch?v=IXDO5pKA9pY)]
* [Object.defineProperty() sur MDN Mozilla](https://developer.mozilla.org/fr/docs/Web/JavaScript/Reference/Objets_globaux/Object/defineProperty)





