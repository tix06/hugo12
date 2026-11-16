---
Title: correction ascii-art partie 1
hidden: true
weight: 23
---

**correction ascii-art : partie 1**

## Bloc 1 – La palette de caractères

```python
ascii_char = ' .:-=+*#%@'
```

1. `len(ascii_char)` vaut **10**.
2. `ascii_char[0]` vaut `' '` (l'espace), `ascii_char[9]` et `ascii_char[-1]` valent tous les deux `'@'` (le dernier caractère).
3. `ascii_char[10]` provoque une erreur `IndexError: string index out of range` : la chaîne contient 10 caractères, numérotés de 0 à 9.
4. Le plus clair est l'espace `' '` (aucune encre), le plus foncé est `'@'` (le plus rempli).

## Bloc 2 – Du pixel RGB au niveau de gris

| pixel `rgb` | `grey = (r+g+b)//3` | `index = grey*9//255` | caractère `ascii_char[index]` |
|---|---|---|---|
| (0, 0, 0) | 0 | 0 | `' '` |
| (255, 255, 255) | 255 | 9 | `'@'` |
| (120, 60, 30) | 70 | 2 | `':'` |
| (200, 200, 100) | 166 | 5 | `'+'` |

5.
```python
def gris(rgb):
    return (rgb[0] + rgb[1] + rgb[2]) // 3

print(gris((120, 60, 30)))   # 70
```

6. `/` renvoie un nombre décimal (`float`). Or l'indice d'un caractère dans une chaîne doit être un **entier** : `ascii_char[2.7]` provoque l'erreur `TypeError: string indices must be integers`.

7. Le niveau de gris maximal est 255. Avec 10 : `255 * 10 // 255 = 10`, et `ascii_char[10]` n'existe pas (question 3). Le plus grand indice possible est 9, c'est-à-dire `len(ascii_char) - 1` :
```python
index = grey * (len(ascii_char) - 1) // 255
```

8. Un pixel blanc (255) donne l'indice 9, donc `'@'`, le caractère le plus **foncé** : ce n'est pas cohérent, l'image serait en négatif. Il faut inverser le niveau de gris :
```python
index = (255 - grey) * 9 // 255
```
Blanc : `(255 - 255) * 9 // 255 = 0` → `' '` ; noir : `(255 - 0) * 9 // 255 = 9` → `'@'`.

## Bloc 3 – Boucles imbriquées

9.
```python
for y in range(4):
    line = ""
    for x in range(10):
        line += '#'
    print(line)
```

10.
```python
ascii_char = ' .:-=+*#%@'
for y in range(10):
    line = ""
    for x in range(20):
        line += ascii_char[y]
    print(line)
```

11. Si la boucle sur `x` est à l'extérieur, chaque chaîne `line` construite contient les pixels d'une **colonne** et non d'une ligne. Une fois écrites les unes sous les autres, les colonnes deviennent des lignes : l'image est retournée (symétrie par rapport à la diagonale, elle apparaît couchée).

12. Un caractère est environ deux fois plus haut que large. Sans espace, l'image apparaîtrait écrasée horizontalement (étirée en hauteur). En ajoutant un espace, chaque pixel occupe deux largeurs de caractère, ce qui rétablit à peu près les proportions.

## Bloc 4 – Une mini-image « à la main »

13. `image[2][0]` vaut **0**. Le premier indice est la ligne (`y`), le second la colonne (`x`) : on écrit `image[y][x]`.
*Attention : avec PIL, c'est l'inverse, on écrit `getpixel((x, y))`.*

14.
```python
ascii_char = ' .:-=+*#%@'

for y in range(len(image)):
    line = ""
    for x in range(len(image[y])):
        grey = image[y][x]
        index = (255 - grey) * 9 // 255
        line += ascii_char[index] + ' '
    print(line)
```
Résultat : l'image représente un smiley.
```
    @ @     
  @     @   
@         @ 
@   @ @   @ 
  @     @   
    @ @     
```

15.
```python
ascii_char = ' .:-=+*#%@'

fileout = open("mini.txt", "w")
for y in range(len(image)):
    line = ""
    for x in range(len(image[y])):
        grey = image[y][x]
        index = (255 - grey) * 9 // 255
        line += ascii_char[index] + ' '
    line += '\n'
    fileout.write(line)
fileout.close()
```

16. Pour `mini.txt` : 6 pixels × 2 caractères (symbole + espace) + `'\n'` = **13 caractères** par ligne.
Pour l'image de 500 × 500 : 500 × 2 + 1 = **1001 caractères** par ligne.

## Bloc 5 – Premier contact avec PIL

```python
from PIL import Image
image = Image.open("Marylin-original.jpg")
```

17.
```python
print(image.size)   # (largeur, hauteur) de l'image en pixels
print(image.mode)   # 'RGB'
```
`image.size` est un tuple (largeur, hauteur) en pixels. `image.mode` vaut `'RGB'` : chaque pixel est décrit par trois composantes rouge, vert, bleu.

18.
```python
pixel = image.getpixel((0, 0))
print(pixel, type(pixel))   # par exemple (231, 228, 223) <class 'tuple'>
```
Le résultat est un **tuple** de 3 entiers entre 0 et 255 : les intensités de rouge, de vert et de bleu du pixel en haut à gauche.

19.
```python
image = image.resize((50, 50))
print(image.size)                  # (50, 50)
print(image.getpixel((25, 25)))    # couleur (R, G, B) du pixel central
```
