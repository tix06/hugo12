---
Title : les bases en javascript
description: bases en javascript, console javascript, objets, methodes
weight: 15
---

* cours 1 sur les fondamentaux en js: [Lien](../js_page1)
* cours 2 sur la structure du langage: [Lien](../js_page2)
* TP 1 - decouverte du js: [Lien](/js/tp1_javascript_decouverte.html)
* TP 2 - TP hack: [Lien](../js_page3)
* TP 3 - calculatrice : [Lien v1](/js/TP1_exercice5.html) ou [Lien v2](/TP1_exercice5_calculatrice.html)
* TP 4 - Animation sur tracé SVG: [Lien](/js/tp2_enonce.html), [correction](/js/tp2_correc.html)

# Les Fondamentaux de JavaScript
## Introduction

Ce cours présente les concepts de base de JavaScript en les comparant avec Python, que vous connaissez déjà. JavaScript est le langage de programmation du web : il permet de rendre les pages interactives.

**Principales différences avec Python :**

- JavaScript s'exécute dans le navigateur (côté client)
- La syntaxe utilise des accolades `{}` au lieu de l'indentation
- Il existe plusieurs façons de déclarer des variables
- JavaScript manipule directement les éléments HTML (le DOM)

---

## Présentation de la console javascript
Javascript est une implémentation dans le navigateur du langage *Ecmascript*.

Javascript est un langage interprété … par le navigateur, donc côté client.
Pour le vérifier, on peut utiliser la console javascript du navigateur pour tester quelques instructions, et interagir avec la page web en cours.

Sur Chrome, cette console se trouve en ouvrant les outils de développement : 

{{< img src="../images/image1.png" alt="console javascript Chrome" caption="la console javascript dans le navigateur Chrome" >}}
Choisir alors l’onglet : *Console* et commencer à taper les instructions, une à une, après l’invite >, comme sur l’image suivante : 

{{< img src="../images/image2.png" alt="E/S" caption="entrée / sortie" >}}
Pour afficher le résultat d’une opération dans la console (équivalent au print en python), on utilise l’instruction `console.log(operation)`.

L’option `filter` de la console devra être sur `Default`

## Les Variables : `let`, `const` et `var`

### En Python (rappel)

En Python, on déclare une variable simplement :

```python
# Une variable simple
age = 15
nom = "Alice"

# On peut la modifier
age = 16
```

### En JavaScript : trois mots-clés

JavaScript propose **trois façons** de déclarer une variable :

```javascript
let age = 15;        // Variable qui PEUT changer
const nom = "Alice"; // Constante qui NE PEUT PAS changer
var ancien = 10;     // Ancienne syntaxe (à éviter)
```

Le *typage* est dynamique, comme en *python*: il n'est pas besoin de préciser le type.

**Règle d'utilisation**

| Mot-clé | Usage | Peut changer ? | Recommandation |
|--- |---- |--- |--- |
| `const` | Valeur fixe | [X] Non | **À utiliser par défaut** |
| `let` | Valeur variable | [V] Oui | Quand la valeur change |
| `var` | Ancienne syntaxe | [V] Oui | À éviter (obsolète) |

**Exemples concrets**

```javascript
// Utiliser const par défaut
const pi = 3.14159;           // Ne changera jamais
const nom = "Alice";          // Ne changera jamais
const bouton = document.getElementById('monBouton'); // Ne changera jamais

// Utiliser let quand ça change
let compteur = 0;             // Va augmenter
let temperature = 20;         // Peut varier
let score = 0;                // Va évoluer

// Erreur : on ne peut pas modifier une const
const age = 15;
age = 16;  // ERREUR : Assignment to constant variable

// Correct : on peut modifier un let
let age = 15;
age = 16;  // OK
```





**Remarque :** A moins que vous soyez sûr que la valeur puisse être modifiée, déclarez vos variables avec `const`, puis changez en `let` seulement si le compilateur vous indique une erreur.


### Quelques différences Python ↔ JavaScript

| Python | JavaScript |
|--- |---- |
| `age = 15` | `let age = 15;` |
| `PI = 3.14` (convention) | `const PI = 3.14;` (imposé) |
| Pas de point-virgule | Point-virgule `;` recommandé |
| `print(age)` | `console.log(age)`| 

---

## Le DOM : Document Object Model

### Qu'est-ce que le DOM ?

Le **DOM** est la représentation en mémoire de votre page HTML. JavaScript peut :

- Lire les éléments HTML
- Les modifier
- Créer de nouveaux éléments
- Réagir aux actions de l'utilisateur

**Analogie avec Python :**

```python
# En Python, vous manipulez des fichiers
fichier = open('data.txt', 'r')
contenu = fichier.read()
fichier.close()

# En JavaScript, vous manipulez des éléments HTML
element = document.getElementById('monId')
contenu = element.textContent
```

### Récupérer un élément : `getElementById()`

**HTML de départ**

Placer un attribut `id` aux balises que l'on veut *indexer*.

```html
<h1 id="titre">Bienvenue</h1>
<p id="description">Ceci est un paragraphe</p>
<button id="monBouton">Cliquez-moi</button>
```

**JavaScript**

```javascript
<script>
// Récupérer les éléments
const titre = document.getElementById('titre');
const description = document.getElementById('description');
const bouton = document.getElementById('monBouton');

console.log(titre); // Affiche: <h1 id="titre">Bienvenue</h1>
</script>
```

> **A faire vous-même (1):** Placer les 2 parties du script ci-dessus dans une même page (*page.html*). Ouvrir avec un navigateur.

**Remarque importante :** L'ID doit être **exactement** le même (sensible à la casse)

```javascript
// Correct
const element = document.getElementById('monBouton');
console.log(element); // Affiche <button id="monBouton">Cliquez-moi</button>

// Erreur : mauvaise casse, ou ID inexistant
const element = document.getElementById('MonBouton');
console.log(element); // Affiche: null
```



---

## Attributs vs Propriétés

### Comprendre la différence

Un élément HTML possède :

- Des **attributs** (définis dans le HTML)
- Des **propriétés** (accessibles en JavaScript)

**Exemple HTML**

```html
<input type="text" id="champNom" value="Alice">
```

**Les attributs (dans le HTML)**

- `type="text"`
- `id="champNom"`
- `value="Alice"`

**Les propriétés (en JavaScript)**

```javascript
const champ = document.getElementById('champNom');

// Propriétés disponibles :
champ.type        // "text"
champ.id          // "champNom"
champ.value       // "Alice" (peut être modifié par l'utilisateur)
champ.textContent // ""
champ.style       // Objet avec toutes les propriétés CSS
```

### La notation pointée

En JavaScript, on accède aux propriétés avec un **point** (comme en Python) :

```python
# Python: notation pointée pour objet.attribut ou objet.methode()
for event in pygame.event.get():
    if event.type == pygame.QUIT:
        running = False
```

```javascript
// JavaScript : notation pointée pour les éléments HTML
const element = document.getElementById('titre');

// Lire une propriété
console.log(element.textContent);  // "Bienvenue"
console.log(element.id);           // "titre"

// Modifier une propriété
element.textContent = "Nouveau titre";
element.style.color = "red";
```

### Propriétés courantes

**`textContent` : Le texte à l'intérieur**

```html
<p id="message">Bonjour tout le monde</p>
```



> **A faire vous-même (2):**  Placer dans votre *page.html* le paragraphe *Bonjour tout le monde*. Ouvrir la console Web et placer l'une après l'autre chacune des instructions *javascript* ci-dessous.

```javascript
const message = document.getElementById('message');

// Lire le texte
console.log(message.textContent); // "Bonjour tout le monde"

// Modifier le texte
message.textContent = "Nouveau message";
// Le HTML devient : <p id="message">Nouveau message</p>
```

**`value` : La valeur d'un champ de saisie**

```html
<input type="text" id="nom" value="Alice">
<input type="range" id="age" min="0" max="100" value="25">
<script>
const champNom = document.getElementById('nom');
const curseurAge = document.getElementById('age');
</script>
```



> **A faire vous-même (3):**  Tester cet exemple: Placer le script dans votre *page.html*. Puis écrire chacune de ces instructions dans la console:

```javascript
// Lire les valeurs
console.log(champNom.value);   // "Alice"
console.log(curseurAge.value); // "25"

// Modifier les valeurs
champNom.value = "Bob";
curseurAge.value = 30;
```

**`style` : Modifier le CSS**
```html
<h1 id="titre">Le Javascript c'est simple</h1>
```

> **A faire vous-même (4):**  Tester cet exemple: Placer le script dans votre *page.html*. Puis écrire chacune de ces instructions dans la console:

```javascript
const element = document.getElementById('titre');

// Modifier le style
element.style.color = "blue";
element.style.fontSize = "24px";
element.style.backgroundColor = "yellow";

// Note: les propriétés CSS avec tirets deviennent camelCase
// CSS: background-color → JavaScript: backgroundColor
// CSS: font-size → JavaScript: fontSize
```

### Tableau récapitulatif

| Propriété | Type d'élément | Usage |
|--- |---- |--- |
| `textContent` | Tous | Lire/modifier le texte |
| `value` | Input, textarea, select | Lire/modifier la valeur saisie |
| `style` | Tous | Modifier le CSS |
| `id` | Tous | Lire/modifier l'ID |
| `className` | Tous | Lire/modifier les classes CSS |

---

## Comparaison complète Python ↔ JavaScript

### Variables

| Concept | Python | JavaScript |
|--- |---- |--- |
| Déclarer une variable | `x = 10` | `let x = 10;` |
| Constante | `PI = 3.14` (convention) | `const PI = 3.14;` |
| Chaîne de caractères | `"texte"` ou `'texte'` | `"texte"` ou `'texte'` |
| Concaténation | `"Hello " + nom` | `"Hello " + nom` |
| Affichage console | `print(x)` | `console.log(x);` |

### Types de données

| Type | Python | JavaScript |
|--- |---- |--- |
| Entier | `age = 15` | `let age = 15;` |
| Décimal | `prix = 19.99` | `let prix = 19.99;` |
| Texte | `nom = "Alice"` | `let nom = "Alice";` |
| Booléen | `actif = True` | `let actif = true;` |
| Rien/Null | `None` | `null` |

**Attention :** `True`/`False` en Python → `true`/`false` en JavaScript (minuscules !)

### Opérateurs

| Opération | Python | JavaScript |
|--- |---- |--- |
| Addition | `x + 1` | `x + 1` |
| Incrémentation | `x += 1` | `x++` ou `x += 1` |
| Égalité | `x == 5` | `x === 5`  |
| Différent | `x != 5` | `x !== 5`  |
| Et logique | `and` | `&&` |
| Ou logique | `or` | `||` |
| Négation | `not` | `!` |

[!] **Important :** En JavaScript, préférez toujours `===` et `!==` (égalité stricte)

---

## Fonctions

### Déclaration

```python
# Python
def dire_bonjour(nom):
    print(f"Bonjour {nom}")

dire_bonjour("Alice")
```

```javascript
// JavaScript - Syntaxe classique
function direBonjour(nom) {
    console.log("Bonjour " + nom);
}

direBonjour("Alice");

// JavaScript - Fonction fléchée (moderne)
const direBonjour = (nom) => {
    console.log("Bonjour " + nom);
};

direBonjour("Alice");
```

### Fonctions sans paramètres

```python
# Python
def afficher_message():
    print("Message affiché")
```

```javascript
// JavaScript
function afficherMessage() {
    console.log("Message affiché");
}

// Ou avec fonction fléchée
const afficherMessage = () => {
    console.log("Message affiché");
};
```

### Retour de valeur

```python
# Python
def additionner(a, b):
    return a + b

resultat = additionner(5, 3)  # 8
```

```javascript
// JavaScript
function additionner(a, b) {
    return a + b;
}

const resultat = additionner(5, 3); // 8
```

---

## Exemple complet : Compteur

### Version Python (pour comparaison)

```python
compteur = 0

def incrementer():
    global compteur
    compteur += 1
    print(f"Compteur: {compteur}")

incrementer()  # Affiche: Compteur: 1
incrementer()  # Affiche: Compteur: 2
```

### Version JavaScript (interaction avec HTML)

```html
<button id="bouton">Cliquer</button>
<p>Compteur: <span id="affichage">0</span></p>
```

```javascript
// Récupération des éléments
const bouton = document.getElementById('bouton');
const affichage = document.getElementById('affichage');

// Variable compteur
let compteur = 0;

// Fonction d'incrémentation
function incrementer() {
    compteur++;
    affichage.textContent = compteur;
}

// Associer la fonction au clic
bouton.addEventListener('click', incrementer);
```

**Explication ligne par ligne :**

1. `const bouton = ...` : Récupère l'élément bouton (ne changera jamais)
2. `const affichage = ...` : Récupère l'élément d'affichage (ne changera jamais)
3. `let compteur = 0` : Variable qui va changer (on utilise `let`)
4. `function incrementer()` : Déclare la fonction
5. `compteur++` : Ajoute 1 au compteur (équivalent à `compteur += 1`)
6. `affichage.textContent = compteur` : Met à jour le texte affiché
7. `addEventListener('click', incrementer)` : "Quand on clique, exécute la fonction"

---

## Exercices d'application

### Exercice 1 : Variables

Complétez le code suivant :

```javascript
// 1. Déclarez une constante PI valant 3.14159

// 2. Déclarez une variable score initialisée à 0

// 3. Augmentez le score de 10

// 4. Affichez le score dans la console
```



### Exercice 2 : Manipulation du DOM

Étant donné le HTML suivant :

```html
<h1 id="titre">Titre initial</h1>
<p id="texte">Paragraphe initial</p>
```

Écrivez le JavaScript pour :
1. Récupérer le titre
2. Changer son texte en "Nouveau titre"
3. Récupérer le paragraphe
4. Changer son texte en "Nouveau paragraphe"



### Exercice 3 : Formulaire interactif

HTML fourni :
```html
<input type="text" id="prenom" placeholder="Votre prénom">
<button id="valider">Valider</button>
<p>Bonjour <span id="affichage">...</span></p>
```

Écrivez le JavaScript pour afficher le prénom saisi quand on clique sur "Valider".



---

## Erreurs courantes à éviter

### Erreur 1 : Oublier `const` ou `let`

```javascript
// Mauvais (crée une variable globale implicite)
compteur = 0;

// Bon
let compteur = 0;
```

### Erreur 2 : Utiliser `const` pour une valeur qui change

```javascript
// Erreur
const score = 0;
score = 10; // TypeError: Assignment to constant variable

// Correct
let score = 0;
score = 10;
```



### Erreur 3 : Confondre `textContent` et `value`

```javascript
// Pour un <p>, <h1>, <div>, etc.
element.textContent = "texte"; // 

// Pour un <input>, <textarea>
element.value = "texte"; // 
```

---

## Aide-mémoire 

```javascript
// ============================================
// VARIABLES
// ============================================
const PI = 3.14;           // Constante (ne change pas)
let compteur = 0;          // Variable (peut changer)

// ============================================
// RÉCUPÉRER UN ÉLÉMENT
// ============================================
const element = document.getElementById('monId');

// ============================================
// LIRE DES PROPRIÉTÉS
// ============================================
element.textContent        // Le texte affiché
element.value             // La valeur d'un input
element.id                // L'identifiant
element.style.color       // La couleur CSS

// ============================================
// MODIFIER DES PROPRIÉTÉS
// ============================================
element.textContent = "Nouveau texte";
element.value = "Nouvelle valeur";
element.style.color = "red";

// ============================================
// FONCTION
// ============================================
function maFonction() {
    // Code ici
}

// ============================================
// ÉVÉNEMENT
// ============================================
bouton.addEventListener('click', maFonction);

// ============================================
// OPÉRATEURS COURANTS
// ============================================
compteur++                // Ajoute 1
compteur += 5             // Ajoute 5
x === y                   // Égalité stricte
x !== y                   // Différence stricte

// ============================================
// CONSOLE
// ============================================
console.log(variable);    // Affiche dans la console
```

---

## Pour aller plus loin

### `const` par défaut

```javascript
// BONNE PRATIQUE : const pour les références
const bouton = document.getElementById('btn');
const affichage = document.getElementById('resultat');

// Ces éléments ne changeront jamais, même si leur contenu change
bouton.textContent = "Nouveau texte";  // OK !
affichage.textContent = "Score: 10";   // OK !

// On ne peut pas réassigner à un autre élément
bouton = document.getElementById('autre'); // ERREUR
```


### Prochaines notions à découvrir: [PAGE 2 sur allophysique](../page2)
- Les conditions (`if`, `else`)
- Les boucles (`for`, `while`)
- Les tableaux (`array`)
- Les objets
- Les événements avancés
- La manipulation du CSS
- Les timers et animations

### Ressources recommandées
- **MDN Web Docs** (français) : https://developer.mozilla.org/fr/
- **JavaScript.info** : https://fr.javascript.info/
- **W3Schools** : https://www.w3schools.com/js/

---

<details>
<summary>Solutions</summary>

```javascript
// Exercice 1
const PI = 3.14159;
let score = 0;
score += 10;
console.log(score);

// Exercice 2
const titre = document.getElementById('titre');
titre.textContent = "Nouveau titre";

const texte = document.getElementById('texte');
texte.textContent = "Nouveau paragraphe";

// Exercice 3
const champPrenom = document.getElementById('prenom');
const boutonValider = document.getElementById('valider');
const affichage = document.getElementById('affichage');

function afficherPrenom() {
    const prenom = champPrenom.value;
    affichage.textContent = prenom;
}

boutonValider.addEventListener('click', afficherPrenom);
```


