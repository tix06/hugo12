---
Title: transformer image ascii
---

*Prérequis:*

* TP1 Ascii art: utiliser des symboles pour dessiner des formes: [Lien](../../fonctions/page51/)
* TP2 Lecture/ Ecriture dans un fichier: [Lien](../../ES/page54/)

# TP3 Projet ascii art: des pixels aux symboles ascii
On va remplacer dans une image la couleur d'un pixel par un caractère ascii dont le remplissage permettra de faire varier la clarté d'un zone de l'image.

Video explicative:

{{< img src="../images/video_ascii.png" link="https://www.youtube.com/watch?v=2U11986Ro9o" caption="lire la video" >}}

* Télécharger les [documents sources](../datas/src.zip) et décompresser l'archive. Trouver dans ce dossier les fichiers *Marylin-original.jpg* et le module *display_image*


* Ouvrir un fichier python dans le même dossier. Importer les modules suivants:

```python
from PIL import Image
from display_image import *
```

Votre code devra ensuite:

* Ouvrir en LECTURE le fichier image à traiter.
* redimensionner cette image de façon à ce qu'elle n'ait que 500 pixels de large/haut:

```python
with Image.open("Marylin-original.jpg") as image:
    image = image.resize((500,500))
```
* déterminer une série de caractères allant dans un ordre croissant d'opacité:
  * " " l'espace correspond à un pixel blanc
  * "@" peut être choisi comme le caractère le plus noir
  * choisir des caractères intermédiaires

```python
ascii_char = ' .:-=+....@'
```

* Ouvrir en ECRITURE le ficher de destination, celui dans lequel on écrira les symboles ascii:

```python
fileout = open("ascii_art.txt","w")
```

* Comme vu dans la video:
  * Parcourir les pixels de l'image à l'aide de 2 boucles `for`
  * Lire la couleur de chaque pixel: `rgb=image.getpixel((x,y))`
  * calculer la valeur en niveau de gris du pixel à partir de sa luminosité: `grey = (rgb[0]+rgb[1]+rgb[2])//3`
  * attribuer à chaque pixel un caractère: calculer l'indice correspondant dans la liste `ascii_char`: `index = grey * 9 // 255`
  * puis l'écrire dans une chaine de caractères: `line += ascii_char[index] + ' '`
  * mettre `'\n'` en fin de ligne et passer à la ligne suivante.

* Une fois la chaine de caractère terminée:
  * placer la chaine `line` dans le fichier *ascii_art.txt*: `fileout.write(line)`
  * fermer le fichier txt: `fileout.close()`

Voila, vous pouvez maintenant vérifier son contenu en l'ouvrant avec un editeur de texte, type bloc notes. Mais pour visualiser l'image représentée par ces caractères, il faudra ajouter les lignes suivantes à votre programme:


```python
image = textfile_to_image('ascii_art.txt')
image.show()
image.save('ascii_art.png')
```

# Liens et sources
* notebook du site [clogique](https://clogique.fr/nsi/notebook/?from=/nsi/premiere/td_tp/TP_Art_Ascii.ipynb#Exercice-7)
* [correction](../ascii_art_c) du Projet ascii-art