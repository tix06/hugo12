---
Title: assembleur
description: langage assembleur
weight: 6
---

*Cours*:

* Histoire et modèle d'architecture Von Neumann / Harvard: [Lien](../page1/)
* Le fonctionnement d'un processeur: [Lien](../page2/)
* Langage assembleur: [Lien](../page3/)

*Séquence composée de 3 TP:*

* TP1 Composer son ordinateur à partir d'un site commercial: [Lien](../page5/)
* TP2: Comment fonctionne un processeur? [Lien](../page51/)
* TP3: Programmes plus evolués, de python à l'assembleur: [Lien](../page3/)

# Le langage *assembleur*
Le langage assembleur est, en programmation informatique, le langage de plus bas niveau qui représente le langage machine sous une forme lisible par un humain. ([wiki](https://fr.wikipedia.org/wiki/Assembleur))

<!--
Le premier programme assembleur a été écrit par Nathaniel Rochester pour l'IBM 701 (le premier ordinateur commercialisé par IBM) en 1954.

{{< img src="../images/archi6.png" link="https://fr.wikipedia.org/wiki/Assembleur" caption="exemple de programme assembleur pour  le microprocessor Motorola 6800 8-bit  - source : " >}}
-->

L'assembleur oblige à programmer la *gestion des mémoires*:

Pour échanger des données avec la mémoire, le processeur transfert l'état d'un registre dans une case mémoire (STR) ou l'état d'une case mémoire dans un registre (LDR). On rappelle que la mémoire contient à la fois les instructions et les données. Mais les *calculs* du processeur se font sur les *registres*. Il faut donc prévoir de charger les valeurs de la RAM vers les registres avant de faire une opération.

D'ailleurs, une instruction machine est une chaine binaire composée de 2 parties:

* un champ "code opération" qui indique au processeur le type de traitement à effectuer.
* un champ opérande qui indique l'adresse des données.

## Le simulateur
* Lancer le simulateur
{{< img src="../images/ARM.png" link="https://www.peterhigginson.co.uk/AQA/" caption="clic droit > ouvrir dans un nouvel onglet pour lancer le simulateur ARM" >}}



## Les 3 familles d'instructions machine
Ce sont les instructions:

* de transfert de données
* arithmétiques
* de rupture de séquence

### Transfert de données
Les opérations de transfert se font d'un registre vers un emplacement mémoire, ou l'inverse.

| Ordre| Instruction | Description en langage naturel|
|--- |--- |--- |
| Affectation (variable)| `x: 23` | Place 23 dans la variable x, c'est à dire 23 dans l'emplacement RAM prévu pour x |
| Affectation (registre) | `MOV R1, #23` | Place la valeur 23 dans le registre R1 |
| Charger | `LDR R1, 78` | *LOAD*: Place dans le registre R1 la valeur stockée à l'emplacement 78 de la RAM |
| Stocker | `STR R1, 151` | *STORE*: Place dans la RAM à l'emplacement 151, la valeur stockée dans le registre R1 |
| Stocker | `STR R1, x` | *STORE*: Place dans la RAM à l'emplacement prévu pour x, la valeur stockée dans le registre R1 |

#### Exemple 1:
Le programme suivant affecte une valeur dans un registre, puis la copie dans la RAM.


```
      MOV R0, #16
      STR R0, 55
      HALT
```

> Copier-coller le script, *assembler*. Régler le bouton *OPTIONS* sur *hex*

**question a**: Vérifier que 16 (base 10) = 10 (base 16).

**question b**: Combien de lignes fait le programme? Quelles sont les adresses dans la RAM des instructions (donner la somme colonne + ligne)?

> Dérouler le script pas à pas (appuis successifs sur *STEP*)

**question c:** Quel est le registre utilisé? Quelle est la valeur déplacée? Quelle adresse de la RAM va contenir la valeur à stocker?

**question d:** Si l'on suppose que la complexité temporelle est égale au nombre de fois qu'il faut appuyer sur le bouton *STEP* pour arriver à la dernière ligne du programme: Quelle est la compléxité de ce programme?

#### Exemple 2: Programme mystère
Dans un programme en assembleur, il sera plus facile de manipuler des variables que des adresses mémoires.

```
      LDR R0, x
      LDR R1, y
      STR R0, y
      STR R1, x
      HALT
      0
      0
      0
x:    23
y:    18
```

> Copier-coller le script, *assembler*.

**question a**: Vérifier que 23 (base 10) = 17 (base 16), et que 18 (base 10) = 12 (base 16).

**question b**: Combien de lignes fait le programme? Quelles sont les adresses dans la RAM des instructions (donner la somme colonne + ligne)? Quelles sont les adresses RAM des données?

> Dérouler le programme à vitesse réduite.

**question c**: Interpréter les lignes 0 à 4 du programme (donner une explication en langage naturel). Que fait le programme mystère?

### Arithmétique
Ce sont les opérations courantes (addition, soustraction, multiplication par 2, division par 2). Elles se font depuis un registre, vers un autre registre.

Voici une liste non exaustive des instructions du{{< a link="https://www.peterhigginson.co.uk/AQA/info.html" caption="simulateur ARM" >}}

Les instructions de traitement suivantes concernent uniquement les registres. 

L'un de ces registres est le *Program Counter*, PC. Celui-ci repère l'état courant dans le programme (la ligne du script à executer).

| Ordre| Instruction | Description en langage naturel|
|--- |--- |--- |
| Ajouter | `ADD R0, R1, #16` | Ajoute 16 à R1 et place le résultat dans R0 |
| Ajouter | `ADD R0, R0, R1` | Ajoute R1 à R0 et place le résultat dans R0 |
| Soustraire | `SUB R0, R0, #16` | Soustrait 16 à R0 et place le résultat dans R0 |
| Ajouter | `ADD R0, R1, #16` | Ajoute 16 à R1 et place le résultat dans R0 |
| Multiplier par 2 | `LSL R0, R0, #1` | déplace les bits de R0 d'un seul rang (#1) vers la gauche et place dans R0 |
| Diviser par 2 | `LSR R0, R0, #1` | déplace les bits de R0 d'un seul rang (#1) vers la droite et place dans R0 |


#### Exemple 3 add: programme qui ajoute 2 nombres entrés par l'utilisateur

* `INP R0,2`: attend un nombre en entrée. 
* `OUT Rd, nombre`: affiche à l'écran. `out Rd,4` affiche un nombre signé ou non(`Rd,5`). `Rd,6` affiche en hexadécimal et `Rd,7` affiche un caractère.

```
      INP R0,2
      INP R1,2
      ADD R2,R1,R0
      OUT R2,4
      HALT
```

**question a:** Ce programme, permet-il d'additionner des nombres relatifs, comme par exemple: $123 + (-145)$? Quelle est alors la représentation binaire de $-145$?

**question b:** Recopier sur votre cahier le script correspondant en python:

```python
x = int(input('entrer la valeur de x'))
y = int(input('entrer la valeur de y'))
x = x + y
print(x)
```

**question c:** Compléter le programme assembleur qui multiplie par 2 le nombre saisi par l'utilisateur (avec LSL), affiche le résultat, et le stocke dans la RAM à l'emplacement 10.

```
     INP R0,2
     LSL R0, R0, ...
     OUT R0, 4
     STR ..., ...

```


**question d:** Ecrire dans votre cahier le script correspondant en python.

### Rupture de séquence
Les ruptures de séquence utilisent des étiquettes, à définir dans le programme. Le programme va alors s'executer normalement, ligne après ligne, sauf si un branchement l'amène à une ligne, portant une etiquette.

* HALT: arrêt du programme

* `CMP Ri, Rj`: effectue la comparaison entre Ri et Rj. Attention, cette instruction ne traite pas le résultat de la comparaison! C'est le rôle de la commande suivante.
* B ou BGT, ... sont les opérations de branchement 

**plus grand que:** On utilise une combinaison de 2 lignes pour effectuer le test *si R1 > R2 aller à la ligne label*:

```
CMP R1, R2
BGT label
```

**plus petit que:** On utilise une combinaison de 2 lignes pour effectuer le test *si R1 < R2 aller à la ligne label*:

```
CMP R1, R2
BLT label
```

**est egal à:** On utilise une combinaison de 2 lignes pour effectuer le test *si R1 == R2 aller à la ligne label*:

```
CMP R1, R2
BEQ label
```

**aller systematiquement à:** `B label` va obliger à toujours revenir à la ligne d'etiquette label


La liste complète des instructions se trouve à la page INFO accessible depuis le bouton [info](https://www.peterhigginson.co.uk/AQA/info.html) du simulateur.



#### Exemple 4 max: programme qui retourne le plus grand des 2 nombres saisis par l'utilisateur
*Ce programme peut être directement chargé depuis le bouton SELECT du simulateur.*

```
0     INP R0,2
1     INP R1,2
2     CMP R1,R0
3     BGT HIGHER
4     OUT R0,4
5     B DONE
HIGHER:
6     OUT R1,4
DONE:
7     HALT
      // Input two numbers and output the higher
```

Dans ce 2eme exemple, si R1 est supérieur à R0 (test à la ligne 2), alors le programme effectue un *branchement conditionnel* à la ligne 3 (BGT est le branchement pour Greater Than). 

Si R1 > R0, alors le programme passe directement de la ligne 3... à celle dont l'etiquette est HIGHER, donc à la ligne 6.

Sinon il passe à la ligne 4 (OUT R0,4), ce qui est le cours naturel de lecture du programme, ligne après ligne. Le branchement à la ligne suivante, B DONE le renvoie à la ligne d'etiquette DONE. Ce qui evite d'executer OUT R1,4 qui est réservé au branchement HIGHER.

*Remarque: on peut choisir n'importe quelle nom pour l'etiquette que l'on met dans le programme: HIGHER, TEST, DONE, ... peu importe.*

**question a:** qu'est ce qui est affiché si l'on saisit la valeur 18 pour R0 et 9 pour R1? Puis 10 pour R0 et 20 pour R1?

**question b:** à quoi sert la ligne 6 `B DONE`? Que se passerait-il si cette ligne n'y était pas, et que l'on saisit la valeur 18 pour R0 et 9 pour R1?

**question c:** Ecrire dans votre cahier le script correspondant en python.

#### Exemple 5: boucle infinie
Le programme s'execute de la manière suivante: ligne 0 (affectation de la valeur 16 au registre R0), puis ligne 1 (on definit une etiquette `boucle`), puis ligne 2 (addition R0+1), puis ligne 3, ligne 4, ...

```
      MOV R0, #16
boucle:
      ADD R0, R0, #1
      OUT R0,4
      B boucle
      HALT
```

**question a:** Pourquoi le programme s'appelle-t-il *boucle infinie*?

Le test conditionnel `if R0 > 20: break`, qui va permettre de sortir de la boucle va s'écrire en assembleur:

```
CMP R0, #20
BGT break
```

L'étiquette `break` devra alors être placée après celle `B boucle` afin de pouvoir poursuivre le programme.

**question b:** Ré-écrire le script précédent afin de sortir de la boucle lorsque R0 stocke une valeur supérieure à 20.



<!--
## Opérations simples
**1.** **Prog 1**. Il s'agit d'obtenir le nombre 84 à partir des nombres 50,25,8,7,3 et 1 avec les opérations : addition et soustraction uniquement.

Copier-coller le script dans le simulateur:

```
MOV R0,#50
ADD R0,R0,#25
ADD R0,R0,#8
ADD R0,R0,#1
HALT
```

Cliquer sur le bouton **ASSEMBLE**. Le simulateur va alors charger toutes les valeurs numériques dans la RAM. Choisir la représentation des nombres en hexadécimal avec le bouton **OPTION** > hex.

{{< img src="../images/STO.png" caption="chargement des valeurs en hexadecimal" >}}

Tester le programme en le déroulant pas à pas (appuis successifs sur le bouton **STEP**)

**2.** **Prog 2**. Obtenir 84 à partir de 90,25,8,7,3 et 1 avec les opérations : addition et soustraction uniquement.

**3.** **Prog 3**. Obtenir 128, en partant de la valeur 1 stockée dans R0. Utilisez les  instructions de multiplication par 2 du langage.
-->
## Programmer avec des boucles





### Prog 1: Calculer 1+2+3...+n où n est entré au clavier: 
Compléter le programme en assembleur ci-dessous pour résoudre le problème puis essayer avec n = 3 en mode pas à pas.

Exécuter avec RUN en vitesse maximale pour n = 10

```
INP R0,2
MOV R1,#0 // compteur de boucle
MOV R2,#0 // somme 
boucle:
ADD ...........
ADD ...........
CMP ...........
.... boucle
OUT R2,4
HALT
```

**questions prog 1.** 

* Estimer le nombre d'opérations significatives effectuées pour n = 10.
* Estimer le nombre d'opérations significatives qui seraient réalisées pour n = 100.
* Ecrire dans votre cahier le script correspondant en python.

### Prog 2: boucle while
Ecrire le programme assembleur équivalent:

```python
x = 0
while x < 3:
      x = x + 1
print(x)
```

A la fin du programme, la variable `x` doit être égale à 3.

*Astuce:* Le `while` est suivi d'une condition d'execution (x<3). Ici, en assembleur, on utilise plutôt une condition d'arrêt.

Ainsi, l'instruction python `while x<3` sera écrite à l'aide de plusieurs lignes en assembleur:

```
CMP R0,#3
BEQ sortieboucle
...
B revenirwhile
```

**questions prog 2.** 

* Quelle est la condition d'arrêt correspondante?
* Ecrire dans votre cahier le script complet en assembleur.

### Prog 3: Pair/Impair
Ecrire en assembleur un programme utilisant des fonctions parmi LSL, LSR, B et BNE qui affiche 1 si le nombre est pair , 0 sinon. (BNE: Branchement si Not Equal).

```python
n = int(input('entrer un nombre'))
x = n//2
x = n * 2
if n == x:
      print(1)
else:
      print(0)
```

**question prog 3.** 

* Ecrire dans votre cahier le script complet en assembleur.

<!--
# Compléments et corrections

* Exemple de programme qui affiche toutes les puissances de 2 jusqu'à 128:*


```
  0       MOV R0, #1
  1       MOV R1, #0
    multiplie:
  2       LSL R0, R0, #1
  3       OUT R0,4
  4       ADD R1,R1,#1
  5       CMP R1, #7
  6       BLT multiplie
  7       HALT
  ```

* Correction de l'exercice somme 1..N

```
      INP R0,2 // demander n
      MOV R1, #0 // somme attention inversion / enonce
      MOV R2, #1 // compteur
boucle:
      ADD R1, R1, R2 // somme
      ADD R2, R2, #1 // compteur incrementer de R1
      CMP R2, R0
      BLT boucle
      OUT R1,4
      HALT
```

* Assembleur pour  le microprocessor Motorola 6800 8-bit (voir image plus haut):

Supposons qu'il existe 2 registres, A et B: Les deux opérations qui s'appellent le stockage (**STA**) et le chargement (**LDA**) du contenu d'une case mémoire dans le registre A (ST pour STore, LD pour LoaD). Il y a bien entendu des opérations similaires pour le registre B (**STB** et **LDB**).

Une autre opération que peut exécuter le processeur est l'addition du contenu du registre A et du contenu du registre B. Et le résultat de l'opération peut être stocké dans le registre A (**ADD A**) ou dans le registre B (**ADD B**). De même, **DEC A** décrémente la valeur contenue dans le registre A, c'est-à-dire soustrait 1 à la valeur contenue dans le registre A et stocke la valeur ainsi obtenue dans le registre A et DEC B réalise le même calcul sur la valeur contenue dans le registre B.

*Exemple:* 

* LDA 7 <=> charger dans la registre A le contenu de la case mémoire n°7.
* LDB 8
* ADD A <=> ajouter le contenu des registres A et B et mettre le résultat dans le registre A
* STA 11 <=> mettre le contenu du registre A dans la case 11.

on pourrait exprimer le programme ci-dessus en binaire en décidant par exemple que l'instruction LDA s'écrit 0, l'instruction LDB s'écrit 1, l'instruction STA s'écrit 2, l'instruction STB s'écrit 3 et l'instruction ADD s'écrit 4, DEC s'écrit 5. A s'écrit 0 et B s'écrit 1. 

Supposons que l'adresse de la première donnée de ce programme en mémoire soit le n°100, on a la suite d'instructions entre les cases mémoires 100 et 107: 0,7,1,8,4,0,2,11

Le processeur doit donc disposer d'un registre appelé *compteur de programme*, PC, qui débute à 100, et qui est incrémenté de 2 après chaque instruction.

A chaque nouvelle instruction, l'**UC** du processeur charge le contenu des cases mémoires d'adresses PC et PC + 1 dans des registres. Son **UAL** décode (operation + argument) et execute:

Par exemple, pour la séquence précédente, les codes **0 et 7** correspondent à l'opération et la donnée pour la première instruction. (LDA 7). Puis viennent **1 et 8**, correspondant à LDB 8, ...etc.

*Tests et branchements:*  Deux instructions supplémentaires seront nécessaires:

**JMP** (jump) suivi de l'argument n charge le nombre n dans le registre PC : sert à détourner le programme de sa route et le forcer à continuer son exécution à l'adresse n. 

**JMZ** (jump if zero): effectue un saut si le contenu du registre A est 0, permet de faire des tests. On ajoute enfin l'instruction END, qui termine le programme. En langage machine, on suppose que JMP s'écrit 6. JMPZ s'écrit 7. END s'écrit 8 avec un argument puisqu'il en faut un : 0.

**JMN** et **JMP** suivi de l'argument n, effectuent un saut si le contenu du registre A est négatif (JMN) ou positif (JMP).

Pour construire une boucle ou un test avec ces nouvelles instructions, il faut tout d'abord trouver une façon de traduire la condition du test ou la condition d'arrêt de la boucle par un test d'égalité à zéro.
-->

# Tuto: simulateur
* Explications en video
{{< img src="/images/video.png" link="https://www.youtube.com/watch?v=mhpwogkbtDU&t=17s" caption="Explications (video) sur le simulateur ARM -" >}}


# Liens
* TP inspiré de [http://www.mathly.fr/archi.php](http://www.mathly.fr/archi.php)
* Cours de David Roche sur [pixees.fr/informatiquelycee](https://pixees.fr/informatiquelycee/n_site/nsi_prem_sim_cpu.html)
* Livre numérique sur le [fonctionnement d'un ordinateur](https://fr.wikibooks.org/wiki/Fonctionnement_d%27un_ordinateur)
* activité sur [l'architecture Von Neumann](http://nsi4noobs.fr/IMG/pdf/e1_1nsi_architecture_von_neumann.pdf)
* Cours de B. Abel: [site lyceum](https://www.lyceum.fr/1g/nsi/6-architectures-materielles-et-systemes-dexploitation/2-jeu-dinstructions-du-processeur/)
* Cours sur l'assembleur, celui du TP: [qkzk.xyz](https://qkzk.xyz/docs/nsi/cours_premiere/architecture/4_assembleur/)
* architecture von Neumann [wikipedia](https://fr.wikipedia.org/wiki/Architecture_de_von_Neumann)
* UAL et multiplexeur [wikipedia](https://fr.m.wikipedia.org/wiki/Unit%C3%A9_arithm%C3%A9tique_et_logique)