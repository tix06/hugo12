---
Title : chiffrement symetrique
description: securisation des communications, chiffrement symetrique, code cesar, analyse frequentielle
weight: 47
---

Ce chapitre contient plusieurs pages:

* sécuriser les communications: [Lien 1](../page6/)
* chiffrement asymetrique: [Lien 2](../page7/)
* TP sur les nombres premiers: [Lien 3](../../algorithmes/page11/)
* Projet sur le *hack* ethique et le chiffrement RSA: [Lien 4](/python_avance/TP/python6_codes/)

# Chiffrements symétriques
du chiffrement de *Cesar* à celui de la *machine Enigma*...
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

## Chiffrement symétrique - definition
Le chiffrement symétrique utilise la même clé (ou la même table) pour chiffrer et déchiffrer le message. L'algorithme peut être connu par l'adversaire. Mais le secret repose sur celui de la *clé*.

# Le chiffrement par décalage, ou chiffre de Caesar
## Principe
Le chiffre de César fonctionne par décalage des lettres de l'alphabet. 

{{< img src="../images/Caesar3.png" caption="Chiffrement par décalage - wikipedia" >}}
Cet algorithme de chiffrement utilise une fonction périodique pour transformer les rangs de chaque lettre:

| a | b | c | d | e | f | g | h | i | j | k | l | m | n | o | p | q | r | s | t | u | v | w | x | y | z |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|0| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24 | 25 |


Le chiffrement par {{< a link="https://fr.wikipedia.org/wiki/Chiffrement_par_substitution" caption="substitution monoalphabetique" >}} utilise une fonction avec *modulo*:

$$x \rightarrow x + cle ~[26]$$

La fonction utilisée est une fonction *périodique*, issue de l'arithmétique modulaire. 

> Compléter l'algorithme du chiffrement de César. On suppose qu'il existe une clé `c` correspondant au décalage utilisé. Le message clair est `m` et le message chiffré est `m_chiffre`

```python
m_chiffre = ""
Pour chaque lettre l du message m:
  l_chiffre = ...
  m_chiffre = ...
```

*On peut utiliser les fonctions `numero(l:str)->int` et `caractere(n:int)->str`*

> **monosubstitution par décalage ou par substitution:** Une lettre du message clair va t-elle donner différentes lettres chiffrées, ou une seule?

## Facilité du décryptage
Pour decrypter le message, on peut tester une à une toutes les clés, jusqu'à découvrir un message intelligible:

```
m_dechiffre = ""
pour chaque valeur i dans {0,25}:
    pour chaque lettre l de m_chiffre:
        l_dechiffre = ...
        m_dechiffre = ...
```


> **Décryptage par FORCE BRUTE**: Combien y-a-t-il de clés possibles à essayer pour celui qui réalise le décryptage? Conclure.

## Substitution monoalphabetique utilisant une table



Le chiffrement par monosubstitution a été également utilisé par différentes méthodes utilisant une table.

{{< img src="../images/polybe.png" caption="Carré de Polybe - le mot « bonjour » est ainsi chiffré par le carré de Polybe :12 34 33 24 34 45 42 - wikipedia" >}}

Le code issu du carré de Polybe a été utilisé par les prisonniers, qui transmettaient leur message en tapant sur les murs {{< a link="https://fr.wikipedia.org/wiki/Tap_code" caption="Tap code" >}}

Vous trouvez ces méthodes de chiffrement trop simpliste? Regardez alors sa déclinaison avec le{{< a link="https://fr.wikipedia.org/wiki/Chiffre_de_Playfair" caption="chiffrement de Playfair" >}}

{{< img src="../images/playfair.png" link="https://www.youtube.com/watch?v=JMkGYoT3-Rw" caption="VIDEO: chiffrement de Playfair - youtube - Astuces et tutoriels" >}}

## Decryptage par analyse fréquentielle

Le **problème** avec ce type de chiffrement monoalphabetique, est qu'il est possible de repérer comment sont transformées certaines lettres à partir de l'**analyse fréquentielle** du message chiffré.

On peut alors utiliser la frequence des lettres pour dechiffrer et comparer avec la frequence moyenne dans une langue. (200 caracteres suffisent). Il y a aussi tout un tas de statistique, comme les lettres uniques, doubles lettres, finales, etc... C'est un marqueur suffisant pour savoir comment le code est fait.


{{< img src="../images/frequenceA_Z.gif" caption="frequence des lettres en français, calculée sur la lecture de plusieurs ouvrages classiques (10 millions de caracteres)" >}}

Cette analyse frequentielle est plus difficile *(mais pas impossible)* dans le cas du chiffrement de Playfair, car celui-ci utilise une methode de substitution d'un groupe de 2 lettres: c'est une substitution *polyalphabetique*. Le nombre de combinaisons possibles avec 2 lettres est alors de $26^2 = 676$.



# Substitution polyalphabétique
## Principe

**Polyalphabetique:** Se dit d'un chiffre où un groupe de n lettres est codé par un groupe de n symboles. Le chiffrement *Playfair*, vu plus haut s'apparente à une substitution polyalphabetique, puisqu'il substitue des digrammes (groupes de 2 lettres) dans le texte d'origine.

Contrairement aux chiffrements monoalphabetiques, qui sont des chiffrements par **flot** (caractères transformés un à un), les chiffrements polyalphabetiques réalisent un chiffrement par **blocs** (plusieurs caractères transformés en une fois).

L'exemple suivant montre une polysubstitution simple avec une **clé de longueur 3** qui va décaler les lettres de l'alphabet :

On définit la clé '123' qui indique que le premier caractère sera décalé d'une position, le second de 2 et le troisième de 3 positions, etc.

Le mot : WIKIPEDIA donne donc dans ce cas XKNJRHEKD.

Mais si on chiffre le mot : AAAAAAAAA cela donnera BCDBCDBCD. La lettre A ne donne pas toujours la même correspondance chiffrée. 

**Chiffrement de Vigenère**:

Le [chiffrement de Vigenère](https://fr.wikipedia.org/wiki/Chiffre_de_Vigen%C3%A8re#Dans_la_culture) utilise ce principe de décalage à partir d'une clé exprimée par un mot.

{{< img src="../images/vigenere2.jpg" caption="image issue du site books.openedition.org" >}}

C'est souvent ce type de codage qui est proposé dans la litterature et le cinema.

{{< img src="../images/benj_gates.png" caption="affiche du film Benjamin Gates et le Tresor des Templiers" >}}



## Décryptage
L'analyse des fréquences est moins pertinente lorsque le message a été chiffré avec un chiffrement polyalphabétique (qui tend à rendre aléatoire la fréquence des lettres).

Si on parvient à découvrir la périodicité, on peut en déduire la longueur de la clé. La connaissance de la longueur de la clé est essentielle pour pouvoir pratiquer l'analyse frequentielle: Une même lettre ne donne pas toujours le même caractère chiffré. 

Le decryptage par force brute repose sur l'essai de toutes les clés possibles, par combinaison sur tous les caractères de la clé. Si celle-ci a une longueur n, cela va faire $X^n$, où X est la longueur de l'alphabet. C'est une fonction *exponentielle*.

La fonction de dechiffrage est alors executée un nombre de fois correspondant à $X^n$, dans le pire des cas. 

# La machine{{< a link="https://fr.wikipedia.org/wiki/Enigma_(machine)" caption="Enigma" >}}
{{< img src="../images/enigma.jpg" caption="Enigma: machine électromécanique portative servant au chiffrement et au déchiffrement - wikipedia" >}}
La machine utilise des **rotors** qui sont mis en position selon une **clé**. L'alphabet est chiffré selon la position initiale de ces rotors. Ceux-ci se **décalent** lors de l'utilisation. 

Des branchements permettent d'ajouter des **permutations** des caractères.

Tout ceci modifie l'alphabet chiffré et augmente sérieusement la complexité.

Comme tout *chiffrement symétrique*, *déchiffrer* se fait avec la même machine, à condition d'utiliser la *même clé*.

Son utilisation la plus célèbre fut celle faite par l'Allemagne nazie, avant et pendant la Seconde Guerre mondiale, la machine étant réputée inviolable selon ses concepteurs. 

Le **principe de la machine Enigma était connu**. Le concepteur savait à l'avance que certains modèles pourraient être volés par les alliés. Ce qui fit son efficacité, c'est le nombre immense de combinaisons possibles pour les réglages initiaux de la machine et le choix de la clef brute du message.

Les cryptanalystes britanniques, dont{{< a link="https://fr.wikipedia.org/wiki/Alan_Turing" caption="Alan Turing" >}}



# Exercices
## Substitution monoalphabétique: Code de César

* **Question 1:** Quelle clé a  été utilisée pour chiffer ce texte (avec l’algorithme de César)? 

$$jyfwavnyhwopl hwwspxbll$$

* **Question 2:** Décrypter ce message.



* **Question 3:** Proposer un programme en python qui chiffre un message clair `m` en un message codé selon la clé numérique `c`.

*Aide:* 

* La fonction `ord('x')` retourne un entier correspondant à la position d'un caractère dans la table ascii.<br>
Par exemple, `ord('A')` retourne 65, `ord('B')` retourne 66,...

* La fonction `chr(N)` retourne le caractère de rang N: `chr(65)` retourne 'A'.

## Substitution polyalphabétique: Chiffrement de Playfair
A partir des explications données dans la video:

* **Question 1:** Construisez la matrice pour l’algorithme de Playfair avec la clé *estienne*. 
* **Question 2:** Chiffrer le message: *ACTIONREACTION*
* **Question 3:** S'agit-il d'une méthode utilisant la substitution monoalphabetique, ou polyalphabetique?
* **Question 4:** Avec cette méthode, le decryptage est-il possible par analyse fréquentielle? 

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

a. 

```
DGFHTMOMEIAMTLMFGOKFGOKEGDDTRWEIAKZGFGFSTEKGOMLASTTIFGFOSTLMFTFGOKMGWMFGOKRTSAJWTWTAWDTFMGFDAOLTWMOSSAFGOKETWKRWFDTEIAFMROAZSGMOFKOTFFTXAWMLARGWETWKJWAFROSDOAWSTAWDAMOFHGWKDTSTEITKSADAOF
```

b. 

```
YOHGMVMFCBRBGWFNIZZPSURWFUOIPUWYITFANIETGGDOCKACPQEBEWPMXEMKVGRAILKWWXZOCILGPMQOVCGEGMYEBQRYACJMWXULFRVQMDCYLZFYZMYTPCRFDCRJNSFIHIQGRZEPRCVWMDILKGYDQORVFMXMCRCNIMUGRBKRBOOIUGPQCBVZNEYACE
```

* **Question 2:** L'un des 2 a été chiffré avec un algorithme de substitution mon-alphabetique, et l'autre, poly-alphabétique. Lequel est mono-alphabétique?

* **Question 3:** Tracer un histogramme à partir du texte chiffré en mono-substitution. On donne un exemple de script ci-dessous pour réaliser le graphique:

```python
import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_axes([0, 0, 1, 1])

etiquettes = ['a', 'b', 'c', 'd', 'e']
valeurs = [23, 17, 35, 29, 12]

# Affichage des données
ax.bar(etiquettes, valeurs)

plt.title("Histogramme")  # Titre du graphique
plt.ylabel('Nombre')  # Titre de l'axe y
plt.xlabel('alphabet')
plt.show()  # Affichage d'une courbe
```

{{< img src="../images/histoabc.png" >}}

## Chiffrement symétrique par la fonction XOR
exercice inspiré de la page sur le chiffrement de [glassus.github.io](https://glassus.github.io/terminale_nsi/T5_Architecture_materielle/5.4_Cryptographie/cours/)

* **Question 1:** La fonction XOR est la fonction du OU EXCLUSIF.

Donner la table de vérité de la fonction XOR

* **Question 2:** A partir des lignes suivantes, vérifier que l'opérateur `^` en python réalise la fonction XOR sur 2 nombres écrits en valeur décimale:

```python
> 3 ^ 4
7
> 4 ^ 5
1
```

* **Question 3:** Programmer la fonction `xor` en python qui retourne le resultat de XOR appliqué aux 2 paramètres a et b.

*Exemple:*

```
>>> xor(0,1)
1
>>> xor(53,23)
34
>>> xor(34,23)
53
```

* **Question 4:** Peut-on utiliser la fonction XOR pour chiffrer PUIS dechiffrer un message, avec la MEME clé de chiffrement? Expliquer à partir de l'exemple ci-dessus. 

* **Question 5:** On s'interresse maintenant à la programmation de la fonction XOR pour chiffrer un message à partir d'un masque:

$$message = "CETTEPHRASEESTVRAIMENTTRESTRESLONGUEMAISCESTFAITEXPRES"$$

Le masque (correspond à la clé) aura une longueur inférieur au message. On utilise le masque selon la méthode de chiffrement polyalphabetique vue en cours.

Le chiffrement demande de faire correspondre les caractères avec des nombres entiers. On utilisera pour cela un alphabet de 32 caractères ($2^5$). Chaque lettre de l'alphabet correspondra alors à un nombre compris entre 0 et 31. 

* **Question 6:** Lorsque l'on place 2 entiers inférieurs à 32 dans la fonction XOR, celle-ci retourne un entier également inférieur à 32. Pourquoi? (*Representer ces nombres en binaire, sur un octet, et verifier cette affirmation*)

* **Question 7:** Compléter la fonction `chiffre(message, masque)` qui chiffre message en le XORant avec masque.

Cette fonction doit pouvoir aussi servir à déchiffrer le message chiffré.

```python
alphabet=[chr(i+ord('A')) for i in range(26)] + ['*','/','@','&','!','à']
def chiffre(message, masque):
    assert len(message)>=len(masque)
    message_chiffre = ""
    for i in range(len(message)):
        indice_lettre = alphabet.index(message[i])
        indice_masque = ...
        val = xor(...,...)
        message_chiffre+=alphabet[val]
    return ...
```

* **Question 8:** Utiliser la fonction `chiffre` pour effectuer le chiffrement puis le dechiffrement du *message*.

* **Question 9:** Pensez vous que cette méthode de chiffrement est assez resistante face à une attaque de cryptoanalyse? Si oui, pourquoi?

<!--
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
-->
# Liens
* Suite du cours: [chiffrement asymétrique](../page7)

# Documentation, sitographie
* Chiffrement : notre antisèche pour l'expliquer à vos parents [article de NextImpact](https://www.nextinpact.com/article/24930/99777-chiffrement-notre-antiseche-pour-expliquer-a-vos-parents)
* chiffrement de Vigenère: [wikipedia](https://fr.wikipedia.org/wiki/Chiffre_de_Vigen%C3%A8re)
* Interstices : [coder et decoder. La machine Enigma](https://interstices.info/turing-a-lassaut-denigma/)
* sécurisez vos données avec la cryptographie [openclassroom](https://openclassrooms.com/fr/courses/1757741-securisez-vos-donnees-avec-la-cryptographie/6031870-controlez-lintegrite-de-vos-messages#:~:text=L'int%C3%A9grit%C3%A9%20des%20donn%C3%A9es%20d%C3%A9signe,prot%C3%A9ger%20la%20confidentialit%C3%A9%20des%20donn%C3%A9es.)