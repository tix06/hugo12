---
author: "Eric Tixidor"
date: 06-28-2020
linktitle: Python arbre decision
menu:
  main:
    parent: 
next: 
prev: /Pyhton algorithme de recommandation
title: Python arbre decision
weight: 18
---

# Arbres de classification

Lien vers le notebook en ligne : [https://mybinder.org/v2/gh/tix06/notebooks_classif/master](https://mybinder.org/v2/gh/tix06/notebooks_classif/master)

> Choisir alors le fichier : `graphes_mini_prog.ipynb`

## Définition
Un arbre de classification est utile pour réaliser des prévisions de manière *explicite*. C'est un outil utilisé 

* pour les algorithmes de *backtracking* (modéliser une partie d'echecs)
* pour l'appentissage automatisé (machine learning) supervisé (les classes des entrées sont connue)

Pour le *machine learning* l'arbre peut évoluer et se restructurer à partir d'informations reçues.

A partir des valeurs des données en entrée, l'algorithme va créer des règles pour segmenter, au mieux, la population (les index des entrées) à chaque noeud. En descendant dans l'arbre de classification, on parcourt ses noeuds. Le nombre d'éléments qu'il reste à classer diminue du noeud parent vers un noeud fils : tous les éléments se répartissent sur tous les noeuds fils.

Enfin, lorsque les éléments d'un noeuds ont tous la même classe, alors la division est terminée. Ce noeud est alors une feuille.

*Exemple :* ici, les noeuds 4, 6, 7, 8, 9, 10 sont des feuilles. Ces noeuds contiennent chacun une partie des éléments qui ont servi à construire l'arbre. La totalité de ces éléments occupent le noeud *racine*, numéro 0, puis sont répartis dans les feuilles selon leur classe.

![exemple d'arbre de classification](../datas/hierarchy.png)

## Principe
Utilisation de la librairie sklearn pour créer un arbre de classification/décision à partir d'un fichier de données.

L'arbre de decision est construit à partir d'une segmentation optimale qui est réalisée sur les entrées (les lignes du tableau).

# Jouer ou ne pas jouer
## fichier de données
Ici, le fichier de données est `datas/jouer0.png`. Il contient les données méteorologiques et les classes (jouer/ne pas jouer au golf) pour plusieurs types de conditions météo (les lignes).

Ce fichier ne devra contenir que des données numériques (mis à part la première ligne, contenant les étiquettes des colonnes, les *features*).

## Classifier puis prédire
Une fois l'arbre de classification établi, on pourra le parcourir pour *prédire* la classe d'une nouvelle entrée, en fonction de ses valeurs : l'arbre sert alors comme une *aide à la décision*.

En pratique, il faudra créer une structure qui contient l'arbre, avec ses noeuds, leur association, et les tests qui sont effectués pour descendre d'un noeud parent à l'un des ses noeuds fils. On peut choisir d'utiliser un *dictionnaire python* pour contenir cette structure. Le *dictionnaire* étant un *tableau associatif*.

Comme les données sont toutes *numériques*, les tests réalisés à chaque noeud, pour traduire la division des éléments s'écrivent de la manière suivante : 

Soit X une liste de listes contenant : les éléments à classer, et les valeurs pour chacun des éléments : 

`X[i]` fait alors référence à la valeur des éléments pour la colonne n°i.

```
pour touts les éléments présents au noeud courant : 
    si X[i] <= valeur_seuil alors :
        descendre vers le noeud fils gauche
        sinon : descendre vers le noeud fils droit
   ```


## Import des librairie et création de l'arbre de décision


```python
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_text
import pandas as pd
df = pd.read_csv("datas/jouer0.csv",sep=";")
#col = df.columns
X = df.iloc[:,:-1] # les données sont toutes les colonnes du tableau sauf la dernière
y = df.iloc[:,-1]  # les classes sont dans la dernière colonne (jouer/ne pas jouer)

clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, y)  # on entraine l'arbre à l'aide du jeu de données
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>temps</th>
      <th>température</th>
      <th>humidité</th>
      <th>vent</th>
      <th>jouer</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>30</td>
      <td>85</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>27</td>
      <td>90</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0</td>
      <td>28</td>
      <td>78</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>-1</td>
      <td>21</td>
      <td>96</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>4</th>
      <td>-1</td>
      <td>20</td>
      <td>80</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>5</th>
      <td>-1</td>
      <td>18</td>
      <td>70</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>6</th>
      <td>0</td>
      <td>18</td>
      <td>65</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>7</th>
      <td>1</td>
      <td>22</td>
      <td>95</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>8</th>
      <td>1</td>
      <td>21</td>
      <td>70</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>9</th>
      <td>-1</td>
      <td>24</td>
      <td>80</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>10</th>
      <td>1</td>
      <td>24</td>
      <td>70</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>11</th>
      <td>0</td>
      <td>22</td>
      <td>90</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>12</th>
      <td>0</td>
      <td>27</td>
      <td>75</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>13</th>
      <td>-1</td>
      <td>22</td>
      <td>80</td>
      <td>1</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>



## accéder au paramètres calculés pour l'arbre


```python
# Using those arrays, we can parse the tree structure:

n_nodes = clf.tree_.node_count
children_left = clf.tree_.children_left    # noeud fils gauche pour le noeud courant (ou -1 si aucun noeud enfant)
children_right = clf.tree_.children_right  # noeud fils droit pour le noeud courant (ou -1 si aucun noeud enfant)
feature = clf.tree_.feature                # numéro de la colonne pour la valeur testée 
#                                          # par exemple : feature = 0 <=> temps
#                                          # par exemple : feature = 1 <=> temperature ...                                            
threshold = clf.tree_.threshold            # valeur seuil du test realisé au noeud courant




```

## Exploration de la structure de données 


```python
for i in  range(n_nodes):
    print('noeud :',i)
    print('fg :',children_left[i])
    print('fd :', children_right[i])
    print('feature : ',feature[i])
    print('thershold :',threshold[i])
    print('----------')
    


```

    noeud : 0
    fg : 1
    fd : 6
    feature :  0
    thershold : 0.5
    ----------
    noeud : 1
    fg : 2
    fd : 3
    feature :  3
    thershold : 0.5
    ----------
    noeud : 2
    fg : -1
    fd : -1
    feature :  -2
    thershold : -2.0
    ----------
    noeud : 3
    fg : 4
    fd : 5
    feature :  0
    thershold : -0.5
    ----------
    noeud : 4
    fg : -1
    fd : -1
    feature :  -2
    thershold : -2.0
    ----------
    noeud : 5
    fg : -1
    fd : -1
    feature :  -2
    thershold : -2.0
    ----------
    noeud : 6
    fg : 7
    fd : 8
    feature :  2
    thershold : 77.5
    ----------
    noeud : 7
    fg : -1
    fd : -1
    feature :  -2
    thershold : -2.0
    ----------
    noeud : 8
    fg : -1
    fd : -1
    feature :  -2
    thershold : -2.0
    ----------


## creation d'une structure de type dictionnaire pour contenir l'arbre
Cette struture contiendra aussi les conditions, afin de pouvoir l'utiliser pour *décision*.


```python
def isleaves(node):
    if (children_left[node]==-1 & children_right[node]==-1) :
        return True
    else:
        return False


def construct(node_id):
    arbre[node_id] = {}
    #if node_id != 0:
    if isleaves(node_id):
        return {'node':node_id}
    else : 
        return {'node':node_id,'feature':feature[node_id],'threshold':threshold[node_id],'fg':construct(children_left[node_id]),'fd':construct(children_right[node_id])}
        
arbre = {}       
construct(0)
```




    {'node': 0,
     'feature': 0,
     'threshold': 0.5,
     'fg': {'node': 1,
      'feature': 3,
      'threshold': 0.5,
      'fg': {'node': 2},
      'fd': {'node': 3,
       'feature': 0,
       'threshold': -0.5,
       'fg': {'node': 4},
       'fd': {'node': 5}}},
     'fd': {'node': 6,
      'feature': 2,
      'threshold': 77.5,
      'fg': {'node': 7},
      'fd': {'node': 8}}}




```python
# visualisation du graphe en console
r = export_text(clf, feature_names=None)
print(r)
```

    |--- feature_0 <= 0.50
    |   |--- feature_3 <= 0.50
    |   |   |--- class: 1
    |   |--- feature_3 >  0.50
    |   |   |--- feature_0 <= -0.50
    |   |   |   |--- class: 0
    |   |   |--- feature_0 >  -0.50
    |   |   |   |--- class: 1
    |--- feature_0 >  0.50
    |   |--- feature_2 <= 77.50
    |   |   |--- class: 1
    |   |--- feature_2 >  77.50
    |   |   |--- class: 0
    



```python
# visualisation rapide de l'arbre de classification
tree.plot_tree(clf)
```




    [Text(167.4, 190.26, 'X[0] <= 0.5\ngini = 0.459\nsamples = 14\nvalue = [5, 9]'),
     Text(83.7, 135.9, 'X[3] <= 0.5\ngini = 0.346\nsamples = 9\nvalue = [2, 7]'),
     Text(41.85, 81.53999999999999, 'gini = 0.0\nsamples = 5\nvalue = [0, 5]'),
     Text(125.55000000000001, 81.53999999999999, 'X[0] <= -0.5\ngini = 0.5\nsamples = 4\nvalue = [2, 2]'),
     Text(83.7, 27.180000000000007, 'gini = 0.0\nsamples = 2\nvalue = [2, 0]'),
     Text(167.4, 27.180000000000007, 'gini = 0.0\nsamples = 2\nvalue = [0, 2]'),
     Text(251.10000000000002, 135.9, 'X[2] <= 77.5\ngini = 0.48\nsamples = 5\nvalue = [3, 2]'),
     Text(209.25, 81.53999999999999, 'gini = 0.0\nsamples = 2\nvalue = [0, 2]'),
     Text(292.95, 81.53999999999999, 'gini = 0.0\nsamples = 3\nvalue = [3, 0]')]



{{< img src="../images/jouer.png" caption="décider de jouer avec un arbre de décision" >}}

Contenu de chaque noeud : 

* la condition qui est testée : par ex au noeud 0, X[0]<=0.5 (le temps est moins bien qu'*ensoleillé*) VRAI => à gauche, FAUX => à droite
* le coefficient de gini (qui doit être égal à 0 ou presque dans les feuilles)
* le nombre d'éléments dans le noeud
* value = le nombre d'éléments de chaque classe [classe 0 : ne jouent pas, classe 1 : jouent]


```python
arbre = construct(0)
print(arbre)
```

    {'node': 0, 'feature': 0, 'threshold': 0.5, 'fg': {'node': 1, 'feature': 3, 'threshold': 0.5, 'fg': {'node': 2}, 'fd': {'node': 3, 'feature': 0, 'threshold': -0.5, 'fg': {'node': 4}, 'fd': {'node': 5}}}, 'fd': {'node': 6, 'feature': 2, 'threshold': 77.5, 'fg': {'node': 7}, 'fd': {'node': 8}}}


# Liens

* wikipedia : arbres de décision : [https://fr.wikipedia.org/wiki/Arbre_de_décision_(apprentissage)](https://fr.wikipedia.org/wiki/Arbre_de_décision_(apprentissage))
* dessiner un arbre dans la console [https://scikit-learn.org/stable/modules/tree.html](https://scikit-learn.org/stable/modules/tree.html)
* utilisation de networkx : [https://networkx.github.io/documentation/stable/reference/introduction.html](https://networkx.github.io/documentation/stable/reference/introduction.html)


```python

```
