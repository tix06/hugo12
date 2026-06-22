+++
title= "variables, opérations"
description = "types de base et opérations sur les variables"
weight = 3
+++

  


# Variables
**1. Definition:** Une variable sert à stocker une valeur, qui peut être un nombre, une chaine de caractère, ou autres. Une variable est identifiée par un nom, et pointe vers un espace mémoire.

{{< img src="../images/var5.png" alt="affectation variable" caption="VARIABLE = espace de STOCKAGE" >}}

**2. Quel nom peut-on choisir pour une variable?:** On peut choisir une lettre simple, minuscule ou majuscule, ou une chaine de caractères SANS espaces, et commençant obligatoirement par une LETTRE. Le nom peut contenir certains caractères spéciaux comme par exemple `_`. *(ne pas utiliser le signe `-`, utilisé pour une soustraction entre 2 variables)*.

Exemples de noms de variables:

* x
* y
* a
* B
* longueur_L1
* nom
* age
* personne3
* Score
* Points_de_vie
* ...

L'idée est de choisir un nom assez explicite, et d'éviter d'utiliser trop souvent x, y, a, b, c, ...

**3. Affectation** On **affecte** une valeur à une variable en utilisant l'opérateur `=`.

Par exemple, pour *affecter* la valeur 5 à la variable x, on fait:

```python
x = 5
```

Pour vérifier la valeur d'une variable, il suffit d'écrire celle-ci:

* soit toute seule dans une cellule du notebook

```python
x
# retourne 
5
``` 

* soit à la *dernière ligne* de la cellule du notebook:

```python
x = 5
# retourne 
5
```

* Soit avec la fonction `print` (ne pas mettre de guillemets)

```python
x=5
print(x)
# retourne 
5
``` 

On peut modifier la valeur d'une variable existante. On peut méme lui affecter le résultat d'une opération:

```python
x = 12/2
x
# retourne
6.0
```


Et utiliser la valeur de cette même variable pour l'opération:

```python
x = x + 1
x
# retourne
7.0
```

**Affectation multiple:** On peut affecter une valeur à plusieurs variables en une seule ligne, ce qui amèliore la lecture d'un script:

```python
a = 1
b = 2
```

peut être remplacé par:

```python
a, b = 1, 2
```

**4. Opérations sur les variables**
Une variable a un **TYPE** qui est défini lors de l'affectation. Python s'adapte lorsque vous faites une affectation et choisit le type correspondant.

Pour démarrer, nous verrons les TYPES **str** (chaine de caractère), **int** (nombre entier) et **float** (nombre décimal, en virgule flottante).

Les opérations possibles sur une variable dépendent de son type. 

* Pour les variables de type nombre **int** et **float**, on peut utiliser les opérateurs `+,-,*,/,**,//,%`
* Pour les variables de type **str** on peut aussi utiliser les opérateurs `+,*` mais le résultat est différent (opérateurs de concaténation).

**5. Variables et paramètres d'une fonction**
Les variables déclarées avec la fonction, entre parenthèse sont appelées *paramètres*. Le schéma suivant illustre l'affectation des valeurs des variables `a = x` et `b = y` lors de l'appel de la fonction `additionne(x, y)`:

{{< img src="../images/variables_fonction.png" >}}


# Visualiseur python
Le site [pythontutor](https://pythontutor.com/render.html#code=x%20%3D%2010%0Ay%20%3D%2014%0Ax%20%3D%20x%20%2B%202%0Aprint%28x%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=311&rawInputLstJSON=%5B%5D&textReferences=false) permet de visualiser le contenu des variables et leur espace de nom.

*exemple 1*:

```python
x = 10
y = 14
x = x + 2
print(x)
```

Cliquer sur *next* pour dérouler le script pas à pas.

{{< img src="../images/pythontutor0.png" link="https://pythontutor.com/render.html#code=x%20%3D%2010%0Ay%20%3D%2014%0Ax%20%3D%20x%20%2B%202%0Aprint%28x%29&cumulative=false&curInstr=4&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=311&rawInputLstJSON=%5B%5D&textReferences=false" caption="exemple de représentation avec 2 variables x et y dans le main" >}}

*exemple 2*:

```python
x = 10
y = 14

def additionne(a,b):
  return a + b

additionne(x,y)
```

{{< img src="../images/pythontutor6.png" link="https://pythontutor.com/render.html#code=x%20%3D%2010%0Ay%20%3D%2014%0A%0Adef%20additionne%28a,b%29%3A%0A%20%20return%20a%20%2B%20b%0A%0Aadditionne%28x,y%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=311&rawInputLstJSON=%5B%5D&textReferences=false" caption="exemple avec appel d'une fonction" >}}

# Editeur Python
Ouvrir dans *winpython > python QTConsole*


{{< img src="/images/qtconsole.png" >}}

<div>
<py-repl id="my-repl" auto-generate="true"></py-repl>
</div>

## Travaux pratiques: opérations sur les nombres

> Tester les scripts suivants dans l'editeur Python. Pour cela, recopier dans l'ordre, et dans la même cellule, chacune des instructions du script, et executer celle-ci. Repondre ensuite aux questions.

### Script 1
Incrémenter une variable...

```python
age = 0
age = age + 1
age
```

* **Question a:** quelle est la valeur de `age` à la fin du script? 

### Script 2
Le programme suivant permet de connaitre en quelle année un enfant, né en 2022, aura 17 ans

```python
age = 0
annee = 2022
age = age + 17
annee = annee + age
annee
```

* **Question b:** en quelle année aura-t-il 17 ans?

### Script 3
On veut réaliser les opérations suivantes:

```python
nombre=2*nombre
nombre=nombre-10
nombre=nombre**2
nombre=nombre-5
```

* **Question c:** Quel est le résultat (c'est à dire la valeur finale de `nombre`) pour une valeur de depart `nombre = 5`?

### Script 4
Écrire un programme dans l’éditeur qui :

- affecte 3 à la variable `nombre` 
- Ajoute 7 au triple du nombre.
- Multiplie le résultat par le nombre lui-même.
- Soustrait au résultat le nombre 1 ;
- Affiche le résultat obtenu.

Ne pas utiliser de nouvelles variables pour les résultats intermédiaires. Seulement `nombre`

* **Question d:** Quel est le résultat?

### Script 5: permuter la valeur de 2 variables
On veut mettre la valeur de `a` dans `b` et celle de `b` dans `a`. Le problème est que lorsque l'on fait...

```python
b = a
a = b
```

... on se retrouve avec les mêmes valeurs pour `b` et pour `a`. Il n'y a pas eu d'echange. L'idée est d'utiliser une troisième variable, `c` pour stocker la valeur de `b`, puis de l'affecter à `a`


* **Question e:** Ecrire la série d'instructions correspondantes. Puis vérifier qu'il y a bien eu échange entre les variables.

## Opérations sur les chaines de caractères

### Script 6
Associer des chaines de caractères.

```python
debut = "bonne annee"
milieu = " "
fin = "grand mere"
message = debut + milieu + fin
message
```

Cet exemple vous a rappelle que l'opérateur `+` est l'opérateur de *concaténation* avec les chaines de caractères. 

* **Question f:** Ecrire un nouveau script qui construit le message suivant: `Ho Ho Ho Ho Ho Ho Ho Ho Ho Ho`, où le nombre de `Ho` est stocké dans une variable N. 

*Astuce: utiliser l'opérateur* `*`

### Script 7
Associer des valeurs numériques et des chaines de caractères

```python
age = 21
nom = "Kevin"
message = "mon nom est " + nom + ", et j'ai " + age + " ans"
message
```

* **Question g:** Le script s'execute t-il, ou bien renvoie-t-il une erreur? Quelle erreur le cas écheant?
* **Question h:** Modifier l'avant derniere ligne par: `message = "mon nom est " + nom + ", et j'ai " + str(age) + " ans"`. Le script fonctionne t-il? Que renvoie t-il?

*Remarque:* La fonction `str` va tranformer la valeur numerique `age` en une chaine de caractères (les caractères "2" et "1").

*Tester également l'instruction:* `print("mon nom est ",nom ," et j'ai ",age, "ans")`

*Que constatez-vous?*

### Script 8
Afficher avec la fonction `print`

```python
a = 45
b = 26
c = a % b
print('le reste de la division de ' + str(a) + ' par ' + ...)
```

* **Question i:** Completer la derniere ligne du script pour afficher la phrase suivante: `Le reste de la division de 45 par 26 est egal a 19` Vous ne devrez pas écrire les chiffres 45, 26 et 19 dans le message. Seulement utiliser les variables, ou une opération sur ces variables.


Nous avons vu qu'une chaine de caractère pouvait être construite comme une association de plusieurs chaines de caractères. Une chaine de caractères est de type *string* (ou `str`) en python.

Pour vérifier le type d'une variable, on utilise la fonction `type`

> Testez chacune des instructions suivantes pour vérifier le type des différentes variables

```python
a = 45
type(a)
b = 26
type(b)
type(a//b)
c = a % b
type(c)
d = a / b
type(d)
m = str(a)
type(m)
```

* **Question j:** Compléter le tableau

| x= |  type(x) |
| --- | --- |
| 45 |  |
| 45%26 | | 
| 45/26 |  | 
| 45//26 |  | 
| str(45) |  |



### Script 9
Calculer en physique

Dans une cellule Python, 

* commencez par attribuer 100 à la variable `m`, et 20 à la variable `v`
* calculer puis afficher E, l'energie cinetique pour un systeme de masse 100kg et de vitesse $20m.s^{-1}$, selon la loi:

$$Ec = \tfrac{1}{2}m.v^2$$

* **Question j:** Quelle est l'expression que vous avez saisie en langage Python? Quelle est la valeur calculée pour l'énergie cinetique?

* **Question k:** Construire une chaine de caractères, en utilisant la fonction `format` et précisant les conditions initiales, les valeurs pour m et pour v, et le résultat du calcul de l'énergie cinétique. Recopier ici cette instruction en python.

*L'expression formatée a été vue dans le cours sur les [variables et opérateur](/docs/python/pages/generalites/page2/), partie "chaines de caractères" et consiste à utiliser la méthode de chaine `"caracteres {}".format(x)`*

* **Question l:** créer une fonction `Ec` qui prend pour paramètres `m` et `v` et retourne le resultat de $Ec = \tfrac{1}{2}m.v^2$. Appeler cette fonction avec les valeurs 100kg et $20m.s^{-1}$

# Portfolio
* Comment se nomment *en python* les 4 types primitifs que l'on a vus lors de ces premieres séances?
* Le changement de type entre variables se fait grace aux fonctions `str`, 'float', `int`, et `bool`
  * Comment transformer la chaine "12" en une valeur entière égale à 12? "12" => 12
  * Comment réaliser l'opération inverse? 12 => "12"
  * Comment transformer la chaine "12" en un nombre flottant? "12" => 12.0
  * Comment transformer l'information 1 en un booléen `True`?
  * Comment réaliser l'opération inverse?
* Qu'est-ce qu'une affectation multiple, en une seule ligne d'instruction?
* Comment échange t-on la valeur de 2 variables `a` et `b`?
* Pourquoi l'instruction: `print("aujourd'hui j'ai "+ 18 +"ans")` ne fonctionne t-elle pas? Corriger cette expression (donner 2 moyens).
* Donner un exemple d'utilisation d'une expression formatée pour écrire le résultat du calcul de la force de gravitation $F=G\times m_1 \times m_2/d^2$, à partir des différentes variables.
* Quel sera le type associé à `F` si l'on réalise le calcul?
* Comment définir une fonction `F_gravitation` pour réaliser le calcul de `F`?
* Comment utiliser cette fonction pour calculer la force de gravitation Terre-Lune?

$M_T = 5.972\times 10^{24}kg$, 

$M_L = 7.348\times 10^{22}kg$, 

$d = 3.844\times 10^{8}m$, 

$G = 6.67\times 10^{-11}SI$

# Liens
* [TP1 sur les opérations et types de base](../../generalites/page2)
* [TP2 sur les variables](../../variables/page4/)
* [cours: structures conditionnelles](../../conditions/page2/)
* [TP3 conditions et fonctions](../../conditions/page3/)
* [TP4 Boucles non bornées - while](../../conditions/page4/)

