---
Title: MB diviseur de tension
description: microbit CTN et pont diviseur de tension, capteur photosensible
weight: 18
---

# luminosité LDR et diviseur de tension

## Principe
La LDR est un composant électronique photosensible. Sa valeur de résistance diminue avec la luminosité.

Pour constater ces variations, on utilisera la LDR dans un montage type *diviseur de tension*.

Un seul des connecteurs *grove* de la carte micro:bit suffira pour alimenter le circuit et mesurer la tension au milieu du pont diviseur. Il faudra utiliser les connecteurs avec fils de couleur sur prise grove:

* Rouge: Alimentation fixe 3V avec l'instruction `pin0.write_digital(1)`
* Noir: GND
* Jaune: pour la mesure de tension avec l'instruction `pin0.read_analog()`

{{< img src="../images/MB_circuitD.png" caption="circuit avec LDR et Resistance" >}}
{{< img src="../images/MB_Div.JPG" caption="montage à réaliser" >}}
## Matériel

* carte micro:bit et shield grove
* fil de connexion grove-connecteurs couleur (rouge noir blanc jaune)
* pince crocodile
* Photoresistance type VT900 serie (light dependant resistor LDR)
* resistance de 10k&#8486;
* lampe de bureau (allumée/éteinte)
* filtres occultants
* multimètre


## Script

```python
# pin0 rouge : alim fixe 3V
# pin0 jaune : lecture tension
# pin0 noir : GND
from microbit import *

pin0.write_digital(1) # sortie 3V
while True:
    display.scroll(pin0.read_analog())
```

