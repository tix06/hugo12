---
Title : fichiers Entrees/Sorties
description: manipulation de fichiers, module os
weight: 16
---

# Entrées/Sorties en console
## Sortie en console
La fonction `print` permet l'affichage d'une valeur en console, quel qu'en soit le type.

On peut afficher un texte simple, ou composé de plusieurs parties, par concaténation de chaine : 

```
clan = 'Vikings'
message = 'Fight Invaders'
print('We are the ' + clan + ' who say' + ' "'+ message + '!"')
# affiche 
# We are the Vikings who say "Fight Invaders!"
```

Le problème de cette méthode de concaténation est que chaque partie composant la chaine doit être de type `str`. Cela est possible avec la fonction `str(variable`, mais il existe une méthode plus efficace : **formater la chaine**.

La méthode `str.format()` sur les chaines de caractères : 

La methode de base : 

```
clan = 'Vikings'
message = 'Fight Invaders'
print('We are the {} who say "{}!"'.format(clan, message))
# affiche 
# We are the Vikings who say "Fight Invaders!"
```

On peut aussi préciser le nombre de caractères ou de chiffres attendus, le type de données, etc. 

*Exemple : affichage d'une table*

```python
for x in range(1, 11):
    print('{:2d} {:3d} {:4d}'.format(x, x*x, x*x*x))
# affichage : 
 1   1    1
 2   4    8
 3   9   27
 4  16   64
 5  25  125
 6  36  216
 7  49  343
 8  64  512
 9  81  729
10 100 1000
```
Cela permet d'aligner des chaînes dans une largeur de taille fixe.

## Entrées au clavier : `input`
La fonction `input` met le programme en pause et attend que l'utilisateur entre une donnée.

```python
nom = input('Quel est votre nom ? ')
print('Bonjour, {}'.format(nom))
```

Toutes les données saisies sont converties en chaîne. Il est donc necessaire de convertir les données numériques dans le type approprié avant de les utiliser : 

```python
prix = input('Combien coute ce camion ?')
prix = float(prix)
if prix < 10000:
  print('Ok, je le prends.')
```

# Lire le contenu d'un fichier
## Repertoire courant
Selon l'IDE python choisi, vous pouvez avoir des difficultés pour ouvrir un fichier. L'interpreteur peut considérer que le repertoire courant n'est pas celui du fichier en cours d'execution, et ne trouve pas votre fichier data, qui se trouve dans le même dossier.

Pour resoudre ce problème, vous pouvez ajouter les lignes suivantes:

```python
import os

dir_path = os.path.dirname(os.path.abspath(__file__))
print('init:',dir_path)

os.chdir(dir_path)
#sys.path.append(dir_path)
print('after:',os.getcwd())
print('conten:t',os.listdir())
```

Le module `os` apporte les fonctions:

* `chdir`: changer de repertoire courant pour le chemin utilisé par l'interpreteur
* `getcwd`: chemin du repertoire courant
* `listdir`: contenu du repertoire courant

## Fichier txt
On utilise la fonction `open` de la librairie standart en python:

La fonction `open` crée donc un fichier. Elle renvoie un objet de la classeTextIoWrapper. Par la suite, nous allons utiliser des méthodes de cette classe pour interagir avec le fichier. Il existe 2 méthode pour utiliser `open`:


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

 
*Exemple de programme : lire un fichier .txt avec un seul mot par ligne, et créer une liste mots*

```python
# initialisation de la liste vide
mots = []

# Lecture du fichier txt et remplissage de la liste
with open('liste_francais.txt', encoding='iso-8859-1') as f:
    for mot in f.read().splitlines():
        mots.append(mot)
```

* open : renvoyer un objet TextIOWrapper
* as : « en tant que »

Le mot-clé `with` permet de créer un "context manager" (gestionnaire de contexte) qui vérifie que le fichier est ouvert et fermé, même si des erreurs se produisent pendant le bloc.

Plus d'informations : [https://python.sdv.univ-paris-diderot.fr/07_fichiers/](https://python.sdv.univ-paris-diderot.fr/07_fichiers/)



## Caractères speciaux
Certains caractères sont fort utiles lors de l’écriture de fichiers texte afin d’organiser les données. Le symbole ; est très utilisé comme séparateur de colonnes pour une matrice, on utilise également le passage à la ligne ou la tabulation. Comme ce ne sont pas des caractères « visibles », ils ont des codes :

* `\` caractère d'echappement (par exemple pour écrire des guillemets dans une chaine)
* `\n` : passage à la ligne
* `\t` : tabulation, indique un passage à la colonne suivante dans le format tsv (Tabulation-separated values).

Lors de la **lecture d'un fichier**, on peut avoir besoin de supprimer ces caractères spéciaux:

```python
table = []
# Lecture du fichier
with open('datas/rne-cm.csv', encoding='utf-8') as f:
    for line in f.read().splitlines():
        table.append(line)

table[2]
# affiche
'32\tGers\t\t\t32249\tMauvezin\tPASCOLINI\tJean-Marc\tM\t'
print(table[2])
# affiche
32 Gers   32249 Mauvezin PASCOLINI Jean-Marc M
len(table[2])
# affiche 
1
```

L'import des données n'a pas placé les valeurs comme des éléments de liste. Il faudrait découper la chaine de caractères au niveau des espaces:

On peut alors remplacer l'instruction `table.append(line)` par `table.append(line.split('\t'))`, ce qui découpe la chaine au niveau des `\t`:

```python
with open('datas/rne-cm.csv', encoding='utf-8') as f:
    for line in f.read().splitlines():
        table.append(line.split('\t'))
table[2]
# affiche
['32',
 'Gers',
 '',
 '',
 '32249',
 'Mauvezin',
 'PASCOLINI',
 'Jean-Marc',
 'M',...]
```

Bien entendu, il faudra adapter l'argument de la fonction `split` en fonction du caractère de séparation utilisé dans le fichier:

Pour le contenu suivant, il faudra utiliser `line.split(';')`

```
;2020;2021;2022;2023;2024;total
seconde;480;495;420;465;465;
premiere;420;525;420;510;465;
terminale;495;480;420;435;435;
;;;;;;
```

## Fichier csv
Le module csv permet de reduire d'une ligne l'import des données (choisir le bon *delimiter*):

```python
import csv
table = []
with open('ficher.csv', 'r') as file:
    reader = csv.reader(file, delimiter=',')
    for row in reader:
        table.append(row)
```

* Souvent, la première ligne ne concerne que l'en-tête (descripteurs). 
* Le reste des données, numériques doivent être converties en *float*
* Supposons que les données contiennent les valeur de x pour la première colonne, et y la deuxième colonne:

```python
x = []
y = []
for i in range(1,len(table[1:])):
    x.append(float(table[i][0]))
    y.append(float(table[i][1]))
```

# Ecrire dans un fichier
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

*Exemple avec une liste => fichier*

```python
animaux2 = ["poisson", "abeille", "chat"]
with open("zoo2.txt", "w") as filout:
    for animal in animaux2:
         filout.write(animal)
```

à la ligne 2 : ouverture du fichier `zoo2.txt` en mode écriture, avec le caractère `w pour write.`

Si nous ouvrons le fichier zoo2.txt avec un éditeur de texte, voici ce que nous obtenons :

`poissonabeillechat`

Ce n'est pas exactement le résultat attendu. Le script peut être amélioré en utilisant une écriture formatée, comme vu plus haut, à la dernière ligne du script : 

```python
         filout.write("{}\n".format(animal))
```
Ce qui donne maintenant, à l'ouverture du fichier : 

```
poisson
abeille
chat
```

Exemple issu de la page [python.sdv.univ-paris-diderot.fr/07_fichiers](https://python.sdv.univ-paris-diderot.fr/07_fichiers/#72-ecriture-dans-un-fichier)

## Tableau de données
* convertir les données en chaine de caractère formatée:


```python
descripteurs = ['courant','tension','puissance']
datas = [[0.100,2.00,0.200],[0.200,4.00,0.400]]
tab = ""
for title in descripteurs:
    # ajout des descripteurs en tete du tableau
    tab = tab + title + ','
for i in range(len(datas)):
    # saut de ligne
    tab = tab + '\n'
    for j in range(len(datas[0])):
        tab = tab + datas[i][j] + ','
```


* exporter avec une extension *csv*

```python
with open("fichier_datas.csv", "w") as filout:
    filout.write(tab)
```

## Exporter des données (sauvegarde)
Il peut être utile de sauvegarder des données en cours de travail, comportant des paramètres que l'on veut retrouver lors d'une prochaine session de travail. 

Utiliser le module `pickle` pour écrire, puis lire une structure de donnée python, comme un dictionnaire ou une liste:

```python
import pickle
```

*Exemple:*

```python
dico = {'b10' : 479.01,
        'b11' : 479.19,
        'b20' : 479.89,
        'b21' : 479.91}
```

* Ecriture:

```python
with open(fichier_export,'wb') as f1:
    pickle.dump(dico,f1)
```

* Lecture:

```python
with open('sauvegarde','rb') as f2:
    dico = pickle.load(f2)
```

# Liens
* Voir cours sur le formatage des sorties : [Lien python.org](https://docs.python.org/fr/3/tutorial/inputoutput.html)