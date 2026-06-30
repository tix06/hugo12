---
Title: MB sons
description: jouer des sons avec le HP de la carte microbit
weight: 19
---

# Jouer un son

Jouer des sons (qui ne sont pas des notes de musique) avec un HP branché sur pin0:

```python
from microbit import *
import music
for i in range (1,11):
  music.pitch(100*i, 2000, pin0)
  print('son de freq ', i*100, ' Hz')
``` 

# Ecrire une partition de musique, avec des notes 

Instruction : `NOTE[octave][:durée]` 

```python
from microbit import *
import music
tune = ["C4:4", "D4:4", "E4:4", "C4:4", "C4:4", "D4:4", "E4:4", "C4:4", "E4:4", "F4:4", "G4:8", "E4:4", "F4:4", "G4:8"]
music.play(tune)
```
