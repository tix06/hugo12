---
author: "Eric Tixidor"
date: 06-26-2020
linktitle: Python Pandas
menu:
  main:
    parent: 
next: /Python AlgoKnn
prev: /python_les_bases
title: Python Pandas
weight: 10
---

# Python : la librairie pandas
## notebook

Le notebook présenté ici est à télécharger à l'adresse suivante : 

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/tix06/notebook_datas.git/master)

[https://mybinder.org/v2/gh/tix06/notebook_datas.git/master](https://mybinder.org/v2/gh/tix06/notebook_datas.git/master)

Puis choisir : `gestionBase_de_donnees_python.ipynb`

Exercez vous en suivant le tutoriel avec ce notebook.

## présentation
Pandas fournit des structures de données puissantes et simples à utiliser, ainsi que les moyens d'opérer rapidement des opérations sur ces structures.

Cette librairie va utiliser et faire des opérations sur un objet : le *DataFrame*
Ce DataFrame est très similaire aux tables des bases de données relationnelles (type MySQL, PostgreSQL, etc.) que l'on manipule grâce au langage SQL.

Ce notebook est inspiré du cours en ligne : 

[https://openclassrooms.com/fr/courses/4452741-decouvrez-les-librairies-python-pour-la-data-science/5558996-passez-de-numpy-a-pandas](https://openclassrooms.com/fr/courses/4452741-decouvrez-les-librairies-python-pour-la-data-science/5558996-passez-de-numpy-a-pandas)

## représentation d'un tableau avec la librairie numpy
*numpy* est une librairie utile pour de nombreuses applications mathématiques. *numpy* permet de manipuler facilement des tableaux. Un tableau est une liste contenant une nouvelle liste pour chacun de ses éléments. C'est une liste de listes.

L'avantage de manipuler des tableaux, *(array)*, plutôt que des listes, c'est de pouvoir réaliser des calculs sur les valeurs comme si la structure de donnée était une matrice.

On va voir ici que cette représentation des données n'est pas la meilleure façon qu'il soit lorsqu'on l'utilise pour une collection (par exemple pour des *informations*).

Prenons l'exemple de la **programmation d'une salle de cinéma** de type cinémathèque :  

On renseigne pour chacune des salles de ce cinéma (pour chacune des lignes), les valeurs : le titre du film (colonne 1), horaire (colonne 2), realisateur (col 3), année (col 4).


```python
#************************************#
#****** un premier exemple **********#
#******* de numpy à panda ***********#
#************************************#

import numpy as np
tableau2D = [
    ['la rage aux poings', '18h00' , 'Eric le Hung', 1975], # film projeté dans la salle 1
    ['le million' , '15h00', 'René Clair', 1931], # dans la salle 2
    ['Rendez vous à Badenberg', '21h00'  , 'René Meurice', 1970], # dans la salle 3
    ['Le cercle rouge', '18h05', 'Jean-Pierre Melville', 1970], # dans la salle 4
]
tableau_numpy = np.array(tableau2D)
tableau_numpy
```


```python
# acceder à l'élément de rang 3 de la ligne 0 : 
tableau_numpy[0,3]
```


```python
# acceder à TOUS les elements au rang 0 (donc la première colonne)
tableau_numpy[:,0]
```

C'est assez pratique certes, mais `tableau_numpy[:, 0]`  quand cette colonne possède un descripteur (le nom du film), ce n'est pas très explicite. 

On va voir maintenant ce qu'apporte la représentation des données avec la librairie *Pandas*.

## représentation des données avec la librairie pandas

Les données sont maintenant mises dans un *DataFrame*, et plus un tableau *array*.


```python
#***************************#
#**** creer un DataFrame ***#
#***************************#

import pandas as pd  # on importe la librairie pandas
tableau2D_df = pd.DataFrame(tableau2D) # on créé un DataFrame tableau2D_df à partir de l'array tableau2D
tableau2D_df # et on l'affiche

```


```python
#******************************************#
#********** passage du tableau np *********#
#*** ainsi que les index et descripteurs **#
#******************************************#

tableau2D_df = pd.DataFrame(tableau_numpy,
                                index = ['salle 1', 'salle 2', 'salle 3','salle 4'],
                                columns = ['titre', 'horaire', 'realisateur', 'année'])
tableau2D_df
```

On peut maintenant réduire le tableau en une seule colonne, par exemple celle dont l'etiquette est *horaire*. On obtient alors une *serie* de données.


```python
# reduire le tableau (SELECT)
tableau2D_df.horaire     # 1ere methode
tableau2D_df['horaire'] # 2e methode
```

Et si l'on a besoin d'une série comprenant 2 colonnes (ou plus), on utilise la syntaxe suivante : 


```python
tableau2D_df[["titre","horaire"]]
```

## parcours et exploration des données
On peut utiliser une boucle bornée qui, à chaque itération, donne :

* l'indice 
* le contenu de la serie pour cet index (c'est à dire les valeurs et leur etiquette pour chacun des objets)

On utilise la fonction `iterrow` associée au DataFrame : 

```
for index, valeurs in DataFrame.iterrows() : 
    ...
```


```python
# parcourir
for ind_ligne, contenu_ligne in tableau2D_df.iterrows():
    print("Voici le film de la %s :" % ind_ligne)
    print(contenu_ligne)
    print("--------------------")
```

## accéder à un seul des objets de la collection
Cette fois, plutôt que d'utiliser une boucle bornée et d'afficher TOUS les objets de la collection, on cherche à en afficher un seul.

Cette fois le tri ne se fait pas selon une colonne, comme par exemple pour `tableau2D_df['horaire']` mais par ligne, avec : 

`tableau_2D_df.loc['salle 3']  par exemple

On aura ainsi le descriptif du film programmé dans cette salle.


```python
# acceder à un objet
tableau2D_df.iloc[2] # Avec iloc(), indexation positionnelle
tableau2D_df.loc["salle 3"] # Avec loc(), indexation par label
```

## Rechercher un film
On va maintenant trier le tableau jusqu'à trouver l'élement correspondant.

On cherche par exemple, dans quelle salle passe le film *'Rendez vous à Badenberg'* : La colonne correspondant à cette valeur est celle dont l'etiquette est `'titre'`. On écrit alors une expression logique, qui est évaluée pour chaque objet, et qui renvoie `true` si le titre correspond à celui recherché, et `false` sinon.

La console affiche alors une serie de données : 


```python
# trier (WHERE)
tableau2D_df["titre"] == 'Rendez vous à Badenberg'
```

> **Question :** Ecrire l'instruction qui renverra `true` pour toutes les salles projettant un film réalisé en 1970.
> Testez votre instruction dans la cellule suivante.


```python

```

## filtrer les données du tableau
On va maintenant appliquer l'expression logique vue plus haut pour reduire le DataFrame aux seuls objets pour lesquels l'expression renvoie `true`. On dit que l'on a **filtré** les données.

**Premier exemple :** filtrage du tableau pour ne conserver que la salle dans laquelle passe le film *'Rendez vous à Badenberg'*. On obtient alors un nouveau DataFrame, mais réduit.


```python
# masquer (WHERE)
tableau_filtre = tableau2D_df[tableau2D_df["titre"] == 'Rendez vous à Badenberg']

tableau_filtre # on affiche le tableau filtré
```

**Exemple 2 :** on cherche le complémentaire de l'expression precedente : filtrer et renvoyer tous les films DIFFERENTS de *`Rendez vous à Badenberg'

On utilise pour cela le symbole ~ (tild) devant l'expression dont on veut le complémentaire : 


```python
tableau_comp = tableau2D_df[~(tableau2D_df["titre"] == 'Rendez vous à Badenberg')]
tableau_comp
```

**Exemple 3 :** filtrer par rapport aux dates de réalisation.

> **Travail :** ecrire l'instruction qui renvoie un nouveau DataFrame, mais uniquement avec des films réalisés en 1970


```python

```

## trier le tableau
On peut vouloir maintenant afficher les films dans l'ordre croissant de diffusion dans la journée.
Pour des raisons de commodité, on modifie le format de l'heure de diffusion pour que le type de données soit `float` et non `str`. Par exemple : '18h00' => 18.00 


```python
tableau2D_df['horaire']=[18,15,20,18.1]
tableau2D_df # on affiche le tableau
```

On peut maintenant trier ce tableau selon l'horaire : 


```python
tableau2D_df.sort_values(by ='horaire')
```

Et voilà, vous n'avez plus aucun excuse pour rater une seance ;-)

# Traitement de données en csv
Le fichier joint `joueursNBA2020.csv` est un extrait des joueurs professionnels de basket de NBA, pour la saison 2019-2020. On va utiliser la librairie pandas pour ouvrir puis explorer ce fichier.


```python
#******************************************#
#******************** fichier csv *********#
#******************************************#
data = pd.read_csv("datas/joueursNBA2020.csv", sep=";")
```


```python
data
```

Les données recupérées doivent souvent être remises en forme. Le tableau ci-dessus présente plusieurs problèmes qui doivent être traités avant de pouvoir exploiter les données : 

* Il y a des colonnes *Unnamed* qui ne servent à rien : elles seront à supprimer
* Il y a plus de lignes que de joueurs. Ces lignes ont pour valeur `NaN`. Il faudra aussi les supprimer.
* Le poids des joueurs, dans la colonne 'poids' est exprimé sous format `str`. Les valeurs sont écrites avec l'unité, *kg*. Il vaudra mieux les tranformer en type `float`, en retirant les caractères *kg*.


```python

```


```python
#***************************************#
# en pratique **************************#
# selection des colonnes renseignées    #
# et suppression des lignes NaN         #
# avec .dropna()                        #
#***************************************#
tableau_reduit=data[['nom','equipe','poste','taille','poids','experience','pays']].dropna()
```


```python
#*************************************#
# puis `cast` de la colonne poids     #
# les valeurs sont de type str et     #
# combinent des float avec kg         #
# par exemple 89.8 kg                 #
#*************************************#

tableau_reduit['poids']=tableau_reduit['poids'].replace(to_replace ='kg', value = '', regex = True) 
```


```python
#************************************#
# puis conversion du type            #
# str vers float                     #
# **********CAST ********************#
#************************************#

tableau_reduit['poids']=tableau_reduit['poids'].astype('float')
```


```python
tableau_reduit.loc[1]['poids']
```


```python
tableau_reduit
```

Et voila, il n'y a plus qu'à explorer ce tableau de données. On peut par exemple : 
    
* filtrer le tableau pour n'afficher que les joueurs du poste 'C'
* filtrer les joueurs pour ne conserver que les joueurs de nationalité autre que americaine.
* Trier les joueurs par taille, ou par poids

> **Travail :** Testez certaines des propositions faites ici...


```python

```

# Liens

* Cours sur openclassroom.com : decouvrir la librairie pandas : [https://openclassrooms.com/fr/courses/4452741-decouvrez-les-librairies-python-pour-la-data-science/5558996-passez-de-numpy-a-pandas](https://openclassrooms.com/fr/courses/4452741-decouvrez-les-librairies-python-pour-la-data-science/5558996-passez-de-numpy-a-pandas)
* kaggle.com presentation des dataframes : [https://www.kaggle.com/arnopub/pandas-pr-sentation-des-dataframe](https://www.kaggle.com/arnopub/pandas-pr-sentation-des-dataframe)
* documentation officielle : [https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html)



```python

```
