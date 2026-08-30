---
author: "Eric Tixidor"
date: 05-26-2020
linktitle: Python algo KNN
menu:
  main:
    parent: 
next: donnees_analyse
prev: pandas.md
title: Python algo KNN
weight: 15
---

# Algorithme des k plus proches voisins
## notebook
<!--
Le notebook présenté ici est à télécharger à l'adresse suivante : 

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/tix06/notebook_datas.git/master)

[https://mybinder.org/v2/gh/tix06/notebook_datas.git/master](https://mybinder.org/v2/gh/tix06/notebook_datas.git/master)

Choisir : `algoKNN.ipynb`
-->
Le notebook présenté ici se trouve à l'adresse [tix06.github.io/jupyterlite_NSI](https://tix06.github.io/jupyterlite_NSI/lab/index.html)

Choisir le dossier `TP4_data_analyse` puis le notebook `algoKNN.ipynb`.

Exercez vous en suivant le tutoriel avec ce notebook.

## Principe

On cherche une correspondance entre les **caractéristiques physiques** d'un joueur de basket et son **poste** sur le terrain.

Pour simplifier, on considerera que les postes sont au nombre de trois : 

* le joueur Centre, noté **'C'** (position 5 sur le schéma)
* Le joueur Ailier, noté **'F'** (positions 3 et 4 sur le schéma)
* Le joueur arrière ou meneur de jeu, noté **'G'** (positions 1 et 2 sur le schéma)


<figure>
    <img src="data:image/png;base64,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">
        <figcaption>image URI</figcaption>
    </figure>

Il nous faut, pour rechercher une correspondance, avoir accès à une base de données des joueurs de basket, jouant par exemple dans un même championnat.

En étudiant cette première population, on va pouvoir prédire quel poste pourrait occuper un nouveau joueur entrant dans ce championnat (qui serait *drafté*), à partir de ses seules caracteristiques physiques.

Cette idée est un peu simpliste : le poste occupé sur le parquet ne dépend pas, bien sur des seules caractéristiques physiques, mais aussi des copétences du joueur.

Mais nous allons chercher dans ce TP si l'idée est plutôt cohérente.

On traite alors un jeu de données bi-dimentionnelles à N classes (où N estle nombre de postes occupés par les joueurs).

On va pour cela utiliser l'algorithme des _k-plus-proches-voisins_. C'est l'un des algorithmes les plus utilisés dans le domaine de l'*apprentissage automatique* ou *machine learning*.

Comme pour tous les types d'apprentissage automatique, le principe est le suivant : 

* on commence par étudier une population donnée, dite d'_entrainement_. La qualité d'échantillonnage utilisé pour cette population va déterminer la bonne prédiction par cet algorithme. L'étude de cette population doit permettre de créer des ensembles d'objets aux propriétés similaires. Par exemple, l'ensemble constitué des joueurs de type *Centre* seront probablement plus *grands* et plus *forts* que les autres joueurs.

* On dispose ensuite d'une population exterieure à cet échantillonnage. On cherche à prevoir leur position sur le terrain par rapport à leurs caractéristiques physiques, d'après les résultats de l'étude préalable.

## La ligue de basket NBA

Les données sont issues de la page : [https://fr.global.nba.com/playerindex/](https://fr.global.nba.com/playerindex/]

<figure>
<img src="../datas/extraitNBA.png" width = 80% alt="tableau joueurs NBA">
<figcaption>extrait du tableau des joueurs de NBA</figcaption>
</figure>


La ligue de basket americaine contient environ 400 joueurs professionnels. La plupart de nationalité américaine. On dispose d'un extrait de ce fichier (voir dans le dossier `datas`), constitué de 57 joueurs, classés par ordre alphabetique.

# Chargement du fichier base de données
## Python : librairies numpy et pandas
Le traitement des données se fera en langage *Python*.

On commence par charger les librairies utiles pour le traitement de ces données. Puis on transforme celles-ci en un DataFrame, une sorte de tableau à 2 entrées. Les valeurs de taille et de poids sont toutes de type `float` après ce premier traitement.


```python
import numpy as np
import pandas as pd
data = pd.read_csv("datas/joueursNBA2020.csv", sep=";")
tableau_reduit=data[['nom','equipe','poste','taille','poids','experience','pays']].dropna()
tableau_reduit['poids']=tableau_reduit['poids'].replace(to_replace ='kg', value = '', regex = True)
tableau_reduit['poids']=tableau_reduit['poids'].astype('float')
tableau_reduit['taille']=tableau_reduit['taille'].astype('float')
```


```python
tableau_reduit.head() # on affiche le debut du tableau avec la fonction .head()

```

## Filtrer les données du DataFrame
On peut maintenant filtrer les joueurs du tableau selon le poste du joueur.
On utilise pour cela la fonction `.loc` associée au DataFrame. On met en paramètre un predicat qui sera testé pour chacun des objets du DataFrame. Seuls les objets au prédicat `true` sont conservés : 

> `ensemble = tableau_reduit.loc[tableau_reduit['poste']=='C']` 

> **Question :** Dans cet exemple :  A quel poste jouent les joueurs conservés dans le DataFrame `ensemble`? Vérifiez le dans la console...


```python

```

## Afficher les joueurs sur un graphique taille-poids

On créé une fonction `points` qui ajoute le nuage de points pour chacun des éléments de la liste `postes` mise en paramètre. On créé un nuage de points de couleur et d'étiquette différent pour chaque poste occupé.

Les paramètres de cette fonction : 

* postes : on peut y mettre le caractère correspondant au poste comme 'G', 'F', ou 'C'. On peut aussi y mettre une liste constituée de certains, ou tous les postes.
* Les autres paramètres sont optionnels : il s'agit de la taille et de la forme du marqueur, et de la transparence.


```python
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, Circle 

def points(postes,size=20,marker='o',alpha=0.5):
    """
    fonction qui ajoute des points au graphique existant
    
    Le paramètres :
    * postes peut être une liste de postes comme par exemple ['G','F','C']
    ou bien un seul poste, comme par exemple 'C'
    * les autres paramètres sont optionnels
    """
    for poste in postes:
        ensemble = tableau_reduit.loc[tableau_reduit['poste']==poste]
        x=ensemble['taille']
        y=ensemble['poids']
        plt.scatter(x,y,label=poste, s=size, marker=marker, alpha=alpha)
```

Avec les lignes suivantes, on affiche sur un même graphique les joueurs du tableau jouant aux postes 'G', 'F', 'C'.

Les joueurs du poste 'C' sont mis en relief avec un marqueur plus gros. 

> **Question :** Repérez à quel endroit se regroupent les joueurs 'C'...


```python
plt.title('caractéristiques des joueurs de NBA 2020')
plt.xlabel("taille")
plt.ylabel("poids")
plt.grid(which='major', linestyle='-', linewidth='0.5', color='red')
points(['F','G'])

points('C',100,'D',1)
axes = plt.gca()
plt.legend()
plt.savefig('datas/centre.png')
plt.show()
```

![joueurs au poste 'C' dans la population NBA](../images/centre.png')

```python

```

> **Travail :** Utilisez la fonction `points` pour représenter les 3 ensembles 'C', 'F' et 'G'. Mais cette fois, on veut mettre en relief : 

> * les joueurs 'F' dans un 2e graphique
> * Puis mettre en relief les joueurs 'G' dans un 3e graphique.


```python
# Correction
plt.title('caractéristiques des joueurs de NBA 2020')
plt.xlabel("taille")
plt.ylabel("poids")
plt.grid(which='major', linestyle='-', linewidth='0.5', color='red')
points(['G','C'])

points('F',100,'D',1)
axes = plt.gca()
plt.legend()
plt.savefig('datas/ailier.png')
plt.show()
```

![joueurs au poste 'F' dans la population NBA](../images/ailier.png')

```python
# Correction
plt.title('caractéristiques des joueurs de NBA 2020')
plt.xlabel("taille")
plt.ylabel("poids")
plt.grid(which='major', linestyle='-', linewidth='0.5', color='red')
points(['F','C'])

points('G',100,'D',0.5)
axes = plt.gca()
plt.legend()
plt.savefig('datas/arriere.png')
plt.show()
```

![joueurs au poste 'G' dans la population NBA](../images/arriere.png')

# Prediction du poste du joueur
## population dont le poste est inconnu
Certains joueurs ont des caractéristiques qui les rendent plus polyvalents. 

> **Question :** En observant le tableau_reduit en entier : Quels sont ces postes polyvalents ? 

Ces joueurs n'ont été mis sur aucun des  graphiques d'apprentissage vus plus haut. Et si vous utilisiez un algorithme prédictif pour deviner le meilleur poste auquel ils devraient être ? 
Nous allons étudier en détail cet algorithme, des k plus proches voisins...

Prenons par exemple les joueurs polyvalents à l'étiquette "G-F". Ces joueurs, sont-ils plutôt pressentis pour être G (arrière), ou F (ailier) ?

C'est ce que nous allons chercher à déterminer.

> **Travail :** en utilisant la méthode `.loc` associée au DataFrame `tableau_reduit` : filtrer les joueurs dont le poste est 'G-F', et affecter ce nouveau DataFrame à la variable `ensemble`
> Afficher alors ce nouveau tableau


```python
# Correction
ensemble = tableau_reduit.loc[tableau_reduit['poste']=='G-F']
ensemble
```

## Choisir un joueur
> **Travail :** Repérer le numéro de l'index du premier joueur au poste 'G-F' dans ce tableau. Afficher l'ensemble des informations relatives à ce joueur à l'aide de l'instruction `ensemble.loc[numero index]`  


```python
# Correction
ensemble.loc[9]
```

## Utiliser la fonction *joueur()* pour l'afficher sur le graphique
Affichons un marqueur pour ce joueur au milieu de la distribution *d'entrainement*.
Pour cela, on utilise une fonction de nom `joueur()` dont les paramètres sont les suivants : 

* num : le numero de l'index du joueur dans le tableau
* rayon : le rayon du cercle dans lequel on recherche les k-plus proches voisins. Ce rayon est mesuré dans une unité relative au poids du joueur. L'echelle de l'axe des abscisses, la taille étant très différente, on réalise un calcul prenant en compte le ration DX/DY pour exprimer l'éloignement dans cette direction (un ecart de 10kg n'a pas la même signification qu'un écart de 10cm...)


```python
def joueur(num, rayon):
    """
    positionne le point relatif au joueur de numero num
    et trace un cercle de rayon r exprimé dans une unité relative à l'axe des Y
    Le demi axe de l'ellipse pour X est calculé par rapport au ratio = DX/DY : 
    r_X = r_y*ratio
    """
    ratio = 0.005 # echelle des X / echelle des Y
    plt.title('caractéristiques des joueurs de NBA 2020')
    plt.xlabel("taille")
    plt.ylabel("poids")
    plt.grid(which='major', linestyle='-', linewidth='0.5', color='red')
    points(['F','G','C'])
    x = ensemble.loc[num]['taille']
    y = ensemble.loc[num]['poids']
    plt.scatter(x,y,label=poste, s=50, marker='P', alpha=1)
    circle = plt.Circle((x, y), 1, color='r')
    fig = plt.gcf()  # gcf() signifie obtenir le chiffre actuel
    ax = fig.gca()  # gca() signifie Obtenir l'axe actuel
    ax.set_aspect(ratio)  # je choisi le ratio DX/DY pour les echelles des axes
    ax.add_artist(Ellipse((x, y), rayon*ratio, rayon, color='yellow',alpha=0.2))
    plt.legend()
    plt.savefig('datas/joueur'+str(num)+'.png')
    plt.show()
```

## Afficher le joueur sur le graphique
> **Travail :** utiliser la fonction `joueur()` pour afficher un marqueur pour ce joueur. On prendra un rayon égal à 20 pour le paramètre *rayon*. 


```python
# correction
joueur(9,20)
```

![joueurs n°9 dans la population NBA](../images/joueur9.png)

## L'algorithme des k-plus proches voisins
L'algorithme des k-plus proches voisins peut s'écrire en langage naturel : 

1) trouver dans la collection d'entrainement les k plus proches voisins du joueur
2) Parmi ces proches voisins, trouver la classification majoritaire
3) Renvoyer la classification majoritaire

> Travail : Commencez par fabriquer un DataFrame `ensembleG` contenant tous les joueurs au poste 'G'.

> Puis, avec cette même methode, construire les DataFrame `ensembleF` et `ensembleC` 



```python
# Correction
ensembleG = tableau_reduit.loc[tableau_reduit['poste']=='G']
ensembleF = tableau_reduit.loc[tableau_reduit['poste']=='F']
ensembleC = tableau_reduit.loc[tableau_reduit['poste']=='C']
```

> Enfin, construire un DataFrame `ensemble` qui sera réalisé par concaténation des 3 premiers.

> Afficher les premieres lignes de ce DataFrame (avec la fonction `.head()` 

> Aide sur la fonction concat : `ensemble = pd.concat([DataFrame1,DataFrame2,DataFrame3])` 


```python
# Correction
ensemble = pd.concat([ensembleG,ensembleF,ensembleC])
ensemble.head()
```

Puis ajoutons une nouvelle colonne avec la *distance* au joueur de numero `num` dans le graphique : 


```python
def distance(num,ratio):
    x = tableau_reduit.loc[num]['taille']
    y = tableau_reduit.loc[num]['poids']
    ensemble['dist'] = ensemble.apply(lambda row: (((row["taille"] - x)/ratio)**2 + (row["poids"] - y)**2)**0.5, axis=1)
    # On trie le tableau par valeur dist croissante
    ensemble_trie = ensemble.sort_values(by = 'dist')
    return ensemble_trie
```


```python
ensemble_trie = distance(9,0.005)
```


```python
ensemble_trie
```

## Trier les résultats
On voudrait maintenant dénombrer, par poste, les joueurs aux caractéristiques les plus proches de notre joueur au poste inconnu. Sur un echantillon des k premiers joueurs du tableau précédent.

> **Travail :** Créer une fonction knn(k) qui renvoie un dictionnaire `score` avec pour chacune des clés, 'G', 'F', et 'G', le nombre de joueurs du tableau parmi les k premiers.


```python
# Correction
def knn(k):
    score={'G':0,'F':0,'C':0}
    for i in range(k):
        z=ensemble_trie.index[i]
        if ensemble_trie.loc[z]['poste']=='G' : 
            score['G']+=1
        elif ensemble_trie.loc[z]['poste']=='F' :
            score['F']+=1  
        else : score['C']+=1
    return score  
```

On peut afficher les 3 premiers joueurs du tableau trié, avec l'une des méthodes associée au DataFrame : 


`DataFrame.head(nombre de lignes à afficher)`



```python
ensemble_trie.head(3)
```


```python
knn(3)
```

> **Travail :** Ecrire une fonction qui renvoie le poste le plus représenté selon la valeur de k choisie. Faites alors quelques essais. Conclure quand à la pertinence du résultat selon la valeur de k choisie.


```python

```

## Prolongement
On peut réaliser ce même travail : pour rechercher les k plus proches voisins :

* d'un autre joueur au profil 'G-F'
* pour un joueur d'un autre profil, comme par exemple 'F-G'


```python

```

# Liens
* TP du site infoforall.fr avec des joueurs de football : [https://www.infoforall.fr/act/algo/k-plus-proches-voisins](https://www.infoforall.fr/act/algo/k-plus-proches-voisins)
* TP du site Lyceum.fr sur la prevision d'une mention au conseil de classe : [https://lyceum.fr/1g/nsi/8-algorithmique/3-algorithme-des-k-plus-proches-voisins](https://lyceum.fr/1g/nsi/8-algorithmique/3-algorithme-des-k-plus-proches-voisins)
* Cours sur pixees.fr: https://pixees.fr/informatiquelycee/n_site/nsi_prem_knn.html
* Article Wikipedia: https://fr.wikipedia.org/wiki/M%C3%A9thode_des_k_plus_proches_voisins





```python

```
