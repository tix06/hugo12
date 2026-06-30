---
Title: reseau radio 1ere
description: programmation de la carte microbit, fonction radio, niveau 1ere NSI
weight: 25
---

# Communication radio
Une présentation générale de la carte microbit et des editeurs pour sa programmation se trouve à la page [MB_init](../MB_init). Ce TP fait suite à celui de SNT, à la page [MB radio](../MB_radio).

La carte microbit possède une antenne radio, ce qui lui permet d'emettre et de recevoir des messages:

{{< img src="../images/archi_MB.png" caption="source: microbit.org" >}}

## Prise en main de l'interface microbit sur Vittascience
*Ce premier travail permet de découvrir l'interface Vittascience.com pour la programmation de la carte microbit. Les questions qui suivent cette manipulation vont permettre d'approfondir les connaissances en langage Python. Les projets qui complètent cette séquence se basent sur la partie RESEAUX du programme (protocole HTTP, securité des transmissions)*

* Aller à la page [Editeur microbit](https://fr.vittascience.com/microbit/?mode=mixed&console=bottom&toolbox=vittascience) sur Vittascience.com

* Brancher la carte microbit sur l'un des ports USB de l'ordinateur. La carte est alors visible depuis l'explorateur comme une nouvelle mémoire flash.

# Réseau privé, public
## Programmation du script initial
> Créer pas à pas le programme suivant à l'aide de l'[Editeur microbit](https://fr.vittascience.com/microbit/?mode=mixed&console=bottom&toolbox=vittascience) sur Vittascience.com

{{< img src="../images/E_R_MB.png" caption="communication radio en reseau" >}}

Commencer par écrire les instructions de debut du programme (ne sont executées qu'une seule fois, au démarrage).

{{< img src="../images/radio1.png" >}}

{{< img src="../images/radio2.png" >}}

Puis ajouter les instructions de la boucle principale: d'abord les instructions d'émission:
{{< img src="../images/radio3.png" >}}

{{< img src="../images/radio4.png" >}}

Puis les instructions de reception:
{{< img src="../images/radio5.png" >}}

{{< img src="../images/radio6.png" >}}

Retrouver la variable `stringData` dans les *Variables*
{{< img src="../images/radio71.png" >}}

Placer la variable `stringData` dans l'expression conditionnelle:
{{< img src="../images/radio7.png" >}}

Retrouver le paramètre `" "` dans le menu *Texte*

{{< img src="../images/radio72.png" >}}

Remplacer le paramètre **1** par le caractère **"1"**:
{{< img src="../images/radio81.png" >}}

Puis les instructions pour le comportement de la carte selon le message reçu:
{{< img src="../images/radio8.png" >}}

{{< img src="../images/radio9.png" >}}

{{< img src="../images/radio10.png" >}}



> A. Téléverser et tester le programme. 

> B. Compléter le code python obtenu:

```python
from microbit import *
import radio
import utime

radio.on()
radio.config(channel = 7, power = 6, length = 32, group=0)
print('Bonjour !' + "")

while ...:
  if button_a.is_pressed():
    ...
  if button_b.is_pressed():
    ...
  stringData = radio.receive()
  if stringData:
    if stringData == '1':
      display.show(...
      utime.sleep(0.015)
      display.clear()
    elif stringData == '2':
      display.show(...
      utime.sleep(0.015)
      display.clear()

```

1. Quel est la signification de chacune des instructions suivantes?

| instruction | description |
|--- |--- |
| `if stringData:` |   |
| `if stringData == '1':` |   |

2. Le programme utilise des instructions apportées par les librairies `radio` et `utime`, utiles pour la programmation de la carte microbit. 

* Quel est le rôle des fonctions suivantes: Recopier et compléter le tableau:

| instruction | description |
|--- |--- |
| `send` |   |
| `receive` |   |
| `sleep` |   |

* Quel est le rôle de la variable `stringData`? *(Que contient-elle?)*

3. Analyse du programme: Décrire le programme avec un [diagramme d'activité](/pdf/NSI_1/diagramme_activite2.pdf).

3. Ce programme, comment devrait-il fonctionner? Quel-s problème-s voyez-vous lorsque plusieurs cartes microbits fonctionnent de concert, avec ce même programme?

{{< img src="../images/vitta_init8.png" >}}

> Pour communiquer à 2 cartes microbit, dans un reseau privé, vous pouvez choisir votre valeur pour `radio.config(group=0)`, comme par exemple `radio.config(group=1)`, ... (maximum 255).

4. Choisir le-s terme-s adapté-s parmi les mots suivants: il s'agit d'un problème de...

* intégrité
* authenticité
* confidentialité



## Projet 1: Générateur de messages
> But: On améliore le dispositif pour faire une selection parmi plusieurs messages (au moins 3). Les messages peuvent être des textes brefs, ou bien des messages de reaction de type LIKE/ UNLIKE.

{{< img src="../images/radio_13.png" caption="discussion" >}}

### Compléments théoriques: index modulo avec `%`
Cette fois, le nombre de messages possibles est supérieur au nombre de boutons (3 messages pour 2 boutons).

Nous allons utiliser une **liste** de messages. Pour acceder à un element de cette liste, nous allons utiliser un **index**. *Exemple:*


```python
# declaration de la liste
L = ['mon message a envoyer', 'LIKE', 'UNLIKE']
# acceder a l'un des elements de la liste:
# 1er element: index 0
print(L[0])
# 2e element: index 1
print(L[1])
# 3e element: index 2
print(L[2])
# attention au depassement d'index de la liste
# l'index 3 n'existe pas
print(L[3])
```

On peut utiliser un index numérique pour parcourir tous les éléments de la liste. *Exemple:*

```python
for i in range(len(L)):
  print(i,L[i])
# affiche:
0 mon message a envoyer
1 LIKE
2 UNLIKE
``` 

Là aussi, avec un variant de boucle `i` qui depasse 2, cela va générer une erreur:

```python
for i in range(10):
  print(i,L[i])
# affiche:
0 mon message a envoyer
1 LIKE
2 UNLIKE
# IndexError
``` 

Pour eviter de depasser l'index maximum de la liste, utiliser l'opérateur *modulo*:

```python
for i in range(10):
  j = i % 3
  print(i,j,L[j])
# affiche
0 0  mon message a envoyer
1 1  LIKE
2 2  UNLIKE
3 0  mon message a envoyer
4 1  LIKE
5 2  UNLIKE
6 0  mon message a envoyer
7 1  LIKE
8 2  UNLIKE
9 0  mon message a envoyer
``` 

On a alors une selection **periodique** des éléments de liste.

### Programmation de la carte microbit
Utiliser maintenant l'interface Python sur [Vittascience.com](https://fr.vittascience.com/microbit/?mode=mixed&console=bottom&toolbox=vittascience) pour réaliser les modifications.

* Bloc "Au démarrage": régler les cartes par binome sur le **même reseau** (même *canal*, et même *group*).

{{< img src="../images/vitta_init12.png" >}}

* Dans le bloc: Répéter indéfiniment (`while True`), il faudra modifier le rôle des boutons et le comportement lorsqu'un message est reçu.

{{< img src="../images/radio11.png" caption="rôle des boutons a et b" >}}

#### Bouton a
* le **bouton_a** sert à selectionner le message dans une liste, en passant au message suivant dans la liste. L'indice est calculé selon une règle d'arithmétique modulaire. Voici un extrait du script à utiliser:

```python
# a placer au "demarrage"
L = ['message', 'like', 'unlike']
i = 0
...
# a placer dans le bloc "repeter indefiniment"
if button_a.is_pressed():
  i = (i+1)%3
...
if button_b.is_pressed():
  radio.send(L[i])
```

* *[En option] Ajout d'un repère visuel*: On peut ajouter un repère visuel pour la selection du message. On éclaire alors la diode de la *première ligne* (`y=0`), dont la position `x` correspond à l'index `x=i`. Cela donne: `display.set_pixel(i,0,9)`

```python
if button_a.is_pressed():
  i = (i+1)%3
  display.clear()
  display.set_pixel(i,0,9)
  utime.sleep(0.2)
```

Les 2 autres instructions servent à effacer l'écran `display.clear()`, et à placer un délai d'attente `utime.sleep(0.2)`, necessaire pour eviter de nombreux appuis prolongés sur le bouton.



#### Bouton b

* Le **bouton_b** servira à envoyer le message.

```python
if button_b.is_pressed():
    radio.send(messages[i])
```

* On pourra placer un repère visuel qui montre l'envoi du message:

```python
if button_b.is_pressed():
    radio.send(messages[i])
    display.show([Image.DIAMOND,Image.DIAMOND_SMALL],delay=100)
    utime.sleep(0.015)
    display.clear()
```

#### Reception d'un message
Lorsqu'un message est reçu:


* **if**, si c'est 'like', on affiche un smiley happy
* **elif**, sinon si c'est 'unlike', on affiche un smiley triste
* **else**, sinon, c'est un message textuel, on l'affiche avec `display.scroll(stringData)`

> Vous avez reussi à échanger des messages avec votre binôme? Poursuivre cette séance avec les 2 projets suivants.

## Projet 2: Auteurs authentifiés
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

Le programme recepteur pourra afficher la chaine de caractère entière, renseignant à la fois le numéro de la carte emettrice ET le message.


Pour lire le numéro au début du message, il faudra PARSER la chaine reçue. *Parser* signifie: *diviser une chaîne de caractères en une liste ordonnée de sous-chaînes*.

Python offre une multitude de possibilités pour travailler avec des chaînes de caractères (strings): voir [page du cours python sur les variables et string](/docs/python/pages/variables/page1/) 



### Rappels: Comment parser une chaine?
Dans un notebook (Atrium > Capytale) ou bien [basthon.fr/](https://notebook.basthon.fr/), saisir les lignes suivantes:

* Composer le message:

```python
n = 1
texte = "la feve est dans la 3e part"
message = str(n) + "_" + texte
print(message)
```

* Parser le message avec un *Slice*:

Il faudra tranformer la chaine `"1_la feve est dans la 3e part"` en 2 chaines: `"1"` et `"la feve est dans la 3e part"`.

```python
message = "1_la feve est dans la 3e part"
n = message[0]
# selection du 1er caractere
print(n) # affiche: 1
message = message[2:]
# slice du 3e caractere au dernier
print(message) # affiche: la feve est dans la 3e part
# on a extrait le numero au debut du message, et reduit le message
print("la carte n°",n," vous informe que\n", message)
```

* Ou **mieux**, parser le message avec la méthode de chaine `split`:

```python
message = "1_la feve est dans la 3e part"
L = message.split('_')
# L vaut ['1','la feve est dans la 3e part']
n = L[0]
message = L[1]
```

> Pour traiter un message dont l'identifiant numérique est composé de **2 chiffres**: Quelle méthode vaut-il mieux privilegier?


### Programmation de la carte microbit
> Adapter le programme pour permettre une communication avec un auteur *authentifié* dans un reseau à plusieurs cartes. 

{{< img src="../images/vitta_init111.png" >}}

Vous allez mettre *2 cartes microbits ou plus* dans un même réseau privé (Réglage dans l'instruction `radio.config(channel = 7, power = 6, length = 32, group=0)`). Choisir le même *channel* et le **même** *group* pour les cartes microbit du même **groupe**.


Utiliser l'interface Python sur [Vittascience.com](https://fr.vittascience.com/microbit/?mode=mixed&console=bottom&toolbox=vittascience).

A partir du programme initial, apporter les modifications pour:

1. Choisir un numero pour votre groupe privé que vous placerez dans `groupe_prive`. Modifiez votre `message` à envoyer.
2. Ecrire une fonction `parse` qui prend en paramètre une chaine de caractère `message`, et un caractère de separation `sep`. Cette fonction doit retourner une liste `L` constituée de 2 éléments: `L[0]` contient le numero du groupe et `L[1]` le message placé après le caractère de séparation. 
3. Ajouter à votre script la fonction `test_parse()` qui teste le bon fonctionnement de la fonction `parse`:

```python
def test_parse():
  assert parse("1_les carrotes sont cuites","_") == ["1","les carrotes sont cuites"]
  assert parse("1_2_3","_") == ["1","2"]
```

Ajouter aussi l'appel de la fonction `parse_test()` dans le corps de votre programme.

4. Lorsque l'on appuie sur le bouton `b`: envoyer un message avec un numero d'identification à 2 chiffres. Ce numero doit être le même pour toutes les cartes microbits du même reseau privé. Le message sera mis en forme avec `str(groupe_prive) + "_" + message`
5. `parser` et afficher tout message qui commence par le bon identifiant, pas les autres messages reçus. Il faudra utiliser une instruction conditionnelle sur le numéro de carte pour afficher (ou non) le message.

*Votre script devrait avoir les instructions suivantes:*

```python
from microbit import *
import radio
import utime

groupe_prive = ...
radio.on()
radio.config(channel = 7, power = 6, length = 32, group=groupe_prive)
message = "message a personnaliser" # personnalisez votre message

def parse(message,sep):
  """retourne une liste constituée de 2 elements
  decoupe de la chaine message autour du caractere sep
  """
  pass

def test_parse():
  assert parse("1_les carrotes sont cuites","_") == ["1","les carrotes sont cuites"]
  assert parse("1_2_3","_") == ["1","2"]

test_parse()

while True:
  if button_b.is_pressed():
    radio.send(...
  stringData = radio.receive()
  if stringData:
    ...
```




> Tester le bon fonctionnement de votre programme dans un reseau contenant plusieurs cartes microbits. Décrivez le reseau (nombre de cartes microbit de chaque groupe et numeros de ces groupes).

## Projet 3: Chiffrement
> But: réaliser une communication privée dans un reseau public.

### Premier programme utilisant un notebook python
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

### Programmation de la carte microbit
[Vittascience.com](https://fr.vittascience.com/microbit/?mode=mixed&console=bottom&toolbox=vittascience)

> Adapter le programme pour permettre une communication *confidentielle* entre 2 cartes microbit. Décrire le programme avec un diagramme d'état.



# Compléments
`radio.config(channel=7)`: Configure la fréquence d'émission : la valeur est un numéro entre 0 et 83

`radio.config(group=0)`:  Configure le groupe : au sein d'une même adresse, 256 groupes numérotés de 0 à 255 peuvent cohabiter`

*programme de base pour faire communiquer 2 cartes microbit:*

```python
from microbit import *
import radio
import utime

radio.on()
radio.config(channel = 7, power = 6, length = 32, group=0)
print('Bonjour !' + "")

while True:
  if button_a.is_pressed():
    radio.send('1')
  if button_b.is_pressed():
    radio.send('2')
  stringData = radio.receive()
  if stringData:
    if stringData == '1':
      display.show(Image.HAPPY)
      utime.sleep(0.015)
      display.clear()
    elif stringData == '2':
      display.show(Image.SAD)
      utime.sleep(0.015)
      display.clear()

```

# Le reseau *mesh*


{{< img src="../images/mesh.png" >}}

D'après un article du Monde (02/05/2026)

> Comment pourrait-on réaliser un reseau *mesh* pour la ville de Nice? Expliquer ce qu'il faudrait utiliser en terme de matériel, de noeuds du reseau, ainsi qu'en terme de logiciels, pour assurer l'intégrité et la confidentialité.

{{< img src="../images/nice.png" >}}

# Liens
* Introduction au module radio (TP Lucioles): [microbit-micropython.readthedocs.io](https://microbit-micropython.readthedocs.io/fr/latest/tutorials/radio.html)
* TP message secret: [microbit.org](https://microbit.org/fr/projects/make-it-code-it/tell-me-a-secret/)
* specifications du contrôleur radio [lancaster-university](https://lancaster-university.github.io/microbit-docs/ubit/radio/)`
* diagramme d'état et diagramme d'activité: [www.uv.es](https://www.uv.es/nemiche/cursos/UML5.pdf)
* diagramme d'état [laurent-audibert.developpez.com](https://laurent-audibert.developpez.com/Cours-UML/?page=diagramme-etats-transitions)
