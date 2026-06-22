---
Title: kmean et exoplanetes
description: KNN et module Scikit-learn, previsions
weight: 27
---

# Utiliser le module Scikit-learn
## Que fait ce module?
*[Scikit-learn](https://fr.wikipedia.org/wiki/Scikit-learn)* est une bibliothèque libre Python destinée à l'apprentissage automatique. Cette bibliothèque propose une série d'outils pour l'étude des données en table comme:

* la regression linéaire
* la classification
* le clustering
* ...

Nous allons utiliser cette bibliothèque pour rechercher des dépendances entre les données des exoplanètes connues. Le travail de [représentation graphique](../page5) nous a montré que ces planètes se regroupent en *clusters* sur les diagrammes en nuages de points. (*echelle log*).

Scikit-learn va nous aider à determiner des classes d'exoplanètes (tellurique, gazeuse, similaire aux étoiles). Nous rappelons que la table [dataset.csv](/scripts/astro/dataset.csv) contient les données des exoplanètes, de leurs étoiles, ainsi que les données ajoutées (Terre et système TOI_270).

Vous pouvez télécharger le dossier complet ici: [sources.zip](../datas/sources.zip), contenant:

* le fichier de dependances `requirment.txt`
* la table `dataset.csv`
* le notebook `intro_IA.ipynb`

*Prérequis:* Ce notebook demande d'être familiarisé avec les types `np.array`, et `pandas.dataframe`.

## Apprentissage non supervisé
Les classes des astres ne sont pas renseignés dans la table *dataset.csv*. Pourtant, il apparait évident que ces astres se regroupent en amas, donc certainement en *familles*.

{{< img src="../images/cluster2.png" caption="radius - mass en echelle log. Données issues du fichier dataset.csv" >}}

Le principe de la recherche de cluster par scikit-learn utilise la fonction [kmeans](https://scikit-learn.org/stable/modules/clustering.html#k-means) de recherche de plus proches voisins. Elle peut être testé avec le script minimum ci-dessous:

```python
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Génération de données aléatoires (non étiquetées)
np.random.seed(42)
data = np.random.rand(100, 2)  # 100 points avec 2 caractéristiques

# Création et entraînement du modèle K-Means
kmeans = KMeans(n_clusters=3, random_state=42)  # 3 clusters
kmeans.fit(data)

# Récupération des résultats
labels = kmeans.labels_  # Les clusters attribués à chaque point
centroids = kmeans.cluster_centers_  # Les centres des clusters

# Visualisation des clusters
plt.scatter(data[:, 0], data[:, 1], c=labels, cmap='viridis', s=50, alpha=0.7)
plt.scatter(centroids[:, 0], centroids[:, 1], c='red', marker='X', s=200, label='Centroids')
plt.title("Clustering avec K-Means")
plt.xlabel("Caractéristique 1")
plt.ylabel("Caractéristique 2")
plt.legend()
plt.show()
```

{{< img src="../images/cluster1.png" caption="exemple de resultat donné par la recherche de clusters (données aléatoires)" >}}

La fonction [kmeans](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html) utilise l'algorithme de *[LLoyd](https://fr.wikipedia.org/wiki/Algorithme_de_Lloyd-Max)*. La recherche d'un centre de cluster (centroïd) pourrait se faire par recherche exhaustive, mais alors, la complexité serait très importante et le temps de calcul rapidement divergent avec le nombre de points. Dans cet algorithme, la recherche est basée sur un *algorithme glouton*. Celui-ci va chercher à minimiser une grandeur appelée *inertie*, qui est calculée comme la distance du centroïd à ses voisins. Enfin, les points sont segmentés en plusieurs clusters, tels que la variance est à peu près identique pour le calcul de l'inertie.

## Données de la table *dataset.csv*
Comme dans l'activité précédente: importer les données de la table:

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('dataset.csv')
df
```

{{< img src="../images/tab_IST.png" >}}

Réduire la table aux colonnes masse, rayon, nom:

```python
df_reduit = df[['mass','radius','_name']]
df_reduit = df_reduit.dropna()
# echelle log
# rappel: les données sont normalisées par rapport à Jupiter
x = np.log(df_reduit['mass'])
y = np.log(df_reduit['radius'])

L = []
for x, y in zip(x, y):
    L.append([x,y])

L[:10]
# Affichage --------------------
[[-5.761407122499511, -2.409803828596342],
 [-4.567874401244395, -2.4079456086518722],
 [-5.0206856299497575, -2.4079456086518722],
 [-5.506572305368496, -2.406835114367845],
 [-5.8781358618009785, -2.419118909249997],
 [-3.101092789211817, -2.419118909249997],
 [-6.16581793425276, -2.372685720673535],
 [-5.4398809308698235, -2.3622289459215606],
 [-5.910806644090528, -2.3580978029243043],
 [-3.669469060594113, -2.4651040224918206]]
# ------------------------------
```

Recherche de cluster par apprentissage automatisé ([Kmean](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html): recherche des plus proches voisins)

```python
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# données (non étiquetées)

data = np.array(L)  

# Création et entraînement du modèle K-Means
kmeans = KMeans(n_clusters=3, random_state=50)  # 3 clusters
kmeans.fit(data)

# Récupération des résultats
labels = kmeans.labels_  # Les clusters attribués à chaque point
centroids = kmeans.cluster_centers_  # Les centres des clusters

# Visualisation des clusters
plt.scatter(data[:, 0], data[:, 1], c=labels, cmap='viridis', s=5, alpha=0.7)
plt.scatter(centroids[:, 0], centroids[:, 1], c='red', marker='X', s=200, label='Centroids')
plt.title("Clustering avec K-Means")
plt.xlabel('mass')
plt.ylabel('radius')
plt.legend()
plt.show()
```
{{< img src="../images/cluster3.png" caption="segmentation en 3 clusters" >}}

On peut alors vérifier la valeur donnée aux 3 étiquettes (classes)
, ainsi que le nombre d'items dans chaque classe:

```python
valeurs, comptes = np.unique(labels, return_counts=True)
valeurs,comptes
# Affichage --------------------
(array([0, 1, 2], dtype=int32), array([156, 381, 493]))
# ------------------------------
```

* classe **0**: couleur **violette** = les étoiles
* classe **1**: couleur **verte** = planètes telluriques
* classe **2**: couleur **jaune** = planète gazeuses

## Superposer les exoplanètes de TOI_270 et celles de la Terre

Selection des planètes TOI_270 ainsi que la Terre dans la table *dataset.csv:*



```python
names = ['TOI-270 d','TOI-270 b','TOI-270 c','earth']
df_p = df[df['_name'].isin(names)]
"""nuage de points df_p issu des observations
"""
x_p = np.log(df_p['mass'])
y_p = np.log(df_p['radius'])
z_p = df_p['_name']
```

Superposition des données de `df_p`:

```python
plt.clf()
axes = plt.gca()
# data et labels sont calculés plus haut 
plt.scatter(data[:, 0], data[:, 1], c=labels, cmap='viridis', s=5, alpha=0.7)
plt.scatter(x_p,y_p,color='red',marker='o')
for x0, y0, z0 in zip(x_p, y_p, z_p):
    axes.text(x0+0.4, y0*1.1, f"({z0})", fontsize=10)
plt.xlabel('mass')
plt.ylabel('radius')
plt.show()
```

{{< img src="../images/cluster4.png" caption="superposition des planètes du système TOI_270 et de la Terre" >}}

## Prévision des classes pour les planètes de TOI_270
### Prediction pour la planète Jupiter
* Documentation: La fonction [Kmeans](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html) du module `scikit-learn`

* En pratique:

```python
kmeans.predict([[0,0]])
# Affichage --------------------
array([2], dtype=int32)
# ------------------------------
```

**Jupiter** est de **classe 2** (cluster jaune)

### Planètes du tableau reduit `x_p, y_p`
```python
Liste = []
for i,j,k in zip(x_p,y_p,z_p):
    Liste.append((i,j,k))
Liste = np.array(Liste)
Liste
# Affichage --------------------
array([['-5.761407122499511', '-2.409803828596342', 'earth'],
       ['-5.115995809754082', '-2.1959753579357875', 'TOI-270 b'],
       ['-4.074541934925921', '-1.6607312068216509', 'TOI-270 d'],
       ['-3.872802292274865', '-1.5329399414613754', 'TOI-270 c']],
      dtype='<U32')
# ------------------------------
```

Prediction à partir des données:

```python
# reduction du tableau aux 2 colonnes masse et rayon
couples_xp_yp = Liste[:,:2]
# prediction
kmeans.predict(couples_xp_yp)
# Affichage --------------------
array([1, 1, 1, 1], dtype=int32)
# ------------------------------
```

Comme attendu d'après le graphique précedent, les 4 planètes du tableau `df_p` sont de **classe 1**. (cluster vert)



