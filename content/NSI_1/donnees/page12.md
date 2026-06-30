---
Title: listes et tableaux en sciences
description: bases en python pour les sciences
weight: 12
---

# listes et algos sciences physiques et chimie
* Les exemples et scripts seront à realiser dans un notebook python.
* On utilisera la{{< a link="/pdf/NSI/python_listes_SPC.pdf" caption="fiche reponse" >}}
## Construire un tableau simple
Pour tracer un graphique, on peut avoir besoin d'une liste de valeurs [0, 1, 2, ... 100] correspondant aux nombres de points relevés.

{{< img src="../images/spc1.png" >}}
Cette liste peut être construite à l'aide d'une boucle bornée:

```python
T = []
for i in range(100):
  T.append(i)
```

On rappelle que `range(100)` créé une suite de valeurs que prendra le variant i, successivement, du premier au dernier.

* Construire un tableau par compréhension
Cette méthode permet de construire une nouvelle liste "à la volée", en parcourant les éléments d'une première liste.

```python
T = [i for i in range(100)]
```

## Relever des valeurs
Lors d'une expérimentation, il est parfois utile de relever des valeurs mesurées au cours du temps.

Ces valeurs peuvent être stockées dans une liste, en utilisant la fonction `append`:

```python
temperature = []
temperature.append(15)
temperature.append(18)
...
```

Il est possible de programmer la saisie de ces valeurs par une interface textuelle.

* une boucle principale demande une valeur à l'expérimentateur (`input`)
* la valeur saisie est ajoutée à la liste
* tant que le caractère de fin n'est pas saisi, continuer (par ex "S")

> à vous de jouer: Ecrire le script de ce programme, en python.


## Tracer un graphique
Le module `matplotlib` permet de tracer des graphiques à partir de listes. La fonction `scatter` trace un nuage de points, et `plot` une figure:

```python
import matplotlib.pyplot as plt
T = [i for i in range(10)]
temperature = [t*1.1 for t in T]
plt.scatter(T,temperature,label="Temperatures")
plt.legend()
plt.xlabel('temps(min)')
plt.ylabel('Temperature(°C)')
plt.show()
```

{{< img src="../images/spc3.png" >}}
## Listes calculées
Souvent, les données issues d'une acquisition sont présentées sous forme d'une table.

{{< img src="../images/spc2.png" >}}
Elles sont alors échangées avec le programme python grâce à un fichier de données en format *csv*. Il est alors possible de créer une liste de données par colonne: listes `t, x, y, v` 

A partir de l'exemple précédent, on peut supposer que:

```
t[0] contient 0
x[0] contient 0
y[0] contient 0
v[0] contient 10
```

On peut alors ajouter une nouvelle *colonne* à ces données, c'est à dire une *nouvelle liste.*

Par exemple: à partir de la définition de l'energie cinétique:

$$Ec = \tfrac{1}{2}* m * v^2$$

Supposons que le mobile ait une masse m = 1 kg:

```python
m = 1
Ec = []
for vitesse in v:
  Ec.append(0.5*m*v**2)
``` 

*Remarque:* de nombreux types de données peuvent être parcourus avec la syntaxe `for x in t`: par exemple des chaines de caractères. La différence avec `range(100)`, c'est que ce dernier créé une liste itérable de valeurs ordonnées, de 0 à 99. On dit que la valeur x est itérable.

> A vous de jouer: 

1. quelle instruction permet de créer la même liste Ec, mais cette fois, par compréhension de liste.
2. télécharger le fichier{{< a link="../data/data_parabolique.csv" caption="data_parabolique.csv" >}}3. Ajouter une nouvelle liste calculée: $Ec = \tfrac{1}{2}* m * (vx^2+vz^2)$. Prendre m = 1. Compléter pour cela le programme:

```python
m = 1
Ec = []
for i in range(len(vx)):
  # vx et vz sont les 2 composantes de v
  # et ont la même dimension
  # v^2 est calculé à partir de
  # vx**2 + vz**2
  Ec.append(
``` 


4. Tracer le graphique Ec en fonction de x.

**Aide: Script pour lire les données d'un fichier** 

```python
fichier = open('data_parabolique.csv','r')   # ouverture du fichier de données
lignes = fichier.readlines()     # parcours du fichier par ligne 

lignes = lignes[1:]              # eliminer la premiere ligne qui contient les labels 
x=[]
t=[]

for ligne in lignes:
    t.append(float(ligne.split(';')[0]))
    x.append(float(ligne.split(';')[1]))
```

## Parcours d'une liste
Soit la liste: 

```python
Temperature=[18.5, 19.0, 20.4, 20.2, 19.8]
```
Pour calculer sur les valeurs de liste, par exemple, la somme, ou la moyenne des valeurs, il faut *parcourir* ces valeurs:

```python
s = 0
for t in Temperature:
  s = s + t
```

> A vous de jouer: adapter ce script pour:

1. calculez la moyenne des valeurs de `Temperature` 
2. Déterminez la valeur maximale de la liste
3. Utilisez votre script pour déterminer la valeur maximale de la liste `z` dans le fichier `data_parabolique.csv` 

## Recherche du nombre d'occurences dans une liste
On peut représenter une molécule par sa liste d'atomes.
Par exemple, la formule suivante peut être mise dans la liste:

```
molecule = ['H','H','H','C','C','O','C','H','H','H']
```

{{< img src="../images/spc5.png" caption="une molecule en formule semi-developpée" >}}
Compter le nombre d'occurences signifie que l'on peut compter le nombre d'atomes identiques, comme par exemple le nombre de `'H'` ou bien le nombre de `'C'`.

```python
n = 0
for atome in molecule:
  # ajouter une condition sur atome
  # si atome vaut 'C' (ou 'O' ou 'H')
  # alors n = n + 1
```

> A vous de jouer. En vous inspirant du script précédent, vous allez écrire **une fonction** `occurences` qui prend une liste en paramètre, appelée *molecule*, ainsi qu'un caractère `c`, et compte le nombre d'occurences de `c` dans la liste *molecule*.

## Matrices
Une liste peut elle-même contenir une liste. Une **matrice** est ainsi une liste de listes, dont les éléments sont tous de même type. La matrice forme une sorte de tableau rectangulaire, dont la premiere ligne correspond à la premiere liste, etc...

Pour parcourir les valeurs d'une matrice, on aura besoin de 2 boucles imbriquées:

```python
# script pour afficher la matrice m
m = [['a','b','c'],['d','e','f'],['g','h','i']]
for ligne in m:
    for c in ligne:
        print(c,' ',end='')
    print('\n')

# affiche 
# a b c
# d e f
# g h i
```

La première boucle bornée créé un itérable `ligne` qui vaut successivement:

* `['a','b','c']` 
* `['d','e','f']` 
* `['g','h','i']` 

La deuxième boucle (imbriquée), créé un itérable `c` à partir de chacune de ces sous-listes:

* a
* b
* c
* ...

Les valeurs de `m` sont accessibles à partir de ses indices, comme pour une matrice:

* `m[0][0]` vaut `a` 
* `m[0][1]` vaut `b`
* `m[0][2]` vaut `c`  
* `m[1][0]` vaut `d` ...

**Exemple**: traitement d'une image

{{< img src="../images/spc4.png" caption="une image numérique est constituée de pixels" >}}
Une image est représentée par un triplet de valeurs (un *tuple*) pour chacun de ses pixels, correspondant à l'intensité (Rouge, Vert, Bleu) (0-255) de ce pixel.

Soit l'image suivante, de dimension 3 pixels * 3 pixels:

{{< img src="../images/spc6.png" >}}
Cette image est représentée par la matrice de valeurs (R,V,B):
```
im = [[(128,30,40), (130,32,44), (128,30,40)], 
      [(30,40,128), (44,32,130), (40,30,128)], 
      [(128,30,40), (130,32,44), (128,30,40)]]
```


> Exercice:<br> Ecrire un programme qui calcule la valeur moyenne sur toutes les valeurs RVB de cette matrice. Cela donnera l'intensité moyenne de cette image (sa luminosité).





