---
Title: Corrigé TD2b listes, tuples, dictionnaires
description: corrigé du TD2b - parcours de liste, compréhension de liste, méthodes de listes et dictionnaires, tracé graphique
hidden: true
weight: 11
---

## Ex 0: Parcours d'une liste — corrigé

* **script 1** affiche `1 10 100 1000`
  * variant : `x`
  * itérable : `L` (la liste elle-même)
  * valeurs successives prises par le variant : `1`, `10`, `100`, `1000` (les éléments de `L`)

* **script 2** affiche `0 1 2 3`
  * variant : `i`
  * itérable : `range(len(L))`, soit `range(4)`
  * valeurs successives prises par le variant : `0`, `1`, `2`, `3` (les indices de `L`)


## Ex 1: table de 3 — corrigé

```python
L = []
for i in range(11):
  L.append(3*i)
```

* **Question a1:** Après exécution, `L` vaut `[0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30]`. L'itérable `i` prend successivement les valeurs `0, 1, 2, ..., 10`.

* **Question a2:** On complète les `...` par `3*i` (le terme général de la table de 3). Pour la table de 7, il suffirait de remplacer `3*i` par `7*i`.

* **Compréhension de liste :**

```python
L = [3*i for i in range(11)]
```


## Ex 2: Energie en sciences physiques — corrigé

```python
t = [0,0.04,0.08,0.12,0.16,0.2,0.24]
vitesse = [5.2,4.8,4.41,4.02,3.63,3.23,2.84]

m = 100

E = []
for v in vitesse:
  E.append(0.5*m*v**2)
```

* **Compréhension de liste :**

```python
E = [0.5*m*v**2 for v in vitesse]
```

* **Question c:** script complet pour le tracé du graphique :

```python
import matplotlib.pyplot as plt   # importer un module

t = [0,0.04,0.08,0.12,0.16,0.2,0.24]      # déclaration de variables/listes
vitesse = [5.2,4.8,4.41,4.02,3.63,3.23,2.84]
m = 100
E = []

for v in vitesse:                 # calcul des termes d'une liste par boucle bornée
  E.append(0.5*m*v**2)

plt.plot(t, E)                    # tracé du graphique
plt.xlabel("temps (s)")
plt.ylabel("Energie cinétique (J)")
plt.show()
```

  * déclarer des variables et des listes → lignes avec `t = ...`, `vitesse = ...`, `m = ...`, `E = []`
  * calculer les termes d'une liste avec une boucle bornée → le bloc `for v in vitesse: E.append(...)`
  * importer un module → `import matplotlib.pyplot as plt`
  * tracer un graphique → les lignes `plt.plot(...)`, `plt.xlabel(...)`, `plt.ylabel(...)`, `plt.show()`


## Ex 3: algorithmes simples utilisant une boucle bornée — corrigé

* **Question d:** somme des $2^i$ pour `i` de 0 à 99 :

```python
somme = 0
for i in range(100):
  somme = somme + 2**i
somme
```

* **Question e:** nombre de boules d'une pyramide à $n$ étages = somme des carrés parfaits (1 boule à l'étage du sommet, 4 à l'étage suivant, 9, 16, ...) ou éventuellement la somme des entiers selon la forme retenue dans le cours ; en reprenant la construction "somme des entiers de 1 à n" adaptée à la pyramide à couches carrées :

```python
n = 7
somme = 0
for i in range(1, n+1):
  somme = somme + i**2
somme
```

Pour `n = 7`, on trouve `somme = 140` boules. Il suffit de remplacer `n = 7` par `n = 99` pour obtenir le nombre de boules d'une pyramide à 99 étages (`328350`).

*(Remarque : si la pyramide de l'énoncé est en réalité un empilement simple - une boule en haut, deux à l'étage suivant, etc. - on adaptera avec `somme = somme + i` au lieu de `i**2`; le principe de la boucle reste identique.)*


## Ex 4: Autres types construits — corrigé

### Tuple

```python
T = (("A",1),("B",2),("C",3))
for elem in T:
  print(elem[0])
```

Affiche bien :
```
A
B
C
```

### Dictionnaire

* Construction par boucle `for` :

```python
D = {}
for elem in T:
  D[elem[0]] = elem[1]
```

* Construction par compréhension de dictionnaire :

```python
D = {elem[0]:elem[1] for elem in T}
```

Dans les deux cas, `D` vaut `{"A":1, "B":2, "C":3}`.


## Ex 5: Méthodes de listes — gérer un plan de vols — corrigé

```python
aeroports = ['CDG', 'ORY', 'LIS']

# a) ajouter JFK en fin de liste
aeroports.append('JFK')

# b) insérer Londres-City en 3e position (juste après ORY)
aeroports.insert(2, 'LCY')

# c) supprimer LIS
aeroports.remove('LIS')

# d) index de JFK
aeroports.index('JFK')

# e) retirer le dernier aéroport ajouté et l'afficher
dernier = aeroports.pop()
print(dernier)

# f) fusionner avec la liste d'une compagnie partenaire
aeroports.extend(['AMS', 'BRU'])

print(aeroports)
```

Points clés :
* **b)** `insert(index, valeur)` insère sans reconstruire toute la liste.
* **e)** `pop()` (sans argument) retire **et retourne** le dernier élément : c'est la seule méthode qui fait les deux actions à la fois.
* **f)** `extend()` fusionne une liste à la fin d'une autre en une seule instruction, sans boucle.


## Ex 6: Trier une liste — classement de notes — corrigé

```python
notes = [12, 8, 15, 10, 20, 6, 14]

# a) tri par copie
notes_triees = sorted(notes)
print(notes_triees)   # [6, 8, 10, 12, 14, 15, 20]
print(notes)          # [12, 8, 15, 10, 20, 6, 14] -> inchangée

# b) tri en place
notes.sort()
print(notes)          # [6, 8, 10, 12, 14, 15, 20] -> a changé
```

* **Question c:** en exécutant `notes = notes.sort()`, `notes` devient `None`. En effet, la méthode `sort()` trie la liste **en place** et ne retourne **rien** (elle retourne `None`) ; en réaffectant son résultat à `notes`, on écrase la liste par `None`.

* **Question d:** le paramètre est `reverse=True`.

```python
notes.sort(reverse=True)
# ou
notes_dec = sorted(notes, reverse=True)
```


## Ex 7: Copier une liste — le piège de la référence — corrigé

```python
original = [1, 2, 3]
copie = original
copie.append(4)
print(original)   # [1, 2, 3, 4]
print(copie)       # [1, 2, 3, 4]
```

* **Question a:** les deux `print` affichent `[1, 2, 3, 4]`.

* **Question b:** ce résultat s'explique car l'instruction `copie = original` ne crée pas une nouvelle liste : elle fait pointer `copie` **vers le même objet en mémoire** que `original`. Modifier `copie` modifie donc directement cet objet unique, ce qui se répercute sur `original`.

* **Question c:** pour obtenir une copie indépendante, on peut par exemple écrire :

```python
copie = original.copy()
```

ou bien :

```python
copie = original[:]
```

Avec l'une ou l'autre de ces méthodes, modifier `copie` (par exemple `copie.append(4)`) laisse `original` inchangée, soit `[1, 2, 3]`.


## Ex 8: Méthodes de dictionnaires — le carnet de capitales — corrigé

```python
capitales = {'France': 'Paris', 'Italie': 'Rome', 'Allemagne': 'Berlin'}

# a) afficher les clés
for pays in capitales.keys():
  print(pays)

# b) afficher les valeurs
for ville in capitales.values():
  print(ville)

# c) afficher pays + capitale
for pays, ville in capitales.items():
  print(pays, ville)

# d) ajouter le Portugal
capitales['Portugal'] = 'Lisbonne'

# e) corriger l'Allemagne si besoin
if capitales['Allemagne'] != 'Berlin':
  capitales['Allemagne'] = 'Berlin'

# f) supprimer l'Italie
del capitales['Italie']

# g) copie indépendante
mes_capitales = capitales.copy()
mes_capitales['Espagne'] = 'Madrid'
print(capitales)        # ne contient pas 'Espagne'
print(mes_capitales)    # contient 'Espagne'

# h) compréhension de dictionnaire
capitales_maj = {pays:ville.upper() for pays, ville in capitales.items()}
print(capitales_maj)
```

Points clés :
* **g)** `capitales.copy()` (ou `dict(capitales)`) crée un nouveau dictionnaire indépendant ; une simple affectation `mes_capitales = capitales` aurait reproduit le piège de référence de l'exercice 7.
* **h)** la compréhension parcourt les couples `(pays, ville)` via `.items()` et applique `.upper()` sur chaque valeur.


