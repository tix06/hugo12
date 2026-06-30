---
Title : Ti83 et mise a niveau microbit
description: mettre a jour charger les modules pour la connexion de la carte microbit avec la calculatrice TI83
weight: 14
---

# Mettre à jour la calculatrice TI-83 Premium CE
## Installer TI CONNECT sur votre ordinateur
{{< img src="../images/maj_ti833.png" caption="Choisissez le modèle de votre calculatrice" >}}
Cliquez sur le bouton *Suivant*.

{{< img src="../images/maj_ti4.png" caption="Télécharger le logiciel Ti-Connect le plus récent" >}}
Installez alors le **logiciel TI CONNECT** sur votre ordinateur: Executer le fichier téléchargé et suivre les instructions d'installation.

## Mettre à jour la calculatrice

Sur la même page du site Texas-Instruments:

{{< img src="../images/maj_ti5.png" caption="Télécharger le système d'exploitation le plus récent pour votre calculatrice" >}}
* Lancer le logiciel TI CONNECT et brancher la calculatrice sur le port USB de votre ordinateur (cable USB vers usb B fourni).

{{< img src="../images/maj_ti7.png" caption="connexion calculatrice - ordinateur" >}}
* Cliquer sur 

1. l'*explorateur de calculatrice* **(1)**,
2. puis sur *ajouter les données de l'ordinateur vers la calculatrice connectée* **(2)**.

{{< img src="../images/maj_ti8.png" caption="explorateur de calculatrice sur TI CONNECT" >}}
L'explorateur de votre ordinateur devrait vous permettre de retrouver le fichier `TI83CEBundle-5.5.2.44.b83` (la version peut différer au moment de votre téléchargement). 

* Sélectionner le fichier.

* Suivre les instructions d'installation.

# Testez votre premier script Python

{{< img src="../images/ti_prise_main.png" alt="video Yvan Monka Ti83" link="https://youtu.be/db5mbuBATEs" caption="Video Yvan Monka: prise en main de la Ti83 Ed python" >}}
# Utiliser des extensions

## Préparer la calculatrice pour utiliser la carte micro:bit

{{< img src="../images/maj_ti2.png" alt="TI83 et microbit" caption="Ti-83 Premium CE Python et micro:bit" >}}
### Télécharger les modules
Se rendre du la page de téléchargement du site Texas Instrument:{{< a link="https://resources.t3france.fr/t3france?resource_id=3078&cHash=513acef78cfa6d808465417be9e08cc3t" caption="Lien" >}}
{{< img src="../images/maj_ti1.png" link="https://resources.t3france.fr/t3france?resource_id=3078&cHash=513acef78cfa6d808465417be9e08cc3t" >}} 

Vous pouvez télécharger l'ensemble de ces fichiers, en un seul *clic*, depuis{{< a link="https://resources.t3france.fr/t3france?resource_id=3078&cHash=513acef78cfa6d808465417be9e08cc3" caption="la page du site Texas instruments" >}}
{{< img src="../images/maj_TI9.png" >}}
Téléchargez le dossier "modules_microbit V1.zip" ou "modules_microbit V2.zip" selon le modèle de carte dont vous disposez

Ceux-ci devraient se trouver dans votre dossier *téléchargements*.

### Téléverser les modules dans la calculatrice

* Lancer le logiciel TI CONNECT et brancher la calculatrice sur le port USB de votre ordinateur (cable USB vers usb B fourni).

{{< img src="../images/maj_ti7.png" caption="connexion calculatrice - ordinateur" >}}
Suivre la même procédure que pour la mise à jour de la calculatrice: Cliquer sur *ajouter les données de l'ordinateur à la calculatrice connectée*. Et sélectionner en une seule fois tous les modules à installer:

* MICROBIT.8xv
* MB_GROVE.8xv
* MB_SENSR.8xv
* MB_RADIO.8xv
* MB_PINS.8xv
* MB_BUTNS.8xv
* MB_DISP.8xv
* ...



# Liens
* Prise en main de la calculatrice et autres tips: [letutosmaths](https://www.lestutosmaths.fr/fr)
* Prise en main du module Python sur la calculatrice TI-83 avec [Ti codes](https://education.ti.com/fr/mises-a-jour-et-logiciels/ti-codes/python/83)
* Chaine Youtube de Yvan Monka du site www.maths-et-tiques.fr: [Lien](https://www.youtube.com/channel/UCaDqmzanCq4ZYhdEm0Df9Qg)
* Chaine Youtube pour pour utiliser la calculatrice TI-83 Premium CE Python avec le microcontrôleur micro:bit : [lien](https://www.youtube.com/playlist?list=PL4V-Xo0EMx4gDQkLAU6pwVKfqCN-sl-T_)

