---
Title: images et formes
hidden: true
---

# Traitement d'images
Le [traitement d'images](https://fr.wikipedia.org/wiki/Traitement_d%27images) est un domaine très riche en algorithmes. Ici, nous nous intérèsserons à la **detection de formes** dans une image par des procédés de [morphologie mathématique](https://fr.wikipedia.org/wiki/Morphologie_math%C3%A9matique).

## La morphologie mathématique
Lien [wikipedia](https://fr.wikipedia.org/wiki/Morphologie_math%C3%A9matique)

On cherche à extraire des informations d'une image initiale. On va utiliser les opérateurs fournis par une librairie de morphologie mathématique à la manière de « briques logicielles », en les combinant et en les enchaînant.

Il est fortement recommandé de procéder aux transformations proposées ci-dessous en utilisant le logiciel [ImageJ](https://imagej.net/ij/index.html). Cela permet d'observer dans un premier temps les effets de chaque transformation et d'etablir une procédure de traitement.

Ces techniques sont la base des systèmes de [vision industrielle](https://fr.wikipedia.org/wiki/Traitement_d%27images).

{{< img src = "../images/imageJ.png" caption = "menus de ImageJ" >}}

L'image test sera celle-ci:

{{< img src = "../images/essai_23_04_04_bis.bmp" caption = "observation au microscope" >}}

Pour commencer, il sera necessaire de réaliser une première opération:

* une binarisation de l'image à partir d'un seuil (Binary > Make Binary)

{{< img src = "../images/img_bin.jpg" caption = "image binarisée" >}}

Le fond de l'image présente des bruits qu'il faudra effacer. Les opérations de morphologie démarrent le plus souvent par:

* une dilatation des formes pleines, ce qui aura pour effet d'absorber les bruits.
* une erosion morphologique pour que les gros éléments reprennent leur forme d'origine.

*L'ordre de ces opérations peut être inversé*.

Les particules présentent des formes connexes complètement incluses. Une opération possible en traitement par morphologie mathématique est le remplissage de formes (Binary > Fill Holes)

{{< img src = "../images/form_fill.png" caption = "principe du remplissage de formes (issu de wikipedia)" >}}

Un dernier problème à résoudre est l'aspect *"collé"* des particules au contact. Il faudra les séparer pour les résoudre et appliquer les traitements statistiques à venir.

* On peut réaliser une segmentation (partition de l'image en ensembles connexes homogènes). 

{{< img src = "../images/watersh.png" caption = "image segmentée: Binary: Watershed" >}}

On peut alors passer à une detection de contour, calculer sur les formes, ...

Pour certains problèmes, seule la position des centres des particules est voulue. La fonction calcule pour chaque pixel son éloignement au bord. Les pixels de valeur maximale sont candidats pour être le centre de la forme.

{{< img src = "../images/img_dist.jpg" caption = "calcul de la distance au bord: Binary > Distance Map" >}}

## Traitement en Python
Pour automatiser ces traitements, nous utiliserons la librairie de traitement d'images:

* [scikit-images: Documentation officielle](https://scikit-image.org/docs/dev/user_guide/install.html)
* [scikit-images: nombreux exemples](https://scikit-image.org/docs/stable/auto_examples/)

A partir d'une [image](../images/essai_23_04_04_bis.bmp) prise au microscope, nous allons chercher à obtenir les contours des billes. Il faudra au préalable obtenir une image *binarisée*. 

Voici un scipt minimal d'ouverture de l'image suivi de sa binarisation:

```python
import matplotlib.pyplot as plt
from skimage import io
from skimage.morphology import binary_dilation,binary_erosion,disk
import numpy as np


fichier_image = "oblates/essai_23_04_04_bis.bmp"
img = io.imread(fichier_image,as_gray=True)
img = np.array(img, dtype=np.float64)/255.

# binariser
img_bin = (img < 0.7) * 1
# dilater + eroder
img_result = binary_erosion(binary_dilation(img_bin,footprint=disk(1)),footprint=disk(1))

# afficher l'image
f,ax = plt.subplots()
ax.imshow(img_result)
plt.show()

```


Puis, à partir de cette image *binaire*, approximer la forme de ces billes, soit par des polygones, soit par des ellipses. 

Cette approximation va permettre de faire des mesures sur ces formes, et peut être de présenter ces mesures à l'aide d'un histogramme.



{{< img src = "../images/img_bin_poly.png" caption = "approximation par un polygone" >}}

{{< img src = "../images/img_ellipse.png" caption = "approximation par une ellipse" >}}

{{< img src = "../images/axes_ratio.png" caption = "histogramme sur les rapports rx/ry des axes des ellipses" >}}
