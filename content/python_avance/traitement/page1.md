---
Title: graphique avec matplotlib
description: Tracé de graphiques avec curseur, contexte graphique
weight: 21
---

# Tracé de graphiques avec curseur
La documentation complète de `matplotlib.pyplot`: [Lien](https://matplotlib.org/stable/api/pyplot_summary.html)

**module**: D'abord importer le module:

```python
import matplotlib.pyplot as plt
```

**Curseur:** Ajouter *Cursor* si vous avez besoin de faire un relevé sur le graphique:

```python
from matplotlib.widgets import Cursor
```

**Script minimal**: voici un exemple de tracé de 2 courbes superposées:

* l'une de type nuage de points `scatter` (points non reliés)
* l'autre de type `plot` (points reliés entre eux)

```python
%matplotlib qt
plt.clf()
axes = plt.gca()
plt.scatter(x_gli,signal_lissage,color='silver',marker='.',label='luminosité')
#plt.grid(True,which='both')
#plt.legend(loc='best')
#plt.title('moyenne glissante')


plt.plot(x_gli,Y_fit,color='red',label='courbe fit')
#plt.grid(True,which='both')
#plt.legend(loc='best')
cursor = Cursor(axes, useblit=True, color='red', linewidth=2)
plt.show()
```

**lignes optionnelles:**

* `%matplotlib qt` va détacher le graphique du flux du notebook, et permettre d'utiliser le curseur (fenêtre graphique `qt`)
* La fonction `gca` permet de gérer les axes et curseur.
* La fonction `clf` permet d'effacer la figure courante et de remettre les réglages graphiques à zero.
* `grid` pour afficher une grille
* `legend` pour ajouter un encadré avec la légende (les labels)

{{< img src="../images/qt_graph.png" >}}


