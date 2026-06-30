---
Title: Capteur lumiere
description: capteur integre, mesure et detection de clarté obscurité, chaine de caracteres
weight: 19
---

# Capteur de luminosité
## Le projet 
Le projet consiste à créer un motif lumineux sur la grille de DEL de la carte micro:bit. La nature du motif et l'intensité des DEL dépendra de la lumière ambiante: l'affichage sera plus lumineux si l'environnement est sombre.

{{< img src="../images/soleillune.png" caption="clair- obscur" >}}

## Prise en main du capteur
Pour ce projet, le panneau de DEL peut être utilisé en capteur de luminosité basique en inversant la polarisation des DEL. 

Celles-ci sont alors utilisées comme capteur de lumière.

{{< img src="../images/DEL_lumi.png" >}}

Le capteur de lumière de la micro:bit mesure la lumière dans une gamme allant de 0 (très sombre) à 255 (très lumineuse).


La mesure du niveau de luminosité passe par la commande ci-dessous.

```python
from microbit import *
display.read_light_level()
```

On peut stocker cette valeur dans une variable, par exemple:

```python
from microbit import *
lumi = display.read_light_level()
```

Il est possible d'afficher la valeur mesurée. En respectant une pause entre 2 valeurs mesurées cela donne:

```python
from microbit import *

while True:
    lumi = display.read_light_level()
    display.scroll(lumi)
    sleep(100)
```

## Version 1 du projet: Seuil de lumière
> Ajouter des branchements sur la variable `lumi` dans le programme pour actionner un *smiley* qui depend de la mesure (clarté/obscurité). 

* Il faudra prévoir un seuil de luminosité pour basculer d'un *smiley* à un autre *smiley*.

* Et mettre l'ensemble dans une boucle `while True:`, comme par exemple:

```python
# script 1
from microbit import *

while True:
    lumi = display.read_light_level()
    if lumi ... ...:
        ...
    else:
        ...
```

La surface de DEL alterne alors entre mesure d'intensité et affichage. D'où le clignottement.

**Question a:** Programmez la premiere version de ce projet, appelée *script 1. Recopier le script sur votre feuille.

## Version 2 du projet: afficher une forme personnalisée
On peut fabriquer nos propres images à partir de chaine de caractère utilisant des chiffres de 0 à 9.

Le script suivant donne un carré de plus forte intensité:

```python
from microbit import *
motif = '99999:90009:90009:90009:99999:'
img = Image(motif)
display.show(img)
```

{{< img src="../images/lumi2.jpg" >}}

Le script suivant donne un carré de plus faible intensité:

```python
from microbit import *
motif = '11111:10001:10001:10001:11111:'
img = Image(motif)
display.show(img)
```

{{< img src="../images/lumi1.jpg" >}}


> Adapter le script 1 pour afficher un carré très lumineux lorsqu'il fait sombre, ou faiblement lumineux lorsqu'il fait clair. Appeler ce nouveau script: *script 2*

**Question b:** Concevoir et tester le script 2. Recopier le script sur votre feuille.


## Version 3: Affichage d'intensité variable
L'intensité lumineuse du motif affiché dépend de la valeur attribuée à chaque pixel:

* '99999:90009:90009:90009:99999:': motif d'intensité forte
* '33333:30003:30003:30003:33333:' motif d'intensité intermédiaire
* '11111:10001:10001:10001:11111:': motif d'intensité faible

On peut créer une chaine de caractères en fonction d'une variable `I` qui varie de 0 à 9 et qui dessine un motif carré. Les 2 premieres lignes du motif sont construites à partir de:

```
motif = str(I + I + I + I + I + ":" + I + "000" + I + ":")
```

La valeur de `I` sera calculée d'après la variable `lumi`selon la loi:

```python
I = int((255 - lumi)/255*9)
```

Le programme principal du script 3 (à compléter) sera alors:

```python
while True:
    lumi = display.read_light_level()
    I = ...
    motif = ...
    img = Image(...)
    display.show(img)
```

> Afficher avec le script 3 un carré dont l'intensité lumineuse varie entre 0 et 9 selon l'intensité lumineuse mesurée. Tester et mettre au point le programme. 

**Question c:** Recopier sur votre feuille le script 3.


## Prolongement 1: utiliser des fonctions
Le script 3 peut être amélioré en utilisant des *fonctions*.
Le programme principal:

```python
while True:
	lumi = display.read_light_level()
	I = intensite(lumi)
	motif = carre(I)
	img = Image(motif)
	display.show(img)
```

> Ajouter les definitions des fonctions `intensite` et `carre` au script 3. Appeler ce nouveau script: le *script 4*.


**Aides:**

1. La fonction `intensite` retourne une valeur de 0 à 9 selon la variable `lumi` en argument:

```python
def intensite(lumi):
	"""retourne une valeur de 0 a 9
	9 <=> lumi = 0
	0 <=> lumi = 255
	Exemples:
	>>> I = intensite(255)
	>>> print(I)
	0
	>>> I = intensite(0)
	>>> print(I)
	9
	"""
	return int((255 - lumi)/255*9)
```

2. La fonction `carre` qui prendra en paramètre la valeur `I`, retourne une chaine de caractères dans le bon format pour dessiner les contours d'un *carré* vide en son centre.

```python
def carre(I):
	"""
	>>> carre(9)
	'99999:90009:90009:90009:99999:'
	>>> carre(1)
	'11111:10001:10001:10001:11111:'
	>>> carre(5)
	'55555:50005:50005:50005:55555:'
	"""
	return ... ... ...
```


**Question d:** Programmez et testez le script 4. Recopiez le sur votre feuille.


## Prolongement 2: motif animé
On pourra remplacer l'image fixe par une animation. Il faudra alterner avec 3 images successives, et attendre un delai de 100ms entre chaque. Utiliser pour cela la fonction `sleep(100)` entre chaque affichage.

{{< img src="../images/lumi3.GIF" >}}

Et ajuster l'intensité lumineuse du motif affiché selon l'éclairage mesuré (voir script 4).


# Documentation
* TP inspiré du document de [Formation_Microbit_Lycee](https://xofe14.scenari-community.org/Publications/Formations/Formation_Microbit_Lycee/co/CapteurLuminosite.html)