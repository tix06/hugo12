---
Title: architecture
description: architecture, binaire, ordonnancement, commandes Unix
weight: 66
---

# Bac 2022 Polynesie: Exercice 2
*Cet exercice traite du thème « architecture matérielle », et principalement d'ordonnancement et d'expressions booléennes.*

{{% badge icon="star" %}}ordonnancement{{% /badge %}} {{% badge icon="star" %}}logique{{% /badge %}}

Un système est composé de 4 périphériques, numérotés de 0 à 3, et d'une mémoire, reliés entre eux par un bus auquel est également connecté un dispositif ordonnanceur. 
À l'aide d'un signal spécifique envoyé sur le bus, l'ordonnanceur sollicite à tour de rôle les périphériques pour qu'ils indiquent le type d'opération (lecture ou écriture) qu'ils souhaitent effectuer, et l'adresse mémoire concernée.

Un tour a lieu quand les 4 périphériques ont été sollicités. **Au début d'un nouveau tour, on considère que toutes les adresses sont disponibles en lecture et écriture.**

Si un périphérique demande l'écriture à une adresse mémoire **à laquelle on n'a pas encore accédé** pendant le tour, l'ordonnanceur répond "OK" et l'écriture a lieu.
Si on a déjà demandé la lecture ou l'écriture à cette adresse, l'ordonnanceur répond "ATT" et l'opération n'a pas lieu.

Si un périphérique demande la lecture à une adresse à laquelle on n'a pas encore accédé en écriture pendant le tour, l'ordonnanceur répond "OK" et la lecture a lieu.
Plusieurs lectures peuvent avoir donc lieu pendant le même tour à la même adresse.

Si un périphérique demande la lecture à une adresse à laquelle on a déjà accédé en écriture, l'ordonnanceur répond "ATT" et la lecture n'a pas lieu.

Ainsi, pendant un tour, une adresse peut être utilisée soit une seule fois en écriture, soit autant de fois qu'on veut en lecture, soit pas utilisée.

Si un périphérique ne peut pas effectuer une opération à une adresse, il demande la même opération à la même adresse au tour suivant.

## Question 1
Le tableau donné en annexe 1 indique, sur chaque ligne, le périphérique
sélectionné, l'adresse à laquelle il souhaite accéder et l'opération à effectuer sur cette adresse. Compléter dans la dernière colonne de cette annexe, à rendre avec la copie, la réponse donnée par l'ordonnanceur pour chaque opération.

On suppose dans toute la suite que :

* le périphérique 0 écrit systématiquement à l'adresse 10 ;
* le périphérique 1 lit systématiquement à l'adresse 10 ;
* le périphérique 2 écrit alternativement aux adresses 11 et 12 ;
* le périphérique 3 lit alternativement aux adresses 11 et 12 ;

Pour les périphériques 2 et 3, le changement d’adresse n’est effectif que lorsque l’opération et réalisée. 

## Question 2
On suppose que les périphériques sont sélectionnés à chaque tour dans l'ordre
0 ; 1 ; 2 ; 3. Expliquer ce qu'il se passe pour le périphérique 1.

Les périphériques sont sollicités de la manière suivante lors de quatre tours successifs :

* au premier tour, ils sont sollicités dans l’ordre 0 ; 1 ; 2 ; 3 ;
* au deuxième tour, dans l’ordre 1 ; 2 ; 3 ; 0 ;
* au troisième tour, 2 ; 3 ; 0 ; 1 ;
* puis 3 ; 0 ; 1 ; 2 au dernier tour.
* Et on recommence...

## Question 3
A.  Préciser pour chacun de ces tours si le périphérique 0 peut écrire et si le
périphérique 1 peut lire.

B.  En déduire la proportion des valeurs écrites par le périphérique 0 qui sont
effectivement lues par le périphérique 1.


On change la méthode d'ordonnancement : on détermine l'ordre des périphériques au cours d'un tour à l'aide de deux listes d'attente `ATTL_L` et `ATT_E` établies au tour précédent.

Au cours d'un tour, on place dans la liste `ATT_L` toutes les opérations de lecture mises en attente, et dans la liste d'attente `ATT_E` toutes les opérations d'écriture mises en attente.

Au début du tour suivant, on établit l'ordre d'interrogation des périphériques en procédant ainsi :

* on interroge ceux présents dans la liste ATT_L, par ordre croissant d'adresse,
* on interroge ensuite ceux présents dans la liste ATT_E, par ordre croissant
d'adresse,
* puis on interroge les périphériques restants, par ordre croissant d’adresse.

## Question 4
Compléter et rendre avec la copie le tableau fourni en annexe 2, en utilisant
l'ordonnancement décrit ci-dessus, sur 3 tours.

Les colonnes e0 et e1 du tableau suivant recensent les deux chiffres de l'écriture binaire de l’entier n de la première colonne.

| nombre n | écriture binaire de n sur deux bits | e1 | e0 |
|--- |--- |--- |--- |
| 0 | 00 | 0 | 0 |
| 1 | 01 | 0 | 1 |
| 2 | 10 | 1 | 0 |
|3  | 11 | 1 | 1 |


L'ordonnanceur attribue à deux signaux sur le bus de données les valeurs de **e0** et **e1** associées au numéro du circuit qu’il veut sélectionner. On souhaite construire à l'aide des portes ET, OU et NON un circuit pour chaque périphérique.

Chacun des quatre circuits à construire prend en entrée deux signaux **e0** et **e1**, le signal de sortie **s** valant 1 uniquement lorsque les niveaux de **e0** et **e1** correspondent aux bits de l'écriture en binaire du numéro du périphérique correspondant.

Par exemple, le circuit ci-dessous réalise la sélection du périphérique 3. En effet, le signal **s** vaut 1 si et seulement si **e0** et **e1** valent tous les deux 1.

{{< img src="../images/page6_1.png" caption="470 × 138" >}}
## Question 5
A.  Recopier sur la copie et indiquer dans le circuit ci-dessous les entrées e0 et e1 de façon à ce que ce circuit sélectionne le périphérique 1.

{{< img src="../images/page6_2.png" caption="566 × 170" >}}
B.  Dessiner un circuit constitué d'une porte ET et d'une porte NON, qui
sélectionne le périphérique 2.
c. Dessiner un circuit permettant de sélectionner le périphérique 0.

{{< img src="../images/page6_3.png" caption="1252 × 590" >}}
{{< img src="../images/page6_4.png" caption="1252 × 788" >}}


# bac 2021 candidat libre exercice 3

{{% badge icon="star" %}}cmd unix{{% /badge %}}

La commande UNIX `ps` présente un cliché instantané des processus en cours d’exécution.

Avec l’option `−eo pid,ppid,stat,command`, cette commande affiche dans l’ordre l’identifiant du processus `PID` (process identifier), le `PPID` (parent process identifier), l’état `STAT` et le nom de la commande à l’origine du processus.

Les valeurs du champ `STAT` indique l’état des processus :

`R` : processus en cours d’exécution

`S` : processus endormi

Sur un ordinateur, on exécute la commande `ps −eo pid,ppid,stat,command` et on obtient un affichage dont on donne ci-dessous un extrait:

{{< img src="../images/page6_7.png" >}}

À l’aide de cet affichage, répondre aux questions ci-dessous.

1. Quel est le nom de la première commande exécutée par le système d’exploitation lors du démarrage?
2. Quels sont les identifiants des processus actifs sur cet ordinateur au moment de l’appel de la commande `ps`? Justifier la réponse.
3. Depuis quelle application a-t-on exécuté la commande `ps`? Donner les autres commandes qui ont été exécutées à partir de cette application.
4. Expliquer l’ordre dans lequel les deux commandes `python programme1.py` et `python programme2.py` ont été exécutées.
5. Peut-on prédire que l’une des deux commandes `python programme1.py` et `python programme2.py` finira avant l’autre?

# bac 2021 candidat libre exercice 2 sujet 2

{{% badge icon="star" %}}ordonnancement{{% /badge %}}

## Les états possibles d’un processus sont : prêt, élu, terminé et bloqué.
1. Expliquer à quoi correspond l’état élu.

2. Proposer un schéma illustrant les passages entre les différents états.

On suppose que quatre processus C₁, C₂, C₃ et C₄ sont créés sur un ordinateur, et qu’aucun autre processus n’est lancé sur celui-ci, ni préalablement ni pendant l’exécution des quatre processus.

L’ordonnanceur, pour exécuter les différents processus prêts, les place dans une structure de données de type file. Un processus prêt est enfilé et un processus élu est défilé.

## Parmi les propositions suivantes, recopier celle qui décrit le fonctionnement des entrées/sorties dans une file :

* Premier entré, dernier sorti
* Premier entré, premier sorti
* Dernier entré, premier sorti

## On suppose que les quatre processus arrivent dans la file et y sont placés dans l’ordre C₁, C₂, C₃ et C₄.

Les temps d’exécution totaux de C₁, C₂, C₃ et C₄ sont respectivement 100 ms, 150 ms, 80 ms et 60 ms.

Après 40 ms d’exécution, le processus C₁ demande une opération d’écriture disque, opération qui dure 200 ms. Pendant cette opération d’écriture, le processus C₁ passe à l’état bloqué.

Après 20 ms d’exécution, le processus C₃ demande une opération d’écriture disque, opération qui dure 10 ms. Pendant cette opération d’écriture, le processus C₃ passe à l’état bloqué.

Sur la frise chronologique donnée en annexe (à rendre avec la copie), les états du processus C₂ sont donnés. 

> Compléter la frise avec les états des processus C₁, C₃ et C₄.


{{< img src="../images/page6_8.png" caption="Annexe de l’exercice 2" >}}


## On trouvera ci-dessous deux programmes rédigés en pseudo-code.

Verrouiller un fichier signifie que le programme demande un accès exclusif au fichier et l’obtient si le fichier est disponible.

| Programme 1 | 	Programme 2 |
|--- |--- |
| Verrouiller fichier_1	| Verrouiller fichier_2 |
| Calculs sur fichier_1 | 	Verrouiller fichier_1 |
| Verrouiller fichier_2 |	Calculs sur fichier_1 |
| Calculs sur fichier_1	 | Calculs sur fichier_2 |
| Calculs sur fichier_2 |	Déverrouiller fichier_1 |
| Calculs sur fichier_1	 | Déverrouiller fichier_2 |
| Déverrouiller fichier_2	 |   |
| Déverrouiller fichier_1	 |   |

1. En supposant que les processus correspondant à ces programmes s’exécutent simultanément (exécution concurrente), expliquer le problème qui peut être rencontré.

2. Proposer une modification du programme 2 permettant d’éviter ce problème.


