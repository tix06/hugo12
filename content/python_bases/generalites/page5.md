---
Title: TP1 calculer en python
hidden: true
weight: 2
---

# Travaux pratiques
Au choix: 

* Ouvrir une console python dans *winpython > python QTConsole*

{{< img src="/images/qtconsole.png" >}}

* Ouvrir un shell python: dans *Pyzo* ou *Spyder* par exemple.

<!--
* L'**editeur** suivant se présente comme un **notebook**. Saisir une ou plusieurs lignes de code Python, puis appuyer simultanement sur *Majuscule(Shift)* + *Entrée* pour **executer le code**.
-->


## Opérations avec des nombres
> Tester les opérations suivantes dans l'editeur Python et répondez aux questions:

<br>

| opérateur | exemple |
|--- |--- |
| + | 12 + 10 |
| * | 12 * 0.1 |
| / | 12 / 10 |
| // | 12 // 10 |
| % | 4 % 2 |
| % | 5 % 2 |
| - | 10 - 12 |
| ** | 2**8 |
| e | 12e-3 |
| `*, /, +, -, ()` | 3-2*(50/2+3) |
| % | 1%3 |
| % | 2%3 |
| % | 3%3 |
| % | 4%3  |
| % | 5%3 |
| % | 12%10|



* **Question a:** Quel est le rôle pour chacun de ces opérateurs? Que donne `N%2` pour N pair; pour N impair?
* **Question b:** Calculer à l'aide de la console le résultat de: $11,27 \times \tfrac{9.10^{21}}{10^4}$. Ecrivez sur votre cahier l'expression utilisée en python pour effectuer ce calcul, ainsi que le résultat, exprimé en langage mathématique.
* **Question c:** Quelles sont les différentes manières d'écrire $9.10^{21}$ en python? 

## Opérations de comparaisons

> à tester dans l'éditeur Python:



| opérateur | exemple |
| --- |--- |
| `==` et nombres entiers| `10*5 == 50` |
| `!=` et nombres entiers| `10*4 != 50` |
| >= et nombres entiers| `10*5 >= 50` ||
| `==` et nombres réels| `0.1 == 0.3/3` |
| `>,+,/,*,()` | `(50/2+3) > 12.5*2` |

* **Question d:** Quel opérateur est prioritaire entre `/` et `+`? *Comme par exemple dans le calcul `2*(50/2+3)`*
* **Question e:** Quel résultat donne `0.1 == 0.3/3`? Expliquer.

## Opérations sur les chaines de caractères

> à tester dans l'éditeur Python:

<br>

| opérateur | exemple |
| --- |--- |
| `+` | &quot;a&quot;+&quot;b&quot;|
| `*` | &quot;bonjour&quot; * 10 |
| `+,*,()` | (&quot;bonjour&quot; + &quot; &quot;) * 10 |


* **Question f:** à partir des exemples proposés, expliquer ce que réalisent les opérateurs + et * avec les chaines de caractères.



On peut aussi réaliser les opérations de comparaison `>, <, ==, !=`sur les chaines. Et aussi le test d'appartenance `in, not in`. Ces opérations retournent un booléen.

* comparaison d'ordre: `"A" < "B"` vaut `True`, `"Ab" < "A"` vaut `False`.
* d'égalité: `"HA" == "ha"` vaut False

**Test d'appartenance** et **ordre lexicographique**: L'opérateur `in` permet de tester si une suite de caractères se trouve dans un chaine. Les opérateurs de comparaison `>` et `<` vont comparer l'ordre des caractères dans l'alphabet.

* `"ou" in "jour"` vaut `True` 
*  `"ou" not in "jour"` vaut False

* **Question g:** que valent chacune des opérations: 
  * `"A" == "a"` 
  * `"Ab" > "Ac"`
  * `"Ab" > "A"`
  * `"Books" > "Money"` 
  * `"Bo" in "Books"`
  * `"Bk" in "Books"`

* **Question h:** Quelle erreur est retournée par l'opération `"bonjour tous les " +2`? (relever la fin du Traceback à partir de *TypeError...*)



## Opérations logiques
> à tester dans l'éditeur Python:

| opérateur | exemples à tester |
| --- |--- |
| `not` |  `not True` |
| `and`| `True and False` |
| `and` |   `True and True`  |
| `or` |  `False or True` |

* **Question i:** Que vaut `not True and False`? Et `not (True and False)`? Pourquoi?

# Fiche de synthèse
* Quels sont les types primitifs vus dans cette leçon? Faire un tableau avec les colonnes:
  * *type*
  * *exemple de valeur*
  * *opérateurs* vus pour ce type, *rôle*, *exemple*
* Quelle instruction permet faire les transformations int->float, int->str, float->str, bool->int?
* Que donne l'instruction: `type(123e3)`
* Quelle valeur maximale peut prendre un entier signé codé sur 32 bits?
* Pour les entiers, donner plusieurs exemples d'utilisation de l'opérateur `//` et de l'opérateur `%`
* Que donne `x%2` si `x` est pair? Si `x` est impair?
* Que donne `x//10`? Cette opération conserve t-elle ou élimine t-elle les unités?
* Même question pour `x%10`
* Pour les chaines de caractères, qu'est-ce qu'une concaténation? Donner un exemple, utilisant l'opérateur `+`.
* Donner un exemple d'utilisation du mot clé `in`. Expliquer son rôle.
* Donner un exemple de comparaison d'ordre lexicographique entre chaines de caractères.
* Soit l'opération logique ci-contre:

`S and not P`

`S` peut prendre l'une des 2 valeurs logiques `True` ou `False`. De même que `P`.

Evaluer cette expression pour chaque combinaison de valeurs pour `S` et `P`. Par exemple, pour `S = True` et `P = True`, cette expression devient `True and not True`, qui est alors evaluée à `False`.

> Résumer dans un tableau.

* Donner la valeur de S et de P pour représenter l'information suivante:

> le temps est ensoleillée (S) et il n'y a pas de pluie (P)

* Donner alors la valeur retournée par l'opération logique `S and not P`