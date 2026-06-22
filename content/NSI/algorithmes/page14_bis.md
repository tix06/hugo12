---
Title: algoritmes de recherche
description: TP, dictionnaire de mots en francais, chronometrage time du module time
hidden: true
weight: 8
---

# Recherche dans une liste de mots
* Télécharger les listes de mots à partir du lien suivant:{{< a link="/scripts/fichiersmots.zip" caption="fichiersmots.zip" >}}

> Dezipper les fichiers de mots. Obtenir 4 fichier avec extension `.txt`
> Ouvrir un editeur python et enregistrer le fichier (save as ...) dans le MÊME dossier. 

Les fichiers:

| fichier | contenu |
|--- |--- |
| gutenberg.txt | Liste exhaustive avec accents, verbes conjugés, quelques noms propres |
| liste_francais.txt | Liste réduite, avec accents |
| ods4.txt | Officiel du Scrabble - Version 4 - 2004 - Sans accents |
| pli07.txt | Petit Larousse Illustré 2007 - Sans accents |

## Import des librairies
On aura besoin pour le TP de l'import suivant. Copier et coller ces lignes dans votre première cellule:

```python
## import
import os
from random import choice
import time
import numpy as np
# os.chdir('U://Documents/scripts_python/dictionnaire_de_mots')
```

La dernière ligne règle le problème de dossier courant pour la lecture de fichiers texte avec la fonction `open`. Il faudra adapter le chemin de `os.chdir` en fonction de votre installation.

> Executer le fichier

> Dans le shell, vérifier que le dossier contient les fichiers `.txt` avec la fonction `os.listdir()`

## Importer un premier fichier texte
Importer la liste de mots du fichier `liste_francais.txt` dans une liste et afficher les 13 derniers éléments de la liste à l'aide du script suivant. 

Par exemple, pour `liste_francais.txt`:

```python
mots = []

# Lecture du fichier txt et remplissage de la liste
with open('liste_francais.txt', encoding='utf-8') as f:
    for mot in f.read().splitlines():
        mots.append(mot)
        
# Affichage des 13 derniers mots
print(len(mots))
mots[-13:]
```

## Recherche séquentielle
### Un même algorithme pour plusieurs listes de mots
**1.** Dans une cellule, coller et executer le script:

```python
from random import choice
choice(mots)
``` 

**2.** La fonction de recherche séquentielle. Recopier le script et le compléter à partir de la spécification:

```python
def recherche_mot(liste_mots):
    """
    recherche un mot dans une liste et renvoie l'indice si le mot est trouvée, -1 sinon
    Params :
    -------------------
    liste_mots : list, une liste de mots, dans un ordre quelconque.
    Variables :
    -----------
    X : str, mot défini aléatoirement dans la liste_mots
    
    Sortie : 
    ------
    j : int, indice dans la liste
    Principe :
    --------
    X est un mot tiré aleatoirememt avec choice(liste_mots)
    on parcourt la liste avec une boucle non bornée, tant que X n'est pas trouvé dans la liste
    on augmente la valeur de j à chaque nouvelle itération
    """
    j = 0
    n = len(liste_mots)
    X = ...  # a completer
    while j<n and X!=liste_mots[j]:
        j ... # à completer
    if j==n : return -1
    return j
```

**3.** Tester alors votre fonction:

```python
recherche_mot(mots)
``` 


On peut lancer un chronomètre juste avant l'appel de la fonction avec l'instruction, puis relever le temps t1-t0:


```python
import time
t0 = time.time()
recherche_mot(mots)
t1 = time.time()
t1-t0 # affichage en s
``` 

> **4.** Répéter plusieurs fois l'appel de la fonction `recherche_mot(mots)`. Par exemple 100 fois (ou 1000 fois pour être encore plus précis). Stocker dans une liste `T` le temps $t1-t0$ mis par la fonction pour trouver un mot aleatoire. Puis calculer la moyenne des valeurs de `T` avec la fonction `mean` de `numpy`:

```python
import numpy as np
T = []

# appel de la fonction recherche_mot et ajouter le temps
# a la liste T
for i in range(100):
    t0 = time.time()
    recherche_mot(mots)
    t1 = time.time()
    T.append(t1-t0)

r = np.mean(T)
r
```

> **5.** Mettre dans une liste `L` le couple `[len(mots), r]`

**6.** Refaire le même travail, pour CHACUNE des listes de mots. Ajouter à chaque fois le nouveau couple `[len(mots), r]` dans `L`.

Et ajouter le couple `[0,0]` (pour une longueur de liste égale à 0, le temps mis est aussi 0).

La liste `L` devrait alors contenir 5 éléments: `[[len(mots1), r1], [len(mots2), r2], ...[0,0]]`

### Graphique en nuage de points y = temps, x = len(mots) 

```python
import matplotlib.pyplot as plt
# creation de listes x,y a l'aide de la librairie np
L = np.array(L)
x = L[:,0]
y = L[:,1]
plt.scatter(x,y)
plt.xlabel('N mots')
plt.ylabel('temps moyen de recherche')
plt.show()
```

## Recherche dichotomique
**1.** Copier-coller et completer le script suivant:

```python
def recherche_dicho_mot():
    """recherche dans une liste de mots un mot X
    Params:
    ------
    X : str, mot à trouver
    Variables:
    ---------
    mots : list, contient des mots triés
    Return :
    --------
    milieu (indice de mot dans la liste) si X est présent dans la liste
    -1 sinon"""
    # on initialise les indices début et fin aux extrémités de la liste
    gauche = 0
    droite = len(mots)
    trouve = False
    X = choice(mots)
    while gauche <= droite and not trouve:
        milieu = (gauche+droite)//2
        if mots[milieu] == X:
            trouve = True
        elif mots[milieu] < X:       
            gauche = milieu + 1   
        else:
            droite = milieu - 1
    if not trouve : 
        return ...
    return ...
```

**2.** L'algorithme de recherche dichotomique ne fonctionne que pour des listes sans accents. Tester la fonction avec les seules listes `ods4.txt` et `pli07.txt`. 

**3.** On peut améliorer l'étude de la recherche dichotomique en ajoutant un compteur du nombre d'itérations à l'interieur de la fonction. Ce compteur sera incrémenté à chaque itération (`while`). La fonction devra retourner cette fois un tuple constitué de (-1, i) ou bien de (milieu, i) selon si l'on trouve le mot.

Le nouveau programme de calcul de temps et du nombre d'itérations moyen est alors:

```python
T = []

# appel de la fonction recherche_mot et ajouter le temps
# a la liste T
for i in range(100):
    t0 = time.time()
    _,nb_cycles = recherche_dicho_mot(mots)
    t1 = time.time()
    T.append([t1-t0,nb_cycles])
T = np.array(T)
r1 = np.mean(T[:,0])
r2 = np.mean(T[:,1])
print('temps moyen',r1,'nbe iter',r2)
```

**Comparer le nombre d'itérations moyen avec la fonction log binaire: $np.log2(len(mots))$**

**4.** Comparer le nouveau tableau de valeurs `T = [[len(mots1), r1], [len(mots2),r2], [0,0]]` avec le précédent. Conclure.

# Tracé de représentations graphiques pour quelques fonctions

La librairie `numpy` facilite la creation des ensembles X,Y pour le tracé des courbes. L'instruction `X=np.linspace(0.1,50,100)` va créer un tableau de 100 valeurs, de 0.1 à 50.  

```python
X=np.linspace(0.1,50,100)
#plt.plot(X,np.log2(X),label='log2(X)') 
#plt.plot(X,X,label='X')
#plt.plot(X,X*np.log2(X),label='X*log2(X)')
#plt.plot(X,X**2, label='X**2')
#plt.plot(X,2**X, label='2**X')
plt.legend()
```

**1.** représenter sur la même figure les fonctions:


* $Y = X$
* $Y = log_2(X)$

**2.** Ajouter sur ce même graphique la fonction:

* $Y = X * log_2(X)$

**3.** Ajouter:

* $Y = X**2$

**4.** Ajouter:

* $Y = 2**X$

**5.** Recopier l'allure de ces courbes. Conclure.

# Lien
* Version initiale du TP sur la recherche sequentielle et dichotomique: [Lien](../page14/)
* Les fichiers de mots viennent de la page: [www.3zsoftware.com](http://www.3zsoftware.com/fr/listes.php)