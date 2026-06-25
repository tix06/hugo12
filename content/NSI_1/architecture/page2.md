---
Title: architecture 2
description: cycle Von Neumann, processeur, CPU
weight: 5
---

*Cours*:

* Histoire et modèle d'architecture Von Neumann / Harvard: [Lien](../page1/)
* Le fonctionnement d'un processeur: [Lien](../page2/)
* Langage assembleur: [Lien](../page3/)

*Séquence composée de 3 TP:*

* TP1 Composer son ordinateur à partir d'un site commercial: [Lien](../page5/)
* TP2: Comment fonctionne un processeur? [Lien](../page51/)
* TP3: Programmes plus evolués, de python à l'assembleur: [Lien](../page3/)

# Qu'est ce qu'un ordinateur?
Un ordinateur est une *machine* qui traite de *l'information*, stockée dans la *mémoire*, à l'aide du *processeur*. Les instructions de ces traitements sont aussi stockés dans la mémoire, sous forme de *programmes*.

Il existe donc une très grande variété de machines que l'on peut appeler des *ordinateurs*: celles présentes dans une PC de bureau, dans un mac, dans un smartphone, un objet connecté, une voiture...

## Rappels sur l'architecture Von Neumann
Dans l'architecture Von Neumann:

* une machine universelle est contrôlée par un programme.
* Les données et programmes sont écrits sur une même mémoire (en binaire). L'ordinateur enregistre les instructions des programmes qu'il exécute dans sa mémoire vive.
* Les instructions sont executée de manière séquentielle, par un **processeur**.
* Les mémoires RAM d'une part et les mémoires non volatiles d'autre part (Disques durs, mémoires flash) sont reliées au processeur (donc aux registres du processeur) par une liaison appelée Bus. En réalité, seule la RAM est directement accessible au processeur.


# Description d'un ordinateur avec microprocesseur
## En video
{{< img src="/images/video.png" link="https://www.youtube.com/watch?v=5hF4ziHwJBQ" caption="Fonctionnement d'un ordinateur - Mooc Architecture" >}}

## à l'echelle de la carte mère
La carte mère d'un ordinateur comprend:

* un microprocesseur
* de la mémoire volatile (random access memory, RAM)
* de la mémoire de masse
* des ports:
  * port ethernet, RJ45
  * port USB
  * ports pour carte wifi, carte son, carte graphique, ...
* des périphériques d'entrée et sortie: écran, haut-parleur, souris, clavier...

Ces périphériques sont connectés aux 3 *Bus* définis plus loin et se comportent comme une mémoire. On leur affecte des adresses (différentes de celles de la RAM) et on communique avec eux en écrivant à ces adresses. Le Bus de contrôle va detecter un changement sur l'une de ces adresses et interrompre le traitement en cours.

Certains ports vont ajouter des extensions à l'ordinateur (carte son, video, wifi). Certains vont être essentiels au fonctionnement de l'ordinateur (mémoires).

## Liaisons entre composants: les Bus
Il existe des Bus de différentes nature pour relier les composants:

* **bus d'adresse:** permet au processeur d'indiquer à la mémoire l'emplacement pour lire/écrire.
* **bus de données:** transporte les données entre la mémoire et le processeur.
* **bus de contrôle:** permet de coordonner le fonctionnement du processeur et de la mémoire.

Les bus peuvent être bi-directionnels: les données transitent dans les 2 sens. Mais aussi directionnel: c'est le cas du bus d'adresse entre le processeur et la RAM, qui n'est parcouru que dans le sens processeur => RAM.


## à l'echelle des composants
Les constituants de l'ordinateur sont composés de circuits intégrés. On trouve 2 grandes catégories de circuits intégrés:

* les circuits combinatoires: l'état de sortie de ces circuits ne dépend que des états d'entrée.
* les circuits séquentiels: l'état de sortie dépend des états d'entrée, mais aussi de l'état courant du circuit. Ces circuits peuvent ainsi stocker une valeur appelée état courant. Les registres sont typiquement des circuits intégrant des circuits séquentiels.

## CPU et MCU: des architectures différentes
* Certaines machines comportent des composants séparés sur la carte mère. Le **microprocesseur** (CPU) est relié aux autres composants par des bus.

* Pour d'autres machines, comportant **microcontrôleur** (MCU), les composants occupent une même puce (un même *chip*). Ces machines sont moins chères et consomment moins d'électricité. 

*voir page 1 du cours sur l'architecture:* [lien](/docs/NSI_1/architecture/page1/)



# Le fonctionnement du processeur
## Généralités
### Videos sur le fonctionnement du processeur
{{< img src="../images/hervediscours.png" link="https://youtu.be/hJnEnrOqHzM?si=VvWwweDQNsbL6CGC&t=295" caption="Hervé Discours - architecture Von Neumann - illustration avec une cuisine (min 5 - 10)" >}}

{{< img src="/images/video.png" link="https://youtu.be/hJnEnrOqHzM?si=m93F0xs8KLClVrNG&t=903" caption="Hervé Discours - architecture Von Neumann - déroulé d'un programme (min 15 - 20), archi X2, memoire cache (min 20-25)" >}}

{{< img src="/images/video.png" link="https://youtu.be/hJnEnrOqHzM?si=jxuQmhHcsPg7C3Vc&t=1788" caption="Hervé Discours - architecture Von Neumann - langage assembleur (min 29 - 35)" >}}


### Les 2 sous parties du processeur
{{< img src="../images/architectureN2.png" caption="Architecture de Von-Neumann - processeur" >}}
L'architecture d'un **processeur** (CPU) comporte 2 parties: 

* L'**UC**: C'est l’*unité de commande*, **UC**, qui traduit chacune des instructions successives du programme en opérations élémentaires. C'est cette partie du processeur  qui est chargée d'obtenir les instructions successives du programme et de les executer. L'**UC** contient:
  * le registre Program Counter, PC
  * le registre d'instruction RI 
  * une horloge.
* La **partie opérative** qui comprend les outils permettent de réaliser les actions élémentaires ordonnés par l'UC. Cette **unité de traitement** est constituée de:
  * l'**UAL** (Unité Arithmétique et Logique) qui réalise les opérations arithmétiques sur des entiers.
  * des **registres internes**, pour stocker de manière très provisoire les retenues des calculs par exemple.

*L'UC traite une séquence d'instructions, alors que l'UAL traite une séquence de données*. L’**UC** est chargée de la reconnaissance des instructions et de leur exécution par l’unité de traitement au *rythme de l’horloge*.

## Le cycle Von Neumann
Le processeur réalise le **cycle de Von Neumann**:

1. Lire une case mémoire d’adresse PC (envoyer l’adresse à la mémoire, et recevoir en retour la donnée à cette adresse).
2. Interpréter cette donnée comme une instruction, et l’exécuter
3. Ajouter 1 au *program Counter* (PC), qui stocke l'adresse de la prochaine instruction.
4. Recommencer

## Détail d'un cycle d'execution
**Important**:

Le processeur ne manipule *pas directement* les données mais leurs *adresses*.

Des **registres** servent à lire et écrire les données en mémoire. Ce sont les registres d'adresse et de données.

### Utilisation des registres en lecture: rôle de l'unité de contrôle
* registre d'adresse: stocke l'adresse de la donnée, avant d'envoyer le signal de lecture
* registre de données: la mémoire va chercher le contenu de l'adresse qui lui est envoyée, et retourne la donnée vers le registre de données. 

La donnée peut être interprétée comme une instruction. Celle-ci est alors décomposée en un code d'opération (OP) ainsi qu'en 2 opérandes, qui sont les adresses d'une données (A et B). OP, A et B sont stockés dans le registre d'instruction (RI).

### Execution de l'opération: rôle de l'unité de traitement
La figure ci-contre représente un schéma classique d'UAL. Celle-ci possède deux entrées A et B sur lesquelles on présente les données à traiter. L'entrée F désigne l'opération à effectuer (vient du code OP). [Source: wikipedia - Unité Arithmétique et Logique](https://fr.wikipedia.org/wiki/Unit%C3%A9_arithm%C3%A9tique_et_logique)

Enfin, l'UAL possède deux sorties, R qui est le résultat de l'opération, et D les éventuels drapeaux. (information d'erreur ou de dépassement)

{{< img src="../images/ALU.png" caption="UAL - Unité Arithmétique et Logique" >}}

### Utilisation en écriture
* registre d'adresse: envoie à la mémoire l'adresse pour l'écriture
* registre de données: envoie la donnée à la mémoire, qui va écrire celle-ci à l'adresse reçue.

# Travail pratique
[programmer en assembleur](../page3/)

# Liens

* Cours de David Roche sur [pixees.fr/informatiquelycee](https://pixees.fr/informatiquelycee/n_site/nsi_prem_sim_cpu.html)
* Livre numérique sur le [fonctionnement d'un ordinateur](https://fr.wikibooks.org/wiki/Fonctionnement_d%27un_ordinateur)
* activité sur [l'architecture Von Neumann](http://nsi4noobs.fr/IMG/pdf/e1_1nsi_architecture_von_neumann.pdf)

* architecture von Neumann [wikipedia](https://fr.wikipedia.org/wiki/Architecture_de_von_Neumann)
* UAL et multiplexeur [wikipedia](https://fr.m.wikipedia.org/wiki/Unit%C3%A9_arithm%C3%A9tique_et_logique)
* Bref historique (fiche) de l'evolution des ordinateur et des systemes d'exploitation: [courstechinfo.be](https://courstechinfo.be/Techno/Historique2.pdf)
