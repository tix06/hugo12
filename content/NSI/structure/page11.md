---
Title: moyenne glissante
description: tableau statique pour effectuer une moyenne glissante
hidden: true
weight: 34
---

*Cet exercice fait suite au cours sur les [tableaux statiques](../page1)*

# Exercice: calculer une moyenne glissante
Les courbes de données issues du monde réel sont souvent *bruitées*. Pour simuler ce type de données, nous allons créer une liste de valeurs cumulées aléatoires.

{{< img src="../images/filtre.png" caption="courbes de données brutes et donnees filtrees" >}}

Pour créer et afficher ces valeurs cumulées, nous créons la liste `signal2` qui est produite à partir de valeurs aléatoires (`signal0`), puis cumulées dans `signal2`:

```python
import numpy as np
from numpy.random import randn
import matplotlib.pyplot as plt

plt.clf()
signal0 = (randn(800))*2
plt.plot(signal0,color='silver',label='Signal aleatoire')
plt.grid(True,which='both')
plt.legend(loc='best')
plt.title('Signal avec bruit')

signal2 = np.cumsum(randn(800))
plt.plot(signal2,color='red',label='Signal cumulé')
plt.grid(True,which='both')
plt.legend(loc='best')
plt.show()
```

**Etapes du traitement: Fonction `lissage`**

* On fait une copie par valeur de `signal2` (liste des valeurs d'origine) dans `signal_filtre` (liste dont les termes seront remplacés par la valeur moyennée):

```
signal_filtre = signal2.copy()
``` 

* On choisit une certaine largeur de liste pour les valeurs dont on fait la moyenne. Par exemple largeur = 10.

* Au rang i, dans la liste bruitée `signal2`: On prélève les valeurs entre les rangs $i- largeur//2$ et $i + largeur//2$ que l'on stocke dans un tableau STATIQUE appelé `signal`. Ce tableau conserve la même *taille* pendant tout l'exercice. (ici, largeur = 10):

```
signal = signal2[i-largeur//2:i+largeur//2]
``` 


* On calcule la moyenne de valeurs de `signal` avec la fonction `moyenne` vue dans l'exercice précédent.

{{< img src="../images/moyenne_gli.png" caption="moyenne sur l'ensemble des valeurs de `signal`" >}}


```
signal_filtre[i] = moyenne(signal)
```

* On place la valeur moyenne dans `signal_filtre[i]`

{{< img src="../images/moyenne_gli2.png" caption="signal filtre contient 10 valeur identiques contigües, il n'y a plus de bruit" >}}

* On répète l'opération pour tous les index `i` compris entre `largeur//2,len(signal2)-largeur//2)`:

```
for i in range(largeur//2,len(signal2)-largeur//2):
```

Puis on affiche les graphique de `signal2` (inchangé) et celle du signal après traitement (courbe lissée).

Nous allons suivre ces étapes:

**1.** Ecrire le script de la fonction `moyenne`


```python
def moyenne(signal):
    s = 0
    b = len(signal)
    for ... in ...:
        s += ...
    return s / b
```

**2.** Créer une fonction `lissage`, qui prend en paramètres une liste `L` et une largeur `v`, et retourne une liste de valeurs filtrées par une moyenne glissante sur `v` valeurs.

```python
def lissage(L,largeur):
    signal_filtre = L.copy()
    for i in range(largeur//2,len(L)-largeur//2):
        signal = L[i-largeur//2:...]
        # signal est le petit tableau de dimension largeur 
        # copié de L entre les indices i-largeur//2 et i+largeur//2
        # on fait la moyenne glissante de signal
        # puis on stocke dans signal_filtre
        signal_filtre[i] = moyenne(...)
    return ...
```

**3.** Placer les valeurs filtrées dans une liste `signal_apres_traitement`: `signal_apres_traitement = lissage(signal2,10)`

**4.** Afficher les 2 courbes, `signal2` et `signal_apres_traitement`

<!-- Correction
```python
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

signal_filtre = lissage(signal2,10)
``` 
-->

Voir [ici pour le tuto](/docs/python/pages/traitement/page1) sur le tracé de graphiques.
