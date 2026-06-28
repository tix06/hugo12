---
Title: images numeriques SNT
description: image matricielle, resolution, definition
hidden: true
weight: 12
---


# Images numeriques
{{% badge color="red" icon="angle-double-up" %}}modelisation{{% /badge %}}

## Images matricielles
Retour sur l'activité *cartes numériques*

{{< img src="../images/zoom1.png" >}}

La profondeur de zoom maximale est donnée pour le fond de carte n°21. (On peut agrandir l'image 21 fois). 

A partir de cette dernière image, l'agrandissement ne va pas donner plus de details. En s'approchant de l'écran, on voit que la limite de résolution est donnée par la résolution de l'écran. 

{{< img src="../images/zoom.GIF" >}}
Les plus petits détails de l'image sont ses *pixels* : des petits carrés remplis chacun avec une seule couleur. Il s'agit d'une image **matricielle**.


### codage de l'image dans un fichier
Coder les pixels de l'image revient à coder les couleurs de ses pixels.
Les valeurs des couleurs des pixels sont alors mises les unes à la suite des autres, et constituent ainsi le fichier image en s'ajoutant aux métadonnées.

```
P1
6 5
0 1 1 1 0
0 0 0 0 1
...
```

Grâce aux métadonnées du fichier, les informations de format (P1, P2, ...) et de dimension (5 * 6), l'ordinateur va traiter cette suite de chiffres pour former une image à l'écran.

### Profondeur de couleur
**Noir et Blanc**

On peut supposer que l'image précédente est en noir et blanc, chaque information de couleur étant codée sur 1 seul bit (valeur 0 ou 1).

**Niveaux de gris**

le tableau suivant représente des valeurs allant du plus foncé au plus clair:

```
# fichier
P2
3 2
0 50 100 150 200 255
```

Les valeurs sont codées sur 1 octet (val 0-255). Il y a un octet par pixel.

**Couleur 24 bits**

Le codage des couleurs utilise la synthèse additive. Voir animation sur Algorea > SNT V2 > photographie numerique > [ambiance lumineuse](https://parcours.algorea.org/contents/4707-4702-1067253748629066205-1625996270397195025-1089626022569595539/)

```
# fichier
P3
3 2
255 0 0 0 255 0 0 0 255 
255 255 255 255 0 0 0 255 0
```

Les valeurs sont codées sur 3 octets (R V B de valeurs 0-255 0-255 0-255). Il y a 3 octets par pixels. 

## Images vectorielles
une [image vectorielle](https://fr.wikipedia.org/wiki/Image_vectorielle) est une image numérique composée de plusieurs objets géométriques individuels (droites, polygones, arcs de cercle). Ainsi, sur les cartes numériques, on utilise le plus possible d'éléments vectoriels, ajoutés comme des calques sur le fond de carte. (routes, ... tout ce qui est rectiligne ou courbe).

La résolution d'une image vectorielle est toujours d'excellente qualité, quelle que soit l'agrandissement voulu. Cependant, ces images ne peuvent pas être utilisées pour numériser des documents.

# Qualité des images





La **définition**  D d'une  image  est  définie  par  un  nombre  de  pixels  selon la longueur et la largeur de l’image  numérique. C'est une caractéristique propre de l'image.

On l'exprime le plus souvent en donnant les dimensions du plan de pixels, par exemple, une image de définition : 

$$1900 \times 1700~pixels$$

La  **résolution**  R d'une  image  numérique  correspond  à sa **densité** en points (pixels).  On mesure la densité de pixels sur l'écran en pixels par pouce (ppi) et la densité de points sur l'image imprimée en points par pouce (dpi). Ce n'est pas une caractéristique de l'image elle-même, mais de sa restitution par un écran (ou imprimé).

Selon le cas, on calculera la résolution selon l'un des côtés de l'image. Ou bien selon la diagonale de l'iamge.

La résolution peut s'exprimer en pixels par pouce. On peut en déduire la résolution en pixels par cm à l'aide de la relation suivante 

entre la **Définition** D, la **Résolution** R, et le nombre de cm par pouces (2,54).

$$R(px/cm) = \tfrac{R(px/pouce)}{2,54(cm/pouce)}$$

En effet : *1 pouce vaut 2,54 cm*. Un petit calcul montre que R = 72 ppi correspond à 28,3 pixels pour 1 cm.



*Exemple :* Soit une image de définition 800x533 que l'on imprime sur du papier photo de taille 15x10 (en cm), calculez la résolution de cette image en ppp.

*Réponse : On prendra :*

*Définition : D = 800px et Longueur : L = 15 cm*. *On cherche R : resolution*
$$R = \tfrac{D}{L}\times 2,54 = \tfrac{800}{15}\times 2,54 = 135 ppp$$