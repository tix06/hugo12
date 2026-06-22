---
Title: tri à partir d'une cle
hidden: true
weight: 6
---

# Partie 1: Appliquer un algorithme de tri
Nous allons appliquer les 2 algorithmes de tri (insertion et selection) sur des listes non ordonnées.

## Mélanger un liste de mots
* (1) Reprendre pour cette première partie le dossier du TP de [recherche dans un dictionnaire de mots](/docs/NSI/algorithmes/page14_bis/). Ouvrir un nouveau fichier python dans ce même dossier. Placer l'import des librairies `random` et `time` à l'ouverture de ce fichier (premières lignes).
* (2) Ajouter au script python les **fonctions de tri** vues dans le cours: [Lien vers le cours](/docs/NSI/algorithmes/page8/)
* (3) importer une liste de mots d'un dictionnaire non accentué. Appeler cette liste `mots`.
* (4) mélanger la liste de mots avec la fonction `random.shuffle` (voir exemple plus bas)
* (5) réduire cette liste à seulement 10000 mots: `mots = mots[:10000]`
* (6) copier cette liste de mots (faire une copie **par valeur**): `mots_melanges = mots.copy()`


*Aide*: 

La fonction `shuffle` du module `random` permet de mélanger en place les éléments d'une liste. *Exemple:*

```python
> import random
> L = [3, 4, 6, 8, 10, 20]
> random.shuffle(L)
> L
# exemple d'affichage
[6, 3, 20, 10, 8, 4]
```

## Fonction `est_triee`
* (7) Programmer une fonction `est_triee` qui vérifie si la liste est bien triée. Cette fonction sera utile pour contrôler que la fonction  de tri effectue bien le tri demandé, sans avoir à parcourir celle-ci après traitement.

Utiliser la base suivante pour la fonction: (et compléter):

```python
def est_triee(L):
	for i in range(1,len(L)):
		if ...:
			return False
	return ...
```

* (8) Utiliser cette fonction pour vérifier que la liste `mots` est mélangée:

```python
> est_triee(mots)
False
```

## Trier le dictionnaire de mots
Votre script devrait avoir l'allure suivante: (les fonctions dont à compléter)

```python
import random
import time

def est_triee(L):
    pass

def tri_insertion(L):
    pass

def tri selection(L):
    pass

mots = []
# Lecture du fichier txt et remplissage de la liste
with open(...) as f:
    for mot in f.read().splitlines():
        mots.append(mot)

mots = mots[:10000]
random.shuffle(...)
mots_melanges = ... .copy()
```

Vous allez tester maintenant vos fonctions de tri sur la liste [dictionnaire-de-mots](/docs/NSI/algorithmes/page14_bis/), une fois celle-ci mélangée.

* **Question 1:** Mesurer le temps mis pour trier la liste de mots à l'aide du tri par insertion. (faire plusieurs essais).

**Remarque**: Si vous voulez comparer 2 algorithmes de tri en place, sur la même liste, il faudra faire une copie par valeur de la liste mélangée. Le tri par insertion puis par selection doit être realisé sur la MEME liste si vous voulez comparer les durées de traitement.


On *rappelle* que la mesure du temps peut être réalisée de la manière suivante:

* Pour le tri par insertion:

```python
start_time = time.time()
tri_insertion(mots)
stop_time = time.time()
interval1 = stop_time - start_time
```

* **Question 2:** Mesurer le temps mis pour trier la liste de mots à l'aide du tri par selection. (faire plusieurs essais). Comparer le temps mis par les 2 algorithmes de tri


# Partie 2: TP tri à partir d'une clé
On peut réaliser un tri à l'aide d'une **clé**. Les objets (les lignes d'un fichier *csv*) contiennent ainsi des valeurs sur plusieurs colonnes. On peut choisir l'une de ces colonnes pour réaliser le tri.

On prendra pour exemple le fichier du classement UEFA des équipes feminines sur plusieurs années. Le tableau est consultable à la page de l'[UEFA.com](https://fr.uefa.com/nationalassociations/uefarankings/womensclub/#/yr/2022)

## import du fichier csv
* -> fichier csv *[classement_uefa.csv](/pdf/NSI/classement_uefa.csv)* à telecharger

> Ci-dessous, le programme minimal pour lire le fichier csv. Testez le à l'aide d'un IDE (Pyzo ou autre). Adaptez si necessaire le chemin vers le fichier:

```python
import csv
with open('classement_uefa.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter = ";")
    teams = []
    for row in spamreader:
        teams.append(row)
print(teams[0])
# affiche
['\ufeffClub', 'Pays', '16/17', '17/18', '18/19', '19/20', '20/21', '\xa0pts\xa0', '\xa0Ass\xa0']
```

La premiere ligne contient l'en-tête du tableau. Il faudra supprimer cette premiere ligne:

```python
del(teams[0])
print(teams[0])
# affiche
['AC Sparta Praha', 'CZE', '3', '9', '3', '3', '8', '26', '11,715']
```

## Nettoyer les données
La valeur de la colonne d'indice 8 contient la chaine de caractères (str) `'11,715'`. Il faudra transformer cette valeur en (float) `11.75`

Même traitement avec la colonne 7.

On peut utiliser la méthode de chaine `replace`:

```python
team = teams[0]
team[7] = team[7].replace(',','.')
team[8] = team[8].replace(',','.')
print(team)
```

> **Importer à nouveau** le tableau source, puis faire ce **traitement sur les 114 équipes** du tableau `teams`. (Utiliser une boucle for)


<!--
Une autre option possible: joindre les 2 sous-listes avec un point '.', puis séparer les éléments de la chaine de caractères au niveau des ';':

> Tester également cette 2e option:

```python
import csv
with open('datas/classement_uefa.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile)
    teams = []
    for row in spamreader:
        s = ".".join(row) 
        # instruction necessaire pour le format de la derniere valeur decimale
        # .join(row) créé une chaine de caractères à partir de la liste
        s = s.split(";")
        # on recréé une liste
        teams.append(s)

del(teams[0])
print(teams[0])

>>> ['AC Sparta Praha', 'CZE', '3', '9', '3', '3', '8', '26', '11.715']
```
-->

## Classement par indice UEFA: colonne 7

Au depart les équipes sont classées par ordre alphabetique:

```
['AC Sparta Praha', 'CZE', '3', '9', '3', '3', '8', '26', '11.715']
['AFC Ajax', 'NED', '-', '5', '8', '-', '3', '16', '9.9']
['Akadimia Elpides Karditsas', 'GRE', '-', '-', '2', '-', '-', '2', '2.145']
['ALG Spor Kulübü Derneği', 'TUR', '-', '-', '-', '-', '0', '0', '2.145']
['Apollon Ladies FC', 'CYP', '4', '3', '-', '2', '0', '9', '4.62']
...
```



On veut adapter l'agorithme de tri par selection pour classer les equipes selon une *clé*, qui sera l'indice de la colonne contenant les points UEFA de l'équipe.

> **A vous de jouer**: adapter le script des algorithmes de tri:

> 1. Ajouter un nouveau paramètre `cle` aux fonctions `tri_insertion` et `tri_selection`.
> 2. Adapter les programmes des 2 fonctions pour trier par rapport à une clé. Modifier par exemple la condition dans la boucle `for` de la fonction de recherche du minimum (ttri par selection) avec `if T[k][cle]<T[indiceDuMin][cle] :`
> 3. Trier maintenant la liste `teams` selon la colonne de rang 7. 

Si vous affichez cette liste, elle presente 2 inconvenients:

  * elle est triée telle que l'equipe la plus faible est au debut du tableau et la meilleure à la fin.
  * l'affichage ne facilite pas la lecture

> 5. Modifier la fonction de tri pour réaliser un tri par l'**élément le plus grand** d'abord.

* **Question 1:** Quel est le classement UEFA des équipes entre la $1^{ere}$ et la $5^e$ equipe? 

## Classement par coefficient des associations: colonne 8
Le classement par *coefficient des associations* ou des pays prend en compte les résultats de tous les clubs d'une association. Il est utilisé pour déterminer le nombre de clubs que pourra engager une association dans les compétitions de l'UEFA les saisons suivantes. C'est la valeur de la colonne 8.

> 6. Classer les équipes par coefficient des associations.

* **Question 2:** Quel est le nouveau classement des équipes entre la $1^{ere}$ et la $5^e$ equipe? 

## Nettoyer les résultats
On souhaite obtenir l'affichage suivant, avec seulement les colonnes *equipe, pays, indice uefa*:


```
0 ('Olympique Lyonnais', 'FRA', '99')
1 ('FC Barcelona', 'ESP', '78')
2 ('VfL Wolfsburg', 'GER', '77')
3 ('Paris Saint-Germain', 'FRA', '60')
4 ('Manchester City WFC', 'ENG', '59')
5 ('FC Bayern München', 'GER', '57')
6 ('Chelsea FC Women', 'ENG', '45')
...
```

> 7. Ajouter les instructions suivantes qui permettront d'afficher les equipes : 
  * Créer un tableau vide T.
  * faire une boucle bornée `for` sur la liste `teams` : `for t in range(...)`
  * Dans la boucle for, à chaque itération, ajouter dans T un tuple constitué des colonnes 0, 1 et 7 pour chacune des équipes.
  * afficher classement et equipe avec :  `print(t,T[t])` 



 


