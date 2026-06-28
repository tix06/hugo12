---
Title: TP pixel art
description: TP python, tableaux, codage d'une image numerique, microbit
weight: 15
---

# Pixel art
## Codage d'une image numérique
Une image numérique est constituée de **pixels** juxtaposés dont on règle l’intensité lumineuse. 
L’image suivante montre le caractère a obtenu en remplissant judicieusement la grille de pixels de 5 pixels * 6 pixels.
C’est en prenant un recul suffisant que l’image retrouve sa finesse, et que les pixels se mélangent pour former la lettre a.

Ici, l’image est en noir et blanc. Les pixels ont une intensité que l’on pourrait représenter par 0 ou 1.
Les pixels d’intensité lumineuse égale à 0 sont noirs. Ceux à 1 sont blancs.

{{< img src="../images/Abitmap.png" caption="détails du caractère a" >}}
On pourrait représenter chaque ligne de cette image par une liste de valeurs 0 ou 1 :

ligne1 = [1, 0, 0, 0, 1]

L’image entière serait alors une liste de listes (une liste contenant les listes de chaque ligne).
On donne ci-contre un extrait :

`image = [[1, 0, 0, 0, 1], [1, 1, 1, 1, 0], … [1, 0, 0, 0, 0] ]`

ou bien, sur plusieurs lignes:

```python
image = [[1, 0, 0, 0, 1],
         [1, 1, 1, 1, 0],
          . . .  
         [1, 0, 0, 0, 0] ]
``` 

> **à vous de jouer:** Compléter la liste contenant l'image du bateau. 

## L’écran LED de la carte microbit
La carte microbit est un microcontrôleur que l'on peut programmer en Python. Cette carte dispose de capteurs intégrés (temperature, luminosité, champ magnétique), peut communiquer par ondes radio.

Et surtout, elle dispose d'un écran de diodes électroluminescentes (DEL), que l'on peut allumer en fonctions des coordonnées x, y de ces diodes.

{{< img src="../images/display.png" caption="coordonnée pour chacune des DEL x,y" >}}
La grille de DEL de la carte microbit est constituée d’un plan de 5 * 5 LED.
L’intensité lumineuse est ajustable avec une valeur entre 0 à 9. 
La valeur 0 correspondant à la LED éteinte, 9, allumée au maximum.
Il y a donc 10 niveaux d’éclairement, pour chaque pixel.

```
# instruction pour allumer une DEL en x,y
display.set_pixel(x,y, 9)
# instruction pour éteindre une DEL en x,y
display.set_pixel(x,y, 0)
```

## Le simulateur de carte microbit
### Programmer l'affichage d'une image
Imaginons que nous ayons à créer une structure de données qui contienne l’image d’un bateau. 

{{< img src="../images/boat.png" caption="deux mâts dessiné avec un tableau de DEL 5 x 5" >}}
On propose le programme suivant en langage Python:



<iframe width='100%' height='500' allowfullscreen frameborder='0' style='border:1px #d6d6d6 solid;' src="https://fr.vittascience.com/microbit/?link=606cc7ccd1533&mode=code"></iframe>

Pour lancer le simulateur, appuyer sur le bouton ![](../images/play.png)

Pour revenir au script, appuyer à nouveau sur ![](../images/play.png)

Le programme de la carte microbit contient en général une boucle qui est répétée indéfiniment: `while True` à la ligne 12.

Dans le bloc qui est répété:

* la boucle bornée `for` à la ligne 12 créé une variable j, qui prend successivement les valeurs 0, 1, 2, 3 et 4. Ces valeurs correspondent aux coordonnées x des DEL à allumer.
* à la ligne 13: la structure conditionnnelle `if` teste si l'élément de la liste x = j et y = 0 est égal à 1:
  * s'il est égal à 1: on allume la DEL en (x,y) = (j,0)
  * sinon, on laisse éteint

Ce programme ne sert donc qu'à allumer les DEL de la première ligne, celle de rang 0.

### Afficher l'image entière
Pour afficher l'image entière, il faudra aussi parcourir les lignes 1, 2, 3 et 4 de la liste.

On pourrait adapter le script en ajoutant dans le bloc `while True:`

```python
  for j in range(5):
    if L[1][j] == 1:
      display.set_pixel(j,1, 9)
  
  for j in range(5):
    if L[2][j] == 1:
      display.set_pixel(j,2, 9)

  for j in range(5):
    if L[3][j] == 1:
      display.set_pixel(j,3, 9)
  . . .
``` 

> **à vous de jouer:** compléter le script précédent, directement dans la fenêtre d'édition, afin d'afficher l'image entière.

### Amélioration du script
Comme vous l'imaginez, il sera possible d'eviter toutes ces répétitions grâce à l'ajout d'une nouvelle boucle `for`. La structure devrait ressembler à ceci:

```python
while True:
  for j in range(5):
    for i in range(5):
      if L[j][i] ... : 
        display.set_pixel( . . . )
```

> Modifier le script pour utiliser une deuxième boucle `for i in range(5)` comme dans l'exemple donné ci-dessus.


### Créez votre propre logo
Utiliser la grille ci-dessous pour créer votre propre logo, avec une grille de 5 * 5 DEL. Programmer ensuite son affichage sur la carte microbit.

{{< img src="../images/grille.png" caption="grille à compléter" >}}