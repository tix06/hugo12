---
Title : niveau a bulles
description: microbit capteur de direction, inclinaison, jeu du snake
weight: 15
---

# Acceleromètre et niveau à bulles
*But: Programmer une série d'instructions conditionnelles et une fonction en Python.*

{{< img src="../images/bulles.png" >}}

## Editeur
Choisir l'editeur **MU** en mode *BBC microbit*

## Afficher la direction d'inclinaison
Le script devra démarrer par les lignes suivantes:

```python
from microbit import *

while True:
    incli_X = accelerometer.get_x()
    incli_Y = accelerometer.get_y()
```

Le programme permet de stocker dans les variables `incli_X` et `incli_Y` les valeurs mesurées par l'accéleromètre.

Vous pouvez charger ce programme dans la carte microbit. Puis ouvrir la console de l'editeur MU (**REPL**), et afficher les valeurs de ces variables: (ces valeurs dependent de l'inclinaison initiale de la carte microbit)

```
>>> incli_X
228
>>> incli_Y
-15
```

Refermez alors la console et revenir sur l'editeur de script...

Compléter le script avec les tests qui permettront d'afficher "D", "G", "H", "B" ou "-" selon si l'inclinaison est vers la **D**roite, **G**auche, **H**aut, **B**as, ou **-** neutre.

On pourra se conformer au diagramme ci-dessous:

{{< img src="../images/diag_incli.png" caption="diagramme de décision if ... elif ... else" >}}

**Flasher**. La lettre qui est affichée depend alors de l'inclinaison!

**sauvegarder** le fichier `.py`dans votre classeur numérique (vos documents, dans un dossier particulier)

## Afficher une bulle
L'inclinaison va maintenant mettre en mouvement une bulle à l'écran. (Un pixel de coordonnées x, y).

On définit les variables `x, y = 2, 2` avant la boucle principale `while True`.

### Boucle principale
On remplacera ensuite chacune des instructions d'affichage `display.show()` par la mise à jour d'une variable `direction`:

```python
display.show("D")
# sera remplace par
direction = "D"
```

à la fin de la boucle, on ajoutera les lignes qui vont:

* appeler la fonction `deplace` avec les arguments: `direction, x, y`. Affecter à `x, y` les valeurs de retour.
* Effacer l'écran
* Afficher le pixel à la position x, y

```python
    x, y = deplace(direction, x, y)
    sleep(100) # optionnel
    display.clear()
    display.set_pixel(x,y,9)
```

Le corps du programme devrait alors ressembler au script suivant:

```python
from microbit import *
def deplace(direction, pos_X, pos_Y):
	# a completer
    return pos_X,pos_Y

x, y = 2,2

while True:
    incli_X = accelerometer.get_x()
    incli_Y = accelerometer.get_y()
    if abs(incli_X ) > abs(incli_Y):
        if incli_X > 20:
            direction = "D"
        elif incli_X < -20:
            #display.show("G")
            direction = "G"
        else:
            direction = "-"
    else:
        if incli_Y < -20:
            direction = "B"
        elif incli_Y > 20:
            direction = "H"
        else:
            direction = "-"
    x, y = deplace(direction, x, y)
    sleep(100)
    display.clear()
    display.set_pixel(x,y,9)
```

### Programmer une fonction avec paramètres
La fonction sert à modifier les valeurs des paramètres `pos_X` et `pos_Y` selon celle de `direction`.

* `direction` est une variable de type `str` et vaut "D", "G", "H", "B" ou "-".
* `pos_X` et `pos_Y` sont de type `int`.
* Les **valeurs de retour** sont `pos_X` et `pos_Y`.

```python
def deplace(direction, pos_X, pos_Y):
	# a completer
	return pos_X, pos_Y
```

Il faudra donc programmer une série de conditions sur `direction` pour modifier les valeurs de position (augmenter ou diminuer d'une unité `pos_X` ou `pos_Y`).

**Problème de depassement**: Les valeurs admises pour `pos_X` et `pos_Y` doivent être comprises en 0 et 4, sinon cela génère un `Value Error` lorsque l'on veut afficher le pixel à l'ecran avec `display.set_pixel(x,y,9)`.

Votre fonction doit aussi prendre en compte cette possibilité et ne pas retourner de valeur `<0` ou `>4`.

{{< img src="../images/pix_a_droite.png" caption="pencher la carte microbit vers la droite" >}}

**Flasher** et testez votre programme. *Parviendrez-vous à maintenir le pixel au centre pendant quelques secondes*?

**sauvegarder** le fichier `.py`

## Prolongement: Le SNAKE
On peut augmenter la complexité du programme en affichant un serpent à l'écran comme dans le jeu *snake*. Les coordonnées des pixels du serpent sont alors stockées dans une Liste `[(x1,y1),(x2,y2),...]` pour permettre leur affichage:

```python
for coord in serpent:
	display.set_pixel(coord[0],coord[1],9)
```

{{< img src="../images/snake.GIF" caption="" >}}

A chaque déplacement, cela ajoute un pixel à la fin de la liste. Il s'agit de la tête du serpent. Il faut alors retirer le premier pixel (`serpent[0]`) si l'on veut que sa longueur reste constante.

{{< img src="../images/depl_snake.png" caption="deplacement du serpent vers le bas" >}}


Dans la boucle principale, une fois que la variable `direction`a été mise à jour, on ajoutera les lignes suivantes pour la gestion du deplacement du serpent:

```python
    x, y =  tete(serpent)
    if direction != "-":
        x, y = deplace(direction, x, y)
        ajoute_tete(serpent, x, y)
        supprime_queue(serpent)
    sleep(100)
    display.clear()
    affiche(serpent)
 ```

 Voir en annexe[^1] le corps du programme complet.

 L'objet `serpent` est alors une liste Python à laquelle on associes les fonctions  `tete`, 'ajoute_tete`, `supprime_queue`et `affiche`.

 Ces fonctions sont décrites dans les commentaires suivants:

 ```python
 def tete(S):
    # retourne les coordonnees x, y de la tete du serpent
    # qui sont stockees dans le dernier element S[-1]
    # sous la forme d'un tupple (x,y)

def ajoute_tete(S, x, y):
    # ajoute un tupple (x,y) a la fin de la liste S 

def supprime_queue(S):
    # decale toutes les valeurs de la liste S vers la gauche:
    # a l'aide d'une boucle bornee sur les indices i:
    # copie toutes les valeurs S[i+1] dans S[i]
    # puis supprime le dernier element

def affiche(S):
    # affiche tous les pixels du serpent
    # a partir de leurs coordonnees dans S

```

 Il restera à écrire le script de ces fonctions. Cette méthode de programmation introduit le chapitre sur les *types construits* en Terminale NSI: On s'intéresse d'abord à l'*interface* de ce nouveau type appelé `serpent`. Puis à son *implémentation*.

 * *interface*: Ce que réalisent les fonctions associées au type construit. Comment on les utilise.
 * *implémentation*: Programmation de ces fonctions.

# Annexe
[^1]: boucle principale du programme `snake.py`

```python
serpent = [(2,0),(2,1),(2,2)]

while True:
    incli_X = accelerometer.get_x()
    incli_Y = accelerometer.get_y()
    if abs(incli_X ) > abs(incli_Y):
        if incli_X > 20:
            direction = "D"
        elif incli_X < -20:
            direction = "G"
        else:
            direction = "-"
    else:
        if incli_Y < -20:
            direction = "B"
        elif incli_Y > 20:
            direction = "H"
        else:
            direction = "-"

    x, y =  tete(serpent)
    if direction != "-":
        x, y = deplace(direction, x, y)
        ajoute_tete(serpent, x, y)
        supprime_queue(serpent)
    sleep(100)
    display.clear()
    affiche(serpent)
```

