---
Title: Donnees en table
description: operations sur les tables, représentation en python
weight: 13
---

# Données en table - introduction
Les tables structurent les données et permettent de réaliser facilement des opérations de recherche d'informations ou de calcul sur ces données. 

Prenons l'exemple une agence de voyage, qui propose des activités sur mesure à ses clients.

{{< img src="../images/voyage1.png" >}}

les données sont organisées en 2 tables *clients* et *sejours*. Il y aura autant de tables que d'*entités*

Les tables *clients* et *sejours* ont un identifiant unique attribué lors de leur enregistrement.

**CLIENTS** 

| IDC | NOM | AGE | ACTIVITE |
|--- |--- |--- |--- |
| 27 | Ritta | 19 | Danse |
| 19 | Blaise | 29 | Cinema |
| 11 | Dede | 59 | Nature |
| 18 |  Indie| 58 | Histoire |
| 12 | Kelly | 30 | Surf |
| 17 | Dupond | 35 | Surf |
| 28 |  Nono | 65 | Plongée | 

**SEJOURS** 

| IDS | VILLE | ACTIVITE |
|--- |--- |--- |
| 1 | Cayenne | Nature |
| 10 | Rio | Danse |
| 11 | Havane | Danse |
| 12 | Oahu | Surf |
| 20 | Durban | Plongée |
| 65 | Sydney | Surf |
| 88 | Rome | Art |
| 90 | Durban | Surf |

L'agence de voyage a besoin d'un programme prenant en entrée un nom de **VILLE**, et affichant la table contenant la reponse à la question:

*Donner les couples (nom de client, identifiant de sejour) tel que ce sejour est dans la **VILLE**, et propose l'activité favorite de ce client*.

*Exemple:* ``suggestion_client(VILLE = 'Oahu')``

**Sortie:**

| VILLE | NOM | IDS |
|--- |--- |--- |
| Oahu | Kelly | 12 |
| Oahu | Dupond | 12 |

*Le but de l'activité est de comprendre les différentes étapes utiles à ce programme*.

1. Créer une table unique `CHOIX_SEJOUR` vide avec toutes les colonnes des 2 tables.
2. Pour chaque ligne de `CHOIX_SEJOUR`, coller bout à bout les lignes de `SEJOUR` et de `CLIENTS` ayant la même `ACTIVITE`. Représenter cette table. Il peut y avoir plusieurs clients pour un même sejour. Dans ce cas, il doit y avoir une ligne unique pour chaque coupe sejour-client.
3. Dans cette table `CHOIX_SEJOUR`, conserver uniquement les lignes correspondant à la ville *Oahu*.
3. Créer une nouvelle table `RESULTAT` à partir de `CHOIX_SEJOUR` en ne conservant que les colonnes `VILLE, NOM, IDS`. Représenter cette table.
4. Attribuer à chaque instruction le nom de l'opération réalisée. Choisir parmi: 
  * Jointure
  * Projection
  * Selection
  * Modification de table

# COURS
## Tables - généralités
### Une table
Une table est une liste de lignes, dont les éléments partagent les mêmes colonnes (descripteurs).

{{< img src="../images/table1.png" >}}
### Une ligne
Chaque ligne est un p-uplet de valeurs (duet, triplet, ...)

{{< img src="../images/table4.png" >}}
### Une colonne
Dans chaque colonne, on trouve des valeurs de même type: le **domaine de valeurs**. 

Chaque colonne porte un nom: le **descripteur** de la colonne.

{{< img src="../images/table2.png" >}}
### Le schéma d'une table
Le schema d'une table est sa structure. C'est l'ensemble de ses descripteurs de colonnes avec leur type. C'est ce qui décrit une table.

> *Exemple:* Donner le schema de la table *clients*

> * IDC : entier
* NOM : caracteres
* AGE : entier
* ACTIVITE : caracteres


### Le contenu d'une table
Le contenu d'une table est formé de ses lignes, qui contiennent les *valeurs*

{{< img src="../images/table3.png" >}}


### L'identifiant ID
Parmi les colonnes, l'une d'entre-elles a un statut particulier: L'IDENTIFIANT. Celui-ci doit être **unique** pour chaque entité, et pour chaque ligne.



{{< img src="../images/table5.png" >}}

## Représenter une table
On peut représenter une table sous forme de texte structuré: en *csv*, *json*, ou *xml*.

Ces formats sont interopérables. On peut les manipuler avec de nombreuses applications. (tableurs, langages informatique). 

### Table mise dans une liste python
Pour ouvrir et lire un fichier *csv* en langage python, on peut utiliser le script suivant:

```python
import csv
with open('voyage.csv', mode='r', encoding='utf-8') as f:
     table = list(csv.reader(f,delimiter=";"))
```

On suppose qu'il n'y a qu'une table par fichier *csv*. 

La représentation d'une table est alors une LISTE de lignes en python.

**Ligne**: La représentation d'une ligne de la table peut être, au choix:

* une liste, un tuple: 
  * voir [Fiche 1: Listes](/pdf/python/listes1_Fiche.pdf)
  * voir [Fiche 2: algorithmes sur les listes](/pdf/python/listes2_Fiche.pdf)
  * voir [Fiche 4: tuple et dictionnaire](/pdf/python/listes4.pdf)
* un dictionnaire
  * voir [Fiche 4: tuple et dictionnaire](/pdf/python/listes4.pdf)

Pour une représentation en *tuple*:

```python
ligne1 = (27, 'Ritta', 19, 'Danse')
```

Les valeurs doivent être placées, sans en omettre une.

Voici alors un extrait de la table CLIENTS mise dans une liste de listes (3 premiere lignes):

| IDC | NOM | AGE | ACTIVITE |
|--- |--- |--- |--- |
| 27 | Ritta | 19 | Danse |
| 19 | Blaise | 29 | Cinema |
| 11 | Dede | 59 | Nature |

```python
table = [(27, 'Ritta', 19, 'Danse'),
         (19, 'Blaise', 29, 'Cinema'),
         (11, 'Dede', 59, 'Nature'),
         ...
         ]
```

### Table mise dans un dictionnaire python
Un dictionnaire est un tableau associatif. Les éléments sont rangés en couples *clé:valeurs*, séparés par une virgule, et mis entre accollades `{}`.


Pour une représentation en *dictionnaire*:

```
ligne1 = {'IDC' : 27, 'NOM': 'Ritta', 'AGE': 19, 'ACTIVITE: 'Danse'}
```

Les *descripteurs* sont les *clés* du dictionnaire. A chaque clé est associée une valeur. 

On accède à l'**une des valeurs** en plaçant la clé entre les `[]`:

```python
>>> print(ligne1['NOM'])
Ritta
```

La **liste des clés** est obtenue par la méthode de classe `keys()` du dictionnaire:

```python
>>> for c in ligne1.keys():
    ....print(c)
IDC
NOM
AGE
ACTIVITE
```

Voici alors un extrait de la table CLIENTS mise dans une liste de dictionnaires (3 premiere lignes):

```python
table = [{'IDC' : 27, 'NOM': 'Ritta', 'AGE': 19, 'ACTIVITE: 'Danse'},
         {'IDC' : 19, 'NOM': 'Blaise', 'AGE': 29, 'ACTIVITE: 'Cinema'},
         {'IDC' : 11, 'NOM': 'Dede', 'AGE': 59, 'ACTIVITE: 'Nature'},
         ...
         ]
```

### Table mise dans un Dataframe
Cette partie sera developpée en TP.

## Insertion dans une table
On suppose que la table a été importée dans une **liste de dictionnaires**. Le traitement affectera TOUTES les lignes de la table.

### Calculer une moyenne
* parcourir tous les elements de liste
* ce sont des dictionnaires: selectionner la valeur associée à la clé
* faire la somme et diviser par le nombre d'éléments de la liste. (le nombre de dictionnaires)
* appel de la fonction avec le tableau

```python
tableau = [{'IDC' : 27, 'NOM': 'Ritta', 'AGE': 19, 'ACTIVITE: 'Danse'},
         {'IDC' : 19, 'NOM': 'Blaise', 'AGE': 29, 'ACTIVITE: 'Cinema'},
         {'IDC' : 11, 'NOM': 'Dede', 'AGE': 59, 'ACTIVITE: 'Nature'}
         ]

def moyenne(L,cle):
  """calcule la moyenne des valeurs associées à clé
  params:
  L: list of dict
  cle: str, la clé commune à chaque dictionnaire, les valeurs associées 
  sont soit int soit float
  """
  s = 0
  for elem in L:
    s += elem[cle]
  return s / len(L)

> moyenne(tableau,'AGE')
35.666667
```

### Ajouter une valeur calculée
On peut souhaiter ajouter la différence avec la moyenne des âges, pour chaque élément du tableau. Il faudra:

* calculer la moyenne des âges (fonction `moyenne`)
* parcourir les dictionnaires du tableau
* lire la valeur associée à `âge`
* `valeur = moyenne(L,'AGE') - elem['AGE']` 
* ajouter le couple `'DIFFERENCE': valeur` pour chaque element du tableau

```python
tableau = [{'IDC' : 27, 'NOM': 'Ritta', 'AGE': 19, 'ACTIVITE: 'Danse'},
         {'IDC' : 19, 'NOM': 'Blaise', 'AGE': 29, 'ACTIVITE: 'Cinema'},
         {'IDC' : 11, 'NOM': 'Dede', 'AGE': 59, 'ACTIVITE: 'Nature'}
         ]

def ajoute_moyenne(L):
  for elem in L:
    age = L['AGE']
    valeur = moyenne(L,'AGE') - elem['AGE']
    elem['DIFFERENCE'] = valeur

> ajoute_moyenne(tableau)
> print(tableau)
[{'IDC' : 27, 'NOM': 'Ritta', 'AGE': 19, 'ACTIVITE: 'Danse', 'DIFFERENCE': -16.6667},
 {'IDC' : 19, 'NOM': 'Blaise', 'AGE': 29, 'ACTIVITE: 'Cinema' 'DIFFERENCE': -6.6667},
 {'IDC' : 11, 'NOM': 'Dede', 'AGE': 59, 'ACTIVITE: 'Nature', 'DIFFERENCE': 23.3333}
]
```

## Opérations sur les tables: selection, projection, jointure
Ces opérations vont créer une nouvelle table.
### Selection
**Definition:** Selectionner revient à extraire les lignes d'une table qui satisfont un critère. Pour réaliser une selection, on utilise une fonction `test` qui prend en paramètre une ligne de la table et retourne un booléen:

{{< img src="../images/table11.png" >}}

**Méthode utilisant une boucle bornée:**

```python
selection = []
for ligne in table:
  if test(ligne):
    selection.append(ligne)
```

**Méthode par compréhension** 

```python
[ligne for ligne in table if test(ligne)]
```

### Projection
**Definition:** Une projection revient à ne conserver que certaines colonnes de la table. Pour réaliser une projection, on créé une nouvelle table:

{{< img src="../images/table12.png" >}}

**Méthode utilisant une boucle bornée et une table de listes:**

```python
projection = []
colonnes = [0,1] # liste de colonnes à conserver
for ligne in table:
  nouvelle_ligne = []
  for i in colonnes:
    nouvelle_ligne.append(ligne[i])
  projection.append(nouvelle_ligne)
```

**Méthode utilisant une boucle bornée et une table dictionnaires:**
```python
table = [{'id':0, 'NOM':'Jean','AGE': 65},
        {'id':1, 'NOM':'Michel','AGE': 45},
        {'id':2, 'NOM':'Manu','AGE': 40}]

projection = []
colonnes = ['id','NOM'] # liste de colonnes à conserver
for ligne in table:
  nouvelle_ligne = {}
  for i in colonnes:
    nouvelle_ligne[i] = ligne[i]
  projection.append(nouvelle_ligne)
>>> projection
[{'id': 0, 'NOM': 'Jean'}, {'id': 1, 'NOM': 'Michel'}, {'id': 2, 'NOM': 'Manu'}]
```

**Méthode par compréhension, table de listes** 

```python
[[ligne[i] for i in [0,1]] for ligne in table]
```


**Méthode par compréhension, table de dictionnaires** 

```python
[{ligne[i] for i in ['id','NOM']} for ligne in table]
# affiche
[{0, 'Jean'}, {'Michel', 1}, {2, 'Manu'}]
```

## Jointure
**Definition:** Une jointure est la fusion de 2 tables pour un même attribut. (commun).
La jointure permet de regrouper des informations dans une même table.

```python
clients = [{'IDC':27, 'NOM': 'Ritta', 'AGE': 19, 'ACTIVITE': 'Danse'},
          {'IDC':19, 'NOM': 'Blaise', 'AGE': 29, 'ACTIVITE': 'Cinema'}]
sejours = [{'IDS': 1, 'VILLE': 'Cayenne', 'ACTIVITE': 'Nature'},
           {'IDS': 10, 'VILLE': 'Rio', 'ACTIVITE': 'Danse'}]
cle = 'ACTIVITE'
table_jointure = []
attribut_commun = 'ACTIVITE'
for sejour in sejours:
    for client in clients:
        if sejour[cle] == client[cle]:
            ligne = {}
            for attribut in sejour.keys():
                ligne [attribut] = sejour[attribut]
            for attribut in client.keys():
                ligne [attribut] = client[attribut]
            table_jointure.append(ligne)
>>> table_jointure
[{'IDS': 10, 'VILLE': 'Rio', 'ACTIVITE': 'Danse', 'IDC': 27, 'NOM': 'Ritta', 'AGE': 19}]
```

