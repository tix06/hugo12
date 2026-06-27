---
Title: javascript DOM
description: javascript dans le code de la page, DOM, variables, types, boucles, procedures, fonctions
weight: 16
---

* cours 1 sur les fondamentaux en js: [Lien](../js_page1)
* cours 2 sur la structure du langage: [Lien](../js_page2)
* TP 1 - decouverte du js: [Lien](/tp1_javascript_decouverte.html)
* TP 2 - TP hack: [Lien](../js_page3)
* TP 3 - calculatrice : [Lien v1](/TP1_exercice5.html) ou [Lien v2](/TP1_exercice5_calculatrice.html)
* TP 4 - Animation sur tracé SVG: [Lien](/tp2_enonce.html), [correction](/tp2_correc.html)

# Javascript : compléments

## javascript dans une page web
Javascript, c’est aussi le langage de script des pages web : on peut aussi : 

* Mettre son code javascript entre les balises `<script>` et `</script>` d’une page HTML. Cette page est construite au fur et à mesure du parcours par l’interpreteur. La partie javascript sera interprétée APRES l’affichage de la page par le navigateur si cet élement script est mis à la fin du document HTML.

* Mettre son code dans un fichier externe : Il faudra d’abord lier le fichier javascript à celui HTML : 
`<script src="monfichierJavascript.js"></script>`

## Principe : le rôle du navigateur et son moteur javascript

{{< img src="../images/image3.png" alt="interpreteur js" caption="l'interpreteur javascript" >}}
* *Browser :* navigateur. C’est est un logiciel conçu pour consulter et afficher le World Wide Web. Techniquement, c'est au minimum un client http ou https (qui sont des protocoles de communication, définis lors du dernier cours)
* *Web console :* Permet de coder, d’interpréter et d’exécuter du code Javascript directement sur le Browser 
* *Js Engine :* Est intégré dans les Browser. Chaque Browser a son propre interpréteur Javascript qui interprète le code et exécute les scripts associés aux pages Web 

En EcmaScript, on passe la majeure partie de son temps à interagir avec des API fournis par l'environnement d'exécution. En ActionScript c'est Flash (objet flash), en JavaScript dans le navigateur c'est le Document Object Model (objet document).

# Structurer son code
La javascript utilise certains symboles pour structurer : 

* à chaque ligne on met un point-virgule pour séparer les instructions
* les accolades { et } séparent les blocs de code
* Commenter son code : // en debut de ligne  ou bien /* texte entre les 2 separateurs */

```
//Commentaire sur une ligne 
/*Commentaire sur 
Plusieurs ligne */
```

Les indentations, comme en python ne sont pas obligatoires pour structurer le code, mais fortement conseillées pour permettre une meilleure lisibilité.

# Les 3 Data types de bases
## Les 3 types simples  
Pour déclarer une variable, on utilise le mot clé : `let` (ou bien `var`, mais qui n’est plus préconisé par le w3c)

Par exemple : `let a = 10 ; let b = “toto“ ;`
Le typage des variables se fait alors de manière dynamique, comme en python.
 
* Number : Représente à la fois les entiers et les nombres flottants.
* String : Représente du texte ou des caractères
* Boolean : Seulement 2 valeurs : - vrai (true) – faux (false)

Pour connaître le type d’une variable, on utilise la fonction `typeof(variable)` 

## conversions de types
a.  Convertir en nombre entier : `parseInt(‘valeur’)`
b.  Convertir en nombre flottant : `parseFloat()`
c.  Tester si la valeur est NaN (not a number) : `isNaN()`
d.  Convertir en chaine de caractère : `string(variable)` avec un 'S' majuscule.

# Les tableaux: type Array
Les tableaux, array, sont des collections d’objets, mis et ordonnés dans une variable unique. On accède à chaque élément du tableau avec son rang. Cette structure de données est assez proche de la liste que l’on a vu en python.

## Déclarer un tableau vide : 2 manières :
`let tab = new Array() ;`

`let tab = [] ;`

## initialiser un tableau :
Pour déclarer et affecter directement des éléments, on fait :

`let fruits = ["Apple","Orange", "Pear"]`

## accéder à un élément du tableau :
(on peut tester ces exemples avec la console)

```javascript
console.log( fruits[0]) ; // "Apple"
console.log( fruit[1]) ;  //...
console.log( fruit[2]) ;  // ..
````



## méthodes associées aux tableaux :
dimension du tableau (nombre d’éléments)

```javascript
tab.length ; // affiche 3

````


## retirer un élément de la fin du tableau
On utilise l'instruction `array.pop()`

```javascript
tab.pop() ;
console.log(tab) ; // affiche ["Apple ", "Orange "]
````



## ajouter un élément à la fin
On utilise l'instruction `array.push(nouvel_element)`


```javascript
tab.push("Plum ") ;
console.log(tab) ; // affiche ["Apple", "Orange ", "Plum "]
```

# Les objets: Type Object
Un objet est un ensemble de propriétés et une propriété est une association entre un nom (aussi appelé clé) et une valeur. C'est l'équivalent des *dictionnaires* python.

On peut définir une propriété en lui affectant une valeur. Ainsi, si on crée un objet maVoiture et qu'on lui donne les propriétés fabricant, modèle, et année :

```javascript
let maVoiture = new Object();
maVoiture.fabricant = "Ford";
maVoiture.modele = "Mustang";
maVoiture.annee = 1969;
```

On peut aussi définir ou accéder à des propriétés JavaScript en utilisant une notation avec les crochets:

```javascript
let maVoiture = new Object();
maVoiture["fabricant"] = "Ford";
maVoiture["modèle"] = "Mustang";
maVoiture["année"] = 1969;
```

L'exemple précédent peut également s'écrire avec la syntaxe littérale pour initialiser les objets:

```javascript
let maVoiture = {
  make: "Ford",
  model: "Mustang",
  year: 1969,
};
```

# Opérations
## opérateurs de base
On retrouve les opérateurs déjà vus en langage python :

* Opérateurs de base : `+, -, *, /` ainsi que l’opérateur `%` modulo (reste de la division) 
* `**`est l’opérateur exposant :  `2**8`  correspond à 2^8 (à la puissance 8)
* Le symbole d’affectation est le =. Par exemple : 
`let a = 10 ;  // instruction qui declare et affecte 10 à la variable a`

**Question 1 :** Alice a 1 frère et 3 sœurs pour 8 bonbons. Elle voudrait partager les bonbons équitablement. Utiliser des variables pour trouver une solution à son problème.

**Question 2 :** Coder un programme qui permet de savoir l’âge d’Alice (28 ans) en secondes. Réaliser les calculs avec des variables aux noms bien explicites pour les heures, jours, années. Si vous pouvez, utilisez des noms en langue anglaise pour les variables.

## Les opérateurs logiques
est égal `==`, est supérieur ou égal `>=`, inferieur ou égal `<=`, et `&&`, ou `||`, non `!`. On peut aussi utiliser `and`, `or`, `not` pour ces 3 derniers opérateurs.

# Fonctions
## function .. return
Une fonction se définit avec le mot clé function selon la structure : 
function nom_de_la_fonction(parametre1, parametre2, …) {
  bloc de code
  return valeur_à_retourner ;
}

Par exemple, pour programmer une fonction nommée f qui retourne le résultat du calcul : 
$$f : n \mapsto 3n+3$$

```javascript
function f(n) { <br>    return 3*n+3 ; <br>}
f(2) // affiche 9
```


## procédure
On peut réaliser une fonction qui ne calcule rien, une procédure : 

Exemple : pour afficher 5 petits chats dans la console : 


```javascript
function drawCats (howManyTimes) {
	     for (let i = 0 ; i < howManyTimes; i++) {
	     	console.log(i + ” =^.^=”);
	     	}
	     }
drawCats(5);
// affiche
=^.^=
=^.^=
=^.^=
=^.^=
=^.^=
```




La boucle bornée for est expliquée dans le chapitre suivant…


# Contrôler le flux du programme
## Conditions : if .. else .. : 

```
if (condition) {
bloc1 ;
       } else {
    bloc2 ;
       }
```

*Exemple :* le programme suivant compare la somme de 2 entiers avec 4 et renvoie below ou over, selon le resultat : 

```
let a = 1,b = 2 ;
if (a+b<4){
result="below";
       } else {
result="over";
      }
```

## Boucles bornées
### Boucle for : 

```
for (let variable; condition à realiser pour boucler; augmenter la variable) {
    bloc de code à realiser ;
}
```

Par exemple, pour afficher toutes les valeurs de 0 à 10 dans la console, on fait : 

```
for (let i =0; i<=10; i++){
    console.log(i);
}
```

### Parcourir les éléments d’un tableau ou d'un objet: 2 manières
* En utilisant la méthode `fruits.lenght` : 

```javascript
for (let i =0; i<=fruits.length; i++){
	console.log(fruits[i]);}
// affiche
Apple
Orange
Plum
```

* En utilisant `for...of`:

```javascript
const object1 = {
  a: "somestring",
  b: 42,
  c: false,
};

console.log(Object.keys(object1));
// Expected output: Array ["a", "b", "c"]
for (const i of Object.keys(object1) ) {console.log(i,object1[i])};
// Affiche:
> "a" "somestring"
> "b" 42
> "c" false
```




### Boucles non bornées : while :
syntaxe : 

```
while (condition à realiser pour boucler) {
    bloc de code
}
```

Par exemple, pour afficher les entiers de 0 à 2 : 

```
let i = 0 ;
while (i<3) {
    console.log(i) ;
    i ++ ;
}
```

La grande différence avec une boucle bornée, c’est que l’instruction qui modifie la variable i est DANS le bloc de code. Si celle-ci est mal écrite, la boucle risque d’être exécutée indéfiniment (à éviter bien sûr).


# Liens
* parcours `for` pour les éléments d'un objet: [MDN mozilla](https://developer.mozilla.org/fr/docs/Web/JavaScript/Reference/Global_Objects/Object/keys)

* Concepts avancés et Jeu d'arcade en javascript (hors programme): [Page 3](../../javascript_avance/page1)

