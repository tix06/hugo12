---
Title : MB LED clignotante
description: shield groove, circuit electronique a LED
weight: 17
---

# LED clignotante

## Principe
On utilise le connecteur grove du microbit pour commander une sortie en tension. On pourra allumer, et faire clignoter une LED, branchée en série avec sa resistance de protection.

Il faudra utiliser les connecteurs avec fils de couleur sur prise grove:



* Jaune: tension commandée : relier au + de la LED  
* Noir: GND : relier à la resistance 1k
* Rouge (3V fixe) et Blanc: non utilisés

{{< img src="../images/led_pin.png" caption="circuit avec LED et Resistance" >}}
{{< img src="../images/MB_led.JPG" caption="montage complet" >}}

## Matériel

* carte micro:bit et shield grove
* fil de connexion grove-connecteurs couleur (rouge noir blanc jaune)
* pince crocodile
* Diode electroluminescente LED
* resistance de 1k&#8486;
* multimètre


## Script

```python
# Jaune: tension commandée : relier au + de la LED  
# Noir: GND : relier à la resistance 1k
# Rouge et Blanc: non utilisés
from microbit import *

while True:
    pin0.write_digital(1) # sortie 3V
    sleep(1000)
    pin0.write_digital(0)
    sleep(1000)
```
