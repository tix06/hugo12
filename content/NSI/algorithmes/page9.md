---
Title: rotation quart de tour
description: images matricielles, rotation, methode diviser pour regner
weight: 11
---

**Télécharger le dossier de travail: {{< download link="/scripts/TP_rotation_image.zip" hint="TP_rotation_image.zip" caption="TP_rotation_image.zip" >}}**

# Coder une image numérique
## Qu'est ce qu'une image numériques?
*Rappels de SNT:* Une image numérique est constituée de pixels colorés (ou noirs et blanc). Le fichier comportant l'image numérique contient alors une succession de valeurs qui codent la couleur de chaque pixels: lire le cours de SNT, paragraphe{{< a link="/docs/SNT_2nde/pages/page5/photo_num/#codage-de-l-image" caption="codage de l'image" >}}
## Librairie PIL
Pour manipuler les images, nous pouvons utiliser le module `PIL` de Python. Celui-ci permet de traiter les pixels d'une image, un par un. Souvent, il faudra parcourir l'image pixel par pixel, sur toute la largeur et toute la hauteur. Cela est possible avec deux boucles imbriquées, à condition de connaitre ses dimensions `largeur, hauteur`:

```python
from PIL import Image
imageSource=Image.open("crabePortrait.bmp")
largeur,hauteur=imageSource.size

for y in range(hauteur): # y varie de 0 à hauteur - 1
    for x in range(largeur): # x varie de 0 à largeur - 1
        # traitement pixel (x,y)

```

Les boucles `for` vont effectuer un parcours:
* sur y (position en hauteur qui varie de 0 à hauteur-1)
* sur x (position en largeur qui varie de 0 à largeur-1)

Le pixel (0,0) est en haut sur le coin gauche. 

*imageSource est une instance de la classe `Image` et possède une methode `getpixel((x,y))` qui renvoie la valeur du pixel pour l'argument (x,y). S'utilise de la manière suivante:*

```python
# lecture
p = imageSource.getpixel((x,y))
# ecriture
planPixels.putpixel((x,y),p)
```

## Manipuler les pixels de l'image
Nous allons travailler sur l'image suivante: **crabePortrait.bmp**.

{{< img src="../images/crabePortrait.bmp" link="../images/crabePortrait.bmp" caption="image de dimension 247 * 330 en format bitmap, RGB 3 octets" >}}

**Défi n°1: explorer la structure de données**

> *A vous de jouer:* ouvrir le fichier `rotation_crabe.py`, analyser le script, puis, à l'aide de la fonction `copie_image`, faire une copie de l'image `crabe_portrait.bmp`

> Vérifier le contenu des données pour quelques uns des points de l'image: afficher la valeur de p si x < largeur//10 et y < hauteur //10

> Laquelle des structures de données représente le mieux le format des données:
> * `[124,90,120]`
> * `(124,90,120)`
> * `#7C5A78`?


<!--
On souhaite maintenant diminuer le contraste, en divisant par 2 chacune de composantes RGB de chacun des pixels de l'image. L'image sera egalement plus sombre. On va créer cette fois une nouvelle instance, `planPixels`, de la classe `Image`, de la même dimension que celle d'origine, pour y copier les pixels un-à-un:

`planPixels=Image.new("RGB",(largeur,hauteur))`

On va placer les pixels de *imageSource* (lecture) dans la nouvelle image *planPixels* (écriture).

*Debut du 2e programme:*

```python
from PIL import Image
imageSource=Image.open("crabePortrait.bmp")
largeur,hauteur=imageSource.size
planPixels=Image.new("RGB",(largeur,hauteur))

for x ...
  for y ...
  # traitement pixel (x,y)
  # a completer ...

planPixels.save("crabe2.jpg")
planPixels.show()
```

On remplira cette image avec les pixels de l'image d'origine de la manière suivante:

> *A vous de jouer:* Compléter le script pour...
> 1. parcourir tous les pixels de l'image, largeur * hauteur.
> 2. lire la valeur RGB de chaque pixel (`getpixel`) et modifier cette valeur, en diminuant le contraste de couleur: $p = (p[0]//2,\ p[1]//2,\ p[2]//2)$
> 3. placer ce pixel sur la nouvelle image en construction planPixels. Utiliser pour cela la methode putpixel((x,y),p) de l'objet `planPixels` où x et y sont les nouvelles coordonnées du pixel p que l'on veut dessiner: `planPixels.putpixel((x,y),p)`
-->


# Rotation d'une image: permutation de pixels
**Défi n°2: Coordonnées pour une rotation droite**

{{< img src="../images/rotation.png" caption="principe de la rotation horaire d'un quart de tour" >}}

> *Répondre aux Questions:*

> 1. Quelles sont les coordonnées des points A et B avant transformation?
> 2. Quelles sont les nouvelles positions des points A' et B' après transformation: Pour un pixel situé initialement en (x,y), quelles sont ses coodonnées (x',y') après transformation? 


<!--
> 5. Donner la complexité de cet algorithme.
*Réponse à la question 3: $x'=-y+hauteur-1$, $y'=x$.* 
-->

**Défi n°3: Rotation droite d'une image**

En vous inspirant de la fonction `copie_image`, écrire une fonction `rotation_droite` qui réalise la rotation d'un quart de tour dans le sens horaire, comme sur l'image ci-dessus.



# Permuter les zones d'une image
On cherche maintenant à effectuer cette transformation, SANS utiliser de nouvelle image *planPixels* comme précédemment. 

On utilisera l'image suivante (carrée) pour cette méthode: **woody.jpg** 

{{< img src="../images/woody.jpg" link="../images/woody.jpg" caption="image woody.jpg" >}}

Le fichier de travail sera `rotation_woody.py`

**Défi n°4: permutation de blocs**

la fonction `echange_quadrant` permet d'echanger les pixels de 2 zones carrées de même dimensions.

{{< img src="../images/deplaceBloc.png" caption="exemple: echange des blocs A et B" >}}

Les zones échangées seront les 4 parties marquées A, B, C et D sur l'image ci-dessous.

{{< img src="../images/woody0.png" caption="image d'origine" >}}

Pour effectuer une rotation droite dans l'image, on va effectuer 3 permutations SUCCESSIVES sur les zones ABCD de l'image:

{{< img src="../images/echanges.png" caption="trois permutations réalisées sur les subdivisions de l'image" >}}

> 1. Pour échanger les zones A et B d'une image, et visualiser le résultat, utiliser la fonction `permutation_blocs_A_B`.
> 2. Ecrire les fonctions `permutation_blocs_B_D` et `permutation_blocs_C_D`. Appliquer les transformations pour obtenir une rotation droite des blocs de l'image `woody.jpg`.




<!--
## Compléter la fonction `echange_pix` suivante

```python
def echange_pix(image,x0,y0,x1,y1):
    """procedure qui echange les pixels d'une image entre une position 
    de depart start et d'arrivée end
    Params:
    ------
    image : objet de la classe Image
    x0,y0: int, int: coordonnées du pixel de depart
    x1,y1: int, int: coordonnées du pixel d'arrivée
    
    Exemple: echange du pixel (0,0) avec celui (120,120)
    --------
    >>> echange_pix(imageSource,0,0,120,120)
    """
    start = image.getpixel((x0,y0))
    end = image.getpixel((x1,y1))
    image.putpixel((x0,y0),end)
    image.putpixel((x1,y1),...)
```


## Compléter la fonction `echange_quadrant` suivante
Cette fonction permet d'echanger les pixels de 2 zones carrées de même dimensions.

{{< img src="../images/deplaceBloc.png" caption="exemple: echange des blocs A et B" >}}
```python
def echange_quadrant(image,x0,y0,x1,y1,n):
    """procedure qui echange tous les pixels du bloc de pixels A
    avec ceux du bloc B, de même dimension n*n.
    L'image doit être carrée, de largeur et hauteur égaux à n
    A et B occupent une position quelconque parmi les 4 quarts de l'image
    Params:
    -------
    image : objet de la classe Image
    x0,y0: int, int: coordonnées du pixel du coin superieur gauche de A
    x1,y1: int, int: coordonnées du pixel du coin superieur gauche de B
    n : int : largeur ou hauteur de l'image, en nombre de pixels
    Example: echange du quart d'image en haut à gauche (A) avec celui 
    ------------ en haut à droite (B) sur une image de largeur 120
     
   
    >>> echange_quadrant(imageSource,0,0,120,0,120)
    """
    for x in range(n):
        for y in range(n):
            echange_pix(image, x0+x,...# à compléter

```

> **Questions:**

> * On veut echanger les blocs A et D, qui font chacun 120*120 pixels. Quelle instruction faut-il écrire, utilisant la procedure `echange_quadrant`.
* Même question pour echanger les blocs A et C.
-->
# Rotation par la méthode Diviser pour Régner


La fonction `rotate` permet de faire tourner l'image d'un quart de tour par une méthode de type *diviser pour régner*:

*Tourner l'image d'un quart de tour, c'est permuter les 4 parties d'une image dont on a permuté l'interieur de ses 4 parties...*

Une fois la partie **divisée** executée (appels recursifs), lorsque les subdivisions de l'image sont constituées d'un seul pixel, les pixels sont déplacés (**règne**) à l'aide de 3 permutations successives, selon le schéma suivant:

{{< img src="../images/echanges.png" caption="trois permutations réalisées sur les subdivisions de l'image" >}}

Il sont alors recombinés pour reformer l'image, tout en suivant les mêmes permutations, mais avec des blocs de pixels plus gros (**fusion**).

Le but est d'obtenir l'image suivante, à l'aide de la fonction `quart_tour`:

{{< img src="../images/woody6.png" caption="image finale" >}}

**Défi n°5: rotation d'une image par la méthode Diviser pour régner**

> 1. Compléter la fonction  `rotate` pour obtenir une image à l'endroit de `woody`.
> 2. Expliquer pourquoi cette méthode s'apparente à la famille *Diviser pour régner*. (On pourra s'aider des schémas ci-dessous, et les remettre dans l'ordre pour repondre).

<!--
```python
def rotate(image,x0,y0,n):
    """procedure recursive qui tourne d'un quart de tour un carré
    de l'image de dimension n.
    à chaque appel recursif, la taille de l'image est divisée par 2.
    Si l'image fait plus d'un seul pixel, la rotation se fait par 
    permutation des (zones de) pixels A<=>B, B<=>D, D<=>C
    Params:
    -------
    image
    x0,y0: int, int: coordonnées du pixel du coin superieur gauche du carré
    n: dimansion du carré
    Example:
    --------
    rotate(imageSource,0,0,420)
    """
    if n>=2:
        m = n//2
        rotate(image,x0,y0,m)
        rotate(image,x0,y0+m,m)
        rotate(image,x0+m,y0,m)
        rotate(image,x0+m,y0+m,m)
        echange_quadrant(image,x0,y0,x0+m,y0,m)
        echange_quadrant(image,x0,y0,x0+m,y0+m,m)
        echange_quadrant(image,x0,y0,x0,y0+m,m)
```

*Analysez la procedure:* On considère l'image de *woody*, quadrillée de la manière suivante. Cette image fait $512 \times 512$ pixels

{{< img src="../images/woody0.png" caption="image d'origine" >}}

> 1. Lors du premier appel de la fonction: que vaut m?

A la fin de la remontée, lorsque m vaut 256, l'image, si on l'affiche est celle-ci:

{{< img src="../images/woody6.png" caption="image finale" >}}

> 2. Compléter la grille avec les lettres A, B, C, D pour montrer la permutation des blocs sur le dessin.

On peut suivre la construction de l'image à différents niveaux de la pile d'appels recursifs, lors de la remontée. Pour faire ceci, ajouter les instructions suivantes en fin de la fonction `rotate`:

```python
        if m > 100:
            image.show()
```

Puis ajouter et executer les lignes suivantes:

```python
from PIL import Image

def quart_tour(image):
    largeur,hauteur=image.size
    assert largeur == hauteur
    rotate(image,0,0,largeur)
    
    
img = Image.open("woody.jpg")
quart_tour(img)
img.save("woody_endroit.jpg")
img.show()
```

Pour suivre la construction de l'image, nous allons placer les repères suivants sur l'image d'origine:

{{< img src="../images/woody1.jpg" caption="image quadrillée" >}}

> 3. Pour chacune des images suivantes:

> * quel est la valeur de m lorsque l'image est affichée?

> * compléter les quadrants montrant la permutation dans chaque sous-partie

> * dans quel ordre ces images sont elles affichées?
-->
{{< img src="../images/woody5.png" caption="image a" >}}

{{< img src="../images/woody4.png" caption="image b" >}}


{{< img src="../images/woody2.png" caption="image c" >}}

{{< img src="../images/woody3.png" caption="image d" >}}




# efficacité de la méthode
*Evaluons l'efficacité de cet algorithme*

> * Est-il plus rapide ou plus lent que votre premier algorithme?

> * Le nombre d'opérations significatives suit une loi de recurence: $T(n) = 4 \times T(\tfrac{n}{2}) + C \times n^2$ Cela confirme t-il votre reponse à la question pécédente?

On rappelle que l'intérêt de la méthode est surtout de ne PAS utiliser de nouvelle image *planPixels* comme précédemment. Il s'agit d'une transformation *en place*.

# Liens et aides
* En cas de difficulté, consulter la page et les videos du site: [monlyceenumerique.fr](http://www.monlyceenumerique.fr/nsi_terminale/a/a3_div_regner.php), aller à la partie sur la rotation des images.
