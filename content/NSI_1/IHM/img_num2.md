---
Title: images numeriques 2
description: traitement d'une image matricielle, filtres, incrustations, detourage
hidden: true
weight: 15
---

* creation d'images numeriques version 1: [Lien](../img_num1)
* creation d'images numeriques version 2: [Lien](../img_num11)
* traitement d'une image: detourage, filtre, incrustation: [Lien](../img_num2)
* tuto pour detourer une image avec Gimp: [Lien](/competences_num/images_num/page1)


*Prérequis:* TP images numeriques ([partie1](../img_num1/))

*Chaque programme sera construit de la manière suivante:*

* import de la librairie PIL
* ouvrir l'image source avec `Image.open`
* relever hauteur et largeur de l'image source
* créer une nouvelle image vide avec `Image.new("RGB",(nouvelle_hauteur, nouvelle_largeur))`
* Créer un nouveau tableau de pixels à partir de l'image source
* Avec une boucle, pour chaque pixel, lire les pixels de l'image source: `p=imageSource.getpixel((x,y))`
* modifier la couleur `p` à l'aide d'un filtre
* Coller ces pixels dans la nouvelle image, selon la transformation voulue: `image_nouvelle.putpixel((x,y),p)`

```python
### copie d'une image ##########
from PIL import Image

imageSource=Image.open("image_d_origine.jpeg")
largeur,hauteur=imageSource.size
imageCopie=Image.new("RGB",(largeur,hauteur))

for y in range(hauteur): 
    for x in range(largeur): 
        p=imageSource.getpixel((x,y))
        # p est un tuple (p[0],p[1],p[2])
        # modification selective des valeurs de p 
        imageCopie.putpixel((x,y),p)

imageCopie.save("image_copie.jpeg")
imageCopie.show()
```


# Filtres appliqués à une image

Quand on applique un filtre vert à une image numérique, on parcourt l'image entière en recopiant pour chaque pixel sa composante verte, et en mettant le rouge et le bleu à 0. 

{{< img src="../images/naruto1.png" >}}

## Fonction filtreCouleur
Vous allez utiliser un IDE python (Spyder ou Pyzo) pour les exercices suivants.

> Adopter tout de suite les BONNES PRATIQUES:

> * pour chaque exercice, vous allez créer un NOUVEAU fichier python. Donnez lui un nom explicite, par exemple `naruto.py` pour le premier exercice
> * mettre tous les fichiers python et les images téléchargées ou générées par l'un des scripts python dans un même dossier, que vous nommerez `images_numeriques` 

ENONCE de l'exercice 1:

Créer une fonction `filtreCouleur` qui prend en argument un objet de type Image et un tuple (r, g, b) , où r, g, et b sont des booléens, et qui renvoie une nouvelle image pour lesquelles les couleurs RGB sont conservées si le booléen
correspondant est True . Par exemple, l'image de Naruto verte ci-dessus est obtenue par le code :

```python
naruto = Image.open("Naruto.png")
narutoGreen = filtreCouleur(naruto, (False, True, False))
narutoGreen.show()
```

Télécharger l'image d'origine: ![](../images/naruto.jpeg)

*Aide:*  Soit `R` un booléen. Alors `int(R)` vaut `1` si `R` vaut `True`, et `0` si `R` vaut `False`. 

Soient R, V, B trois variables de type `bool`, valant `True` ou `False`.

On peut appliquer le filtre sur la couleur `p` du pixel en faisant:

```python
p = (p[0]*int(R),p[1]*int(V),p[2]*int(B))
```

*Correction: (à venir)*

<!--
```python
def filtreCouleur(image,filtre):    
    (R,V,B) = filtre
    imageSource=Image.open(image)
    largeur,hauteur=imageSource.size
    image_verte=Image.new("RGB",(largeur,hauteur))
    
    for y in range(hauteur):
        for x in range(largeur):
            p=imageSource.getpixel((x,y)) # p est la valeur RGB du pixel
            if p[0]+p[1]+p[2] < 760:            
                p = (p[0]*int(R),p[1]*int(V),p[2]*int(B))
            else:
                p = (255,255,255)
            image_verte.putpixel((x,y),p) # nouvelle abscisse de 0 à h-1
    return image_verte       

narutoGreen = filtreCouleur("naruto.jpeg", (False, True, False))

narutoGreen.save("narutoGreen.jpg")
```
-->

Créer ainsi des images NarutoRouge.png , NarutoBleu.png , NarutoJaune.png , NarutoMagenta.png et NarutoCyan.png

## Assembler les personnages
ENONCE de l'exercice 2:

Créer maintenant un ruban d'images, comme sur l'image suivante: 

{{< img src="../images/naruto2.png" >}}


*Correction: (à venir)*
<!--
```python
def ruban_d_images(image):
    imageSource=Image.open(image)
    largeur,hauteur=imageSource.size
    image_ruban=Image.new("RGB",(largeur*4,hauteur))
    L = [(True,False,True),(False,True,False),(False,False,True),(True,True,True)]
    for i in range(4):
        image_filtre = filtreCouleur(image,L[i])
        for y in range(hauteur):
            for x in range(largeur):
                p=image_filtre.getpixel((x,y))
                image_ruban.putpixel((x+largeur*i,y),p)
    return image_ruban

image_ruban = ruban_d_images("naruto.jpeg")
image_ruban.show()
```
-->

# Incrustation d'image sur fond vert
[L'incrustation d'image](https://fr.wikipedia.org/wiki/Incrustation) sur un nouveau décors est largement utilisé dans le cinéma.

L'algorithme qui *fabrique* la nouvelle image parcourt les pixels de l'image d'origine (celle avec le fond vert). A partir d'un certain seuil, si la couleur du pixel est franchement verte, c'est le pixel du decors qui placé dans la nouvelle image.

ENONCE de l'exercice 3:

Utilisez les 2 images suivantes pour en créer une nouvelle, artificielle, en incrustant la première image dans la seconde.

{{< img src="../images/fond_vert.jpeg" caption="image issue du site www.event-picture.com" >}}



{{< img src="../images/apesanteur.jpeg" caption="une station spatiale" >}}

# Liens
* effets speciaux: [tpeeffetsspeciauxnumeriques.wordpress.com](https://tpeeffetsspeciauxnumeriques.wordpress.com/2016/12/08/lincrustation-sur-fond-vert-ou-fond-bleu/)
<!--
* remerciements à [www.zonensi.fr](https://www.zonensi.fr/NSI/Premiere/C04/ImagesBMP/ImagesBMP.pdf) pour l'idée du premier exercice
* et [labodemaths.fr](https://labodemaths.fr/WordPress3/nsi-fin-correction-tp-traitement-image/) pour l'idee du 2e exercice
-->

