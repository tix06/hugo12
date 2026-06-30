--- 
Title: radio MB projet 1
description: TP authentification des emetteurs recepteurs radio
hidden: true
weight: 27
--- 

*Séance qui comporte 3 TP:*

* Communication radio, programmation POO: [page1](../MB_radio3)
* Authentification: [Projet 1](../MB_radio4)
* Chiffrement: [Projet 2](../MB_radio5)

solution du premier script: Communication radio, programmation POO: [correction](/scripts/radio_microbit/script_poo.py)
# Projet 1
> But: Utiliser une règle d'authentification entre 2 cartes de votre réseau privé.

Votre reseau privé n'est pas à l'abris d'un utilisateur non invité. Vous souhaiteriez alors savoir de QUI vient le message reçu. 

{{< img src="../images/radio_12.png" >}}



L'idée est d'utiliser la chaine de caractère émise pour y placer des informations, en plus du message. Ces informations pourraient identifier la carte émettrice. Ainsi, plutôt que d'envoyer:

```
"le lundi ne mange pas a la cantine"
```

la carte n°1 enverra: 

```
"1_le lundi ne mange pas a la cantine"
```

Le programme recepteur pourra afficher les seuls messages qui proviennent de la carte amie (n°1 par exemple), pas les autres.

Pour les recepteurs du message, il faudra alors PARSER cette chaine. *Parser* signifie: *diviser une chaîne de caractères en une liste de sous-chaînes*.

Python offre une multitude de possibilités pour travailler avec des chaînes de caractères (strings): voir [page du cours python sur les variables et string](/docs/python/pages/variables/page1/) 



## Premier programme utilisant un notebook python
Dans un notebook (Atrium > Capytale) ou bien [basthon.fr/](https://notebook.basthon.fr/), saisir les lignes suivantes:

* Dans une première cellule: composer le message:

```python
n = 1
texte = "la feve est dans la 3e part"
message = str(n) + "_" + texte
print(message)
```

* Dans une autre cellule: Parser le message:

Il faudra tranformer la chaine `"1_la feve est dans la 3e part"` en 2 chaines: `"1"` et `"la feve est dans la 3e part"`.

```python
message = "1_la feve est dans la 3e part"
n = message[0]
# selection du 1er caractere
print(n)
message = message[2:]
# slice du 3e caractere au dernier
print(message)
# on a extrait le numero au debut du message, et reduit le message
print("la carte n°",n," vous informe que\n", message)
```

* 3e cellule du notebook: Parser avec la méthode de string `split`:

```python
message = "98_la feve est dans la 3e part"
n, texte = message.split('_')
print(n)
print(texte)
```

> Quel avantage voyez vous avec la seconde méthode (`split`)?

* Certains messages reçus peuvent être formatés différemment: Il se peut que ceux-ci ne comportent pas de séparateur  `_`. Après tout, vous pouvez recevoir des messages de très nombreux membres du reseau. 

```python
message = "la feve est dans la 3e part"
n, texte = message.split('_')
```

> Que se passe t-il si vous appliquez systématiquement la méthode `split` au message reçu? Le micro contrôleur va t-il s'arrêter de fonctionner?

* `try ... except`

```python
stringData = "98_la feve est dans la 3e part"
#stringData = "la feve est dans la 3e part"
try:
  n, texte = stringData.split('_')
except:
  # reception d'un message sans caractere '_'
  n= 0
  texte = stringData
```

> Tester le programme avec chacune des propositions pour `stringData`. Quel est le comportement de cette structure conditionnelle `try..except`?

## Programmation de la carte microbit
> Vous allez créer une communication avec un auteurs *authentifiés* dans un reseau à plusieurs cartes. 

Vous allez mettre 4 cartes microbits dans un même réseau (Réglage dans l'instruction `radio.config(channel = 7, power = 6, length = 32, group=0)`). Choisir le même *channel* et le **même** *group* pour **4 cartes microbit.**



Utiliser maintenant l'interface Python sur [Vittascience.com](https://fr.vittascience.com/microbit/?mode=mixed&console=bottom&toolbox=vittascience) pour réaliser les modifications.

### Etape 1
A partir du [programme initial](/scripts/radio_microbit/script_poo.py), apporter les modifications pour:

* envoyer un message avec un numero d'identification à 2 chiffres. Ce numero doit être le même pour les cartes microbits du micro-reseau, et doit rester secret. 
* afficher tout message qui commence par cet identifiant, pas les autres messages reçus. Il faudra utiliser une instruction conditionnelle sur le numéro de carte pour afficher (ou non) le message.

{{< img src="../images/vitta_init111.png" >}}

> Programmer les méthodes de la classe `Communication_radio`: 
>* la méthode `select_message` pour selectionner, et construire le message avant de l'expedier. 
>* Et la méthode `parse` pour lire le message. Cette méthode ne retourne la chaine de caractère QUE si le numero qui debute la chaine de caractères est celui du groupe.

Puis apporter les modifications necessaires pour faire fonctionner le programme.


**Aide:** ci-dessous le programme Python en programmation non fonctionnelle et non orientée objet. C'est le programme que vous devrez adapter en POO.

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
numero = 99

while True:
  if button_a.is_pressed():
    display.clear()
    l = len(messages)
    i = (i + 1) % l
    display.set_pixel(i,0,9)
    utime.sleep(0.2)
  if button_b.is_pressed():
    message_complet = str(numero) + "_" + messages[i]
    radio.send(message_complet)
    display.show(img,delay=100)
    utime.sleep(0.015)
    display.clear()
    

  stringData = radio.receive()
  if stringData:
    try:
      n, texte = stringData.split('_')
    except:
      # reception d'un message sans caractere '_'
      n= 0
      texte = stringData
    if int(n) == numero:
      if texte == 'LIKE':
        display.show(Image.HAPPY)
        utime.sleep(0.2)
        display.clear()
      elif texte == 'UNLIKE':
        display.show(Image.SAD)
        utime.sleep(0.2)
        display.clear()
      else:
        display.scroll(texte)

```

### Etape 2
Modifier le programme pour accepter les message d'un **groupe** d'amis ayant plusieurs numeros distincts d'identification. Il faudra:

* modifier l'attribut `nombre` pour qu'il ait le type `list`.
* et modifier les instructions où l'on interragit avec `nombre`

# Aide
Solution partielle: [projet2_0_authentifier_POO.py](/scripts/radio_microbit/projet2_0_authentifier_POO.py)

<!--
Solution: [projet_authentifier_POO.py](/scripts/radio_microbit/projet2_authentifier_POO.py)
-->

