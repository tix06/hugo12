---
Title: MB grove
description: shield groove, capteurs passifs
weight: 16
---

# MB Grove : capteur luminosité

## Principe
La carte microbit associée au shield grove permet d'utiliser de nombreux *capteurs passifs*. L'instruction à utiliser: `pin0.read_analog()`. Cette instruction permet la lecture d'une tension de type analogique sur l'entrée PIN0, quel que soit le composant passif.

{{< img src="../images/MB_LDR_grove.jpeg" >}}

## Matériel

* carte microbit et shield grove
* capteur de luminosité grove ou autre capteur passif
* eventuellement: lampe de bureau, filtres occultants

## Script


```python
from microbit import *


while True:
    
    display.show(Image.SQUARE)
    sleep(1000)
    display.clear()
    display.scroll(pin0.read_analog())
```

# Liens
Voir exemples sur [http://ww2.ac-poitiers.fr/sc_phys/sites/sc_phys/IMG/pdf/prise_en_main_carte_microbit_langage_python.pdf](http://ww2.ac-poitiers.fr/sc_phys/sites/sc_phys/IMG/pdf/prise_en_main_carte_microbit_langage_python.pdf)
