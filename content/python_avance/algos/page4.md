---
Title: TP boucles non bornées
hidden: true
weight: 14
---


# TP4: algorithmes essentiels
## Editeur Python
Au choix, utilisez:

* un **notebook**. 

{{< img src="/images/notebook.png" >}}

Dans une même **cellule**: Saisir une ou plusieurs lignes de code Python, puis appuyer simultanement sur *Majuscule(Shift)* + *Entrée* pour **executer le code**.

* l'editeur **Pyzo**:

Mettre **`##`** avant chaque script pour créer une *cellule*. Executer la cellule et passer à la suivante avec *MAJ+CTRL+ENTREE*.

* l'editeur **Spyder**:

Mettre **`#%%`** avant chaque script pour créer une *cellule*. Executer la cellule et passer à la suivante avec *MAJ+ENTREE*.

{{< img src="../images/cell.png" >}}





## Ex 1: Diviser sans l'opérateur `/`
La division entière de `a`par `b` revient à soustraire `N` fois `b` à la valeur `a`. Ce nombre `N` est le résultat de ce que l'on appelle, la division entière de `a` par `b`.

Il s'agit de la DIVISION EUCLIDIENNE.

Le script contient une boucle non bornée. La *condition d'éxecution* est que le nombre **a** doit rester supérieur à **b** lorsqu'on lui soustrait **b**

*script*

```python
a = 20
b = 6
N = 0
while a >= b:
  a = a - b
  N = N + 1
```

Vous pouvez visualiser les étapes de mise en oeuvre de ce programme en utilisant le lien suivant: {{< a link="https://pythontutor.com/render.html#code=a%20%3D%2020%0Ab%20%3D%206%0AN%20%3D%200%0Awhile%20a%20%3E%3D%20b%3A%0A%20%20a%20%3D%20a%20-%20b%0A%20%20N%20%3D%20N%20%2B%201&cumulative=false&curInstr=13&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false" caption="pythontutor.com" >}}




* **Question a:** Que vaut la variable `a` à la fin du script? Quelle variable stocke le reste de la division? Quelle variable stocke le quotient de la division entière?

> Adapter maintenant le programme pour afficher le *quotient* de la division euclidienne, mais aussi le *reste*. Utiliser une expression formatée avec la fonction `print`: `print("quotient: {}, reste: {}".format(...,...))`

* **Question b:** Recopier le script de cette expression formatée sur votre feuille.


## Ex 2: fonction division_euclidienne
Créer une fonction `division_euclidienne` à partir de l'exercice 1. Cette fonction devra retourner l'expression formatée.

```python
def division_euclidienne(a,b):
  N = 0
  while a .. b:
    ...
  return 'quotient: {}, reste: {}'.format(...,...)
```

* **Question c:** Recopier le script sur votre feuille.
<!--
## Ex 2: Racine carrée
On va adapter le script suivant pour déterminer la racine carrée de 13. La méthode va permettre d'évaluer à $10^-{2}$ près la valeur de $\sqrt {13}$.

```python
# initialisation de la variable x
x = ...
while <condition d execution>:
  instruction
```

* Au début: à l'**étape d'initialisation** de la variable: On part d'une variable x que l'on initialise à 3, puisque $3^2 = 9$, donc inférieur à 13.

* La **condition d'execution** de la boucle non bornée sera `x**2 < 13`.


* Dans le bloc de la boucle `while`: On va **incrémenter** `x` de 0.01 à chaque itération, dans le bloc de la boucle bornée.

* **Question c:** Recopiez le script sur votre feuille de réponse. Quelle est la valeur approchée de $\sqrt {13}$?
-->

## Ex 3: compte epargne
Un étudiant ouvre un compte epargne et dépose la somme de 10 euros. Ce compte est remunéré à hauteur de 2% par an. Il oublie complètement l'existance de ce compte. Au bout de combien d'années aura t-il doublé la somme?

> Resoudre le problème en completant et en testant le script suivant dans une cellule Python

```python
somme = 10
somme_arrivee = ...
annee = 0
while somme <= ...:
  ...
  ...
...
``` 

* **Question d:** Quel nombre **x** d'années se sont écoulées? La somme a t-elle exactement doublé au bout de ces **x** années? 


* **Question e:** Créer une fonction `compte_epargne` à partir de ce script. Cette fonction prendra pour unique paramètre: `somme`, la somme de départ.

## Ex 4: tirage aleatoire
Le programme suivant utilise la fonction `randint`, qui effectue le tirage aleatoire d'une valeur comprise entre 2 bornes:

`randint(1,6)` permet d'effectuer un tirage aleatoire d'une valeur entiere entre 1 et 6.

```python
from random import randint
n = 1
nombre = randint(1,6)
while nombre != 1:
  n = n + 1
  nombre = randint(1,6)
print(n)
```

> Visualiser les étapes de mise en oeuvre de ce programme en utilisant le lien suivant: {{< a link="https://pythontutor.com/render.html#code=from%20random%20import%20randint%0An%20%3D%201%0Anombre%20%3D%20randint%281,6%29%0Awhile%20nombre%20!%3D%201%3A%0A%20%20n%20%3D%20n%20%2B%201%0A%20%20nombre%20%3D%20randint%281,6%29%0Aprint%28n%29&cumulative=false&curInstr=11&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false" caption="pythontutor.com" >}}



* **Question f:** A quoi sert ce programme: *(choisir et justifier)*
  * à compter le nombre d'apparition du nombre 1?
  * ou à calculer le nombre de lancers jusqu’à l’apparition du premier 1?



* **Question g:** Supposons que le tirage aléatoire `randint(1,6)` donne successivement les valeurs: 2, 4, 3, 5, 5, 1. Quelle valeur pour `n` est affichée à la fin du programme? Faire un suivi des variables avec un **tableau**.

<!--
Ajouter une condition supplémentaire dans l'instruction `while randint(1,6) != 1 and ... :` pour résoudre ce problème de l'arrêt.
-->

## Ex 5: PGCD 
### Principe
*PGCD: Plus grand commun diviseur.*

**algorithme d'Euclide**

Euclide propose l’algorithme suivant:

1. Calculez le reste r dans la division de a par b
2. Si r est nul alors le pgcd est b
3. Sinon recommencer l’étape 1 avec a = b et b = r


*Exemple d’exécution : a = 32, b = 12 :*

– 32 = (2 x 12) + 8

– 12 = (1 x 8) + 4

– 8 = (2 x 4) + 0

On a donc pgcd(32, 12) = 4

### Exercice
Programmer la fonction `PGCD` qui prend 2 paramètres, `a` et `b`, et qui retourne le *PGCD* de `a` et `b`. Utiliser une boucle non bornée `while`.

# Portfolio
Lorsque l'on écrit une boucle bornée, le programme comporte 3 phases:

* une première phase d'*initialisation de la variable*
* une instruction *`while <condition d execution>`*
* un *bloc* qui sera répété dans la boucle tant que la condition est Vraie. Le bloc doit contenir une instruction qui modifie la valeur de la variable, et la rapproche de la *condition d'arrêt*.

> Définir chacun de ces termes à l'aide d'un des exemples precedents:

* *initialisation de la variable*
* *condition d'execution*
* *bloc d'instructions*
* *condition d'arrêt*

* Quelle est la condition d'arrêt pour les exemples suivants:

```python
# ex 1
while a!=0:
# ex 2
while a>b:
# ex 3
while a>0 and b>0:
```


