---
Title: indice de similarité avec la Terre
hidden: true
weight: 25
---

# Etape 5: Indice de similarité avec la Terre
## Creation d'une table unique
### Import librairies

```pyhon
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.widgets import Cursor
```


### Import BDD
La base de données doit être téléchargée ici : [exoplanetes.db](/scripts/BDD/exoplanetes.db)

On prépare un [dataframe](/docs/NSI/projet/page10/) avec les données d'exoplanètes issues d'une BDD (TOUTES les exoplanètes):

```python
# Toutes exoplanetes / BDD
import sqlite3

try:
    conn = sqlite3.connect('exoplanetes.db')
    cur = conn.cursor()
    print("Base de données crée et correctement connectée à SQLite")

    sql = "SELECT sqlite_version();"
    cur.execute(sql)
    res = cur.fetchall()
    print("La version de SQLite est: ", res)
    


except sqlite3.Error as error:
    print("Erreur lors de la connexion à SQLite", error)
sql = "PRAGMA table_info(planetes_es);"
cur.execute(sql)
res = cur.fetchall()
L = [ligne[1] for ligne in res]
sql = "select * from planetes_es"
cur.execute(sql)
res = cur.fetchall()
dataset = pd.DataFrame(res,columns=L)
dataset
```

{{< img src="../images/exoplanetes_bdd.png" caption="table des exoplanetes" >}}

### Créer un dataframe avec les données de la Terre

```python
R_Jup = 71e6  # m
M_Jup = 1.898e27 # kg
M_earth = 5.9724e24
R_earth = 6378.137e3
M_sun = 1
R_sun = 1
planete1 = {
    '_name':'earth',
    'star':'Sun',
    'mass': M_earth/M_Jup,
    'radius': R_earth/R_Jup,
    'eccentricity': 0.0167,
    'orbital_period': 365.25,
    'semi_major_axis': 1,
    'M_star':M_sun,
    'R_star':R_sun

}
df2 = pd.DataFrame([planete1])
df2
```

### Créer un dataframe avec les exoplanètes du systeme TOI

Préparer un fichier *csv* ou *txt* avec tous les résultats de vos recherches sur les planètes *observées*. Ou {{< a link="/scripts/BDD/donnees_transit_planetes.txt" caption="Telecharger" >}} un exemple de fichier. Nommez le **`donnees_transit_planetes.txt`** pour la suite.

**Importer les données du fichier:**

```python
df = pd.read_csv('donnees_transit_planetes.txt',sep='\t')
df
```

*Les données du fichier sont importées avec la fonction `read_csv`:*

* *Le paramètre `sep` doit correspondre au caractère de séparation: `\t` pour un espace tabulation, sinon `,` ou `;` selon le logiciel tableur utilisé.*
* *`header` est un autre paramètre optionel, pour préciser le numero de ligne qui contient les en-tête de colonne*.


Les données des masses ont été ajoutées à partir du document suivant, converties en `M_J`:

{{< img src="../images/donnees_TOI.png" caption="données des masses pour les planetes de TOI" >}}


*Rappel: les masses des exoplanetes sont souvent exprimées en `M_J`, (en masses de Jupiter). Pour exprimer directement ces masses en `M_J`, cela va necessiter de realiser une conversion:*

$$mass = m \times M_{Terre} / M_J$$

*m: masse de l'exoplanete `TOI_x` dans le tableau precedent, exprimée en masses Terre*.

```python
# creation dataframe a partir du fichier
G = 6.67e-11
R_Jup = 71e6 # m
M_Jup = 6.9911e7 # kg
M_sol = 1.9885e30 # kg
R_sol = 696.342e6 # m

df['R_star']=df['star_radius']*R_sol # m
df['M_star']=df['star_mass']*M_sol # kg

df['tau']=(df['fin_transit']-df['debut_transit'])*24*3600 # s
df['delta']=1-df['lum_min'] # sans dim
df['R_p']= np.sqrt(df['delta']) * df['R_star'] # m
df['radius']=df['R_p']/R_Jup # en R_J
# vitesse planete : V_p = 2*R_star/tau
df['V_p']= 2*df['R_star']/df['tau']
# rayon orbital : r = G*M_star/V_p**2
df['r_orb']= G * df['M_star']/df['V_p']**2
# periode revolution: T = 2*np.pi*r/V_p
df['T'] = 2*np.pi*df['r_orb']/df['V_p']
df['orbital_period'] = df['T']/(24*3600) # en jours de 24h
df = df[['_name','radius','orbital_period','star_name','star_mass','star_radius']]
df
```



{{< img src="../images/df_TOI.png" caption="table des exoplanetes du systeme TOI" >}}

## Concatenation des 3 tableaux

```python
dataset = pd.concat([dataset,df2,df],ignore_index = True)
dataset
```

{{< img src="../images/exo_concat.png" caption="table toutes exoplenetes + earth" >}}

# Calcul du coefficient IST
Ajout d'une colonne IST, indice de similarité avec la Terre: voir methode de calcul [ici](https://www.wikiwand.com/fr/articles/Indice_de_similarité_avec_la_Terre)


```python
M_earth = float(dataset[dataset['_name']=='earth']['mass'])
R_earth = float(dataset[dataset['_name']=='earth']['radius'])
# definir un coefficient adimentionné pour l'IST
# et calculer pour toutes les planetes du tableau
dataset['IST'] = 1-abs(dataset['radius']-R_earth)/(dataset['radius']+R_earth)
# trier
dataset.sort_values('IST', ascending=False, inplace=True, ignore_index=True)
dataset = dataset[['_name','planet_status','mass','radius','orbital_period','semi_major_axis','eccentricity','IST']]
dataset[dataset['IST']>0]
```

*L'IST a été calculé sur la seule valeur du rayon de la planete*

{{< img src="../images/tab_IST.png" caption="liste ordonnée par IST decroissant" >}}

Le tri se fait avec l'instruction `dataset.sort_values('IST', ascending=False, inplace=True)`. On choisit de numéroter les lignes de dataset après le tri.

Puis rechercher dans cette table nos exoplanètes de TOI:

```python
dataset[dataset['_name'].str.startswith('TOI-270')]
```

Les extensions a-b-c sont celles des exoplanetes de la base de données. Celles avec 1-2-3 sont celles de notre étude. Ces 2 séries d'information se referent aux 3 mêmes exoplanètes.

{{< img src="../images/tab_TOI_IST.png" caption="Place des TOI dans la table" >}}

*On peut bien sûr ajouter d'autres caractéristiques des planetes pour le calcul de l'IST et les comparer à la Terre.*

> Sauvegardez votre dataframe dans un fichier .csv

Vous pourrez alors poursuivre vos traitements, sans avoir à executer tout le notebook.

```python
dataset.to_csv('dataset.csv', index=False)
```

* Lien vers l'[étape 6](../page5): Etude graphique


