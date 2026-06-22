---
Title: correction ascii-art
hidden: true
---

**correction ascii-art**


```python
from PIL import Image
from display_image import *

ascii_char = ' .:-=+*#%@'

with Image.open("Marylin-original.jpg") as image:
    image = image.resize((500,500))
#image.show()

fileout = open("ascii_art.txt","w")

for y in range(500):
    line = ""
    for x in range(500):
        rgb=image.getpixel((x,y)) # rgb est une liste (R,G,B) du pixel
        grey = (rgb[0]+rgb[1]+rgb[2])//3
        index = grey * 9 // 255
        line += ascii_char[index] + ' '
    #print(line)
    line += '\n'
    fileout.write(line)
fileout.close()

    
image = textfile_to_image('ascii_art.txt')
image.show()
image.save('ascii_art.png')
```