---
Title: transformer image ascii
weight: 21
---

*Prérequis:*

* TP6b: Listes et symboles pour dessiner des formes: [Lien](/python_bases/boucles/page7/)
* TP7 Lecture/ Ecriture dans un fichier: [Lien](../../ES/page54/)

# TP8 Projet ascii art: des pixels aux symboles ascii
On va remplacer dans une image la couleur d'un pixel par un caractère ascii dont le remplissage permettra de faire varier la clarté d'un zone de l'image.

* Télécharger les [documents sources](/scripts/PIL/src.zip) et décompresser l'archive. Trouver dans ce dossier les fichiers *Marylin-original.jpg* et le module *display_image*
* Enregistrer tous vos fichiers python **dans ce même dossier**.

## Partie 1 : préparation (≈ 45 min)
Avant de réaliser le projet, on manipule séparément chacun des éléments qui seront utilisés en partie 2.

### Bloc 1 – La palette de caractères (≈ 5 min)

```python
ascii_char = ' .:-=+*#%@'
```

1. Que vaut `len(ascii_char)` ?
2. Que renvoient `ascii_char[0]`, `ascii_char[9]` et `ascii_char[-1]` ?
3. Que se passe-t-il avec `ascii_char[10]` ? Pourquoi ?
4. Quel caractère représente le pixel le plus **clair** ? Et le plus **foncé** ?

*Comme dans le TP sur le code César, on utilise la position d'un caractère dans une chaîne pour faire correspondre une valeur à un symbole.*

### Bloc 2 – Du pixel RGB au niveau de gris (≈ 10 min)
La couleur d'un pixel est donnée par un tuple `(R, G, B)` : trois entiers entre 0 et 255.

5. Écrire une fonction `grey(rgb)` qui reçoit un tuple `(R, G, B)` et renvoie son niveau de gris: $(R+V+B)//3$

*cahier labo*: 

6. Compléter ensuite le tableau :

| pixel `rgb` | `grey = (r+g+b)//3` | `index = grey*9//255` | caractère `ascii_char[index]` |
|---|---|---|---|
| (0, 0, 0) | | | |
| (255, 255, 255) | | | |
| (120, 60, 30) | | | |
| (200, 200, 100) | | | |


7. Pourquoi utilise-t-on la division entière `//` et pas `/` ? (Essayer `ascii_char[2.7]`.)
8. Pourquoi multiplie-t-on par **9** et pas par 10 ? Comment écrire ce nombre pour que la formule fonctionne avec une palette de n'importe quelle longueur ?
9. D'après le tableau, quel caractère obtient-on pour un pixel **blanc** ? Est-ce cohérent avec la question 4 ? Modifier le calcul de `index` pour qu'un pixel blanc donne un espace et un pixel noir donne `'@'`.

### Bloc 3 – Boucles imbriquées (≈ 10 min)

10. À l'aide de deux boucles `for`, afficher un rectangle de 4 lignes et 10 colonnes de `#`.
11. Afficher un dégradé de 10 lignes et 20 colonnes : la ligne numéro `y` est remplie avec le caractère `ascii_char[y]`.

<!--
12. Dans le programme de la partie 2, la boucle sur `y` (lignes) est **à l'extérieur** et la boucle sur `x` (colonnes) **à l'intérieur**. Que se passerait-il si on inversait les deux boucles ?

-->
12. Dans la partie 2, on ajoute un espace `' '` après chaque caractère. Pourquoi ? (Comparer la hauteur et la largeur d'un caractère à l'écran.)

### Bloc 4 – Une mini-image « à la main » (≈ 10 min)
Une image en niveaux de gris peut être représentée par une liste de listes :

```python
image = [[255,255,0,0,255,255],
         [255,0,255,255,0,255],
         [0,255,255,255,255,0],
         [0,255,0,0,255,0],
         [255,0,255,255,0,255],
         [255,255,0,0,255,255]]
```

13. Que vaut `image[2][0]` ? Lequel des deux indices correspond à la ligne (`y`), lequel à la colonne (`x`) ?
14. Parcourir l'image avec deux boucles et afficher le dessin en caractères ascii (utiliser le calcul de `index` corrigé à la question 8). Que représente l'image ?
15. Au lieu d'afficher le dessin, l'écrire dans un fichier `mini.txt` : [ouvrir le fichier en écriture](/python_bases/es/page54/) (`"w"`), écrire chaque ligne terminée par `'\n'`, puis fermer le fichier. Ouvrir `mini.txt` avec un éditeur de texte pour vérifier.
16. Combien de caractères contient chaque ligne du fichier `mini.txt` (en comptant le `'\n'`) ? Combien en contiendra chaque ligne pour l'image de 500 × 500 pixels de la partie 2 ?

### Bloc 5 – Premier contact avec PIL (≈ 10 min)
Vous avez téléchargé les [documents sources](/scripts/PIL/src.zip).

> Executez le programme suivant:

```python
from PIL import Image
image = Image.open("Marylin-original.jpg")
```

17. Afficher `image.size` et `image.mode`. Que représentent ces valeurs ?
18. Afficher `image.getpixel((0, 0))`. De quel type est le résultat ? Que représentent ses valeurs ?
19. Redimensionner l'image avec l'instruction `image = image.resize((50, 50))`. Que vaut maintenant `image.size` ? Afficher la couleur du pixel situé au centre de l'image.

## Partie 2 : le projet ascii art (≈ 40 min)

Video explicative:

{{< img src="../images/video_ascii.png" width="400" link="https://www.youtube.com/watch?v=2U11986Ro9o" caption="lire la video" >}}

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
<!--
* [correction](../ascii_art_p1_c) de la partie 1

* [correction](../ascii_art_c) du Projet ascii-art
* -->

