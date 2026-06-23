---
Title: regression lineaire
description: regression, modelisation avec scipy.optimize
weight: 24
---

# Regression linéaire
## Principe
La regression linéaire consiste à déterminer une fonction `y = a.x + b` dans un nuage de points `(x,y)`, à condition que ceux-ci semblent suffisament alignés. Cette fonction permettra alors de faire des prédictions sur la valeur `y` selon celle de `x`.

## Exemple de données brutes
Commencer par importer les données de l'exemple 1: [datas.csv](/scripts/regression/datas.csv)

Placer le fichier dans le même dossier que votre fichier de travail, que vous appelerez `regression.py`



```python
import csv
table = []
with open('fichier.csv', 'r') as file:
    reader = csv.reader(file, delimiter=',')
    for row in reader:
        table.append(row)
```

Vérifier la nature des données importées en affichant les premières lignes: 

```python
>>> table[:10]
```

Dans ce premier exemple, nous allons travailler sur une partie des données. Celles-ci ne contiennent que des informations numériques. On limite le traitement aux 90 premieres valeurs:

```python
x = []
y = []
for i in range(90):
    x.append(float(table[i][0]))
    y.append(float(table[i][1]))
```

Voir maintenant l'allure en traçant le graphique (x,y): ([méthode vue ici](/docs/python/pages/traitement/page1/))

```python
import matplotlib.pyplot as plt
plt.clf()
axes = plt.gca()
plt.scatter(x,y,color='silver',marker='.',label='Signal brut')
plt.grid(True,which='both')
plt.xlim(0,100)
plt.ylim(0,5)
plt.legend(loc='best')
plt.title('Signal avec bruit')
plt.show()
```

**Questions:** Les points présentent-ils un certain alignement? Sur quelle-s partie-s de la courbe bruitée?


## Mettre en place la regression linéaire
On commence par definir le modèle mathématique. Ici, celui d'une application affine.

```python
def fit_func(x,a,b):
    return a*x+b
```

La regression linéaire consiste à calculer les valeurs des coefficient `a` et `b`. C'est l'outil  `scipy_optimize.curve_fit` qui va ajuster les coefficients de regression, sur le nuage de points selectionnés.

```
from scipy.optimize import curve_fit
# placer des valeurs dans les coefficients a et b
a = 0
b = 0
borne_inf = ??
borne_sup = ??
# calculer les parametres
params, mcov =curve_fit(fit_func,x[borne_inf:borne_sup],y[borne_inf:borne_sup])
a = params[0]; b=params[1]
```

Pour que l'exemple fonctionne, il faudra placer des valeurs pour les bornes inferieures et superieures, par exemple:

```python
borne_inf = 0
borne_sup = 90
```

Une fois que le programme a calculé ces coefficients, remplir une liste `Y_fit` avec les valeurs de regression. On utilise bien sûr la fonction du modèle, `fit_func`:

```
Y_fit=[]
for i in range(borne_inf,borne_sup):
    Y_fit.append(fit_func(x[i],a,b))
```

Il reste à verifier la qualité de la regression en affichant:

* le nuage de points (x,y)
* la courbe modélisée (x[borne_inf:borne_sup],Y_fit)

```python
plt.clf()
axes = plt.gca()
plt.scatter(x,y,color='silver',marker='.',label='Signal brut')
plt.grid(True,which='both')
plt.xlim(0,100)
plt.ylim(0,5)
plt.legend(loc='best')
plt.title('Signal avec bruit')
plt.plot(x[borne_inf:borne_sup],Y_fit,color='red',label='courbe fit')
plt.show()
```

# Application
On va appliquer le traitement sur une autre partie du nuage de points. Les données simulent le cours d'un actif numérique sur plusieurs jours:

* x: numéro du jour, sur plus d'une année (500 jours?)
* y: valeur de l'actif en dollards

> Utiliser le même fichier [datas.csv](/scripts/regression/datas.csv), que vous allez cette fois exploiter en entier.

La valeur montre des fluctuations quotidiennes, mais aussi un premier maximum obtenu après 90 jours. Il s'agit de ce que l'on nomme un ATH, ou "All time high", qui désigne le pic historique d'un actif financier.

{{< img src="../images/ath.png" caption="exemple de courbe montrant plusieurs ATH - www.blog.bim.finance" >}}

La fin du relevé montre une nouvelle tendance haussière. C'est sur cette dernière partie du nuage de points que vous allez faire une regression linéaire.

> Utiliser la courbe de regression linéaire pour faire une prediction: quel sera le jour où la valeur de l'actif sera le même que lors de son précédent ATH?


