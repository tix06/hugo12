---
Title: recherche de correlations
description: module seaborn, visualisation, recherche de clusters dans un nuage de points
weight: 26
---

# Etape 6: Analyse graphique
Utiliser le tableau de données des planètes: {{< a link="/scripts/astro/dataset.csv" caption="dataset.csv" >}}

> Importer les librairies et les datas:

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.widgets import Cursor
import seaborn as sns

df = pd.read_csv('dataset.csv')
df
```

{{< img src="../images/tab_IST.png" caption="liste ordonnée par IST decroissant" >}}

## Utiliser une librairie de traitement de données python
*Seaborn Python* est une bibliothèque (un ensemble de modules) de visualisation de données en Python. 

*Pandas dataframe.corr()* est une fonction qui calcule les correlations de paires à partir des *séries* (valeurs des colonnes) du dataframe.

La méthode de calcul est proposée [ici](https://datatab.net/tutorial/pearson-correlation)

{{< img src="../images/Equation_Pearson_Correlation.png" link="https://datatab.net/tutorial/pearson-correlation" caption="credit - datatab.net" >}}

*Principe:*

* on commence par créer une matrice de correlation à partir des colonnes de la table (*dataframe*). Aux intersections ligne/colonne on donne le résultat de la correlation entre les 2 séries (fonction `corr`)
* puis on affiche cette matrice, en superposant des couleurs: fonction `heatmap`

```python
corr = df.corr()
sns.heatmap(corr,cmap='coolwarm',annot=True,linewidth=0.9)
plt.show()
```

{{< img src="../images/seaborn2.png" caption="seaborn - matrice de correlation sur les colonnes du dataset" >}}

On voit par exemple que les grandeurs `radius` et `orbital_period` ne présentent pas de correlation (0.076), le maximum étant 1:

```python
>>> corr['orbital_period']['radius']
0.076
```

## Rechercher des *clusters* de planètes
On peut aussi utiliser la méthode `pandas.plotting` qui donne les nuages de point en miniature:

```python
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
scatter_matrix(df,figsize=(8,8))
plt.show()
```

{{< img src="../images/sklearn_corr.png" >}}

*Rq:* Les diagonales affichent les histogrammes pour les données de la série.

On a vu [ici](../page3) une autre manière de partager la fenêtre en plusieurs graphiques, et mettre les axes en *echelle logarithmique*:


{{< img src="../images/seaborn3.png" >}}

## Placer nos planètes étudiées
Choisir des axes avec des données correlées.

> Pour commencer, filter les données pour les planètes à mettre en evidence: la Terre, ainsi que celles de TOI:

```python
names = ['TOI-270 d','TOI-270 b','TOI-270 c','earth']
df_p = df[df['_name'].isin(names)]
df_p
```

{{< img src="../images/df_filtre.png" caption="tableau des planetes à repérer dans le graphique" >}}

> Puis utiliser le script suivant pour superposer 2 nuages de points, dont l'un en couleur:

```python
%matplotlib qt
plt.clf()
axes = plt.gca()
"""nuage de points df issu de la BDD
"""
x = df['radius']
y = df['orbital_period']
z = df['_name']
plt.scatter(x,y,color='silver',marker='.',alpha=0.5)


   
"""nuage de points df_p issu des observations
"""
x_p = df_p['radius']
y_p = df_p['orbital_period']
z_p = df_p['_name']

plt.scatter(x_p,y_p,color='red',marker='o',label='Rho')
for x, y, z in zip(x_p, y_p, z_p):
    axes.text(x, y, f"({z})", fontsize=8)
plt.xscale('log')
plt.yscale('log')
cursor = Cursor(axes, useblit=True, color='red', linewidth=2)
plt.show()
```

{{< img src="../images/exemple_graphique.png" caption="orbital_period vs radius en echelle log" >}}






## à vous de jouer
Faire un choix d'axes pertinent, afin de trouver des clusters d'exoplanètes et les comparer avec nos planètes d'étude.


# Suite
* Analyse, segmentation des données en clusters et previsions avec le module `scikit-learn`: [étape 7](../page6)

