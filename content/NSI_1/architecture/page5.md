---
Title: ordinateur et processeur
description: monter un ordinateur, carte mère, composants
hidden: true
weight: 7
---

*Séquence composée de 3 parties:*

* TP1 Composer son ordinateur à partir d'un site commercial: [Lien](/docs/NSI_1/architecture/page5/)
* TP2: Comment fonctionne un processeur? [Lien](/docs/NSI_1/architecture/page51/)
* TP3: Programmes plus evolués, de python à l'assembleur: [Lien](/docs/NSI_1/architecture/page3/)

*Cours*:

* Modèle d'architecture Von Neumann: [Lien](/docs/NSI_1/architecture/page2/)

# Comment monter un PC à partir de sa carte mère?
## Activités
> Aller sur le site [LDLC.com](https://www.ldlc.com/informatique/pieces-informatique/carte-mere/c4293/) et choisir, parmi les pièces détachées, la première carte mère proposée. Cliquer sur l'onglet *Fiche Technique*, et selectionner les *références* proposés ci-dessous:

{{< img src="../images/criteres.png" >}}

### Quelle-s carte-s mère-s est-sont proposée-s?
### Faire un tableau avec chacune des références proposées, et en regard, la *désignation*:

| référence | désignation |
|--- |--- |
| DDR4 |type de RAM | 
| AMD AM4 |... | 
| ... |... | 

### Définir chacun des termes de la colonne *désignation*. On pourra faire une recherche sur internet, ou voir la video suivante:


{{< img src="../images/mooc_nsi.png" link="https://www.youtube.com/watch?v=OyCuVWKhmx4" caption="Chaine Youtube Mooc NSI" >}}

### Retrouver les différents éléments qu'il faudra ajouter sur la carte mère ci-dessous:

{{< img src="../images/CM_phantom.jpg" caption="carte ASRock A520M Phantom Gaming 4" >}}

### Repérer également sur cette carte les nappes de fils de connexions parallèles (appelée *Bus*). [Explications ici.](https://web.maths.unsw.edu.au/~lafaye/CCM/pc/bus.htm)

## Bilan
* Représenter les bus reliant les différents composants de la carte mère (voir ex 4 de la [feuille de TD](/pdf/NSI_1/archi_1_transistors.pdf)

{{< img src="../images/carte_mere.png" >}}

* Le processeur Intel 8080 (1974) avait une vitesse d’horloge de 2 MHz. L’exécution d’une instruction nécessitait entre 4 et 11 cycles d’horloge, selon l’instruction. Quel est le nombre moyen d’instruction qu’il pouvait exécuter par seconde ? (voir ex 1 de la [feuille de TD](/pdf/NSI_1/archi_2_transistors.pdf))
* On donne la loi du calcul du *débit* en bits/s pour le bus de données reliant le processeur à la RAM? : $$D = freq \times 8$$ Expliciter chacun des termes.
* Le 8080 utilisait un bus d'adresses sur 16 bits et un bus de données sur 8 bits, donnant un accès facile à 64 Ko de mémoire. Il avait sept registres de 8 bits, et un compteur de programme sur 16 bits. Quel était le débit par le bus de données reliant le processeur à la RAM? 
* Le processeur ATMEL  AVR est également un processeur 8 bits, souvent utilisé dans les cartes Arduino. Il a une horloge de 20 MHz et toutes les instructions s’exécutent en 1 cycle d’horloge (à part la multiplication). Combien de fois est-il plus rapide que l’Intel 8080 ? (voir ex 1 de la [feuille de TD](/pdf/NSI_1/archi_2_transistors.pdf))
* Le debit du Bus pour les DDR4 est donné à 39 000 Mbits/s. Calculer le temps d'échange pour charger une matrice de 36Mo.


# Comment choisir un processeur?
## Activité
> Aller sur le site [LDLC.com](https://www.ldlc.com/informatique/pieces-informatique/processeur/c4300/) et choisir, parmi les pièces détachées, le premier processeur proposé. Cliquer sur l'onglet *Fiche Technique*, et selectionner les *références* proposés ci-dessous:

{{< img src="../images/critere_proc.png" >}}

### Quel-s processeur-s est-sont proposé-s?
### Faire un tableau avec chacune des références proposées, et en regard, la *désignation*:

| référence | désignation |
|--- |--- |
| 6 |nombre de Coeurs | 
| 12 | nombre de Threads | 
| ... |... | 

### Définir chacun des termes de la colonne *désignation*. On pourra utiliser le [glossaire suivant](https://www.materiel.net/guide-achat/g5-le-processeur-pc/9117/).
### Préciser la différence entre le nombre de Coeurs et le nombre de Threads

{{< img src="../images/coeur_thread.png" link="https://www.youtube.com/watch?v=z80inke28CM" caption="Chaine Youtube Le Vlog High Tech" >}}


## Bilan
* A l'aide d'un schéma, placer les différentes mémoires, présentes à l'intérieur ou à l'exterieur d'un microprocesseur, en précisant leur éloignement par rapport à l'Unité de Contrôle: registres, cache, et RAM.
* Définir ce qu'est le *parallélisme*.

# Décrire le fil d'execution d'un processeur ([seance 2](../page51))
