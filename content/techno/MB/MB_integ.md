---
Title : capteurs integres
description: capteurs de la carte microbit
weight: 15
---

# Capteurs intégrés
## Description
La carte microbit dispose de plusieurs capteurs intégrés:

* temperature
* acceleromètre à 3 axes
* mesure de champs magnétique
* luminosité

## Mesure d'horizontalité
### Principe
On utilisera le capteur "acceleromètre".

Le champs de pesanteur génère une force, le poids, qui peut être mesurée par l'acceleromètre. Une des applications principale des accéléromètres est le calcul d’inclinaison. Ca permet de savoir comment est orienté votre microcontrôleur par rapport à la terre. C'est ainsi que sur un smartphone, celui-ci passe du mode portrait au mode paysage par rotation d'un quart de tour.

C'est un composant électronique qui réalise cette mesure: une tige de silicium est chargée électriquement et la cage dans laquelle elle se trouve également, le déplacement de charges portée sur la tige est détectable et on en déduit le sens du déplacement.{{< a link="https://couleur-science.eu/?d=669308--comment-fonctionne-un-accelerometre-de-smartphone" caption="source" >}}
{{< img src="https://howtomechatronics.com/wp-content/uploads/2015/11/MEMS-Accelerometer-How-It-Works.jpg" link="http://howtomechatronics.com/how-it-works/electrical-engineering/mems-accelerometer-gyrocope-magnetometer-arduino/" caption="principe d’un accéléromètre électromécanique (la partie rouge se met en mouvement par rapport au reste et le décalage est détecté grace au déplacement de charge qu’elle porte) — " >}}
### Script 1
Ce programme lit les valeurs toutes les 100 ms et affiche une flèche correspondant à la direction du mouvement sur l’écran micro:bit.

La mesure de l'acceleration est faite dans la direction X:

{{< img src="../images/MB_3axes.png" >}}
```python
from microbit import *

while True:
    acc = accelerometer.get_x()
    if acc > 0:
        display.show(Image.ARROW_E)
    else:
        display.show(Image.ARROW_W)
    sleep(100) 
```

### Script 2
L’écran montre un pixel qui sera bien centré si le micro:bit est bien à l’horizontale ou qui sera décalé en direction de l’inclinaison dans le cas contraire. Le but est donc de mettre le micro:bit parfaitement à plat, de sorte qu’uniquement la LED centrale soit allumée. {{< a link="https://www.tigerjython4kids.ch/franz/drucken.php?inhalt_mitte=robotik/microbit/sensor.inc.php" caption="source" >}}
```python
from microbit import *

x = 1
y = 1

while True:
    accX = accelerometer.get_x()
    accY = accelerometer.get_y() 
    if accX > 100 and x < 4:
        x += 1
    elif accX < -100 and x > 0:
        x -= 1
    elif accY > 100 and y < 4:
        y += 1
    elif accY < -100 and y > 0:
        y -= 1
    display.clear()
    display.set_pixel(x, y, 9)
    sleep(100)
```

## Utilisation de la boussole

La boussole s'utilise avec `compass` mais elle doit etre calibrée avant utilisation : [voir doc](https://microbit-micropython.readthedocs.io/fr/latest/tutorials/direction.html)

L'instruction en micropython est: `compass.heading()` 

*Exemple:*

```python
from microbit import *

compass.calibrate()

while True:
    aiguille = ((15 - compass.heading()) // 30) % 12
    display.show(Image.ALL_CLOCKS[aiguille])
```

## Utilisation du thermomètre
L'instruction pour mesurer la température est: `temperature()`, que l'on peut afficher directement sur la carte avec `display.scroll(temperature())`.

Voir aussi l'exemple avec l'affichage à LED: [Lien](../MB_7/index.html)

# Liens 
[Vincent Le Mieux, www.laboiteaphysique.fr](https://www.isnbreizh.fr/nsi/activity/microbitRessources/assets/decouverte_microbit.pdf) 