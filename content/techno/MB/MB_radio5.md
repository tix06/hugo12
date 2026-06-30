---
Title: Chiffrement
description: TP chiffrement a partir d'un reseau de cartes microbits communiquant par radio, niveau term NSI
weight: 28
---

*Séance qui comporte 3 TP:*

* Communication radio, programmation POO: [page1](../MB_radio3)
* Authentification: [Projet 1](../MB_radio4)
* Chiffrement: [Projet 2](../MB_radio5)

# Projet 2: Chiffrement
> But: réaliser une communication privée dans un reseau public.

## Premier programme utilisant un notebook python
**Chiffrer / Code Cesar:** Le code César réalise une permutation des caractères, selon leur rang (table ASCII), grâce à une clé de chiffrement/ déchiffrement.

Les fonctions utiles du langage sont: `ord` et `chr`:

```python
>>> ord('a')
97
>>> chr(98)
'b'
>>> chr(122)
'z'
``` 

Pour utiliser une clé de chiffrement, il sera nécessaire d'utiliser un décalage avec un modulo(26) afin d'obtenir une lettre chiffrée dans l'alphabet a-z:

```python
no_lettre = ord(lettre)
chiffre = no_lettre + cle # decalage sans modulo, depassement possible
chiffre = (lettre + cle)%26 # decalage avec modulo 26, chiffre de 0 à 25
chiffre = (lettre-97 + cle)%26 + 97 # decalage avec modulo 26, chiffre de 97 à (97 + 25) = 122
``` 

Comme l'alphabet a-z va du rang 97 à 122 dans la table ascii, on choisira la 3e méthode:

```
chiffre = (lettre-97 + cle)%26 + 97
```

> Créer une fonction de chiffrement appelée `chiffre`, qui retourne la lettre chiffrée selon les arguments `lettre` (lettre en clair) et `cle` (la clé de chiffrement).


La fonction chiffre peut aussi servir à déchiffrer. Il suffira de remplacer la clé de chiffrement par son opposé: $3 => -3$.

Assurez vous à l'aide de quelques tests, que la fonction donne de bons résultats, pour chiffrer et dechiffrer un caractère.

> Créer une fonction de chiffrement appelée `chiffre_texte`, qui retourne la texte chiffré. La fonction aura pour arguments: `texte` (texte en clair) et `cle` (la clé de chiffrement).

Assurez vous à l'aide de quelques tests, que la fonction donne de bons résultats, pour chiffrer et dechiffrer un texte.

## Programmation de la carte microbit
Editeur [Vittascience.com](https://fr.vittascience.com/microbit/?mode=mixed&console=bottom&toolbox=vittascience)

> Adapter le programme pour permettre une communication *confidentielle* entre 2 cartes microbit. Décrire le programme avec un diagramme d'état.

# Projet 3: Compteur de *likes*
## Programme
On considère le réseau social de type "X (ex Twitter)" dans lequel A, B, C, et D sont des usagers (des twittos)

* A suit B
* B suit C
* C suit A et B
* D suit B

La structure de données sera un *dictionnaire* Python: 

```python
# un exemple de dictionnaire représentant un graphe à 4 cartes
G = {'A':['B'],'B':['C'],'C':['A','B'],'D':['B']}
```

Vous allez expérimenter la chaine de messages dans ce réseau social.

* Chaque twittos envoie, régulièrement, un message sur le reseau:

Ce message contient pour unique contenu le mot *Publi*. L'émetteur du message devra s'identifier lorsqu'il fait une *publi*:

```python
# pour le twittos B
radio.send("B_Publi")
```

Lorsque A reçoit un message de B (c'est à dire le message qui commence par `"B"`): comme `"B"` est dans sa liste `self.reseau['A'], A envoie un like à B. (un message `"B_LIKE"`). Et affiche un smiley HAPPY:

```python
display.show(Image.HEART)
utime.sleep(0.2)
display.clear()
```

Si B reçoit le message `"B_LIKE"`. Il verifie que le premier caractère `n` correspond à son propre numero de carte (`n == self.numero`). il affiche un COEUR, puis la valeur de son compteur, incrémentée de 1.


> Démarrer le programme de manière synchrone sur chaque carte microbit du reseau. Faites une publication de manière régulière (chronométer). Expérimenter pendant 2 à 5 minutes, puis relever les valeurs des compteurs sur chaque carte.

Les valeurs sont-elles en accord avec la structure du reseau?

> Redigez une description de votre programme, de votre experimentation, ainsi qu'un commentaire des résultats.

## Aide
On utilisera la classe: 

```python
class Communication_radio:
  def __init__(self, ch=7,gpe=0,messages=['LIKE','Publi'],numero='A', reseau = {'A':['B'],'B':['A']}):
    self.channel = ch
    self.group = gpe
    self.messages = messages
    self.img = [Image.DIAMOND,Image.DIAMOND_SMALL]
    self.numero = numero
    self.reseau = reseau
    self.compteur = 0
  
  def select_message(self):
    message_complet = str(self.numero) + "_" + self.messages[1]
    return message_complet
  
  def img_send(self):
    display.show(self.img,delay=100)
    utime.sleep(0.015)
    display.clear()
    
  def parse(self,stringData):
    """decoupage de stringData en une chaine n ('A, 'B', ...)
    et un texte grace a la methode split('_')
    returns:
    --------
    - etat du compteur +1 si n == self.numero ET texte == 'LIKE'
    - 'LIKE' si n est le numero d'un compte suivi ET texte == 'Publi'. Et emission radio avec radio.send('n_LIKE')
    - '', string vide, si n ne correspond a aucun des 2 cas precedents
    """
    # a completer
```

Le travail demandé consiste alors à compléter la méthode de classe `parse`. Il est conseillé de bien comprendre la correction du Projet 1 avant de commencer: [Solution du projet_authentifier_POO.py](/scripts/radio_microbit/projet2_authentifier_POO.py)

Après l'import des librairies, et la déclaration de la classe `Communication_radio`, le programme sera le suivant:

```python
# Attention a changer le 4e argument par la lettre attribuee a votre carte ('A', 'B', ...)
# modifier aussi le reseau {'A':['B'],'B':['A']} si vous avez plus
# de 4 cartes
com = Communication_radio(7,0,['LIKE','Publi'],'B',{'A':['B'],'B':['A']})
radio.on()
radio.config(channel = com.channel, power = 6, length = 32, group=com.group)
   
while True:
  if button_a.is_pressed():
    radio.send(com.select_message())
    com.img_send() # affiche l'animation lors de l'envoi du message

  stringData = radio.receive()
  if stringData:
    texte = com.parse(stringData)
    if texte == 'LIKE':
      display.show(Image.HAPPY)
      utime.sleep(0.4)
      display.clear()
    else:
        display.scroll(texte)
        utime.sleep(0.4)
        display.clear()  
```

*Correction:* [script](/scripts/radio/compteur_LIKE.py)
