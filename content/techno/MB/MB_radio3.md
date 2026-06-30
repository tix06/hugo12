---
Title: reseau radio term
description: sequence reseau de niveau terminale NSI
weight: 26
---

*Séance qui comporte 3 TP:*

* Communication radio, programmation POO: [page1](../MB_radio3)
* Authentification: [Projet 1](../MB_radio4)
* Chiffrement: [Projet 2](../MB_radio5)

# Communication radio
Une présentation générale de la carte microbit et des editeurs pour sa programmation se trouve à la page [MB_init](../MB_init). Ce TP fait suite à celui de 1ere NSI, à la page [MB radio2](../MB_radio2).

La carte microbit possède une antenne radio, ce qui lui permet d'emettre et de recevoir des messages:

{{< img src="../images/archi_MB.png" caption="source: microbit.org" >}}

## Prise en main de l'interface microbit sur Vittascience
*Ce premier travail permet de découvrir l'interface Vittascience.com pour la programmation de la carte microbit. Les questions qui suivent cette manipulation vont permettre d'approfondir les connaissances en langage Python. Les projets qui complètent cette séquence se basent sur la partie RESEAUX du programme (protocole HTTP, securité des transmissions)*

* Aller à la page [Editeur microbit](https://fr.vittascience.com/microbit/?mode=mixed&console=bottom&toolbox=vittascience) sur Vittascience.com

* Brancher la carte microbit sur l'un des ports USB de l'ordinateur. La carte est alors visible depuis l'explorateur comme une nouvelle mémoire flash.

# Réseau social, public
## Programmation du script initial
> Copier-coller le programme suivant à l'aide de l'[Editeur microbit](https://fr.vittascience.com/microbit/?mode=mixed&console=bottom&toolbox=vittascience) sur Vittascience.com


{{< img src="../images/E_R_MB.png" caption="communication radio en reseau" >}}

```python
from microbit import *
import radio
import utime

# variables globales
ch = 7
gpe = 0
messages = ['lundi','LIKE','UNLIKE']
i = 0
img = [Image.DIAMOND,Image.DIAMOND_SMALL]
# parametres radio
radio.on()
radio.config(channel = ch, power = 6, length = 32, group=gpe)

while True:
  if button_a.is_pressed():
    display.clear()
    l = len(messages)
    i = (i + 1) % l
    display.set_pixel(i,0,9)
    utime.sleep(0.2)
  if button_b.is_pressed():
    radio.send(messages[i])
    display.show(img,delay=100)
    utime.sleep(0.015)
    display.clear()
    

  stringData = radio.receive()
  if stringData:
    if stringData == 'LIKE':
      display.show(Image.HAPPY)
      utime.sleep(0.2)
      display.clear()
    elif stringData == 'UNLIKE':
      display.show(Image.SAD)
      utime.sleep(0.2)
      display.clear()
    else:
      display.scroll(stringData)

```

> Téléverser et tester le programme. 

1. Quel est la signification de chacune des instructions suivantes?

| instruction | description |
|--- |--- |
| `if stringData:` |   |
| `if stringData == 'LIKE':` |   |

2. Le programme utilise des instructions apportées par les librairies `radio` et `utime`, utiles pour la programmation de la carte microbit. 

* Quel est le rôle des fonctions suivantes: Recopier et compléter le tableau:

| instruction | description |
|--- |--- |
| `send` |   |
| `receive` |   |
| `sleep` |   |

* Quel est le rôle de la variable `stringData`? *(Que contient-elle?)*

3. Selection de message:
Expliquez le rôle des instructions suivantes:

```python
l = len(messages)
i = (i + 1) % l
```

4. Analyse du programme: Décrire le programme avec un [diagramme d'activités](/pdf/SNT/diagramme_activite.pdf) (exemple à la page 4).

5. Ce programme, comment devrait-il fonctionner? Quel-s problème-s voyez-vous lorsque plusieurs cartes microbits fonctionnent de concert, avec ce même programme?

{{< img src="../images/vitta_init8.png" >}}

6. Choisir le-s terme-s adapté-s parmi les mots suivants: il s'agit d'un problème de...

* intégrité
* authenticité
* confidentialité



## Programmation orientée objet
On souhaite effacer du programme les variables globales. Les variables  seront regroupées comme attributs de la classe `Communication_radio`. On ajoutera à cette classe les méthodes qui serviront à rendre le script plus concis.

Voici le script que vous allez utiliser: **Créer un nouveau fichier, coller ce nouveau script et complétez le pour qu'il soit fonctionnel.**

```python
from microbit import *
import radio
import utime


class Communication_radio:
  def __init__(self, # a completer)
    # a completer
  
  def message_suivant(self):
    # a completer
  
  def select_message(self):
    # a completer
  
  def img_send(self):
    # a completer


com = Communication_radio(7,0,['lundi','LIKE','UNLIKE'])
radio.on()
radio.config(channel = com.channel, power = 6, length = 32, group=com.group)
   
while True:
  if button_a.is_pressed():
    com.message_suivant()
  if button_b.is_pressed():
    radio.send(com.select_message())
    com.img_send() # affiche l'animation lors de l'envoi du message

  stringData = radio.receive()
  if stringData:
    if stringData == 'LIKE':
      display.show(Image.HAPPY)
      utime.sleep(0.2)
      display.clear()
    elif stringData == 'UNLIKE':
      display.show(Image.SAD)
      utime.sleep(0.2)
      display.clear()
    else:
      display.scroll(stringData)
```






**Question:** quelles sont les différentes méthodes que vous pouvez envisager pour que la communication entre 2 cartes microbit reste confidentielle?

{{< img src="../images/vitta_init12.png" >}}

# Projets
> Poursuivre cette séance avec les 2 projets suivants.

* Authentification: [Projet 1](../MB_radio4)
* Chiffrement: [Projet 2](../MB_radio5)


# Compléments
`radio.config(channel=7)`: Configure la fréquence d'émission : la valeur est un numéro entre 0 et 83

`radio.config(group=0)`:  Configure le groupe : au sein d'une même adresse, 256 groupes numérotés de 0 à 255 peuvent cohabiter`

# Liens
* Introduction au module radio (TP Lucioles): [microbit-micropython.readthedocs.io](https://microbit-micropython.readthedocs.io/fr/latest/tutorials/radio.html)
* TP message secret: [microbit.org](https://microbit.org/fr/projects/make-it-code-it/tell-me-a-secret/)
* specifications du contrôleur radio [lancaster-university](https://lancaster-university.github.io/microbit-docs/ubit/radio/)`
* diagramme d'état et diagramme d'activité: [www.uv.es](https://www.uv.es/nemiche/cursos/UML5.pdf)
* diagramme d'état [laurent-audibert.developpez.com](https://laurent-audibert.developpez.com/Cours-UML/?page=diagramme-etats-transitions)
