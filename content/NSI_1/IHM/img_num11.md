---
Title: TP images num version d'origine
description: TP img numeriques version d'origine
hidden: true
weight: 14
---

* creation d'images numeriques version 1: [Lien](../img_num1)
* creation d'images numeriques version 2: [Lien](../img_num11)
* traitement d'une image: detourage, filtre, incrustation: [Lien](../img_num2)
* tuto pour detourer une image avec Gimp: [Lien](/competences_num/images_num/page1)


# Traitement d'images numeriques en langage python
*Ce TP est une variante de celui proposé à l'adresse [suivante](../img_num1). Dans cette version, on n'utilisera pas de matrice pour placer les informations de couleur de l'image, ce qui rend le traitement plus direct, mais moins en lien avec le programme de 1ere NSI.*

## Version utilisant une manipulation plus poussée de la librairie PIL.image
Le module PIL permet de manipuler divers formats d'images plus ou moins complexes sans avoir à se préoccuper de la façon dont sont réellement codés ces formats.

PIL reconnait automatique la largeur et la hauteur en pixels de l’image, permet la création d’une grille de pixels,... 


{{< img src="../images/chats.bmp" link="../images/chats.bmp" caption="Image de chatons à télécharger" >}}

Voici le programme minimal pour lire les pixels de l'image

```python
from PIL import Image


imageSource=Image.open("chat.bmp")
largeur,hauteur=imageSource.size
planPixels=Image.new("RGB",(largeur,hauteur))
```

Les structures de données imageSource  et planPixels sont des objets qui stockent les couleurs des pixels dans un tableau. Ces objets possède les methodes `getpixel` et `putpixel` suivantes:

```
>>> imageSource.getpixel((x,y))
retourne un tuple constitué des couleurs (R, V, B) du pixel de coordonnée (x,y)
>>> planPixels.putpixel((x,y),p)
place le tuple p de valeurs (R,V,B) sur le pixel (x,y)
```

*Remarques*: 
* pour la fonction `putpixel`, la position (x,y) d'un pixel sur l'image varie de `(0,0)` à `(l-1,h-1)`, si `l` et `h` designent les dimensions de l'image.
* le tuple de couleurs p: imaginons que nous voulions placer un pixel bleu, alors: 

```python
p= (0, 0, 255)
planPixels.putpixel((x,y),p)
```


## Ecrire dans un nouveau fichier
Après lecture du fichier, on peut constituer une nouvelle image. Voici le programme complet que vous modifierez selon le traitement voulu:

```python
### traitement d'une image ##########
from PIL import Image


imageSource=Image.open("chats.bmp")
largeur,hauteur=imageSource.size
planPixels=Image.new("RGB",(largeur,hauteur))

for y in range(hauteur): # y varie de 0 à hauteur - 1
    for x in range(largeur): # x varie de 0 à largeur - 1
        p=imageSource.getpixel((x,y)) # p est la valeur RGB du pixel
        # la position d'un pixel sur l'image varie de (0,0) à (l-1,h-1)
        planPixels.putpixel((x,y),p) # nouvelle image identique a la precedente

planPixels.save("chatModif.jpg")
planPixels.show()
```

> Quelle opération doit on réaliser sur chacun des pixels pour que les chats regardent de l’autre côté ? Compléter le programme ci-dessus afin d'obtenir cette nouvelle image, avec des petits chats qui regardent à DROITE.

## Pix-Art
Avec l'image d'origine suivante:

{{< img src="../images/marylin_original.JPEG" link="../images/marylin_original.JPEG" caption="Marylin Monroe" >}}

> Apporter les modifications necessaires pour filtrer les couleurs par zone, de manière selective. On pourra obtenir une nouvelle oeuvre inspirée de l'image suivante:

{{< img src="../images/img4.jpg" caption="Marylin Monroe type Pop-art" >}}

*Aide:* La condition suivante permet de selectionner les pixels de la partie gauche de l'image, **et** qui ont une composante Rouge supérieure à 100:

```python
if (x<largeur//2 & p[0] > 100) :
	# traitement sur p
```
