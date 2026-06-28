---
title : meta-données EXIF
description: TP extraction de donnees EXIF avec python PIL puis geolocalisation et affichage d'un marqueur
titleHidden: true
hidden: true
weight: 21
---

# Qu'est ce qu'une photographie numérique ?
Une photographie numérique, comme tout autre objet numérique, c'est un **fichier de données numériques**, c'est à dire des valeurs codées en binaire.

Une partie des données correspond à des métadonnées, c'est à dire des données *périphériques*. L'autre partie contient les données relatives à l'image.

## métadonnées
Ce sont des informations relatives à la capture de l'image, qui sont incorporées au fichier d’image lui-même. Ce sont les données EXIF.

Ces métadonnées couvrent un large éventail de données, comme par exemple **l'information de la date et de l’heure** de la prise de vue. <br>Les appareils numériques enregistrent la date et l’heure de la prise de vue et l’insèrent dans les données de la photo;

Ce sont aussi **des réglages de l’appareil**. Cela comprend des informations statiques telles que la marque et le modèle de l’appareil et des informations variables telles que l’orientation, l’ouverture, la vitesse d’obturation, la longueur de focale, la sensibilité…

**Des informations géographiques** provenant d’un éventuel système GPS connecté à l’appareil. 

*En résumé:*

* la marque et le type d'appareil photographique
* la lentille de l'objectif
* les réglages lors de la prise de vue
* la date, les coordonnées de géolocalisation
* la dimension de l'image *pixels horizontaux, pixels verticaux*
* la profondeur de couleurs (nombre de couleurs possibles par pixel)
* ...

## Format des données EXIF
Ces données peuvent être mises en forme de *dictionnaire* en Python. Il faut utiliser une librairie particulière (une extension du langage). Ceci est réalisé en langage python avec le programme suivant : 

```Python
from PIL import Image
img = Image.open( 'photo.jpg' )
exif_data = img._getexif()
```

## Définitions: liste et dictionnaire en Python

* une liste, c'est une collection de données, accessibles à l'aide d'un index. Par exemple, pour la liste L, le premier élément c'est : `L[0]`.
* Un dictionnaire, c'est une collection de données, accessibles à l'aide d'une clé. `D[clé1]` par exemple.

On peut alors explorer cette variable *dictionnaire* à partir de ses clés.

Un dictionnaire peut contenir plusieurs clés. Elles sont alors séparées par des vigules, comme par exemple : 

`monDictionnaire = {clé1 : valeur1, clé2 : valeur2, clé3 : valeur3}`

Pour accéder à `valeur3` du dictionnaire `monDictionnaire`, il faudra faire par exemple : 

`monDictionnaire[clé3]`

## Exemple de données EXIF d'une image
Lorsque l'on ouvre un fichier image à l'aide d'instruction en Python, on a accès aux données EXIF qui sont alors stockées dans le dictionnaire `exif_data`.



> Cliquer sur *Executer* pour executer ces quelques lignes en python, qui retournent les données de localisation:

<br>

<iframe width='100%' height='500' allowfullscreen frameborder='0' style='border:1px #d6d6d6 solid;' src="https://fr.vittascience.com/python/?link=606c3b6b5d61b&mode=code"></iframe>

<br>

> Lire la latitude du lieu où a été prise l'image.

**Compléments sur le programme** 

Le petit programme ci-dessus stocke les données EXIF d'une image dans la variable `exif_data`. On explore ce dictionnaire `exif_data` pour afficher la coordonnée de latitude à laquelle la photographie a été prise.

Pour faire cela, on repère d'abord que les coordonnées de localisation se trouvent à la clé 34853. => `exif_data[34853]` 

La valeur contenue dans cette clé est aussi un dictionnaire. L'angle est exprimé en degrés à la clé 1 : `exif_data[34853][1]`
La valeur retournée est un tuple de 2 valeurs. On cherche la valeur du premier élement, celui de rang 0 : on fait alors : `exif_data[34853][1][0]`

On complète cette valeur de longitude avec les minutes et secondes d'angle, comme sur l'exemple interactif ci-dessus. 

# Peut-on extraire des informations d'une photo numérique ?
Oui !  Et c'est justement ce que nous allons faire. L'une des questions que l'on peut se poser est :
> Peut-on **géolocaliser une photographie** à partir des seules données contenu dans le fichier image ?

{{< img src="../IMG_5900.JPG" alt="photographie numerique iphone" >}}
L'appareil qui a pris la photographie nous est à priori inconnu, mais les données numériques, dans le fichier, y sont *structurées*. 
Cette structure, commune à tous les fichiers du même *format*, permet une grande diversité de logiciels de visualisation et de traitement d'images.

# Qu'est ce qu'une *meta-donnée* ?
Il s'agit, entre autres, de la date, de l'heure, des paramètres de prise de vue (vitesse, sensibilité, etc.), de la compression, de la **géolocalisation** de l'image, etc.
Ce sont des informations qui ne sont pas celles codant les pixels de l'image. On les nomme : *les données EXIF*

# Comment extraire ces données EXIF (TP en classe)?

* Parcourir le dossier *Documents* de votre session. Retrouver le dossier *scripts*.
Celui doit contenir l'image à analyser.
* Utiliser un IDE python  et saisir les lignes de code suivantes. 
* Enregistrer le programme dans le MÊME dossier que celui contenant l'image. Utiliser le nom suggeré au début de chaque programme

## Programme n°1 : afficher les données EXIF
```
# programme print_exif.py
#chargement des bibliothèques PIL et webbrowser
from PIL import Image
#chargement de l'image ( même dossier que le programme)
im = Image.open( 'IMG_5900.JPG' )
exif_data = im._getexif()
#on affiche les données exif
print(exif_data)
```

## Programme n°2 : explorer la variable `exif_data[34853]`
```
# programme explore_exif.py
#chargement des bibliothèques PIL et webbrowser
from PIL import Image
import webbrowser
#chargement de l'image ( même dossier que le programme)
im = Image.open( 'IMG_5900.JPG' )
# chargement des données exif, c'est un dictionnaire les données gps sont à la clé 34853
# repéré à l'aide de l'explorateur de variable de l'ide python
exif_data = im._getexif()
#chargement des données de la clé 34853
# on crée un dictionnaire pour contenir les données GPS
test={}
test=exif_data[34853]
# explorer la variable test pour savoir comment elle est structurée
# ce dictionaire contient des listes
# la latitude est à la clé 2 qui est une liste de tuples
print(test)
```

* On pourra ouvrir l'explorateur de variables pour parcourir toutes celles définies dans le programme : View > Panes > variable explorer
![menu](../menu.png)

  * double clic sur `exif_data` permet d'ouvrir l'exporateur avec plus de detail sur les données EXIF. Parcourir les différents champs affichés : Quelles informations relatives à la prise de la photographie pouvez vous deviner ?
  ![EXIF detail](../explo1.png)
  * double clic sur `34853` : observer les 4 premiers champs, relatifs à la géolocalisation.
  ![EXIF 34853](../explo2.png)

* On peut afficher directement les données de la variable exif_data : Dans la console, taper `exif_data`

* On peut aussi avoir la liste de toutes les clé du dictionnaire exif_data: 
 dans la console : `list(exif_data.keys())`

## Programme 3 : extraire la latitude et la longitude

```
# programme geolocalisation.py
#chargement des bibliothèques PIL et webbrowser
from PIL import Image
from webbrowser import open
#chargement de l'image ( même dossier que le programme)
im = Image.open( 'IMG_5900.JPG' )
# chargement des données exif, c'est un dictionnaire les données gps sont à la clé 34853
# repéré à l'aide de l'explorateur de variable de l'ide python
exif_data = im._getexif()
#chargement des données de la clé 34853
# on crée un dictionnaire pour contenir les données GPS
test={}
test=exif_data[34853]
"""
explorer la variable test pour savoir comment elle est structurée
ce dictionaire contient des listes
la latitude est à la clé 2 qui est une liste de tuples, on y accede avec test[2]
test[2][0] est le le 1er tuple : (degré, 1)
le second => test[2][1] : (minute,1) 
le 3ème => test[2][2] : (seconde,100)
Dans la fonction coordonnee(deg,min,sec) : 
on divise le 1er terme du tuple par le second par exemple test[2][1][0]/test[2][1][1]
et on transforme en degré :
(division par 1, ou 60 ou 100 selon s'il s'agit de deg, min ou sec)
"""




def coordonnee(deg,min,sec):
    """transformation des coordonnées au format décimal"""
    co_deg = deg[0]/deg[1]/1
    co_min = min[0]/min[1]/60
    co_sec = sec[0]/sec[1]/3600
    return co_deg+co_min+co_sec

lat = coordonnee(test[2][0],test[2][1],test[2][2])
lon = coordonnee(test[4][0],test[4][1],test[4][2])

print("la latitude est: ")
print(lat)
print(test[1])

print("la longitude est: ")
print(lon)
print(test[3])
```

## Programme complet
Ajouter les lignes suivantes au programme *geolocalisation.py*
```
# on affiche le tout dans openstreetmap
zoom='18'
webbrowser.open('https://www.openstreetmap.org/note/new?lat='+str(lat)+'&lon='+str(lon)+'#map='+zoom+'/'+str(lat)+'/'+str(lon))
```

### Correction du programme
La localisation n'est pas la bonne car elle ne tient pas compte des directions cardinales N,S,E,W : 
Ajouter les instructions qui corrigent les valeurs de latitude et de longitude, avant d'afficher la carte sur Openstreetmap.
Aidez vous de l'algorithme suivant, écrit en langage naturel : 
```
si test[1]=='S` alors:
  lat ← -lat

si test[3]=='W' alors:
  lon ← -lon
``` 
