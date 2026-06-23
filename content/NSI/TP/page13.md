---
Title: Courbes de transit
description: exploration des dossiers et fichier avec le module os, analyse courbe de transit, moyenne glissante
weight: 82
---

# Etape 1: Courbe de transit
## Outil de navigation: explorateur Python
On souhaite créer un outil de navigation qui permettra de se deplacer dans l'arborescence des dossiers et fichiers. Cela permettra de selectionner le-s fichier-s à traiter depuis la console python, sans modifier le code du programme.

*Exemple*:

{{< img src="../images/demo.GIF" >}}

On pourra au choix:

* Utiliser, ou s'inspirer du fichier source suivant: [astep_2025_v0.py](/scripts/astro/astep_2025_v0.py)
* Programmer cette partie du programme de manière itérative (avec boucle while)
* Programmer cette partie à l'aide d'un algorithme récursif (niveau Term NSI)

Les fonctions python qui permettent de naviguer entre dossiers et fichiers font partie du module `os.path`, dont la documentation officielle est ici: [doc python](https://docs.python.org/3/library/os.path.html)

On utilisera principalement:

* `os.getcwd()`: str, le dossier courant
* `os.path.abspath()`: retourne le chemin absolu du dossier courant
* `os.chdir(d)`: change de dossier pour aller au dossier d
* `os.chdir('..')`: remonte d'un niveau
* `os.listdir()` ou `os.listdir(d)` : retourne la liste des fichiers et dossiers du dossier courant ou bien du dossier d
* `os.path.isdir(f)`: booléen True si `f` est un dossier
* `os.path.isfile(f)`: True si f est un fichier
* `f.endswith('.csv')`: True si l'extension de f est .csv

Ouvrir et executer le fichier avec un IDE python quelconque. Pour le tracé de graphiques, il est recommandé d'utiliser *IDLE (Python GUI)* de la distribution Winpython.

## Ouverture du fichier csv
Pour chacun des fichiers de données, ouvrir une nouvelle cellule du notebook et adapter le script suivant:

```python
import csv
table = []
with open('TIC323295479-01_20240617_ASTEP-ANTARCTICA_R_measurements.csv', 'r') as file:
    reader = csv.reader(file, delimiter=',')
    for row in reader:
        try:
            line_values = []
            for val in row:
                val = float(val)
                line_values.append(val)
        except:
            line_values = row
        table.append(line_values)

# test
table[:3]
"""
[['BJD', 'FLUX', 'ERRFLUX', 'AIRMASS', 'SKY'],
 [478.87701, 0.999509, 0.00222, 1.015, 218.0],
 [478.87718, 1.003059, 0.002213, 1.015, 219.0]]
"""
```

## Lissage de la courbe
Les données utiles occupent les colonnes 0 (BJD) et 1 (FLUX) de la table. Les valeurs de FLUX (nuage de points en gris) étant très *bruitées*, il conviendra de réaliser un lissage des points (**courbe rouge**):

{{< img src="../images/fit1.png" >}}

Le programme suivant réalise une moyenne glissante (**courbe rouge**): pour chaque indice i, on fait une moyenne du FLUX sur une fenêtre de 100 points, centrés sur l'indice i. `y[i-50:i+50]`

> Compléter la fonction [lissage](/docs/NSI/structure/page11/), ainsi que le script aux points (1), (2), (3):

```python
import matplotlib.pyplot as plt
from matplotlib.widgets import Cursor

def moyenne(signal):
    """fonction qui calcule la moyenne 
    sur les donnees de la liste signal
    """
    s = 0
    # à completer
    return s / b



def lissage(L,largeur):
    signal_filtre = L.copy()
    for i in range(largeur//2,len(L)-largeur//2):
        signal = L[...:...]
        # on fait un slice
        # signal est le petit tableau de dimension egale à largeur
        # dont on fait la moyenne glissante
        # puis on place cette valeur moyenne dans signal_filtre, au rang i
        signal_filtre[i] = moyenne(...)
    return signal_filtre

x = [] # colonne 0 de la table = BJD
y = [] # colonne 1 de la table = FLUX

# (1) import des valeurs de x et y à partir du fichier en ouverture

# (2) utilisation des fonction lissage

plt.clf()
axes = plt.gca()
plt.scatter(x,y,color='silver',marker='.',label='luminosité')
plt.grid(True,which='both')
plt.legend(loc='best')
plt.title('luminosité transit')

# (3) tracé de la courbe de lissage
plt.plot(...,..., color='red',label='moyenne glissante')
plt.grid(True,which='both')
plt.legend(loc='best')
cursor = Cursor(axes, useblit=True, color='red', linewidth=2)

plt.show()
```

<!--
```python
import matplotlib.pyplot as plt
from matplotlib.widgets import Cursor

def moyenne(signal):
    s = 0
    b = len(signal)
    for elem in signal:
        s += elem
    return s / b



def lissage(L,largeur):
    signal_filtre = L.copy()
    for i in range(largeur//2,len(L)-largeur//2):
        signal = L[i-largeur//2:i+largeur//2]
        # signal est le petit tableau de dimension largeur 
        # dont on fait la moyenne glissante
        # puis on stocke dans signal_filtre
        signal_filtre[i] = moyenne(signal)
    return signal_filtre

x = [] # colonne 0 de la table = BJD
y = [] # colonne 1 de la table = FLUX
for i in range(len(table[1:])-1):
    x.append(table[i+1][0])
    y.append(table[i+1][1])

fenetre_gli = 100
x_gli = x[fenetre_gli//2:-fenetre_gli//2]
signal_lissage = lissage(y,fenetre_gli)[fenetre_gli//2:-fenetre_gli//2]
# ouverture fenetre graphique qt
%matplotlib qt
# cursor non implémenté en inline sous jupyter notebook
 
plt.clf()
axes = plt.gca()
plt.scatter(x,y,color='silver',marker='.',label='luminosité')
plt.grid(True,which='both')
plt.legend(loc='best')
plt.title('luminosité transit')


plt.plot(x_gli,signal_lissage,color='red',label='moyenne glissante')
plt.grid(True,which='both')
plt.legend(loc='best')
cursor = Cursor(axes, useblit=True, color='red', linewidth=2)

plt.show()
```
-->

On peut alors utiliser les fonctions de la fenêtre graphique pour relever les coordonnées *à la main* des intersections des courbes:

{{< img src="../images/fit3.png" caption="option 1: le transit démarre au point A et termine au point B" >}}

{{< img src="../images/fit4.png" caption="option 2: le transit démarre au milieu du segment n°2 et termine au milieu du segment n°4" >}}

Avec l'*option 2*:

| planète | tau (h) | incertitude sur tau |delta | incertitude sur delta | 
|--- | --- | --- | --- | --- |
| `TOI 270-1` | `7.2` | à definir | `1-0.991` | à definir |

<!--
## Modélisation par segments (en option)
Un autre option pour lire les valeurs des intersections sur la courbe de FLUX est de réaliser une modélisation du nuage de points par segments:

{{< img src="../images/fit2.png" >}}

```python
# bornes des 4 parties de courbe
borne_inf_segment1 = 478.9
borne_sup_segment1 = 479.05

borne_inf_segment2 = 479.05
borne_sup_segment2 = 479.18

borne_inf_segment3 = 479.25
borne_sup_segment3 = 479.35

borne_inf_segment4 = 479.35
borne_sup_segment4 = 479.45

def recherche(L,val):
    i = 0
    while L[i]<val:
        i+=1
    return i

def fit_func(x,a,b):
    return a*x+b

def modelisation_segment(borne_inf,borne_sup,X,Y,fit_func,a,b):
    i0 = recherche(X,borne_inf)
    i1 = recherche(X,borne_sup)
    params, mcov =curve_fit(fit_func,X[i0:i1],Y[i0:i1])
    a = params[0]; b=params[1]
    for i in range(i0,i1):
        Y_fit[i] = fit_func(X[i],a,b)


x_gli = x[fenetre_gli//2:-fenetre_gli//2]
signal_lissage = lissage(y,fenetre_gli)[fenetre_gli//2:-fenetre_gli//2]
Y_fit = signal_lissage.copy()
modelisation_segment(borne_inf_segment1,borne_sup_segment1,x_gli,signal_lissage,fit_func,0,0)
modelisation_segment(borne_inf_segment2,borne_sup_segment2,x_gli,signal_lissage,fit_func,0,0)
modelisation_segment(borne_inf_segment3,borne_sup_segment3,x_gli,signal_lissage,fit_func,0,0)
modelisation_segment(borne_inf_segment4,borne_sup_segment4,x_gli,signal_lissage,fit_func,0,0)
#%%
# Revenir ici pour chaque tracé de Y_fit
plt.clf()
axes = plt.gca()
plt.scatter(x_gli,signal_lissage,color='silver',marker='.',label='luminosité')
plt.grid(True,which='both')
#plt.legend(loc='best')
#plt.title('moyenne glissante')


plt.plot(x_gli,Y_fit,color='red',label='courbe fit')
#plt.grid(True,which='both')
#plt.legend(loc='best')
cursor = Cursor(axes, useblit=True, color='red', linewidth=2)
# cursor non implémenté sous jupyter notebook
plt.show()
```
-->

# Suite
* Lien vers l'[etape 2](../page10/): Notebook python utilisé comme calculatrice.
* retour vers la page de présentation: [retour](../page9)