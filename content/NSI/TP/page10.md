---
Title: dataframes
description: calcul des caracteristique de l'exoplanete
weight: 83
---



# Traitement de données d'observation en astrophysique
## Importer les données et librairies utiles

> Dans une cellule d'un *notebook*, copier-coller les lignes suivantes:

```python
import numpy as np
import pandas as pd
# Constantes solaires 
Rsol = 6.9598e8               # rayon solaire en m
rhosol = 1408                 # densite solaire kg/m3
Msol = 1.98855e30             # masses solaire en kg

# Mercure, Jupiter (SI)
V_merc = 47                   # km/s
R_Jup = 71e6                  # m
# Constantes terrestres
MEarth = 5.9736e24             # masses de la terre en kg
REarth = 6.371e6               # rayon de la terre en m
rhoEarth = 5514.               # densité de la terre  kg/m3
  
# Changements d'unité
onemasinrad = np.pi/180./3600000. # 1 mas in radian     
kparsec = 3.08567758e19           # 1 kpc en m
parsec = 3.08567758e16            # 1 pc en m

# Constantes physiques
G = 6.67e-11                   # m3 kg−1 s−2
UA = 149597870700              # m
```

## Planète TOI 270-01

> Utilisez le *notebook* pour placer les valeurs de *delta* et *tau* mesurées sur la [courbe de transit](../page13)

Pour la planète TOI 270-01 du système TOI 270, (*valeurs à vérifier sur la [courbe de transit](../page13)*):

```python
# Données de l'etoile 
R_star = Rsol * 0.37
M_star = Msol * 0.36
# Observables sur la courbe de transit
delta = 0.0044 # sans unité
tau = 4600     # s
```



### Rayon planete a partir de delta
$$R_p = R_{star}\times \sqrt{delta}$$

La racine carrée est une fonction de la librairie `numpy`, avec `numpy.sqrt`
Le résultat du calcul peut nécessiter l'écriture d'un format particulier pour faciliter la lecture:

> Utilisez le *notebook* pour calculer le rayon de la planète observée:

```python
## Calcul du rayon planétaire    
Rp = np.sqrt(delta) * R_star
print("Rp = {:.3e} m.".format(Rp))    
print("Rp = {:5.3f} REarth.".format(Rp/REarth)) 
# ---- affichage console --- #
Rp = 1.708e+07 m.
Rp = 2.681 REarth. 
```

### Vitesse exoplanète Vp
$$V_p = \tfrac{2 \times R_{star}}{\tau}$$

On peut vérifier que l'on obtient:

```python
# ---- affichage console --- #
Vp = 1.120e+05 m/s.
Vp = 2382.170 V_merc.
```

### Rayon orbite planete
$$r = \tfrac{G \times M_star}{V_p^2}$$

### Periode revolution
$$T = \tfrac{2\pi \times r}{V_p}$$

*Format numérique*:

Une fois que l'on obtient T, en secondes, il peut être utile de représenter cette valeur en jours, heures, min, s:

```python
jours = T//(3600*24)
h = (T-jours*24*3600)//3600
m = (T-jours*24*3600-h*3600)//60
s = T-jours*24*3600-h*3600-m*60
print("{:3.0f} j, {:3.0f} h, {:3.0f} min {:3.2f} s".format(jours,h,m,s))
# ---- affichage console --- #
2 j,  11 h,  22 min 43.12 s
```

> Faire ces mêmes calculs pour chaque planète observable.


# Synthèse des résultats: fichier csv
Les fichiers *csv* sont interopérables: on peut les editer avec un editeur de texte, ou un tableur. On peut les importer facilement pour un traitement en langage *python*.

## Utiliser un tableur

* Les [courbes de transit](../page13) ont permis de mesurer les valeurs de profondeur de transit $\delta$ et de durée de transit $\tau$. 
* Ces valeurs seront reportées dans un fichier *csv* avec les autres informations sur les planètes et leur étoile. Utiliser un tableur. *Attention à bien utiliser des points comme séparateur décimal*.

{{< img src="../images/tab_excel.png" caption="tableau rempli à l'aide d'un tableur" >}}

* **Exporter** (ou enregistrer) en format *csv*.

On peut vérifier en ouvrant le fichier *csv* que les données sont mises dans un format particulier (séparation à l'aide d'un point virgule...)
{{< img src="../images/tab_csv.png" caption="fichier csv" >}}

## Import dans le notebook python
* L'import avec la librairie **pandas** se fait de la manière suivante: *(rien de plus simple)*

```python
df = pd.read_csv('exoplanetes.csv',sep=';')
df
```

{{< img src="../images/df5.png" >}}

# Suite 
> La [suite (étape 3)](../page12) va demander un apprentissage d'une nouvelle structure de données: le *dataframe*. Cela représente plusieurs avantages:

* la visualisation des données en table dans un notebook python,
* la manipulation des données (creation de nouvelles colonnes calculées, projection, selection, ...) qui est similaire au travail déjà vu sur les tables (SQL). Le langage diffère, mais l'esprit est le même.
* L'utilisation des librairies de traitement de données est facilitée (seaborn, ...)

[retour vers la page de présentation](../page9)