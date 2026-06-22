---
Title: TP1 listes
description: TP, liste, dictionnaire, indices, modifier supprimer et ajouter des éléments, liste de listes, matrices, tracé graphique
weight: 9
hidden: true
---


**Rappels de cours sur les listes**

* [page 1: listes et boucles bornées](/docs/python/pages/boucles/page2/)
* [page 2: types construits: list, tuple, dict](/docs/python/pages/variables/page2/)

**Editeur Python**

* Utiliser un **notebook**. Saisir une ou plusieurs lignes de code Python, puis appuyer simultanement sur *Majuscule(Shift)* + *Entrée* pour **executer le code**.



# TP5 Listes
## Ex 1: Elements d'une liste
### Utiliser un indice
Dans une cellule, saisir la ligne suivante:

```python
s = ['lundi', 'mardi',  'mercredi']
```

> Prevoir ou tester chacune des propositions suivantes:

| proposition | résultat/commentaire |
|--- |--- |
| `s[0]` |  |
| `s[1]` |   |
| `s[-1]` |   |


* **Question a1:** Quel est l'indice du dernier élément d'une liste? (*on ne connait pas le nombre total*)

> Modifier des éléments de liste

| proposition | résultat/commentaire: `print(s)` |
|--- |--- |
| `s[2] = "jeudi"` |   |
| `s[4] = "samedi"` |  erreur de type: ... ... |


* **Question a2:** Comment modifie-t-on la liste `['lundi', 'mardi',  'mercredi']` pour obtenir `['lundi', 'mardi',  'jeudi']`?

* **Question a3:** Pourquoi l'instruction `s[4] = "samedi"` génère t-elle une erreur?


### Slice: découpage d'une liste à partir des indices
Pour découper une liste, on utilise le séparateur `:` entre les indices de début et fin de liste.

Avec la liste:

```python
s = ['lundi', 'mardi',  'mercredi', 'jeudi', 'vendredi']
```

> Prevoir ou tester chacune des propositions suivantes:

| proposition | résultat/commentaire |
|--- |--- |
| `s[1:]` | slice du 2e element de liste jusqu'au dernier |
| `s[1:4]` |  slice du 2e element de liste jusqu'à celui de rang ... |
| `s[:4]`|   |
| `s[1:-1]`|   |
| `s[0:-2]`|   |
| `s[:-3]`|   |

* **Question b:** Que retourne la proposition `s[1:]`? Découpe t-elle la liste après le premier élément, le 2e élément, ou bien retourne t-elle la liste entière?

## Ex 2: Opérations sur les éléments et sur les listes
### Modifier une valeur (opérateurs `+-/*`)
Saisir le script suivant:

```python
t = [2, 8,  9,  2]
t[2]  = t[2] + 5
```

* **Question c:** Que vaut t à la fin du script `t[2]  = t[2] + 5`? La valeur 5 est-elle ajoutée à chaque élément de la liste, ou bien à un seul élément?  



### Coller 2 listes (opérateur +)
Saisir le script suivant, ou bien voir son execution sur [pythontutor](https://pythontutor.com/render.html#code=l1%20%3D%20%5B1,2,3%5D%0Al2%20%3D%20%5B4,5,6%5D%0Al1%20%3D%20l1%20%2B%20l2&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=311&rawInputLstJSON=%5B%5D&textReferences=false)

```python
l1 = [1,2,3]
l2 = [4,5,6]
l1 = l1 + l2
print(l1)
```

* **Question d1:** Que fait l'opérateur `+` entre 2 listes?

> Prevoir ou tester le script suivant:

```python
l1 = [1,2,3]
l2 = l1 * 3
print(l2)
```

* **Question d2:** Que fait l'opération `* 3` sur une liste? 

# Ex 3: Méthodes de listes
### Ajouter, retirer, étendre une liste
> Dans une cellule, saisir la ligne suivante:

```python
s = ['lundi', 'mardi',  'mercredi']
```

Puis tester chacune des propositions suivantes:

| proposition | résultat/commentaire |
|--- |--- |
| `len(s)` |  |
| `s.append('jeudi')` |  |
| `len(s)` |  |
| `s.append('vendredi')` |   |
| `len(s)` |  |
| `s.pop()` |   |
| `len(s)` |  |
| `s.extend(["samedi","dimanche"])` |  |
| `len(s)` |  |

* **Question e1:** Pourquoi la valeur renvoyée par `len(s)` évolue t-elle au cours de l'exercice? Quel est le rôle de chacune de ces méthodes (`len`, `pop`, `extend`). 

* **Question e2:** Laquelle de ces méthodes peut-on utiliser pour réaliser l'opération `l1 = l1 + l2` comme dans l'exercice précédent? Ecrire l'instruction équivalente.


### Rechercher dans une liste
> Dans une cellule, saisir la ligne suivante:

```python
from random import shuffle
s = ['lundi', 'mardi',  'mercredi', 'jeudi', 'vendredi']
shuffle(s)
print(s)
```

* **Question e3:** Quel est le rôle de la fonction `shuffle`?

> Dans le shell python, utiliser la méthode `index`:

```python
>>> s.index('lundi')
```

* **Question e4:** Quel est le rôle de la fonction `index`?


## Ex 4: chaine de caractere comme une liste
* script 1

```python
debut = "Bon"
fin = "jour"
debut + fin
```

* script 2

```python
debut = "20"
fin = "22"
debut + fin
``` 

* script 3

```python
debut = [2,0]
fin = [2,2]
debut + fin
```

* **Question f1:** Y-a-t-il une ressemblance entre:
  *  l'opérateur `+`appliqué à une chaine de caractères
  *  l'opérateur `+` appliqué à une liste?

### Transformer en liste
* script 4: transformer un str en une liste

```python
phrase = "une phrase assez longue"
L = list(phrase)
```

* script 5: découper un str en une liste

```python
phrase = "mais,pourquoi,autant,de,virgules?"
L = phrase.split(',')
print(L)
```

* **Question f2:** à partir de ces exemples, comment pourrait-on obtenir `['une', 'phrase', 'assez', 'longue']` à partir de la chaine `phrase`?

## Ex 5: utiliser l'indice (liste) ou une clé (dictionnaire)
### indice
> Compléter l'instruction `print(...)` qui, selon le numéro `n` du jour de la semaine (1-7) affiche le nom du jour de la semaine.


```python
semaine = ['Lundi', 'Mardi','Mercredi','Jeudi','vendredi','samedi','dimanche']
for n in range(len(semaine)):
  print(semaine[...])
```



### clés d'un dictionnaire
Même exercice, mais cette fois-ci avec un dictionnaire. 

Pour parcourir les clés du dictionnaire `semaine`, on utilise une boucle `for` avec l'iterable `semaine.keys()`

```python
semaine = {1:'Lundi',2:'Mardi',3:'Mercredi',4:'Jeudi',5:'vendredi',6:'samedi',7:'dimanche'}
for i in semaine.keys():
  print(i)
```

> Compléter l'instruction `print(...)` pour afficher chaque jour de la semaine:

```python
semaine = {1:'Lundi',2:'Mardi',3:'Mercredi',4:'Jeudi',5:'vendredi',6:'samedi',7:'dimanche'}
for n in semaine.keys():
  print(semaine[...])
```

* **Question g:** Compléter la phrase: Pour parcourir les éléments de liste, on fait une boucle avec un variant sur les `[indices/clés]`. Pour les éléments d'un dictionnaire, on utilise un variant sur les `[indices/clés]`. 


### Clé de type str
Un dictionnaire accepte aussi des chaines de caractère pour clé. Exemple:

```python
D = {"John":"+33620200202", "Doe":"+33640400404"}
print(D["John"])
print(D["Doe"])
```

### Traiter les éléments d'un dictionnaire
> Compléter le programme. A chaque itération, vous devrez:

* lire le jour de la semaine associé à la clé `n`
* ajouter le jour dans une liste `L`


```python
L = []
semaine = {1:'Lundi',2:'Mardi',3:'Mercredi',4:'Jeudi',5:'vendredi',6:'samedi',7:'dimanche'}
for n in semaine.keys():
  jour = semaine[...]
  L.append(...)
print(L)
```

* **Question h1:** Quelle instruction est utilisée pour parcourir les clés d'un dictionnaire? 
* **Question h2:** Quelle instruction est utilisée pour placer une nouvelle valeur dans une liste (à la fin de cette liste)?

### Placer des éléments dans un dictionnaire
> Compléter le script ci-dessous. Celui-ci doit:

* parcourir les éléments de liste (parcours par indice)
* si l'indice est pair,  c'est une clé, mémoriser cette clé
* si l'indice est impair, c'est une valeur, mémoriser cette valeur
* placer dans un dictionnaire tous les couples clé:valeur

```python
L = ['nom','Alice','classe','Premiere','activité','Judo']
D = {}
for i in range(len(L)):
  if ... % 2 == ...:
    cle = L[...]
  else:
    valeur = L[...]
    D[....] = valeur
print(D)
```

* **Question h3:** Quelle instruction est utilisée pour tester la parité de l'indice `i`?
* **Question h4:** Quelle instruction est utilisée pour placer un nouveau couple clé:valeur dans le dictionnaire?





## Ex 6: Liste de listes
On définit une liste appelée `matrice`

> Dans une cellule Python, saisir la ligne suivante:

```python
matrice  = [[1,2,3], [4,5,6],  [7,8,9],  [10,11,12]]
```

> Utiliser le shell python pour explorer les propositions du tableau. 

* **Question h1:** Recopier et compléter le tableau:

| proposition | valeur |
|--- |--- |
| `matrice[0]` |  retourne le premier élément de `matrice` |
| `matrice[1]` |  ... |
| `matrice[1][2]` |   |
| `matrice[2][1]` |   | 
| `matrice[3][0]` |   | 

* **Question h2:** on souhaite maintenant remplir la 1ere colonne du tableau, celle des *propositions*. En faisant des recherches à l'aide de l'editeur Python, retrouver celle qui affichera la bonne valeur, puis recopier et completer le tableau.

| proposition | valeur |
|--- |--- |
| `matrice[..][..]` | 2  |
| `matrice[..][..]` | 4 | 
| `matrice[..][..]` | 12  | 

* **Question i:** On considère la liste de listes suivante :

```python
tictactoe = [['O', 'O',  'O'],
             ['O', 'O',  'O'],
             ['O', 'O',  'O']]
```
*(la liste peut être écrite sur une même ligne ou avec un retour à la ligne pour chaque élément comme vu ici)*

* **Question j:** Quelles instructions faut-il écrire pour obtenir une diagonale de 'X'? Utiliser des instructions comme `tictactoe[...][...] = 'X'`


## Ex 7: Algorithme sur une liste
### Parcours de liste
Commençons par créer une liste L de la manière suivante:

```python
> L = list('abdef')
> print(L)
["a","b","d","e","f"]
```

On peut parcourir la liste `L` grâce à ses indices, avec `range`

```python
# script 1
for i in range(len(L)):
  print(L[i])
```

```python
# script 2
for i in L:
  print(i)
```

* **Question k1:** L'un de ces scipts est un parcours par *indice*, l'autre par *élément*: Retrouver parmi les 2 scripts lequel est un parcours par *indice*. Le variant `i` prend-il les mêmes valeurs?



### Traitement des valeurs de la liste
Cette liste ne contient pas de `"c"`. Vous allez le rajouter en procédant à un décalage des valeurs de la liste.

1. Commencez par étendre la liste avec un nouveau caractère, `"f"` par exemple.
2. Parcourir la liste à partir de l'élément `"d"` jusqu'à la fin.
3. Dans la boucle: Décalage. Remplacer la valeur de l'élément de rang `i+1` par celle de rang `i`
4. Mettre `"c"` à la bonne place.

> Ecrire et tester le programme.

* **Question k2:** Recopier votre script une fois que celui-ci est fonctionnel.

## Ex 8: tracer un graphique
On donne les listes de relevés du temps et de la vitesse pour un mobile. 

La vitesse `v[0]`est relevée au temps `t[0]`, `v[1]`est relevée au temps `t[1]`, etc...

```python
t = [0,0.04,0.08,0.12,0.16,0.2,0.24]
v = [5.2,4.8,4.41,4.02,3.63,3.23,2.84]
```

* Completer le script python suivant pour afficher un graphique en nuage de points, avec le temps en abscisses et la vitesse en ordonnées.

*La fonction `scatter` va placer les points sur le graphique à partir de 2 listes, qu'il faudra placer en argument. Par exemple `plt.scatter(x,y)` place les points à partir de leur abscisses `x` et leur ordonnées `y`.

```python
import matplotlib.pyplot as plt
plt.scatter(...
plt.show()
```

* La fonction `scatter` propose de nombreuses options, qui valent `None` par defaut. Utiliser la [documentation officielle](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html) et choisir une valeur pour l'un de ces paramètres optionnels (forme du point, couleur, ...)

* Ajouter les fonctions `clf, grid, xlabel et ylabel` pour personnaliser votre graphique:

```python
import matplotlib.pyplot as plt

plt.clf()
plt.grid()
plt.scatter(...
plt.xlabel('temps(min)')
plt.ylabel('vitesse (m/s)')
plt.show()
```


* **Question l:** Expliquer le rôle de chacune de ces fonctions: `clf`, `grid`, `xlabel` et `show`.

# Portfolio
* Quel est l'indice du premier élément de liste? Du dernier?
* Comment atteindre l'élément de rang 6 dans la liste `L`? (Pour lire sa valeur; pour modifier sa valeur)?
* Quelle instruction permet de déplacer une valeur du rang i au rang i+1 dans une liste `L`?
* Comment note t-on le slice sur une liste `L`, pour ne conserver que les éléments du rang 1 jusqu'à l'avant dernier rang?
* Quelles sont les différentes méthodes de liste, et quel est leur rôle? Exemples.
* Soit la liste `L = [['a','b'],['c','d']]`. Comment atteindre l'élément 'c', premier élément de la 2e sous-liste?
* Comment parcourt-on une liste par *élément*, à l'aide d'une boucle `for`? Et comment parcourt-on par *indice*? Exemples.
* Qu'est ce qu'un VARIANT de boucle? (préciser à l'aide des exemples précédents)
* Quelle instruction `for` permet de parcourir les clés d'un dictionnaire?
Comment atteindre la valeur d'un dictionnaire `D`, associé à la clé `7`?
* Les clés d'un dictionnaire sont-elles forcement des clés numériques? Ou bien peut-on aussi placer des clés de types *string*? Exemple.
* Comment placer toutes les valeurs d'un dictionnaire dans une liste `L` (voir ex 5)?

* Quelle librairie python permet de tracer des graphiques? Quel module?
* Quelle instruction permet de tracer un nuage de point avec la liste X en abscisses et Y en ordonnée?

# Liens
* TP5 [listes, indices, méthodes](../page3/)
* TP6 [boucles et parcours de liste](../../../python_avance/boucles/page4)

