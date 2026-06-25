---
Title: TP simulation portes logiques
description: TP simulation portes logiques
weight: 11
---

# TP et outils
On utilisera:

* Le simulateur de circuit électronique en ligne: [https://logic.ly/demo/](https://logic.ly/demo/)
* Le logiciel Writer pour compléter la [fiche réponses](/pdf/NSI_1/DocumentRéponse.odt).

## Prise en main du logiciel
Représenter les 3 circuits ci-dessous avec l'editeur logic.ly

{{< img src="../images/sim-circ.png" link="https://logic.ly/demo/" caption="Exemples de circtuits créés à l'aide du simulateur logic.ly" >}}

**Questions:** 

**1.a.** Les circuits permettent-il une interaction avec l'utilisateur?

**1.b.** Pour chaque circuit: Quels sont les composants utilisés?

**1.c.** Pour chacun des circuits: Expliquer le comportement du circuit, pourquoi la lampe s'allume (ou pas)?

Toute fonction logique peut se décomposer en fonctions NON, ET, OU. Les exemples suivants ont pour but de se familiariser avec ces combinaisons de portes logiques, et d'aboutir à la construction d'un ADDITIONNEUR à 2 bits.

## Simulation d'une porte logique NON
Voici le schéma formel représentant la fonction NON, réalisée à l'aide d'une porte logique NAND (NON ET):

{{< img src="../images/Nand2Not.png" caption="schéma formel" >}}

Vous allez adapter ce schéma pour réaliser sur le circuit suivant sur le simulateur:

{{< img src="../images/Nand2Not2.png" caption="realisation sur logic.ly" >}}

Les 2 entrées de la portes NAND sont reliées au même interrupteur. L'interrupteur fournit une tension au circuit, à 2 état (Allumé / Eteint).

Une lampe est aussi mise en entrée, sur l'interrupteur, afin de visualiser l'état d'entrée.

**2.a.** Représenter la table des états pour ce dispositif. S'agit-il de la même table que celle de l'opérateur NON?

| E | S |
| --- | --- |
| 0 |   |
| 1 |   |

**La formule logique** associée au schéma que vous avez réalisé est:

$$NOT(x) = NAND(x,x)$$

**2.b.** Commentez cette **formule**. Identifiez chacun des termes par rapport au circuit.

## Simulation d'une porte logique ET
Voici le schéma formel représentant la fonction ET, réalisée à partir des portes logiques NOT et NAND:

{{< img src="../images/Nand2And.png" caption="schéma formel" >}}

Réalisez le circuit correspondant sur *logic.ly*

**3.a.** Représenter la table des états pour ce dispositif. S'agit-il de la même table que celle de l'opérateur ET?

| E1 | E2 | S |
| --- | --- | --- |
|   | 0 |   |   
|   | 1 |   |
|   | 0 |   |   
|   | 1 |   |

La formule correspondant à cette association est:

$$AND(x,y) = NOT(NAND(x,y))$$

**3.b.** Commentez cette formule. Identifiez chacun des termes par rapport au circuit.

## Porte logique OR
Sachant que:
$$NOT(OR(x,y)) = AND(NOT(x),NOT(y))$$



**4.a.** Construire et représenter le schéma électronique de $AND(NOT(x),NOT(y))$ à partir des portes AND et NOT.

**4.b.** Ce circuit est-il équivalent à $NOT(OR(x,y))$?

**4.c.** Conclure: Comment réaliser la fonction $OR(x,y)$ à partir des portes NOT et AND?

## Additionneur 1 bit
Un additionneur 1 bit est vu comme deux fonctions booléennes `s` le chiffre des unités et `cout` la retenue de sortie dépendant de trois entrées:

* 3 entrées : deux bits `a` et `b` et une retenue d'entrée `cin` 

* 2 sorties : Le bit de résultat `s` et une retenue de sortie `cout`



**5.a.** Créer un circuit add1 qui implémente l'additionneur 1 bit à partir du schéma ci-dessous

{{< img src="../images/add_1_bit.png" caption="Additionneur 1 bit" >}}

**5.b.** Compléter la table de vérité des fonctions `s` et `cout`

| a | b | cin | s | cout |
| --- | --- | --- |--- | --- |
|   | 0  | 0 |   |    |
|   |  0 | 1 |   |  |
|   |  1 | 0 |   |    |
|   |  1 | 1 |   |  |
|   | 0  | 0 |   |    |
|   |  0 | 1 |   |  |
|   |  1 | 0 |   |    |
|   |  1 | 1 |   |  |

**5.c.** Expliquez en quoi le circuit suivant est bien un additionneur de 2 bits, avec retenue.

*Le TP est inspiré de {{< a link="http://www.mathly.fr/tp_portes.php" caption="mathly.fr" >}}*

# Liens


* autre logiciel de simulation electronique en ligne : https://www.lucidchart.com/pages/fr/exemple/logiciel-schema-electrique
* Enoncé original sur: {{< a link="http://www.mathly.fr/tp_portes.php" caption="mathly.fr" >}}
