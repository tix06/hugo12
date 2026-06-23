---
Title: sql et python
description: traitement sql et visualisation
weight: 25
---

# Etape 4: Base de données exoplanetes.db
## Principe
Nous allons utiliser un **script Python** pour nous connecter à la base de données `exoplanetes.db` et tester quelques requêtes en langage SQLite.

Nous utiliserons la librairie `sqlite3` de Python.

Il est conseillé d'utiliser l'IDE *Spyder*, ou bien *Jupyter Notebook* pour editer et interpréter les scripts écrits en Python.

La base de données doit être téléchargée ici : [exoplanetes.db](/scripts/BDD/exoplanetes.db)

{{< img src="../images/exoplanets.png" caption="extrait de la base de données" >}}

## Script de base

```python
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


cur.close()
conn.close()
print("La connexion SQLite est fermée")
``` 

Rappel: Le mécanisme `try ... except` est détaillé à la page [mise au point d'un programme Python](/docs/NSI/langages/page5/#gestion-des-exceptions-try-except)

Voici la traduction de ce script en langage naturel:

```python
essayer:
  connexion a la base de donnees exoplanetes.db
  creation d un curseur SQL
  Afficher ("Base de données cree et correctement connectee à SQLite")
  executer la requete SQL "SELECT sqlite_version();"
  affecter le resultat de la requête dans la variable res

si une erreur survient:
  Afficher ("La version de SQLite est: ", sqlite3.Error)

sinon:
  # autres requetes SQL

fermeture du curseur
fermeture de la connexion
Afficher ("La connexion SQLite est fermée")
```

## Explorer la base de données
* L'instruction suivante permet d'explorer la base de données:

`"PRAGMA table_info(planetes_es);"`

> **Q1.** Ajouter cette requête à votre script python pour afficher les attributs de la table `planetes_es` de la base de données `exoplanetes.db`

* Voici un extrait de la reponse à cette requête:

```
[(0, '_name', 'VARCHAR(38)', 1, None, 1), (1, 'planet_status', 'VARCHAR(9)', 1, None, 0), (2, 'mass', 'NUMERIC(19, 14)', 0, None, 0), (3, 'radius', 'NUMERIC(19, 14)', 0, None, 0), ...]
```

> **Q2.** Quel est l'attribut du nom des planetes de cette table?


> **Q3.** Ecrire une instruction en python qui affiche uniquement la liste des attributs. Mettre cette liste dans une liste nommée `L`

```
['_name',
 'planet_status',
 'mass',
 'radius',
 'orbital_period',
 'semi_major_axis',
 'eccentricity',
 'discovered',
 'detection_type',
 'molecules',
 'star_name',
 'star_distance',
 'star_mass',
 'star_radius',
 'star_sp_type',
 'star_age',
 'star_teff',
 'star_magnetic_field']
 ```

On peut **améliorer la présentation** des résultats, et mettre la table retournée dans un **dataframe**. On utilise alors la liste `L` des attributs (question précédente). Voir tuto [dataframe](/docs/NSI/projet/page10/)

```python
# Toutes les données relatives aux étoiles dont le nom commence par Kepler-89
import numpy as np
import pandas as pd
sql = "select * from planetes_es where _name like 'Kepler-89%'"
cur.execute(sql)
res = cur.fetchall()
df = pd.DataFrame(res,columns=L)
df
```

{{< img src="../images/exop_kepler.png" >}}

Et pour obtenir une *vue* avec certaines colonnes:

```python
sql = "select _name,mass,radius from planetes_es"
cur.execute(sql)
res = cur.fetchall()
df = pd.DataFrame(res,columns=['_name','mass','radius'])
df
```

{{< img src="../images/df1.png" >}}

On peut souhaiter éliminer les lignes pour lesquelles les renseignements ne sont pas complets (lignes avec `Nan`):

```python
df.dropna(how='any', inplace=True)
```

Et ajouter des colonnes au *dataframe*, comme par exemple le calcul de la masse volumique de la planète: *(attention, les valeurs de la table sont referencées à celles de Jupiter)*

```python
R_Jup = 71e6 
M_Jup = 1.898e27
df['rho']=df['mass']*M_Jup/(4/3*np.pi*(df['radius']*R_Jup)**3)
df
```

{{< img src="../images/df2.png" >}}


> **Q4.** Cette base est-elle bien modélisée, respecte t-elle bien les contraintes d'intégrité vues en cours? Pq?

> **Q5.** Tester quelques unes des requêtes sur cette base. Par exemple:

1. Toutes les données relatives à l'étoile *Kepler-89 b*
2. Tous les noms des planètes dont la masse est plus de 10 fois supérieure à celle de Jupiter (Indiquer quelles sont ces planètes dans l'extrait de la table)
3. Les planètes ainsi que le nom de l'étoile hôte, dont l'étoile est située à moins de 40 pc de la Terre.
4. Les noms des 20 étoiles les plus proches de la Terre où des planètes ont été détectées.
5. Nombre total de planètes dans la table `(utiliser COUNT(*))`
6. Nombre total d'étoiles dans la table (utiliser `COUNT(DISTINCT ... )`)
7. Table des planètes qui n'ont été détectées ni par "Radial Velocity", ni par "Primary Transit" 
8. Le nombre de planètes qui n'ont été détectées ni par "Radial Velocity", ni par "Primary Transit"
9. Moyenne des distances entre le Soleil et les différentes étoiles de la table (utiliser `AVG`). *Attention à ne compter qu'une seule fois chacune des étoiles.*
10. Table des planètes où le type de l'étoile est G ... (utiliser `LIKE "G%"`)
11. Nom des planètes et distances au soleil, où de l'eau a été détectée (utiliser `LIKE`)

# Etude graphique
La recherche de dépendances entre grandeurs se fera en traçant un graphique, avec différents essais pour les axes x,y: On peut chercher par exemple la *dépendance* masse volumique <-> rayon:

```python
%matplotlib qt
plt.clf()
axes = plt.gca()
x = df['radius']
y = df['rho']
z = df['_name']
plt.scatter(x,y,color='silver',marker='.',label='Rho')

# ajout d'une etiquette
for x, y, z in zip(x, y, z):
    axes.text(x, y, f"({z})", fontsize=8)
cursor = Cursor(axes, useblit=True, color='red', linewidth=2)
plt.show()
```

{{< img src="../images/df3.png" >}}

## Superposer les données des exoplanètes découvertes par TOI-270 avec la BDD
Commencer par selectionner et nettoyer les données issues de la base de données:

```python
# BDD - Toutes exoplanetes
sql = "PRAGMA table_info(planetes_es);"
cur.execute(sql)
res = cur.fetchall()
L = [ligne[1] for ligne in res]
sql = "select * from planetes_es"
cur.execute(sql)
res = cur.fetchall()
df0 = pd.DataFrame(res,columns=L) # table entiere
df0 = df0[['_name','orbital_period','radius']] # projection sur les colonnes utiles
df0.dropna(how='any', inplace=True) # retirer les lignes avec datas non renseignées
df0
```

{{< img src="../images/df14.png" >}}

**importer et traiter les données issues des observations**
Cette partie est détaillée à la page [données en dataframe](/docs/NSI/projet/page10/)

```python
df = pd.read_csv('donnees_planetes.txt',sep=';')
G = 6.67e-11
R_Jup = 71e6 
M_Jup = 6.9911e7
df['tau']=(df['fin_transit']-df['debut_transit'])*24*3600
df['delta']=1-df['lum_min']

df['M_star']=7.158780e+29
df['R_star']=257512600.0
df['R_p']= np.sqrt(df['delta']) * df['R_star']
df['radius']=df['R_p']/R_Jup
# vitesse planete : V_p = 2*R_star/tau
df['V_p']= 2*df['R_star']/df['tau']
# rayon orbital : r = G*M_star/V_p**2
df['r_orb']= G * df['M_star']/df['V_p']**2
# periode revolution: T = 2*np.pi*r/V_p
df['T'] = 2*np.pi*df['r_orb']/df['V_p']
df['T_jours'] = df['T']/(24*3600)
df
```

{{< img src="../images/df16.png" >}}

**Tracer les 2 nuages de points**

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
plt.xlabel('radius')
plt.ylabel('orbital_period')
cursor = Cursor(axes, useblit=True, color='red', linewidth=2)
plt.show()
```

{{< img src="../images/exemple_graphique.png" caption="orbital_period vs radius en echelle log" >}}

## Partager la fenêtre graphique en plusieurs graphiques

> Travail: le script ci-dessous permet de visualiser plusieurs graphiques sur la même sortie. Adapter le script pour sélectionner les grandeurs correlées. 

```python
plt.figure(figsize=(12, 8))
plt.subplot(221)

x = 'semi_major_axis'
y = 'orbital_period'
plt.scatter(dataset[x],dataset[y], marker="o", s=25)
plt.xlabel(x)
plt.ylabel(y)
#plt.xscale('log')
#plt.yscale('log')
plt.xticks(())
plt.yticks(())
#plt.legend(loc="best")


plt.subplot(224)
x = 'semi_major_axis'
y = 'orbital_period'
plt.scatter(dataset[x],dataset[y], marker="o", s=25)
plt.xlabel(x)
plt.ylabel(y)
#plt.xscale('log')
#plt.yscale('log')
plt.xticks(())
plt.yticks(())



plt.subplot(222)
x = 'semi_major_axis'
y = 'orbital_period'
plt.scatter(dataset[x],dataset[y], marker="o", s=25)
plt.xlabel(x)
plt.ylabel(y)
#plt.xscale('log')
#plt.yscale('log')
plt.xticks(())
plt.yticks(())

plt.subplot(223)
x = 'semi_major_axis'
y = 'orbital_period'
plt.scatter(dataset[x],dataset[y], marker="o", s=25)
plt.xlabel(x)
plt.ylabel(y)
#plt.xscale('log')
#plt.yscale('log')
plt.xticks(())
plt.yticks(())


plt.show()
```

{{< img src="../images/seaborn1.png" >}}

# Et maintenant...
* Vous savez placer les nouvelles exoplanètes sur un graphique en nuage de points, au milieu des autres planètes de la base de données.
* Vous savez sélectionner la représentation qui donnera le plus d'informations:

{{< img src="../images/seaborn3.png" caption="exemple de représentations à partir de différents choix d'axes" >}}

Une voie d'étude serait de rechercher des *clusters* (regroupements) de planètes pour certains choix d'axes, et d'associer nos exoplanètes à celles-ci.

Une autre voie possible serait d'intégrer la Terre, avec toutes ses caractéristiques connues, dans la table de la base de données. On établirait alors un coefficient, appelé Indice de Similarité avec la Terre (IST), qui permettrait de trier ces planètes selon l'IST décroissant: [Lien vers l'étape 5](../page4)


