---
Title: solution mastermind
hidden: true
---

*solution*

```python
#%% methode utilisant des listes
from random import choice

ordi = ""

for i in range(4):
    ordi += choice(('J','O','C','R','V'))
ordi = list(ordi)
print(ordi)

joueur = []
essais = 0
while joueur!= ordi and essais < 12:
    joueur = list(input("entrer une combinaison de 4 couleurs (JOCRV)"))
    correspond = ordi.copy()
    essais += 1
    B = 0
    N = 0
    for i in range(4):
        if joueur[i] == ordi[i]:
            N += 1
            correspond[i] = 'X'
            print('trouve {} à la position {} dans {}'.format(joueur[i],i,ordi))
    for i in range(4):
        if joueur[i] in correspond:
            j = correspond.index(joueur[i])
            print('joueur[{}] dans {} , index={}'.format(i,correspond,j))
            correspond[j] = 'X'
            B += 1
    print(ordi,correspond)
    print("B:{}, N: {}".format(B,N))
    
if joueur == ordi:
    print('c est gagné!')
else:
    print("perdu")
```

*Exemple d'utilisation:*

```
['R', 'J', 'V', 'J']
entrer une combinaison de 4 couleurs (JOCRV)JJJJ
trouve J à la position 1 dans ['R', 'J', 'V', 'J']
trouve J à la position 3 dans ['R', 'J', 'V', 'J']
['R', 'J', 'V', 'J'] ['R', 'X', 'V', 'X']
B:0, N: 2
entrer une combinaison de 4 couleurs (JOCRV)RJJV
trouve R à la position 0 dans ['R', 'J', 'V', 'J']
trouve J à la position 1 dans ['R', 'J', 'V', 'J']
joueur[1] dans ['X', 'X', 'V', 'J'] , index=3
joueur[3] dans ['X', 'X', 'V', 'X'] , index=2
['R', 'J', 'V', 'J'] ['X', 'X', 'X', 'X']
B:2, N: 2
entrer une combinaison de 4 couleurs (JOCRV)RJVJ
trouve R à la position 0 dans ['R', 'J', 'V', 'J']
trouve J à la position 1 dans ['R', 'J', 'V', 'J']
trouve V à la position 2 dans ['R', 'J', 'V', 'J']
trouve J à la position 3 dans ['R', 'J', 'V', 'J']
['R', 'J', 'V', 'J'] ['X', 'X', 'X', 'X']
B:0, N: 4
c est gagné!
```