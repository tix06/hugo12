---
Title: lecture - ecriture fichier
description: lire et ecrire dans un fichier python, fonctions ord et chr, boucles
weight: 10
---

au cours de ce TP, vous allez apprendre à:


* parcourir les caractères ou les éléments d'un fichier
* traiter les éléments un par un. Placer les éléments traités dans un fichier
* lire/ecrire dans un fichier

# Manipuler des fichiers txt en python
## Parcourir des séquences
Les séquences, comme le chaines `str` et les listes `list` python peuvent être parcourues avec une boucle `for`. On appelle *parcourir* le traitement des caractères ou des éléments l'un après l'autre. 

> Traiter les 2 exercices suivants pour démarrer ce TP.

**ex 1:** (a) Afficher une image à partir d'une Liste. Compléter le script:

```python
L1 = [' ^___^','" o o "', '===X===','   "  ']
for l in L1:
    print(...
```

(b) Afficher une image à partir d'une *liste de listes* de caractères.

```python
L2 = [[' ', '^', '_', '_', '_', '^'], ['"', ' ', 'o', ' ', 'o', ' ', '"'], ['=', '=', '=', 'X', '=', '=', '='], [' ', ' ', ' ', '"', ' ', ' ']]

for ligne in L2:
    s = ''
    for c in ligne:
        s += ...
    print(...
```

*Remarquer que l'on utilise ici 2 boucles imbriquées, avec 2 variants: le variant `ligne` puis le variant `c`, qui contient chaque caractère de `ligne`.*


**ex 2:** Quelle est l'image cachée dans cette matrice?

```python
M = [['20', '2F', '5C', '5F', '2F', '5C', '20'],
     ['28', '20', '2E', '20', '2E', '20', '29'],
     ['3D', '5C', '5F', '76', '5F', '2F', '3D']]
```

*Solution partielle:*

```python
for l in M:
    s = ''
    for r in l:
        s += ...
    print(...
```

*Rappels:* 

* *Conversion valeur hexa -> decimal: utiliser `int(valeur,16)`*
* *Conversion decimal -> ascii: utiliser `chr`*

## Lecture/ecriture dans un fichier
### Introduction au TP
Les manipulations qui vont suivre demandent quelques pré-requis. Vous allez tester les instructions suivantes avant de réaliser le TP sur le déchiffrement.

> Tester et comprendre chacun des exemples proposés ci-dessous.

#### Instruction de retour à la ligne `\n`:

Dans une chaine de caractères, pour faire un retour ligne, on utilise la combinaison de symboles `\n`.

Exemple: 

```python
>>> discours = "Je sais ta passion, et suis ravi de voir\nQue tous ses mouvements cèdent à ton devoir ;"
>>> print(discours)
Je sais ta passion, et suis ravi de voir
Que tous ses mouvements cèdent à ton devoir ;
```

#### Afficher le caractère `\`
`\` est un caractère d'echappement. C'est à dire que lorsqu'il est placé dans une chaine de caractères, il n'est pas affiché mais interprété. Pour l'afficher, il faut alors mettre 2 fois le même symbole:

```python
>>> print('\\')
\
```

#### Décalage  de 1 rang pour un caractère "a" -> "b"
* On détermine le rang ascii du caractère: `rang = ord("a")`
* On definit un nouveau caractère avec décalage dans l'alphabet: `chr`

```python
>>> rang = ord("a")
>>> car = chr(rang + 1)
>>> print(car)
b
```

Il s'agit d'un décalage de type monoalphabétique, permettant de chiffrer un texte pour le rendre secret. Ici, la clé de chiffrement est égale à 1. (1 seul rang de décalage).

#### Ecrire dans un fichier txt
* méthode 1: fonctions `open` et  `close`. On créé un objet qui sert à désigner le fichier. Choisir un nom quelconque, pour l'exemple qui suit ce sera `fileout`. On utilise la fonction `open` avec pour paramètres, le nom du fichier (son chemin), suivi du caractère 'w' (pour `write`, ouverture du fichier en *écriture*).

On peut alors placer du texte dans le fichier à l'aide de la méthode `write`: `fileout.write("...")`

Penser alors à fermer le fichier de lecture: `fileout.close()`

```python
fileout = open('exemple.txt','w')
fileout.write("Je sais ta passion, et suis ravi de voir\nQue tous ses mouvements cèdent à ton devoir ;")
fileout.close()
```

*On peut alors vérifier le fichier et son contenu en parcourant le dossier avec l'explorateur windows*.

* méthode 2: système d'instructions `with` + `open`

Le programme suivant est équivalent à celui de la méthode 1. Avec le mot clé `with`, les instructions de d'écriture dans le fichier sont mis dans un bloc, et donc indentées. A la sortie de ce bloc, le fichier est automatiquement *fermé*, ce qui fait l'economie de l'instruction `close`, et evite les oublis...

```python
with open('exemple.txt','w') as fileout:
    fileout.write("Je sais ta passion, et suis ravi de voir\nQue tous ses mouvements cèdent à ton devoir ;")
   
```

#### Lire le contenu d'un fichier txt
* méthode 1: fonctions `open` et  `close`. On créé un objet qui sert à importer le fichier. Choisir un nom quelconque, pour l'exemple qui suit ce sera `file`. On utilise la fonction `open` avec pour paramètres, le nom du fichier (son chemin), suivi du caractère 'r' (pour `read`, ouverture du fichier en *lecture*).

On peut alors récuperer le contenu textuel du fichier à l'aide de la méthode `read`. Dans l'exemple ci-dessous, on place le texte du fichier dans la variable `texte`. 

On peut traiter cette variable comme on le souhaite, l'afficher en entier (`print(texte)`), ou parcourir et traiter les caractères les uns après les autres (`for c in texte: ...`)

Penser alors à fermer le fichier de lecture: `file.close()`

```python
file = open('exemple.txt','r')
texte = file.read()
file.close()
print(texte)
```

* méthode 2: système d'instructions `with` + `open`

Le programme suivant est équivalent à celui de la méthode 1. Avec le mot clé `with`, les instructions de lecture du fichier sont mis dans un bloc, et donc indentées. A la sortie de ce bloc, le fichier est automatiquement *fermé*, ce qui fait l'economie de l'instruction `close`, et evite les oublis...

```python
with open('exemple.txt', 'r') as file:
    texte = file.read()
print(texte)
``` 

## TP Déchiffrement d'un texte
* Télécharger le fichier [texte_chiffre.txt](../datas/texte_chiffre.txt) (faire un clic droit=> *sauvegarder la cible du lien sous...*)
* le placer dans le même dossier que votre fichier *python*.
* Dans le fichier `texte_chiffre.txt`, le texte est-il écrit en clair ou est-il chiffré?

Les chiffrements les plus anciens reposaient sur un simple décalage des caractères, comme vu dans les informations préliminaires. Par exemple, avec une clé de décalage égale à 1, le "a" devient un "b", le "b" -> "c", etc...

A partir des informations précédentes, écrire un script python qui devra:

1. Ouvrir le fichier 'texte_chiffre.txt' en LECTURE 
2. Lire le contenu et le placer dans une variable `texte`
3. Ouvrir un nouveau fichier en ECRITURE, que vous appelerez 'texte_dechiffre.txt'
4. Parcourir les caractères de `texte`, les uns après les autres: `for c in texte:`
5. Dans la boucle  `for`: si le caractère `c` est différent de `\` c'est à dire `c != "\\"`
  * déterminer le rang ascii de `c`
  * definir un nouveau caractère en essayant la clé de décalage égale à -1
  * écrire ce nouveau caractère dans le fichier 'texte_dechiffre.txt'
6. Sinon, écrire `\n` dans le fichier 'texte_dechiffre.txt'
7. fermer le-s fichier-s si besoin.
8. Vérifier alors le contenu de votre fichier 'texte_dechiffre.txt'. Si celui-ci est toujours chiffré, recommencer avec une nouvelle clé (-2, puis -3, ...)

Si vous avez terminé:

* Utiliser votre script pour créer une fonction que vous appelerez `chiffre_dechiffre` et qui aura 3 paramètres:
  * texte0 : le fichier texte d'origine
  * texte1 : le fichier texte de destination
  * decalage_ascii : la clé de décalage
  
Cette fonction devra créer un nouveau fichier `texte1` à partir du texte du fichier `texte0`. Tous les caractères de `texte1` seront définis à partir de ceux de `texte0` en utilisant une clé de déclage: `decalage_ascii`

*Exemple d'utilisation:*

```python
chiffre_dechiffre('texte_chiffre.txt','texte_dechiffre.txt',2)
```

Utilisez alors votre fonction pour réaliser le chiffrement d'un texte relativement long.

# Suite
* [Solution](../page541) du TP lecture - ecriture python

* Projet transformer image -> ASCII: [Lien](../../TP/ascii_art)

* Utiliser des fonctions pour calculer: [Lien](../../TP/page52)
