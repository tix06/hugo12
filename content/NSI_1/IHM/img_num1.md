---
Title: images numeriques
description: format matriciel, module PIL, drapeaux pays
weight: 13
---

* creation d'images numeriques version 1: [Lien](../img_num1)
* creation d'images numeriques version 2: [Lien](../img_num11)
* traitement d'une image: detourage, filtre, incrustation: [Lien](../img_num2)
* tuto pour detourer une image avec Gimp: [Lien](../img_num22)

# Créer des images numeriques - Partie 1
Les images numériques matricielles sont des tableaux de pixels. On peut concevoir images de *synthèse* à partir d'instructions en python (ou autre langage). Des librairies comme `PIL` permettent de manipuler les pixels comme les données d'une table.

Dans cette seance, nous allons:

* créer des images de synthèse

{{< img src="../images/pixart1.png" >}}

* modifier des images existantes.

{{< img src="../images/img5.png" >}}

## formats de données
Le portable pixmap file format (PPM), le portable graymap file format (PGM) et le portable bitmap file format (PBM) sont des formats de fichier graphique utilisés pour les échanges. Ils correspondent respectivement à des images en noir et blanc (ppm), en niveaux de gris (pgm), et en couleur (pbm).

Les fichiers bruts comportent alors l’indication du format sur leur première ligne avec l’information : P1 pour le format ppm, P2 pour le pgm et enfin P3 pour le pbm.


## Couleurs : RVB
Il  existe  plusieurs  modes  de  codage  informatique  des  couleurs,  le  plus  utilisé  pour  le  maniement  des images  est  l'espace  colorimétrique  Rouge,  Vert,  Bleu (RVB  ou  RVG:  Red  Green  Blue)  par  synthèse additive. 

Une image RVB est composée de la somme des trois rayonnements lumineux Rouge, Vert,  Bleu dont les  faisceaux sont superposés. A l'intensité maximale  ils produisent une  lumière blanche 255, 255, 255 en codage décimal, ou FF FF FF en hexadecimal.

## profondeur de couleur
* norme HD: la profondeur en haute definition est de 1 octet par canal coloré R, V ou B

* norme 4K : UHD = 10 bits par canal coloré

## Gimp: colorimètre
> A vous de jouer: vous allez mesurer l'intensité des couleurs sur l'image suivante

{{< img src="../images/img1.png" link="../images/img1.png" caption="clic droit: telecharger" >}}

[Télécharger l'image](../images/img1.png).

> Adopter tout de suite les BONNES PRATIQUES:

> * Créer un nouveau dossier pour y mettre tous les fichiers sources et les images.


A l'aide du logiciel Gimp, ouvrir l'image du carré rouge et relever les valeurs RVB du colorimètre.


# Synthèse d'images
## Rectangle rouge
Vous allez créer une image (rectangle rouge) à partir d'un programme python.

Utiliser un IDE python pour les exercices suivants: *Pyzo* ou *Spyder*.

> Adopter tout de suite les BONNES PRATIQUES:

> * pour chaque exercice, vous allez créer un NOUVEAU fichier python.
> * Donner un nom explicite au fichier, par exemple `rouge.py` pour le premier exercice



* Définir les variables globales largeur et hauteur:

```python
largeur=600
hauteur=420
```

* Créer un nouveau fichier texte avec les instructions:

```python
f=open('red_square.ppm','w') 

############ entête du fichier ##################
f.write('P3'+'\n') # P1 était le code pour un pbm format ascii
			  # P3 correspond au ppm format ascii
f.write(str(largeur)+' '+str(hauteur)+'\n')
# valeur max pour l'intensité des couleurs :
f.write('255'+'\n')
############### fin de l'entête ##################
```

* Definir une fonction pour remplir le fichier avec les valeurs codant la couleur:

```python
#########  declaration de la fonction ############
def rectangle(couleur,h,l) :
	""" 
	@param couleur: str
	couleur est un triplet d'entiers, code RGB
	@example: dessiner un rectangle entierement noir
	>>> rectangle('0 0 0',largeur,hauteur)
	"""
	for i in range(h*l) :
			f.write(couleur+'\n')
```

* Puis appel de la fonction et fermeture du fichier:

```python
rectangle('255 0 0',largeur,hauteur)
f.close()
```




* Ajouter la librairie PIL. 

Ce qui donne le script complet suivant:

```python
from PIL import Image
largeur=600
hauteur=420

#f=open('red_square','w') 
f=open('red_square.ppm','w') 

############ entête du fichier ##################
f.write('P3'+'\n') # P1 était le code pour un pbm format ascii
			  # P3 correspond au ppm format ascii
f.write(str(largeur)+' '+str(hauteur)+'\n')
# valeur max pour l'intensité des couleurs :
f.write('255'+'\n')
############### fin de l'entête ##################

#########  declaration de la fonction ############
def rectangle(couleur,h,l) :
	""" 
	@param couleur: str
	couleur est un triplet d'entiers, code RGB
	@example: dessiner un rectangle entierement noir
	>>> rectangle('0 0 0',largeur,hauteur)
	"""
	for i in range(h*l) :
			f.write(couleur+'\n')
######## appel fonction ############################			
rectangle('255 0 0',largeur,hauteur)
########### fermeture fichier ######################
f.close()
```

> Executer le programme avec les commandes de l'IDE python, puis...
> * Ouvrir le fichier avec un **editeur de texte** (notepad++) et observer les données.
> * Ouvrir le fichier avec un logiciel de dessin (GIMP)

## Drapeaux de pays
> Adopter tout de suite les BONNES PRATIQUES:

> * pour chaque nouveau défi, vous allez créer un NOUVEAU fichier python.
> * Donner un nom explicite au fichier, par exemple `allemagne.py` pour le premier défi, `belgique.py` pour le 2e...

Adapter maintenant le script du rectangle rouge pour editer en python les drapeau suivants.

Attention à BIEN faire correspondre le nombre de valeurs codantes pour la couleur des pixels. Si le nombre ne correspond par exactement à la dimension $largeur \times hauteur$ définie dans l'en-tête du fichier, vous risquez d'avoir une image sombre (erreur à l'affichage)

{{< img src="../images/img2.png" link="../images/img2.png" caption="drapeau allemand. 3 appels de la fonction rectangle('255 0 0',largeur,hauteur//3)" >}}

Attention à bien modifier le nom du fichier généré. Le nommer par exemple `drapeau_all.ppm`

{{< img src="../images/img3.png" link="../images/img3.png" caption="drapeau belge. Utiliser une boucle bornée pour créer le drapeau ligne par ligne." >}}

## motifs périodiques
> * pour chaque nouveau défi, vous allez créer un NOUVEAU fichier python.
> * Donner un nom explicite au fichier, par exemple `pixart1.py` pour le premier défi, `pixart2.py` pour le 2e...

Dans chaque nouveau fichier, vous allez écrire le script qui va créer les images suivantes, à partir des matrices de valeurs binaires, `mat`. Dans cette matrice, vous placerez les valeurs en liste (une liste par ligne), et placerez ces lignes dans la matrice `mat`. Une valeur 0 pourra coder par exemple le bleu, et la valeur 1 le rouge (l'image ne contient que 2 couleurs).

* pixart1.ppm

{{< img src="../images/pixart1.png" >}}

```python
from PIL import Image
largeur=12
hauteur=12

f=open('pixart1.ppm','w') 

############ entête du fichier ##################
f.write('P3'+'\n') 
f.write(str(largeur)+' '+str(hauteur)+'\n')
# valeur max pour l'intensité des couleurs :
f.write('255'+'\n')
############### creation matrice ################
mat = []
for i in range(hauteur):
    ligne = []
    for j in range(largeur):
        ligne.append(0)
        ligne.append(...
    mat.append(...
#########  declaration de la fonction ############
def creation_image(M,h,l) :
    """ 
    @variable couleur: str
    couleur est un triplet d'entiers, code RGB
    @example: dessiner un pixel entierement noir
    >>> couleur = '0 0 0'
    """
    for i in range(h) :
        for j in range(l):
            if M[i][j] == 1:
                couleur = '255 0 0'
            else:
                couleur = '0 0 255'
            f.write(couleur+'\n')
######## appel fonction ############################	
creation_image(mat,largeur,hauteur)		
########### fermeture fichier ######################
f.close()
```

* pixart2.ppm

{{< img src="../images/pixart2.png" >}}

Pour chacune de ces images, vous complèterez le script de la [fiche de cours](/pdf/NSI_1/python_grille.pdf).

# Lecture puis traitement des pixels de l'image - Partie 2
## Lire les pixels de l'image
Dans cette activité, nous allons utiliser la fonction de lecture des couleurs des pixels d'une image. Puis transformer cette image par effet mirroir. Les chatons devront regarder à DROITE après transformation.


{{< img src="../images/chats.bmp" link="../images/chats.bmp" caption="Image de chatons à télécharger" >}}


La fonction getpixel du module PIL.Image. Cette fonction prend en paramètres les coordonnées du pixel à lire, sous forme d'un tuple `(x,y)`. *Exemple:*

```python
>>> imageSource.getpixel((x,y))
# retourne un tuple constitué des couleurs (R, V, B) du pixel de coordonnée (x,y)
```

Voici le programme minimal pour ouvrir l'image et déterminer ses dimensions:

```python
from PIL import Image


imageSource=Image.open("chats.bmp")
largeur,hauteur=imageSource.size
```

Pour lire les couleurs de TOUS les pixels, et appliquer une transformation, on va placer les valeurs dans une *matrice*, dans un certain ordre:

```python
mat = [[0]*largeur for i in range(hauteur)]
for i in range(hauteur):
    for j in range(largeur):
        p = imageSource.getpixel((j,i))
        # j correspond à x 
        # et i <=> y
        mat[i][j]=p
```

Puis placer les valeurs de la matrice dans un fichier `.ppm`, comme vu dans les activités précédentes:

```python
####### ecriture du fichier pour la nouvelle image
f=open('pixart2.ppm','w') 

f.write('P3'+'\n') 
f.write(str(largeur)+' '+str(hauteur)+'\n')
# valeur max pour l'intensité des couleurs :
f.write('255'+'\n')
#########  declaration de la fonction ############
def creation_image(M) :
    """ 
    @param couleur: str
    couleur est un triplet d'entiers, code RGB
    @example: dessiner un rectangle entierement noir
    >>> rectangle('0 0 0',largeur,hauteur)
    """
    h = len(M)
    l = len(M[0])
    for i in range(h) :
        for j in range(l):
            couleur = M[i][j] # tuple
            pixel = str(couleur[0]) + ' ' + str(couleur[1]) + ' ' + str(couleur[2])
            f.write(pixel+'\n')
######## appel fonction ############################	
creation_image(mat)
########### fermeture fichier ######################
f.close()
```

> Comment doit-on placer les pixels dans la matrice pour que les chats regardent de l’autre côté ? Modifier le programme ci-dessus afin d'obtenir cette nouvelle image, avec des petits chats qui regardent à DROITE.

## Pix-Art
Avec l'image d'origine suivante:

{{< img src="../images/marylin_original.JPEG" link="../images/marylin_original.JPEG" caption="Marylin Monroe" >}}

> Apporter les modifications necessaires pour filtrer les couleurs par zone, de manière selective. On pourra obtenir une nouvelle oeuvre inspirée de l'image suivante:

{{< img src="../images/img4.jpg" caption="Marylin Monroe type Pop-art" >}}

*Aide:* La condition suivante permet de selectionner les pixels de la partie gauche de l'image, **et** qui ont une composante Rouge supérieure à 100:

```python
if (j<largeur//2 and p[0] > 100) :
	# traitement sur p
```

Ce qui va donner:

```python
mat = [[0]*largeur for i in range(hauteur)]
for i in range(hauteur):
    for j in range(largeur):
        p = imageSource.getpixel((j,i))
		if (j<largeur//2 and p[0] > 100) :
			# traitement sur p
        mat[i][j]=p
```

*Sur une idée venue de la visite de la collection de Luigi e Peppino Agrati, Naples.*

{{< img src="../images/marylin_ITA.png" caption="Extrait de l'oeuvre de Andy Warhol (1967). Marilyn." >}}

Ce TP est une variante de celui proposé à l'adresse [suivante](../img_num11).

# Projet - construire une image à partir de calques
voir l'énoncé [ici](../img_num2)