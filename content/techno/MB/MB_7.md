---
Title: affichage 7 segments
description: extension avec affichage sept segments
hidden: true
weight: 25
---

# Utiliser un affichage à 7 segments

## Principe
On affiche les valeurs retournées par le capteur interne de température sur le dispositif d'affichage LED 7 segments.

L'afficheur sera banché sur le port grove PIN0.

{{< img src="../images/MB_7.jpeg" caption="afficheur à LED" >}}
## Matériel

* microcontrôleur microbit et shield grove
* composant grove avec affichage LED à 7 segments

## Script


```python
from microbit import *

ASCII_4DD_NUM = bytearray(b'\x3F\x06\x5B\x4F\x66\x6D\x7D\x07\x7F\x6F')

def start4dd(clk,dio):
  dio.write_digital(0)
  clk.write_digital(0)

def stop4dd(clk,dio):
  dio.write_digital(0)
  clk.write_digital(1)
  dio.write_digital(1)

def writeByte4dd(clk,dio,cmd):
  for i in range(8):
    dio.write_digital((cmd>>i)&1)
    clk.write_digital(1)
    clk.write_digital(0)
  clk.write_digital(0)
  clk.write_digital(1)
  clk.write_digital(0)

def command4dd(clk,dio,cmd):
  start4dd(clk,dio)
  writeByte4dd(clk,dio,cmd)
  stop4dd(clk,dio)

def init4dd(clk,dio):
  command4dd(clk,dio,0x40)
  command4dd(clk,dio,0x88|6)

def write4dd(clk,dio,s,p=0):
  if not 0<=p<=3:
    raise ValueError('Position out of range')
  command4dd(clk,dio,0x40)
  start4dd(clk,dio)
  writeByte4dd(clk,dio,0xC0|p)
  for i in s:
    writeByte4dd(clk,dio,i)
  stop4dd(clk,dio)
  command4dd(clk,dio,0x88|6)

def encodeNum(str):
  s=bytearray(len(str))
  for i in range(len(str)):
    o=ord(str[i])
    if o>=48 and o<=57:
      s[i]=ASCII_4DD_NUM[o-48]
  return s

def setNumber(clk,dio,n):
  if not -999<=n<=9999:
    raise ValueError('Number out of range')
  write4dd(clk,dio,encodeNum('{0: >4d}'.format(int(n))))

init4dd(pin0, pin14)

Afficheur = None

while True:
  Afficheur = temperature()
  setNumber(pin0, pin14, Afficheur)
  display.scroll(Afficheur)
  sleep(1000)
```

