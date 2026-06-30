---
Title: mesure de c du son
description: microcontroleur microbit avec extension ultrasons pour effectuer les mesures et traitement python
weight: 20
---

# TP : Mesure d'une durée de propagation d'ultra-sons
## Principe
On cherche à mesurer la durée de propagation des ultra-sons lors de leur reflexion sur un obstacle.

{{< img src="../images/E_R.png" alt="mesure de la duree de propagation des US" caption="Dispositif" >}}
Pour une distance d<sub>1</sub> entre le dispositif ultra-sons et l'écran, on relève la durée de propagation t (en micro secondes) sur la carte microbit.

Cette mesure est déclanchée par l'appui sur le bouton a de la carte microbit.

## Script
Commencer par uploader le script ci-dessous dans la carte microbit selon la méthode utilisant l'editeur Mu (flasher): [voir page présentation microbit](/docs/techno/pages/MB_init/#utiliser-l-editeur-mu)

{{< img src="/docs/techno/pages/images/helloworld.png" caption="Mu editor" >}}
```python
from microbit import *
from machine import time_pulse_us
import time, music, math

analogiq_in = [pin1]


def mesure_temps_A_R(broche = pin1):
    """Module Grove - Ultrasonic Ranger
    Retourne la durée d'un aller/retour des ultra_sons en microsecondes
    Paramètre : Nom de la broche utilisée
    """
    broche.write_digital(0)
    time.sleep_ms(2)
    broche.write_digital(1)
    time.sleep_ms(10)
    broche.write_digital(0)
    broche.read_digital()
    dt = time_pulse_us(broche, 1)
    return dt

while True:
  if button_a.is_pressed():
    dt = mesure_temps_A_R()
    display.scroll(dt)
``` 

## Brancher le dispositif à ultra-sons
Brancher l'emetteur-capteur à ultra-son sur la carte micro:bit. Choisir le port groove appelé PIN1 sur la carte.

Diriger l'emetteur-capteur à ultra-sons vers un support rigide, afin que les ondes ultrasonores se reflechissent et reviennent vers le recepteur.

{{< img src="" >}}
## Mesures
Une fois le script téléversé : 

Lorsque l'on appuie sur le bouton A, la fonction mesure_temps_A_R permet de communiquer avec l'emetteur-capteur à ultra-son. L'affichage de la durée de propagation pour un aller-retour s'affiche sur l'écran LED du microcontrôleur, chiffre après chiffre (`scroll`). La durée est en &micro;s.

<em>Exemple d'affichage d'une durée dt = 833&micro;s:</em>
En positionnant l'emetteur-capteur à environ 15 cm d'un support reflechissant, on lit : 

<img src="../images/mu_833.png">

En supposant que la célérité du son vaut 340m/s au moment de l'experience, cela donne une distance parcourue de $340 \times 833.10^{-6} = 0,28m$, double de la distance au support.

Cela semble cohérent. Mais il faudrait discuter de la précision attendue sur les 2 derniers digits mesurés par le dispositif...

# exploitation des mesures
* Répeter les mesures et relever la durée mise par les ultra-sons pour se reflechir sur un support rigide. Sur le cahier, consigner les données dans un tableau:

| distance parcourue (m) | 0 | 0.25 | 0.5 | 1.0 | ... |
|--- |--- |--- |--- |--- |--- |
| temps (s) | 0 | .. | .. | .. | .. |

* Ouvrir un editeur Python, comme par exemple **Pyzo**, et saisir le script ci-dessous. Enregistrer le programme dans vos *Documents* avec une extension `.py`, comme par exemple: `courbe.py`
* Modifier les valeurs dans les listes X et Y afin d'afficher la courbe de la distance parcourue en fonction du temps (Y = distance; X = temps).
* Relever alors l'équation de la courbe modélisée, déterminer la célérité des ondes **c**, ainsi que le coefficient de correlation.
* **QUESTIONS:** Dans le programme python ci-dessous, quelle partie du script correspond à:
    * l'import de librairie
    * la définition des listes X et Y
    * le traitement statistique des données
    * l'affichage du graphique

```python
import matplotlib.pyplot as plt

import numpy as np
from scipy.optimize import curve_fit
from matplotlib.widgets import Cursor

#--------------------------------------------------
#création des listes de variables utilisées dans le programme
#--------------------------------------------------

X=[0,1,2,3,4,5]
Y=[0.0,1.1,1.9,3.0,4.1,4.9]


#--------------------------------------------------
#partie modélisation
#--------------------------------------------------
#variables utilisées dans la modélisation polynomiale standard
a=0.9
b=0

#mise en place de l'outil curve fit (scipy)
def func(x,a,b):
    return a*x+b

X = np.asarray(X) # conversion des listes en matrices 
Y = np.asarray(Y) # pour pouvoir calculer a*X+b

y = func(X,a,b)

params, mcov =curve_fit(func,X,Y)
# params = coefficients retournés par le calcul de modélisation avec R2 minimal
# mcov = matrice de covariance, permet de quantifier la variation de chaque variable par rapport à chacune des autres
a = params[0]; b=params[1]

#--------------------------------------------------
#partie calcul de r2 coefficient de correlation
#--------------------------------------------------
residuals = Y- func(X, params[0],params[1])
ss_res = np.sum(residuals**2)
ss_tot = np.sum((Y-np.mean(Y))**2)
r_squared = 1 - (ss_res / ss_tot)
print(r_squared)

#-------------------------------------------------
#             partie graphique avec quadrillage
#-------------------------------------------------

# label et config des axes
plt.xlabel('X (s)')
plt.ylabel('Y (m)')

# Plot
plt.plot(X,Y,'o') # nuage de points de l'acquisition
plt.plot(X,func(X,a,b),'g',linewidth=1) # courbe modelisee
equation = "Y = "+str(round(a,3))+" * X + "+str(round(b,3)) + ", coef correlation r2 = " + str(round(r_squared,5))
plt.legend(["mesures","courbe modélisée"])
plt.title(equation)

# modifier les axes APRES avoir positionné les points si besoin de choisir l'echelle
axes = plt.gca()
cursor = Cursor(axes, useblit=True, color='red', linewidth=2)

# affichage
plt.show()
```


<!--
## Analyse du signal ultra-sons (oscilloscope)
* Modifier le script pour que la boucle `while` n'execute qu'une seule instruction : `dt = mesure_temps_A_R()`.
* Diriger alors les ondes emises par le circuit microbit vers un autre recepteur à US, lui même relié à un oscilloscope.
* Analyser le signal, et interpréter alors les instructions dans la fonction `mesure_temps_A_R`:


```python
    broche.write_digital(0)
    time.sleep_ms(2)
    broche.write_digital(1)
    time.sleep_ms(10)
``` 
-->

# Liens


* scénarisation du TP proposé par la DANE de Normandie : [voir ici (radar de recul)](https://numerique-sciences-informatiques.discip.ac-caen.fr/IMG/pdf/radar-de-recul.pdf)
* page principale avec telechargement de [micro_grove.py](https://numerique-sciences-informatiques.discip.ac-caen.fr/kit-grove-pour-micro-bit-et-applications-en-snt)
