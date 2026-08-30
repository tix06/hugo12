---
author: "Eric Tixidor"
date: 01-05-2021
linktitle: securite informatique
menu:
  main:
    parent: 
next: 
prev: 
title: Securite informatique
weight: 2
---

# Chiffrements symétriques
## Vocabulaire
* **Chiffrer:** transformer les caractères d'un texte pour le rendre incompréhensible, sauf pour celui qui possède la clé de chiffrement.
* **Déchiffrer:** transformer le texte chiffré en texte clair à l'aide de la clé de chiffrement
* **Décrypter:** transformer le texte chiffré en texte clair sans posséder la clé.
* **Cryptologie:** science du secret: possède deux branches
  * **cryptographie:** étude de l'art du chiffrement
  * **cryptanalyse:** analyse des méthodes de chiffrement pour les casser (décrypter)

## à quoi sert le chiffrement?
Le chiffrement a pour but de protéger nos données, nos communications, mais aussi de signer nos messages et de s'assurer que l'on communique bien avec la bonne personne:

* **Authentification**: L'authentification est la procédure qui consiste, pour un système informatique, à vérifier l'identité d'une entité (personne, programme, machine).
* **L'intégrité** des données désigne le fait que les données ne soient pas modifiées au cours d'une communication ou de leur stockage. <br>
Ainsi, si vous envoyez un texte chiffré sur un canal non sécurisé, le texte chiffré pourra être intercepté et altéré par un attaquant avant d'atteindre son destinataire. Pour contrôler cette intégrité, on associe au message une valeur de contrôle.
* **La confidentialité:** Le chiffrement permet de protéger la confidentialité de vos données à l'aide d'une clé secrète. 

## Le chiffrement par décalage, ou chiffre de Caesar
Le chiffre de César fonctionne par décalage des lettres de l'alphabet. 

<a href="https://fr.wikipedia.org/wiki/Chiffrement_par_décalage">
<figure>
  <img src="../images/Caesar3.png">
<figcaption>Chiffrement par décalage - wikipedia</figcaption>
</figure>
</a>

Cet algorithme de chiffrement utilise une fonction périodique pour transformer les rangs de chaque lettre:

| a | b | c | d | e | f | g | h | i | j | k | l | m | n | o | p | q | r | s | t | u | v | w | x | y | z |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24 | 25 | 26 |

<br>

> Compléter l'algorithme du chiffrement de César. On suppose qu'il existe une clé `c` correspondant au décalage utilisé. Le message clair est `m` et le message chiffré est `m_chiffre`

```python
Pour chaque lettre l du message m:
  l_chiffre = ...
  m_chiffre = ...
```

### Facilité du décryptage

> **Décryptage par FORCE BRUTE**: Combien y-a-t-il de clés possibles à essayer pour celui qui réalise le décryptage? Conclure.

### Un chiffrement par substitution monoalphabetique
Le chiffrement par  <a href="https://fr.wikipedia.org/wiki/Chiffrement_par_substitution">substitution monoalphabetique</a>: Chaque lettre de l'alphabet est transformée en une nouvelle lettre. Et cette nouvelle lettre est unique (sinon, il y aurait ambigüité, et le déchiffrement ne serait pas possible). Ici, la fonction utilisée pour le chiffrement de César, est un simple décalage:

$$x \rightarrow x + cle$$

Mais il peut y avoir d'autres fonctions plus complexes utilisées. Voire, même aucune fonction, mais une table de correspondance entre lettre en clair et symbole chiffré. La clé aurait alors la longueur de l'alphabet.

Le chiffrement par monosubstitution a été également utilisé par différentes méthodes utilisant une table.

<a href="<a href="https://fr.wikipedia.org/wiki/Carré_de_Polybe">
<figure>
  <img src="../images/polybe.png">
<figcaption>Carré de Polybe - le mot « bonjour » est ainsi chiffré par le carré de Polybe :12 34 33 24 34 45 42 - wikipedia</figcaption>
</figure>
</a>

Vous trouvez cette méthode de chiffrement trop simpliste? Regardez alors sa déclinaison avec le <a href="https://fr.wikipedia.org/wiki/Chiffre_de_Playfair">chiffrement de Playfair</a>, qui associe une clé à la table de Polybe, et rajoute du pseudo aléatoire dans le chiffrement:

<a href="https://www.youtube.com/watch?v=JMkGYoT3-Rw">
<figure>
  <img src="../images/playfair.png">
<figcaption>VIDEO: chiffrement de Playfair - youtube - Astuces et tutoriels</figcaption>
</figure>
</a>

### Decryptage par analyse fréquentielle
Le code issu du carré de Polybe a été utilisé par les prisonniers, qui transmettaient leur message en tapant sur les murs (<a href="https://fr.wikipedia.org/wiki/Tap_code">Tap code</a>).

Le **problème** avec ce type de chiffrement monoalphabetique, est qu'il est possible de repérer comment sont transformées certaines lettres à partir de l'**analyse fréquentielle** du message chiffré.

On peut alors utiliser la frequence des lettres pour dechiffrer et comparer avec la frequence moyenne dans une langue. (200 caracteres suffisent). Il y a aussi tout un tas de statistique, comme les lettres uniques, doubles lettres, finales, etc... C'est un marqueur suffisant pour savoir comment le code est fait.


<figure>
  <img src="../images/frequenceA_Z.gif">
<figcaption>frequence des lettres en français, calculée sur la lecture de plusieurs ouvrages classiques (10 millions de caracteres)</figcaption>
</figure>

Ce n'est pas le cas du chiffrement de Playfair, car celui-ci utilise une methode de substitution d'un groupe de lettres: c'est une substitution *polyalphabetique*.

### Une amélioration: Substitution polyalphabétique
L'analyse des fréquences est moins pertinente lorsque le message a été chiffré avec un chiffrement polyalphabétique (qui tend à rendre aléatoire la fréquence des lettres). <br>

**Polyalphabetique:** Se dit d'un chiffre où un groupe de n lettres est codé par un groupe de n symboles. Le chiffrement *Playfair*, vu plus haut s'apparente à une substitution polyalphabetique, puisqu'il substitue des digrammes (groupes de 2 lettres) dans le texte d'origine.

L'exemple suivant montre une polysubstitution simple avec une clé de longueur 3 qui va décaler les lettres de l'alphabet :

On définit la clé '123' qui indique que le premier caractère sera décalé d'une position, le second de 2 et le troisième de 3 positions, etc.

Le mot : WIKIPEDIA donne donc dans ce cas XKNJRHEKD.

Mais si on chiffre le mot : AAAAAAAAA cela donnera BCDBCDBCD. La lettre A ne donne pas toujours la même correspondance chiffrée. Mais on peut analyser la périodicité et en déduire la longueur de la clé. La connaissance de la longueur de la clé est essentielle pour pouvoir pratiquer l'analyse frequentielle.

La machine <a href="https://fr.wikipedia.org/wiki/Enigma_(machine)">Enigma</a> utilisait ce principe de codage.

<a href="https://fr.wikipedia.org/wiki/Enigma_(machine)">
<figure>
  <img src="../images/enigma.jpg">
<figcaption>Enigma est une machine électromécanique portative servant au chiffrement et au déchiffrement de l'information.  - wikipedia</figcaption>
</figure>
</a>

La machine utilise des rotors qui sont mis en position selon une clé. L'alphabet est chiffré selon la position initiale de ces rotors. Ceux-ci se décalent lors de l'utilisation. Ce qui modifie l'alphabet chiffré et augmente sérieusement la complexité.

Déchiffrer se fait avec la même machine, à condition d'utiliser la même clé.

Son utilisation la plus célèbre fut celle faite par l'Allemagne nazie, avant et pendant la Seconde Guerre mondiale, la machine étant réputée inviolable selon ses concepteurs. 

Le **principe de la machine Enigma était connu**. Le concepteur savait à l'avance que certains modèles pourraient être volés par les alliés. Ce qui fit son efficacité, c'est le nombre immense de combinaisons possibles pour les réglages initiaux de la machine et le choix de la clef brute du message.

Les cryptanalystes britanniques, dont <a href="https://fr.wikipedia.org/wiki/Alan_Turing">Alan Turing</a>, purent continuer les travaux du mathématicien polonais Marian Rejewski. Ils furent, dans des circonstances favorables, capables de decrypter les messages Enigma, ce qui donna un avantage certain aux alliés pendant la guerre.

### Points communs des chiffrements symétriques
Ces algorithmes fonctionnent selon:

- Entrée
- repetition n fois de substitutions et permutations. Utilise une clé unique pour chiffrer et dechiffrer.
- Sortie


# Fondamentaux de la cryptographie moderne
Les principes de Kerckhoff (6 principes, 3 restent aujourd'hui preponderants malgrès la difference de technologie)

1. Materiellement sûr: Si on a un temps infini, on finira par trouver le code, mais le message n'aura plus d'interêt. 
2. Ce n'est pas l'algorithme qui est secret, ce sont les paramètres. L'algorithme constitue un systeme de confiance. C'est d'ailleurs le même algorithme qui est utilisé par tout le monde et pour tout.
3. Il faut changer ou modifier la clé toutes les x utilisations.

Les effets recherchés:

- Diffusion: propriété où la redondance statistique dans un texte en clair est dissipée dans les statistiques du texte chiffré. (Claude Shannon).
- Confusion: correspond à une volonté de rendre la relation entre la clé de chiffrement et le texte chiffré la plus complexe possible (Claude Shannon).

*Consequence:* **L'effet d'avalanche:** une modification même minime en entrée va entrainer de grandes modifications en sortie.

# Chiffrements asymétriques
Pour le chiffrement symétrique, le seul secret, c'est la clé de chiffrement. Cette clé doit avoir, pour des raisons pratiques, une longueur raisonnable (64, 128, 256 bits). Ce chiffrement permet de communiquer de manière *confidentielle*, ou de préserver la *confidentialité* de nos données sur un disque dur. Le problème avec le seul chiffrement symétrique, c'est qu'il ne permet pas de repondre aux besoins d'*authentification* (reconnaitre l'identité) et d'*authenticité* (le message n'a pas été modifié).

Pour comprendre ces termes, on utilise le scenario suivant. Alice et Bob sont 2 personnes qui veulent echanger des messages de manière sécurisée. Une 3e personne, appelée *Trudy* joue le rôle d'un attaquant.

<figure>
  <img src="../images/trudy.png">
<figcaption>Le trio Alice - Bob - Trudy</figcaption>
</figure>

Le chiffrement asymétrique utilise plusieurs clés, une pour le chiffrement, et une autre pour le dechiffrement. Il repose sur des propriétés mathématiques de l'arithmetique modulaire. (voir principe du chiffrement RSA)


## Principe du chiffrement RSA
### Confidentialité
Il doit y avoir 2 clés. L'une de ces clés doit rester secrête, et conservée par l'expediteur du message: c'est la clé **privée**. L'autre clé utile pour le chiffrement et le dechiffrement est partagée: elle est dite **publique**. On peut indifféremment chiffrer avec la clé publique et déchiffrer avec celle privée, ou l'inverse.

<a href="https://youtu.be/8BM9LPDjOw0?t=268">
<figure>
  <img src="../images/scienceetonnante.png">
<figcaption>VIDEO chiffrement asymetrique (demarrer à 4min28) - chaine ScienceEtonnante</figcaption>
</figure>
</a>

Ainsi, comme la clé de Bob est publique, Alice peut utiliser cette clé pour chiffrer le message qu'elle veut lui envoyer, un peu comme si elle mettait le message dans un coffre (*celui de Bob*). Et Bob, qui possède la clé privée correspondante (la clé de *son* coffre) peut alors déchiffrer le message d'Alice.

<figure>
  <img src="../images/asymetric.png">
<figcaption>Chiffrement asymetrique</figcaption>
</figure>

### Authentification
On peut utiliser cet algorithme pour authentifier l'auteur du message, et réaliser une **signature numérique**.

Imaginons que Bob utilise sa clé *privée* pour chiffrer un message M. Il l'envoie à Alice, qui, en utilisant la clé publique de Bob, pourra le déchiffrer. Elle pourra ainsi s'assurer que Bob en est bien à l'origine et que son contenu n'a pas été modifié.

En effet, comme il est le seul à posséder la clé *privée*, ce message M vient bien de Bob.

> Compléter la situation où Bob envoie un message de type Bonjour à Alice, en utilisant sa clé privée:

<figure>
  <img src="../images/alicebob1.png">
<figcaption>Bonjour Alice - via chiffrement asymetrique</figcaption>
</figure>

Le point faible de cet échange vient de la distribution de la clé publique entre Bob et Alice.

Cet échange n'est réellement sécurisé qu'à la condition que la clé publique de Bob, vienne bien de Bob. Et que personne ne se soit introduit dans la discussion pour substituer la clé publique de Bob par la sienne (attaque de l'*homme du milieu*). 

> Compléter la situation suivante où Eve réalise une attaque dite de l'homme du milieu. Elle envoie au préalable sa propre clé publique à Alice et Bob. Puis elle se fait passer pour chacun des 2 lors de la discussion.


<figure>
  <img src="../images/alicebob2.png">
<figcaption>Bonjour Alice, bonjour Bob - Eve</figcaption>
</figure>

Pour s'authentifier, Bob doit d'abord envoyer à Alice un *certificat*, qui contient sa clé publique mais aussi d'autres informations qui permettent de verifier la validité de ce certificat, en particulier l'*emetteur*: le nom de l'autorité de certification, une *infrastructure à clé publique* (PKI) qui a validé l'identité de Bob.

**Certificats:** Les navigateurs permettent d'ouvrir les pages des sites qui ont pu être *authentifiés*. Pour faire ceci, les navigateurs intègrent un certain nombre de certificats reconnus. Pour les autres, ils utilisent une chaine de certification: les navigateurs font confiance à certaines autorités de certification, qui ont au préalable, certifié leurs clients (possesseurs de sites web).

Si la chaine de confiance est rompue, votre navigateur affiche cette image qui va certainement vous dissuader de poursuivre votre navigation:


<figure>
  <img src="../images/certificat.png">
<figcaption>certificat non reconnu</figcaption>
</figure>

En pratique, le certificat est un ensemble d'informations sur le propriétaire du domaine, la durée de validité, l'algorithme utilisé pour l'authentification, la clé publique, et surtout l'*emetteur*. Lorsqu'Alice reçoit le certificat que lui envoie Bob, elle consulte l'*emetteur* du certificat pour verifier qu'il s'agit bien du bon certificat, que celui-ci appartient bien à Bob.

<figure>
  <img src="../images/echange_certif.png">
<figcaption>procedure d'echange de certificat</figcaption>
</figure>

# Principe d'une communication securisée HTTPS
Lors d'une communication HTTPS: les objectifs d'authentification, authenticité et de confidentialité sont remplis. Lors du protocole de communication, les chiffrements asymétriques et symétriques sont tous 2 utilisés:

> Que Se Passe-t-il Entre un Navigateur Web (client) et un Serveur ?

* le client demande au serveur que celui-ci s'authentifie (1)
* Le serveur envoie au navigateur une copie de son certificat SSL (2)
* Le navigateur vérifie s'il fait confiance à ce certificat SSL. Si oui,le client envoie de manière sécurisée une clé de session qui servira pour la communication (3). L'envoie de la clé se fait à l'aide du chiffrement asymétrique (RSA). Le client utilise la clé publique du serveur pour cet envoi.
* Cette clé sera utilisée pour des chiffrements symétriques entre le client et le serveur (4).


<figure>
  <img src="../images/schema_ssl.jpg">
<a href="https://www.ovh.com/fr/ssl/fonctionnement-ssl.xml">
<figcaption>établissement d'une communication securisée - OVH</figcaption></a>
</figure>

> **Signature numérique:** Lorsqu'on utilise sa propre clé privée pour envoyer un message, et qu'une autorité de certification peut garantir l'origine de cette clé privée, alors ce message envoyé a valeur de signature numérique. Il permet d'authentifier l'emetteur du message.

# Exercices
## Substitution monoalphabétique: Code de César

* **Question 1:** Quelle clé a  été utilisée pour chiffer ce texte (avec l’algorithme de César)? 

<figure>
jyfwavnyhwopl hwwspxbll
</figure>

* **Question 2:** Décrypter ce message.



* **Question 3:** Proposer un programme en python qui chiffre un message clair `m` en un message codé selon la clé numérique `c`.

*Aide:* 

* La fonction `ord('x')` retourne un entier correspondant à la position d'un caractère dans la table ascii.<br>
Par exemple, `ord('A')` retourne 65, `ord('B')` retourne 66,...

* La fonction `chr(N)` retourne le caractère de rang N: `chr(65)` retourne 'A'.

## Substitution polyalphabétique: Chiffrement de Playfair
A partir des explications données dans la video:

* **Question 1:** Construisez la matrice pour l’algorithme de Playfair avec la clé *estienne*. 
* **Question 2:** Chiffrer le message: *COUPERLETRANSMETTEUR*.
* **Question 3:** S'agit-il d'une méthode utilisant la substitution monoalphabetique, ou polyalphabetique?
* **Question 4:** Est-ce qu'avec cette méthode, le decryptage peut être facilité par l'analyse fréquentielle? 

## Frequences des lettres dans un texte
La fonction suivante retourne une liste de 26 valeurs de type *float*, donnant dans l'ordre de l'alphabet, la frequence pour chaque lettre dans un texte:

```python
def freq(m):
    frequences = [0]*26
    n = len(m)
    for c in m:
    ...
```

* **Question 1:** Compléter le script de la fonction `freq`.

Soient les deux textes chiffrés suivants:

a. DGFHTMOMEIAMTLMFGOKFGOKEGDDTRWEIAKZGFGFSTEKGOMLASTTIFG FOSTLM FTFGOK MGWMFG OKRTSA JWTWTA WDTFMG FDAOLT WMOSSA FGOKET WKRWFD TEIAFM ROAZSG MOFKOT FFTXAW MLARGW ETWKJW AFROSD OAWSTA WDAMOF HGWKDT STEITK SADAOF

b. YOHGMV MFCBRB GWFNIZ ZPSURW FUOIPU WYITFA NIETGG DOCKAC PQE- BEW PMXEMK VGRAIL KWWXZO CILGPM QOVCGE GMYEBQ RYACJM WX- ULFR VQMDCY LZFYZM YTPCRF DCRJNS FIHIQG RZEPRC VWMDIL KGYDQO RVFMXM CRCNIM UGRBKR BOOIUG PQCBVZ NEYACE

* **Question 2:** L'un des 2 a été chiffré avec un algorithme de substitution mon-alphabetique, et l'autre, poly-alphabétique. Lequel est mono-alphabétique?


## Chiffrement symetrique par la fonction XOR
Cet exercice est inspiré du TP cryptographie du site de [hmalherbe.fe - NSI](http://hmalherbe.fr/thalesm/gestclasse/documents/Terminale_NSI/2020-2021/TP/TP_Term_NSI_cryptographie/TP_Term_NSI_cryptographie.html)

La fonction XOR est la fonction du OU EXCLUSIF.

* **Question 1:** Donner la table de vérité de la fonction XOR
* **Question 2:** Programmer la fonction `xor` en python qui retourne le resultat de XOR appliqué aux 2 paramètres a et b.

*Exemple:*

```
>>> xor(0,1)
>>> 1
```

On utilisera pour cet exercice les fonctions suivantes, qui permettent de transformer un texte en binaire, à partir du code ascii des lettres:

```python
def text2bin(texte):
    """ convertit une chaine de caracteres en binaire
    param:
    texte: str, une chaine de caracteres
    return:
    bin: str, une sequence de 8 bits par caracteres
    chaque sequence de 8 bits est la valeur du code ascii du caractere
    convertie en binaire (sur un octet)
    exemple:
    >>> text2bin('HELLO')
    >>> '0100100001000101010011000100110001001111'
    """
    bin = ''
    for l in texte:
        bits = f'{ord(l):b}'
        # f est une fonction de formatage et convertit
        # une valeur decimale ord(l) en binaire
        # ord(l) donne la valeur numerique correspondant au caractere ascii l
        oct = octet(bits)
        bin += oct
    return bin

def octet(bits):
    """ rajoute les 0 au nombre binaire pour mettre en format de 8 bits
    """
    byte = str(bits)
    for i in range(8-len(bits)):
        byte = '0' + byte
    return byte
```



* **Question 3:** programmer toutes ces fonctions dans un fichier python (ou un notebook). Tester en particulier la fonction `text2bin` sur un texte relativement court (2 caractères). Recopier le résultat obtenu.

La fonction suivante transforme une séquence de chiffres binaires en une valeur décimale:

```python
def bin2dec(oct):
    # oct est un str de 8 caracteres
    n = 0
    for i in range(len(oct)):
        n += int(oct[-i-1])*2**i
    return n
```

Exemple:

```
>>> bin2dec('001001')
>>> 9
```

* **Question 4:** Utiliser cette fonction pour écrire le script de `bin2text`, la fonction inverse de `text2bin`, qui, pour une sequence binaire donnée, de longueur multiple de 8 bits, retourne la chaine de caracteres correspondants.

Le XOR (OU exclusif) est très utilisé dans les protocoles de chiffrement symétrique. En effet, c’est une opération qui est sa propre réciproque, ce qui n’est pas le cas du ET ni du OU.

On souhaite chiffrer un message (par exemple une chaîne de caractères) à l’aide d’une clé binaire. Seuls des caractères ASCII sont utilisés.

* **Question 5:** Ecrire le script de cette fonction, que l'on appelera `chiffre_xor`. Cette fonction prend 2 paramètres: la séquence de bits à chiffrer, ainsi que la clé de chiffrement. Cette clé est de dimension inférieure ou égale au premier paramètre. Il faudra l'appliquer de manière périodique aux bits de la séquence à chiffrer (voir cours sur le chiffrement poly-alphabetique).
* **Question 6:** Utiliser les fonctions du programme pour: 
  * convertir un message secret en une sequence binaire
  * chiffrer cette sequence binaire avec l'algorithme XOR, en utilisant la clé `10101`
  * afficher le message chiffré
  * dechiffrer le message
  * afficher le message dechiffré


<!--
## Chiffrement asymetrique: Connaissance du cours

Que signifient les objectifs de confidentialité, intégrité, et authentification ?
-->




# Liens
* Chiffrement : notre antisèche pour l'expliquer à vos parents [article de NextImpact](https://www.nextinpact.com/article/24930/99777-chiffrement-notre-antiseche-pour-expliquer-a-vos-parents)
* Les certificats [article de NextImpact](https://www.nextinpact.com/article/21092/97852-de-cacert-a-lets-encrypt-longue-route-vers-https-pour-tous)
* autorité de certification [video Youtube - chaine de Yann Bidon](https://www.youtube.com/watch?v=FSq-FXx5dxU)
* sécurisez vos données avec la cryptographie [openclassroom](https://openclassrooms.com/fr/courses/1757741-securisez-vos-donnees-avec-la-cryptographie/6031870-controlez-lintegrite-de-vos-messages#:~:text=L'int%C3%A9grit%C3%A9%20des%20donn%C3%A9es%20d%C3%A9signe,prot%C3%A9ger%20la%20confidentialit%C3%A9%20des%20donn%C3%A9es.)