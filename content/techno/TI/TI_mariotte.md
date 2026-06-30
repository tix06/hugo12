---
Title : Loi de Mariotte
description: TP utilisant la calculatrice TI83, l'extension avec la carte microbit et le dispositif de mesure de pression volume
weight: 16
---

# Ti83 et loi de Mariotte

{{< img src="../images/TI_pv.png" caption="dispositif TI83CE microbit capteur" >}}
## Matériel

* TI 83 CE edition Python
* carte microbit
* Capteur grove MPX5700AP capable de mesurer la pression de l'air dans une plage de 15 kPa à 700 kPa. Sensibilté 6,4 mV/kPa.

## Notice
Les différents programmes `PRESS.8xv` et `BOYLEMAR.8xv` seront déjà installés sur la calculatrice. Celle-ci devra être préparée avec les librairies utiles selon la procédure expliquée sur la [Fiche de prise en main](/pdf/SNT_texas/MBpresentation.pdf)

> Préparer le matériel

* La carte microbit doit être équipée du shield grove.
* Connecter la calculatrice sur la carte microbit. 
* Connecter le capteur de pression sur le shield (entrée PIN0).
* Mettre la seringue dans la position 12mL et fermer celle-ci sur le capteur.

> Lancer le programme

* Sur la calculatrice: Touche **prgm**: Choisir 2-Python App
* Dans la liste des programmes installés: Choisir BOYLEMAR avec le curseur. Valider avec la touche **entrer**.
* Touche **var**. Choisir la fonction `mesure()`. Valider avec **OK** (touche **graphe**).
* Vous avez alors 3s pour positionner et maintenir la seringue sur le volume 2mL comme indiqué sur l'écran. Puis à nouveau 3s pour chacun des autres volumes proposés... 
* Une fois la serie de mesures réalisée, le graphique P-V est affiché à l'écran.
* Pour prendre connaissance et traiter les données: 
  * Revenir en mode calculatrice: touche **on** puis **2nde** **mode(quitter)**. Valider.
  * touche **stats** puis *1:modifier*. La liste 1 est celle du volume(mL) et la liste 2 celle de la pression(kPa).

{{< img src="../images/TI_capture1.png" caption="tableau de mesures obtenu à 25°C" >}}
## Liens vers les documents

* Prise en main du dispositif [TP0 Fiche de JL. Balas](/pdf/SNT_texas/MBpresentation.pdf)
* TP Loi de Mariotte: [Fiche Ti de A. Yazi](/pdf/SNT_texas/pression.pdf)
* [PRESS.8xv](/pdf/SNT_texas/PRESS.8xv)
* [BOYLEMAR.8xv](/pdf/SNT_texas/BOYLEMAR.8xv)
