---
Title: Tkinter les bases
description: Tkinter les bases
weight: 8
---

# Tkinter les bases
* télécharger le dossier zip:{{< a link="/scripts/Tkinter/tuto_tkinter.zip" caption="tuto_tkinter.zip" >}}* le placer dans vos *Documents*
* Extraire tout
* Ouvrir le fichier *main.py* avec un IDE Python de la suite Winpython


## Import des modules
Le module `tkinter` apporte l'environnement graphique.

Le module `PIL` permet la gestion des images.

Démarrer votre fichier par:

```python
from tkinter import *
from PIL import Image, ImageTk
```

## Créer une fenêtre Tkinter
La fenêtre est un objet de la classe `Tk`. Pour l'exemple qui suit, on lui donne le nom de `fen1`. 

On créé un objet fenêtre à partir de l'instruction: `fen1 = Tk()`

La dernière ligne permet d'afficher la fenêtre à l'écran. Il faudra auparavent ajouter les *objets esclaves*.

```python
if __name__ == '__main__':
    fen1 = Tk()
    # ajouter des objets esclaves à la fenêtre
    # puis finir par:
    fen1.mainloop()
```

## Objets esclaves
Ces objets sont à ajouter à `fen1`, une fois celle-ci créé. Donc après `fen1 = Tk()`

### Canvas
C'est la partie de la fenêtre dans laquelle on dessine.

On commence par créer un objet canvas appelé ici `can1`: c'est l'instruction `can1 = Canvas(fen1, ...arguments...)`. Les arguments vont permettre de choisir par exemple la largeur en pixel du canvas (*width*) et sa hauteur (*height*).

Puis on positionne `can1` avec la méthode `pack`. Sans cette deuxième ligne `can1.pack(side=LEFT, padx=5, pady=5)`, l'objet esclave est créé mais non attaché à la fenêtre (et donc n'apparait pas).

```python
if __name__ == '__main__':
    ...
    can1 = Canvas(fen1, bg='dark grey', height=400, width=600)
    can1.pack(side=LEFT, padx=5, pady=5)
```

### des boutons
Les boutons vont permettre d'appeler des fonctions lorsque l'on clique dessus.

Par exemple, le bouton 1, `bou1` va appeler une fonction de `fen1` héritée lors de sa création à partir de la classe `Tk`. C'est la fonction `quit`.

Et le bouton 1, `bou2`, va appeler la fonction `replay` qu'il vous faudra programmer. Que voudrez vous qu'il se passe lorsque l'on clique sur ce bouton...? Effacer le canvas, dessiner une grille,...?

```python
if __name__ == '__main__':
    ...
    # un bouton
    bou1 = Button(fen1, text='Quitter', command=fen1.quit)
    bou1.pack(side=BOTTOM)
    # un autre bouton
    bou2 = Button(fen1, text='(Re)Jouer', command=replay)
    bou2.pack()
``` 

*Remarques:* en python, il est possible de mettre en argument d'une fonction une autre fonction. C'est ce qui est réalisé ici, avec les fonctions `fen1.quit` et `replay`. On appelle ces fonctions sans mettre de parenthèses: on écrit `replay` et non `replay()`.

### Etiquette: Label
On peut écrire un texte dont le contenu sera evolutif, comme un panneau d'affichage dont le contenu est variable:

```python
if __name__ == '__main__':
    ...
    text_affichage = StringVar()
    txt1 = Label(fen1, textvariable=text_affichage, justify=LEFT, font='TkFixedFont')
    txt1.pack()
    text_affichage.set("Cliquer sur \n le bouton \n pour demarrer")
```

Plus tard, dans le programme, il suffira d'écrire `text_affichage.set("nouveau \n message")` pour afficher un *nouveau message*, à la même place.

### textBox
Equivalent de `input` mais pour l'environnement tkinter. Il faudra definir le champs de saisie (objet Text), et le bouton pour validation:

```python
if __name__ == '__main__':
    ...
    # Une textBox
    textBox = Text(fen1, height=1, width=15)
    textBox.pack()
    # Bouton pour valider la saisie
    bou3 = Button(fen1, text='Valider', command=readtext)
    bou3.pack()
```

Il faudra alors programmer la fonction de rappel `readtext`:

```python
def readtext():
    result=textBox.get("1.0","end")
    text_affichage.set(result)
```



### Image dans le canvas
Plusieurs étapes sont necessaires pour:

* ouvrir une image du dossier
* redimensionner l'image
* créer un objet image à partir du module tkinter: `image_bomb`
* dessiner l'image dans le canvas à la position 100 * 100

```python
if __name__ == '__main__':
    ...
    # une image de dimension 50 pixels * 50 pixels 
    image = Image.open("images/bomb.png")
    image = image.resize((50, 50), Image.ANTIALIAS)
    image_bomb = ImageTk.PhotoImage(image)
    bomb = can1.create_image(100, 100, anchor="nw", image=image_bomb)
```

Plus loin dans le programme, il suffira d'écrire `bomb = can1.create_image(200, 200, anchor="nw", image=image_bomb)` pour dessiner l'image à la position 200 * 200 par exemple.

### Dessiner dans le canvas
**Dessiner un carré**<br>
On utilise la méthode: `.create_rectangle(X0, Y0, X1, Y1)`<br>
X, Y sont les coordonnées du coin supérieur gauche du carré.<br>
Il peut y avoir des paramètres optionnels.

{{< img src="../images/tkinter_rect.png" >}}
*Exemple: pour dessiner un carré de côté r dans le canvas:*

```python 
can1.create_rectangle(X, Y, X + r, Y + r, outline='black', fill=couleur)
```

**Dessiner un cercle:**<br>
On utilise la méthode: `.create_oval(x-r, y-r, x+r, y+r)` 

{{< img src="../images/tkinter_oval.png" >}}
**Dessiner une ligne:**<br>
On utilise la méthode: `.create_line(x0, y0, x1, y1)` 

{{< img src="../images/pendu.png" caption="Exemple: le jeu du pendu" >}}
# Evenements
## Gestion d'un clic de souris dans le canvas
Pour ajouter un écouteur de clic dans le canvas, il faut ajouter dans le bloc principal (après avoir créé l'objet `fen1` et `can1`:

```python
if __name__ == '__main__':
  ...
  can1.bind('<Button-1>', clic)
  ...
```

Ici, la fonction qui sera appelée lorsque l'on clique avec le bouton gauche de la souris dans le canvas est la fonction`clic` qu'il faudra programmer.

Lors de l'appel de cette fonction, il ne faut pas ajouter d'agument ni de parenthèses.

On peut par exemple vouloir afficher les coordonnées de la souris lors du clic:

```python
def clic(event):
    """ Gestion de l'événement clic gauche sur la zone graphique """
    # MODE JEU
    # (X,Y) : position du pointeur de la souris
    X = event.x
    Y = event.y
    text_affichage.set("{}, {}".format(X,Y))
```

*Remarque:* la fonction de rappel `clic` a un paramètre obligatoire, `event` lors de sa création.

## Cliquer sur une image
Pour ajouter un ecouteur de clic sur une image, on procède d'une manière presque identique:

Après avoir placé l'image dans le canvas, on lui associe une fonction de rappel:

```python
if __name__ == '__main__':
    ...
    # Pierre
    image = Image.open("images/pierre.png")
    image = image.resize((image.size[0] // 2, image.size[1] // 2), Image.ANTIALIAS)
    photo_pierre = ImageTk.PhotoImage(image)

    pierre = can1.create_image(0, 0, anchor="nw", image=photo_pierre)
    can1.tag_bind(pierre, "<ButtonRelease>", play_pierre)
    ...
```

Ici, la fonction de rappel sera `play_pierre`. Le clic sur cette image pourra peut-être afficher un message:

```python
def play_pierre(event):
    texte = "Joueur joue: \n PIERRE"
    text_affichage.set(texte)
``` 

## Gestion des touches du clavier
De nombreux jeux utilisent les touches du clavier pour commandes. L'écoute du clavier se fait avec `fen1.bind("<Key>", nom_de_la_fonction_de_rappel)`:

```python
if __name__ == '__main__':
    ...
    fen1.bind("<Key>", clavier)
    ...
```


On peut alors programmer une fonction de rappel `clavier` qui affiche le caractère appuyé:

```python
def clavier(event):
    t = event.keysym
    text_affichage.set("Touche pressée : {}".format(t))
```

# Exemples
## Exemple 1: dessiner une grille
Souvent, le jeu utilise un quadrillage sur tout le canvas.

On peut programmer une fonction `carre` qui dessine un carré de côté r, puis appeler cette fonction lors du dessin initial, dans une autre fonction.

```python
def carre(r, X, Y, couleur):
    """
    dessine le contour d'une case colorée
    """
    can1.create_rectangle(X, Y, X + r, Y + r, outline='black', fill=couleur)
```  

La fonction qui dessine le fond quadrillé utilisera 2 boucles bornées imbriquées. Si chaque carré a pour côté H: L'idée est d'utiliser les dimensions du canvas pour avoir un nombre entier de carrés de côtés H:

```python
    for j in range(int(can1['height']) // H):
        for i in range(int(can1['width']) // H):
            carre(H,...
``` 


*famille de jeux: le morpion, puissance 4, echecs, demineur*

## Exemple 2: dessiner selon le texte saisi
On pourrait *dessiner avec un ordre*: la fonction de rappel  `readtext` pourrait évaluer les caractères saisis, et, s'il s'agit de:

* `tete`: dessiner la tête du personnage
* `corps`: dessiner le corps
* `bras`: dessiner ses bras
* `jambes`: dessiner ses jambes

*famille de jeux: jeu de devinette, jeu de rôle, jeu du pendu*

## Exemple 3: ajouter une image lors d'un clic
Avec la fonction `clic`, on peut créer une nouvelle image dans le canvas avec:

```python
def clic(event):
    """ Gestion de l'événement clic gauche sur la zone graphique """
    # MODE JEU
    # (X,Y) : position du pointeur de la souris
    X = event.x
    Y = event.y
    bomb = can1.create_image(X, Y, anchor="nw", image=image_bomb)
```  


Le mieux, serait d'aligner l'image sur la grille de fond lorsque l'on clique dans l'une des cases du quadrillage.

Si les carrés ont pour côté H: Il faudra que X et Y soient multiples de H. 

**Utiliser la division entière:** 

`X = (X // H) * H` 

et `Y = (Y // H) * H` 

*famille de jeux: demineur, puissance 4, morpion* 

