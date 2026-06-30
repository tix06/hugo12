---
Title: loi de Mariotte
description: mesure dispositif, copie des valeurs depuis REPL et traitement python
weight: 23
---
# Loi de Mariotte - utilisation d'un dispositf à microcontrôleur


## Dispositif
La seringue est branchée sur le capteur de pression, lui-même relié au port grove PIN0 de la carte microbit.

La carte est branchée sur un port USB de l'ordinateur.

{{< img src="../images/pression_i1.png" >}}
L'écran LED de la carte microbit affichera la valeur de la tension sur *PIN0*. 

Grâce à sa liaison série sur le port USB, le logiciel *Mu* affichera les données mesurées au cours de l'acquisition sous un format: `[(volume1, tension1), (volume2, tension2), ...]`

## Editeur Mu
Lancer l'editeur *Mu*. Choisir au demarrage le mode *BBC microbit*.

Dans la fenêtre d'edition, coller le script suivant:

```python
from microbit import *

datas = []
v = 70

while True:

    if button_a.is_pressed(): 
        display.clear()
        lecture = pin0.read_analog()
        v = v -10
        display.scroll(lecture)
        datas.append((v,lecture))
        print(datas)
    elif button_b.is_pressed(): 
        datas = []
        v = 70
        display.scroll("RAZ")
    else: 
        display.show(Image.SQUARE)



```

> Questions: à partir de la lecture du script...

> 1. A quoi servent les 2 premières lignes sous l'*import* de la librairie *microbit*: `datas = []`, et `v = 70`?
2. Que se passe t-il lorsque l'on appuie sur le bouton **a** de la carte microbit?
3. Que se passe t-il lorsque l'on appuie sur le bouton **b**?
4. Comment faudrait-il adapter le script pour réaliser une mesure de pression pour des volumes décroissants d'air, de 5mL en 5mL?

## Téléversement du programme
Appuyer sur le bouton *FLASHER* pour téléverser le programme dans la carte microbit.

{{< img src="../images/pression_mu1.png" caption="bouton FLASHER" >}}
## REPL
Pour afficher les sorties textuelles de la carte microbit (`print()`), il faudra ouvrir l'interface avec le bouton REPL.

{{< img src="../images/pression_mu2.png" caption="bouton REPL" >}}
Pour démarrer le programme d'acquisition, appuyer sur le bouton de démarrage du programme au dos de la carte.

{{< img src="../images/pression_i3.png" caption="Bouton de (re)démarrage" >}}
Lors de l'appui sur le bouton **a**, une nouvelle mesure est enregistrée. la liste des valeurs acquises est alors affichée dans la fenêtre du logiciel.


Lors de l'appui sur le bouton **b**, la liste est remise à zero (recommencer l'acquisition).

## Mesurer
Enregistrer votre première valeur, pour un volume de 60mL: 

* appuyer sur le bouton **a**.

Pour enregistrer votre 2e valeur:

* maintenir la pression pour un volume de 50mL
* appuyer sur le bouton **a** 

Vous devriez voir à l'écran la liste `[(volume1, tension1), (volume2, tension2)]`. 

{{< img src="../images/pression_mu3.png" caption="affichage de la liste de mesures dans le REPL" >}}
Verifier que les volumes enregsitrés correspondent bien aux positions du piston lors de l'acquisition, sinon recommencer (bouton **b**).

## Copier les valeurs
A la fin de l'acquisition (volume de 30, ou 20 mL):

* Selectionner les valeurs directement dans la fenêtre du REPL. 

{{< img src="../images/pression_mu4.png" caption="selection dans le REPL" >}}
* Clic droit: *enregistrer*

{{< img src="../images/pression_mu5.png" caption="selection dans le REPL" >}}
# Traitement des données
## Graphique volume - tension
Se rendre sur l'application en ligne : [basthon.fr](https://basthon.fr)

Choisir *Notebook*

{{< img src="../images/pression_basthon1.png" >}}
Ecrire dans la cellule du notebook `datas = ` et coller les valeurs mesurées.

{{< img src="../images/pression_basthon2.png" >}}
A la suite, coller le script suivant:

```python
import matplotlib.pyplot as plt

volume = []
tension = []
inv_volume = []
pression = []

for mesure in datas:
    volume.append(mesure[0])
    tension.append(mesure[1])

plt.xlabel("Volume mL")
plt.ylabel("Tension")



# Plot
plt.plot(volume,tension,'o') # nuage de points de l'acquisition


# affichage
plt.show()
```

{{< img src="../images/pression_basthon3.png" >}}
**Executer la cellule** (Maj + Entrée) ou bonton triangle sur la barre de commande du logiciel.

> Quelle est l'allure de la courbe tension = f(volume)?

## Etude de l'evolution de la pression
Dans la boucle : `for mesure in datas:`, ajouter les instructions qui permettront de completer la liste `inv_volume`. On veut mettre dans cette liste `inv_volume` les valeurs calculées à partir de $1 / volume$

Comme les valeurs du volume sont mises dans `mersure[0]`cela donne dans le script python:

```python
for mesure in datas:
    volume.append(mesure[0])
    tension.append(mesure[1])
    inv_volume.append(1/mesure[0])
```

> Tracer alors le graphique tension = f(`inv_volume`). Que constatez-vous?

## Utiliser la fonction d'etalonnage
La tension du capteur correspond à une certaine valeur de pression. 

* A l'aide d'un manomètre, mesurer la pression atmosphérique **`Po`** en hPa
* Relever la valeur de tension donnée par le capteur à pression **`Uo`** 

La valeur de tension est exprimées en **unités**, un nombre compris entre 0 et 1023 (codage de la valeur en 10 bits).

Le coefficient de conversion *tension-pression* est donné à **8 hPa/unite**

Pour une *tension* **U** mesurée lors de l'experience (exprimé en **unités**, la *pression* **P** correspondante est donnée par:

$$P = Po + 8\times(U-Uo)$$



Utilisez cette relation d'etalonnage pour créer une nouvelle liste `pression` à partir de celle `tension`. Par exemple, avec Po=1000hPa, et Uo=190 *unités*:

```python
  pression.append(1000 + 8 * (mesure[1] - 190))
```

> Tracer alors le graphique pression = f(`inv_volume`). Que constatez-vous?

## Mise en evidence la loi de Mariotte
La loi de Mariotte s'énonce ainsi:

$$P \times V = Constante$$

Cette loi est-elle en accord avec la courbe obtenue?

# Prolongement: Modelisation
Adapter alors le script suivant pour obtenir la courbe modélisée $P = f(\tfrac{1}{V})$

*Cellule python 1*: équation de la courbe modélisée

```python
from scipy import stats
import numpy as np
inv_volume_np = np.asarray(inv_volume)
pression_np = np.asarray(pression)
a, b, r_value, p_value, std_err = stats.linregress(inv_volume, pression)
a, b, r_value
```

*Cellule python 2* créer une fonction de prédiction à partir du modèle

```python
def H(x,a,b):
    return a * x + b
```

*Cellule python 3* graphique avec courbe modélisée

```python
plt.clf()
plt.plot(inv_volume_np,pression_np,'o') # nuage de points de l'acquisition
plt.plot(inv_volume_np, H(inv_volume_np,a, b), c='r')
plt.show()
```




