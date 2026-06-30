---
Title: portes logiques
description: etude des portes logiques en circuit integré, branchements sur la carte microbit
weight: 22
---

# TP Portes logiques - NSI Term
## But de la seance
Vous allez étudier les portes logiques fournies pour la seance. Vous utiliserez une carte microcontrôleur *Microbit* pour disposer d'une générateur de tension à 2 sorties. Chacune de ces sorties sera branché à l'une des entrées de la porte logique. Les boutons de la carte microbit serviront à choisir le niveau de tension 0 ou 3,3V pour les entrées de la porte logique.

## Progammer la carte microbit
La carte microbit est présentée dans [cette fiche](/docs/techno/pages/MB_init/).

Dans un premier temps, vous allez consulter la [fiche du TP](/docs/techno/pages/MB_led/) sur le clignottement d'une Diode Electroluminescente.

Ce que doit réaliser le programme: On pilote les niveaux de tension PIN0 et PIN1 à l'aide des boutons a et b de la carte microbit:

| bouton | niveau de tension |
|--- |--- |
| **a** relâché | PIN0 à 0V |
| **a** appuyé | PIN0 à 3,3V |
| **b** relâché | PIN1 à 0V |
| **b** appuyé | PIN1 à 3,3V |

Sur l'**editeur Mu**: Copier et compléter le programme suivant. *Brancher* la carte microbit sur un port USB de l'ordinateur (maintenir le câble au cours de la seance). Et *flasher* la carte (charger le programme).

```python
# Ecrit ton programme ici ;-)
# Jaune: tension commandée : relier au + de la LED  
# Noir: GND : relier à la resistance 1k
# Rouge du PIN1 : relier à la borne +Vcc du circuit integre
# Blanc: non utilises
from microbit import *

while True:
    if button_a.is_pressed():
      # à completer

```

## PIN0 et PIN1 de la carte
Brancher les connecteurs grove sur les PIN0 et PIN1. Utiliser alors des fils electriques pour acceder aux contacts des connecteurs grove:

* PIN0: contact noir (0V)
* PIN0: contact jaune (0 ou 3,3V selon le programme)
* PIN1: contact noir (0V)
* PIN1: contact rouge (3,3V fixe)
* PIN1: contact jaune (0 ou 3,3V selon le programme)

{{< img src="../images/portes/porte1.JPG" alt="carte microbit" caption="conneceurs grove de la carte microbit" >}}
Relier alors les contacts noirs et jaune de chaque connecteur grove sur une ligne verticale de la plaquette d'essai (breadboard).

{{< img src="../images/portes/porte2.JPG" alt="connection carte microbit sur breadboard" caption="connection carte microbit sur breadboard" >}}
## Premiers essais
On va maintenant utiliser la diode electroluminescente pour tester si le programme fonctionne: Brancher la diode en série avec sa resistance de protection $1k\Ohm$ aux bornes de la tension du PIN0 (entre les contacts jaune et noir).

{{< img src="../images/portes/porte5.JPG" alt="DEL et resistance de protection" caption="Branchement en serie de la DEL" >}}
Tester si celle-ci s'allume lorsque l'on appuie sur le bouton.

## Cabler la porte logique
Les circuits intégrés fournis pour la seance sont de différents types. Certaines possèdent des portes logiques à 2 entrées (AND, OR, NAND), alors que celle NAND ne possède qu'une entrée. Des marques de couleur ont été peintes pour les identifier plus facilement:

| code | porte logique |
|--- |--- |
| 4081 (bleue) | AND |
| 4071 (orange) | OR |
| 4011 (jaune) | NAND |
| 4069 (vert) | NOT |

Chaque circuit intégré comporte plusieurs portes logiques. Pour celles à 2 entrées, on peut les repérer comme sur le schéma suivant:

{{< img src="../images/portes/porte3.png" alt="portes logiques PIN 2 entrées" caption="Portes logiques à 2 entrées" >}}
Pour le circuit NOT, à une entrée, la disposition des portes logiques est comme ceci:

{{< img src="../images/portes/porte4.png" alt="portes logiques PIN 1 entrée" caption="Portes logiques NOT" >}}
* Disposer le circuit integré jaune 4011 sur le breadboard
* selectionner l'une des portes logique du composant



* Brancher la diode avec, en serie, sa resistance de protection à la sortie de la porte logique. Fermer le circuit de la diode sur l'un des contacts noirs (0V) de PIN0 ou PIN1.



* alimenter le circuit intégré: brancher la borne **+Vcc** sur le contact rouge du PIN1 (3,3V) et la borne **GND** (masse) sur l'un des contacts noirs (0V) de PIN0 ou PIN1.

{{< img src="../images/portes/porte7.JPG" alt="diode en sortie" caption="branchement de la diode en sortie" >}}
* brancher les contacts commandés (jaunes) des PIN0 et PIN1 sur les entrées de la porte logique

{{< img src="../images/portes/porte6.JPG" alt="circuit complet à porte logique" caption="circuit complet" >}}
* Actionner alors les boutons a et b de la carte microbit pour tester toutes les combinaisons possibles en entrée. Renseigner la table de vérité.

| E1 | E2 | S |
| --- | --- | --- |
| 0 | 0 |  |
| 0 | 1 |  |
| 1 | 0 |  |
| 1 | 1 |  |


## Prolongements
Modifier le montage pour tester les autres portes logiques fournies.



