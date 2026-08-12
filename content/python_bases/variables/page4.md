+++
title= "variables, opérations"
description = "types de base et opérations sur les variables"
weight = 3
+++

  


# Variables
**1. Definition:** Une variable sert à stocker une valeur, qui peut être un nombre, une chaine de caractère, ou autres. Une variable est identifiée par un nom, et pointe vers un espace mémoire.

{{< img src="../images/var5.png" alt="affectation variable" caption="VARIABLE = espace de STOCKAGE" >}}


Une variable est donc une zone précise de la mémoire vive de l'ordinateur (on parle d'adresse mémoire). À partir de cet emplacement, on trouvera une succession de bits dont l'agencement spécifique déterminera à la fois une valeur et un type.

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

*exemple 1*: un espace mémoire pour chaque variable

```python
x = 10
y = 14
x = x + 2
print(x)
```



{{< img src="../images/pythontutor0.png" width="300" link="https://pythontutor.com/render.html#code=x%20%3D%2010%0Ay%20%3D%2014%0Ax%20%3D%20x%20%2B%202%0Aprint%28x%29&cumulative=false&curInstr=4&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=311&rawInputLstJSON=%5B%5D&textReferences=false" caption="exemple de représentation avec 2 variables x et y dans le main" >}}

> Cliquer sur l'image pour lancer l'app *pythontutor*. Cliquer sur *next* pour dérouler le script pas à pas.

*exemple 2*: un espace mémoire pour les variables et pour les fonctions

```python
x = 10
y = 14

# creation de la fonction avec le mot clé def
def additionne(a,b):
  return a + b

# appel de la fonction avec a = 10 et b = 14
additionne(x,y)
```

{{< img src="../images/pythontutor6.png" width="300" link="https://pythontutor.com/render.html#code=x%20%3D%2010%0Ay%20%3D%2014%0A%0Adef%20additionne%28a,b%29%3A%0A%20%20return%20a%20%2B%20b%0A%0Aadditionne%28x,y%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=311&rawInputLstJSON=%5B%5D&textReferences=false" caption="exemple avec appel d'une fonction" >}}

> Cliquer sur l'image pour lancer l'app *pythontutor*. Cliquer sur *next* pour dérouler le script pas à pas.

# Travaux pratiques
### [Lien vers le TP2](../page6)

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

