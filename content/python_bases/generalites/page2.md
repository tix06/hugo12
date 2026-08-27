---
Title: calculer en python
linkTitle: types de base
weight: 1
---

  


# Les types de base: numériques, string, booléens
En python, les objets **natifs de base** ont pour type:

* nombre entier: integer ou `int` en Python
* nombre réel décimal: `float` 
* chaine de caractères: `str`
* les valeurs logiques: booléen `bool`

Lorsque l'on présente une valeur dans le programme, le langage s'adapte selon le type, comme on le verra plus loin.

> Pour vérifier le type d'un objet, on utilise la fonction `type`

*Exemples*

```python
> type(12)
int
> type(12.0)
float
> type('12')
str
> type(True)
bool
```

> Pour changer le type, on utilise les **fonctions** `int, float, str`. On utilise par exemple `int` lorsque l'on veut transformer un *float* ou un *str* en un entier:

```python
> int('12')
12
> str(12)
'12'
> float(12)
12.0
```

## Les nombres entiers et décimaux
### Entier
**Un entier: type int** *(ou integer)*. C'est un **nombre** qui n'a pas de point décimal. Les *algorithmes* utilisent en général des *entiers*, ce qui est avantageux pour les opérations de comparaison comme `==` ou `!=`.

*valeurs possibles*: `1, 2492042932330932, -23,...` 

Certaines opérations retournent un résultat de type *entier*:

*expressions possibles*: `13+3928, 34*2+10//3, 12%5, 2**8, ...` 

Un entier peut avoir une valeur aussi grande que celle que la machine peut stocker. Pour un nombre entier non signé, stocké sur 32 bits, cette valeur maximale vaut $2^{32}-1$

**un nombre entier négatif: type int** s'écrit avec un $-$ devant: $-10$ par exemple. Les entiers signés, codés sur 32 bits ont des valeurs qui s'étendent entre $[-2^{31},2^{31}-1]$

## Décimal
**un nombre décimal: type float** s'écrit avec un *point* comme séparateur, comme par exemple: `6.02` 

*valeurs possibles*: `1.0, 249204.2932330932, -23.47,...` 

Les nombres exprimés avec l'opérateur `e` (*puissance de 10*), sont aussi des *float*, des décimaux:

```python
> a = 12e3 # a vaut 12000
> print(a)
12000.0
> type(a)
float
```

La division de 2 nombres avec l'opérateur $/$ retourne toujours un type *float*, même avec des entiers:

```python
> 20/8
2.5
> 20/10
2.0
```


Les *float* en Python ont une *précision limitée*. Ils sont généralement codés sur 15 chiffres significatifs et encodés sur 53 bits. Cela génère des imprecisions comme par exemple:

```python
> 0.3/0.1
2.9999999999999996
```

## Chaine de caractère
C'est une séquence constituée d'un ou plusieurs caractères, entourés de guillemets simples ou doubles.

Notez que des chiffres mis entre guillemets sont des chaines de caractères et ne peuvent pas être manipulés comme des nombres (voir plus loin).

*Exemples*

```python
"Bonjour"
'Hello'
"18"
"Un longue chaine de caractères"
'une autre chaine'
```

### caractères spéciaux
Certains **caractères spéciaux** ne sont pas affichés, mais permettent la mise en forme: 

* Par exemple, le caractère `\n` génère un retour à la ligne:

```python
> citation_python = 'je disais, "être ou ne pas être,\ntelle est la question"'
> print(citation_python)
# affiche
être ou ne pas être,
telle est la question
```

### addition de chaines
*L'addition de chaines** *(concaténation)* se fait avec l'opérateur `+`

```python
> print("Bonjour"+"Hello")
BonjourHello
```

* L'opérateur `*` permet des répétitions multiples:

```python
> print('Hi'*3)
HiHiHi
```

* Ou bien avec des accolades `{}` dans une expression formatée. Exemples:

```python
# Exemple 1 avec .format
m = 100
Ec = 1200
resultat = "Pour le systeme m = {} et E = {}".format(m,Ec)
print(resultat)
# affiche
# Pour le systeme m = 100 et E = 1200
```

```python
# Exemple 2 avec un f-string
m = 100
Ec = 1200
resultat = f"Pour le systeme m = {m} et E = {Ec}"
print(resultat)
# affiche
# Pour le systeme m = 100 et E = 1200
```

L'exemple 2 illustre une chaine particulière appelée **f-string**. C'est une chaine:

* préfixée par un `f`
* suivie par une chaine entre guillemets `""` ou `''`
* contenant des accolades `{}`
* où tout texte placé entre accolades sera remplacé par la valeur de la variable correspondante.

### Test d'appartenance
L'opérateur `in` permet de tester si une suite de caractères se trouve dans un chaine:

* `"ou" in "jour"` vaut `True` 
*  `"ou" not in "jour"` vaut `False`

### Ordre lexicographique
On peut comparer les caractères ou les mots à partir de leur rang dans l'alphabet:

```python
'A' > 'B'
# Affiche False
'A' < 'B'
# Affiche True
'sauver'>'sauveur'
# Affiche False
```

## Les valeurs logiques
Ce sont les valeurs `True` et `False`. 

### opérations avec not, and et or
On peut les combiner dans des formules logiques avec les opérateurs `not`, `and`, `or`:

```python
> True and False
False
> True or False
True
```

### opérateurs de comparaison

Une opération de comparaison, utilisant les signes  `==`, `!=`, `>`, `>=`, `<`, `<=` retourne un booléen `True` ou `False`:

```python
> 0 == 0
True
> 0 == 1
False
> 0 != 1
True
```

*Expressions possibles*: `0 == 0, 8+1 == 2 * 3, 13 >= 1, 'A'<'B', 'a'>'c', 'Sol' in 'Soleil', ...`

### Utiliser les opérations booléennes dans un programme
Le booléen permet un branchement dans un algorithme (voir les structures conditionnelles). *Exemples:*

```python
if True:
  # instruction 1
else:
  # instruction 2

# execution du bloc d'instruction 1

if False:
  # instruction 1
else:
  # instruction 2

# execution du bloc d'instruction 2

if 10 > 1:
  # instruction 1
else:
  # instruction 2

# execution du bloc d'instruction 1
```

On peut souhaiter executer infiniment le même bloc d'instructions, avec l'instruction `while:

```python
while True:
  # bloc d'instructions
```

### Changer de type avec la fonction `bool`
Lors de la transformation de type avec `bool` ou `int`, le `True` correspond à un 1 et le `False` à un 0:

```python
> bool(1)
True
> bool(0)
False
> int(True)
1
> int(False)
0
```



# Les opérations de base
**1.** Un langage informatique permet de réaliser des opérations sur des valeurs. L'écriture de ces opérations peut différer de ce que l'on écrit avec la calculatrice. Voici la liste des opérateurs en Python:

| opérateur | rôle | équivalent  sur une calculatrice |
|--- |--- |--- |
| + | addition | $1 + 99$ |
| - | soustraction | $99 - 1$ |
| * | multiplication | $10 \times 10$ |
| / | division | $\tfrac{1}{3}$|
| // | division entière | pas d'équivalent |
| % | reste de la division | pas d'équivalent |
| ** | exposant | $2^{4}$ |
| e | puissance de 10 (pour l'écriture en notation scientifique) | $1.2E-3$ ou $1.2\times 10^{-3}$ |


**2.** Ces opérateurs peuvent aussi être appliqués sur des chaines de caractères.


| opérateur | rôle | exemple |
|--- |--- |--- |
| + | concaténation (ajoute les chaines de caractères) | &quot;Aïe&quot; + &quot;Aïe&quot; + &quot;Aïe&quot;|
| * | multiplication (ajoute plusieurs fois la même chaine, bout à bout | &quot;Aïe&quot; * 3|

**3.** Un nombre ne peut pas être ajouté à une chaine de caractères:

```python
10 + "x"
# retourne
...
TypeError: unsupported operand type(s) for +: 'int' and 'str' )
```

**4. Opérations logiques**
Une *opération logique* consiste à comparer 2 valeurs et tester si celles-ci sont égales, ou s'il y a une relation d'ordre entre elles. Le résultat d'une opération logique ne peut être que `True` ou `False`:

| opérateur | pour tester... |
|--- |--- |
| `==` | l'égalité |
| `!=` | l'inégalité (est différent de) !
| > | l'ordre supérieur |
| < | l'ordre inférieur |
| >= | l'ordre supérieur ou égal |
| <= | l'ordre inférieur ou égal |

ainsi, pour tester l'égalité entre 3 et 1+2, on peut écrire en python:

```python
3 == 1+2
# retourne 
True
3 == 1+1
# retourne
False
3 > 1+1
# retourne 
True
```

*Remarque:* Le test de l'égalité n'est pas adapté pour les nombres réels. Seulement pour les nombres entiers. Ainsi, en Python, l'opération `0.1*3 == 0.3` renvoie ... `False`!

# Calcul sur des valeur entières
Les programmes informatiques préfèrent utiliser des valeurs entières pour les calculs, même si les calculs avec nombres à virgules sont possibles. Pour cette raison, les opérateurs `//` et `%` sont souvent utilisés en combinaison.

* *Rappel:* **La division euclidienne** de `a` par `b` est définie comme ceci: le dividende de `a` est égal au quotient de `a//b` multiplié par le diviseur `b`, augmenté du reste `a%b`:

$$a = (a//b)*b + a%b$$

* *Usages classiques*:
  * `n%2` vaut 0 si `n` est pair
  * `n%2` vaut 1 si `n` est impair
  * `n%10` conserve les unités
  * `n//10` conserve les dizaines et supprime les unités.


# travaux pratiques

##### {{% button href="../page5" icon="palette" style="tip" %}}TP1{{% /button %}} Calculer en python

# Liens
* Chapitre 1
  * [types de base](../../generalites/page2)
  * [TP1 sur les opérations et types de base](../../generalites/page5)
* Chapitre 2
  * [Variables](../../variables/page4/)
  * [TP2 sur les variables](../../variables/page6/)
* [cours: structures conditionnelles](../../conditions/page2/)
* [TP3 conditions et fonctions](../../conditions/page3/)
* [TP4 Boucles non bornées - while](../../conditions/page4/)




