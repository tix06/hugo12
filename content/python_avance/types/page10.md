---
Title : tables de données
description: listes de listes, tri avec clé (lambda), conversion en dictionnaires, import de fichiers csv
weight: 12
---

# Les tables de données en Python

*Ce cours s'appuie sur les notions déjà vues sur les [types simples](../page1/) et les [types construits](../page2/) (listes, dictionnaires, mutabilité). Il prépare l'[exercice sur la table des pays](../page5/).*

Une grande partie des données que l'on manipule en informatique se présentent sous forme de **tables** : un ensemble d'enregistrements (une ligne par individu, par mesure, par pays...), chacun décrit par les mêmes attributs (les colonnes). C'est le cas d'une feuille de tableur, d'une table de base de données, ou d'un fichier `.csv`.

# Modéliser une table avec des listes
La structure la plus simple pour représenter une table en Python est une **liste de listes** : chaque ligne de la table est elle-même une liste.

Par convention, on place souvent en première ligne les **étiquettes de colonnes** (le nom de chaque attribut), puis une ligne par individu :

```python
table = [
    ["Pays", "Nb élèves secondaire", "Jours de vacances/an", "Durée secondaire (ans)"],
    ["France", 5660000, 112, 7],
    ["Allemagne", 6900000, 65, 9],
    ["Espagne", 3500000, 105, 6],
    ["Grèce", 700000, 119, 6],
]
```

## Accéder à une valeur
Une table étant une liste de listes, on accède à une valeur précise avec un **double indiçage** : `table[i][j]` désigne la valeur de la ligne `i`, colonne `j`.

```python
table[0]
# affiche ['Pays', 'Nb élèves secondaire', 'Jours de vacances/an', 'Durée secondaire (ans)']
table[1]
# affiche ['France', 5660000, 112, 7]
table[1][0]
# affiche 'France'
table[1][1]
# affiche 5660000
```

## Parcourir une table
Parcourir les **lignes** de données (sans l'en-tête) se fait avec une boucle bornée classique :

```python
for ligne in table[1:]:
    print(ligne)
```

Pour parcourir aussi les **colonnes** d'une ligne, on imbrique une seconde boucle, en s'appuyant sur `range(len(ligne))` :

```python
for ligne in table[1:]:
    for j in range(len(ligne)):
        print(table[0][j], ":", ligne[j])
    print("---")
```

# Copier une table
Le cours sur les types construits a montré que copier une liste par simple affectation (`copie = original`) crée un **alias** : les deux noms désignent le même objet.

Pour une liste « plate », on évite ce piège avec `original[:]` ou `list(original)`. Mais pour une **liste de listes**, il faut être plus prudent :

```python
donnees = table[1:]           # copie de la liste externe
donnees[0][1] = 0
table[1][1]
# affiche 0  !! table a été modifiée alors qu'on n'a modifié que "donnees"
```

`table[1:]` crée bien une **nouvelle liste externe**, mais ses éléments — les lignes — restent les **mêmes objets** que dans `table`. C'est une copie dite *de surface* (*shallow copy*) : seul le premier niveau est dupliqué.

Pour obtenir une copie totalement indépendante, y compris des lignes, il faut une copie *profonde* (*deep copy*), fournie par le module `copy` :

```python
from copy import deepcopy

donnees = deepcopy(table[1:])
donnees[0][1] = 0
table[1][1]
# affiche 5660000  # table n'a pas été modifiée cette fois
```

# Rechercher un extremum dans une colonne
Rechercher, par exemple, le pays ayant le plus grand nombre d'élèves (colonne d'indice 1) suit le schéma classique de recherche de maximum : on mémorise le meilleur candidat rencontré jusqu'ici, et on le met à jour à chaque ligne qui fait mieux.

```python
meilleure_ligne = table[1]
for ligne in table[2:]:
    if ligne[1] > meilleure_ligne[1]:
        meilleure_ligne = ligne

print(meilleure_ligne[0], meilleure_ligne[1])
# affiche Allemagne 6900000
```

# Trier une table selon une colonne
Le cours sur les types construits a présenté `sorted` et `sort` pour trier une liste dans son ordre naturel. Ces deux outils acceptent en réalité un paramètre optionnel, `key`, qui indique **selon quel critère** comparer les éléments — utile ici puisqu'on ne veut pas trier des lignes entières « au hasard », mais selon une colonne précise.

`key` attend une **fonction** qui, appliquée à un élément, renvoie la valeur à utiliser pour la comparaison. Pour une fonction aussi courte, on utilise en général une **fonction lambda** (fonction anonyme, écrite en une ligne) plutôt qu'une fonction `def` complète :

```python
lambda ligne: ligne[1]
# équivaut à une fonction sans nom qui, à une ligne, associe ligne[1]
```

On peut alors trier la table selon le nombre d'élèves, du plus grand au plus petit :

```python
tri_par_effectif = sorted(table[1:], key=lambda ligne: ligne[1], reverse=True)
for ligne in tri_par_effectif:
    print(ligne[0], ligne[1])
# affiche
# Allemagne 6900000
# France 5660000
# Espagne 3500000
# Grèce 700000
```

*Documentation (extrait) :*
```
sorted(iterable, key=None, reverse=False)
    - key : fonction appliquée à chaque élément avant comparaison
    - reverse=True : tri décroissant plutôt que croissant
```

# Passer d'une table à des dictionnaires
Accéder à une valeur par sa position (`ligne[1]`) est efficace mais peu lisible : rien n'indique, à la lecture du code, que l'indice `1` correspond au nombre d'élèves. Une alternative consiste à représenter chaque ligne par un **dictionnaire**, où les clés sont les étiquettes de colonnes.

```python
etiquettes = table[0]
ligne_france = table[1]

France = {
    etiquettes[0]: ligne_france[0],
    etiquettes[1]: ligne_france[1],
    etiquettes[2]: ligne_france[2],
    etiquettes[3]: ligne_france[3],
}
# affiche {'Pays': 'France', 'Nb élèves secondaire': 5660000, 'Jours de vacances/an': 112, 'Durée secondaire (ans)': 7}
```

On peut généraliser cette construction à toutes les lignes de la table, à l'aide d'une boucle, pour obtenir un **dictionnaire de dictionnaires** — une structure très courante pour représenter des données structurées :

```python
pays_dict = {}
etiquettes = table[0]

for ligne in table[1:]:
    nom_pays = ligne[0]
    pays_dict[nom_pays] = {}
    for j in range(1, len(etiquettes)):
        pays_dict[nom_pays][etiquettes[j]] = ligne[j]

pays_dict['France']
# affiche {'Nb élèves secondaire': 5660000, 'Jours de vacances/an': 112, 'Durée secondaire (ans)': 7}
```

# Importer une table depuis un fichier CSV
Un fichier **CSV** (*Comma-Separated Values*) stocke une table sous forme de texte : chaque ligne du fichier est une ligne de la table, et les valeurs sont séparées par un caractère précis (une virgule `,` le plus souvent, mais un point-virgule `;` est fréquent dans les fichiers produits en France, la virgule y étant déjà utilisée comme séparateur décimal).

Le module `csv` de la bibliothèque standard permet de lire un tel fichier sans avoir à découper les lignes soi-même avec `split` :

```python
import csv

with open('datas/classe.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';')
    classe = []
    for row in spamreader:
        classe.append(row)
```

Décomposons ce script :

* `open('datas/classe.csv', newline='')` ouvre le fichier. L'argument `newline=''` est recommandé par la documentation de `csv` pour éviter des problèmes de fin de ligne selon le système d'exploitation.
* `csv.reader(csvfile, delimiter=';')` construit un objet **itérable** : chaque itération donne la ligne suivante du fichier, déjà découpée en liste de chaînes de caractères, selon le séparateur indiqué (ici `;`).
* La boucle `for row in spamreader:` parcourt ces lignes une par une, et le script les accumule dans la liste `classe` avec `append` — la même technique de **construction de liste par accumulation** que celle vue avec `while`/`for` dans le TP sur les listes.

À la fin, `classe` est une liste de listes, exactement comme la table `table` du début de ce cours — on peut donc lui appliquer tout ce qui vient d'être vu : parcours, copie, recherche d'extremum, tri par clé, conversion en dictionnaires.

*Point de vigilance :* le module `csv` lit **toujours** les valeurs comme des chaînes de caractères, y compris les nombres. Une valeur `"5660000"` lue dans un fichier CSV doit être convertie explicitement avec `int(...)` ou `float(...)` avant tout calcul (voir le cours sur les [conversions de types](../page1/)).

*Pour aller plus loin :* le module `csv` propose aussi `csv.DictReader`, qui utilise automatiquement la première ligne du fichier comme clés et renvoie directement chaque ligne sous forme de dictionnaire — ce qui réalise en une seule instruction ce que la section précédente a construit à la main :

```python
with open('datas/classe.csv', newline='') as csvfile:
    lecteur = csv.DictReader(csvfile, delimiter=';')
    for ligne in lecteur:
        print(ligne)
# chaque "ligne" est un dictionnaire, par exemple :
# {'Pays': 'France', 'Nb élèves secondaire': '5660000', ...}
```

# Suite
* Exercice d'application : [manipuler la table des pays](../page5/) (copie, recherche, tri, dictionnaires).
