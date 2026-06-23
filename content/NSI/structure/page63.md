---
Title: coloration d'un graphe
description: bac Am Nord J1 2025, coloration d'un graphe, networkx
hidden: true
weight: 46
---

Le notebook se trouve à l'adresse: [capytale](https://capytale2.ac-paris.fr/web/c/0938-8932097)

# TP sur la coloration d'un graphe
 Le [théorème des quatre couleurs](https://fr.wikipedia.org/wiki/Th%C3%A9or%C3%A8me_des_quatre_couleurs) indique qu'il est possible, en n'utilisant que quatre couleurs différentes, de colorier n'importe quelle carte découpée en régions connexes, de sorte que deux régions adjacentes (ou limitrophes), c'est-à-dire ayant toutes une frontière (et non simplement un point) en commun reçoivent toujours deux couleurs distinctes. 

 L'énoncé peut varier et concerner, de manière tout à fait équivalente, la coloration des faces d'un polyèdre ou celle des sommets d'un graphe planaire, en remplaçant la carte par un graphe dont les sommets sont les régions et les arêtes sont les frontières entre régions.

 Même si l'énoncé de ce théorème est élémentaire, on n'en connaît pas de preuve simple. Les démonstrations connues décomposent le problème en un nombre de sous-cas tellement important qu'elles nécessitent l'assistance d'un ordinateur pour être vérifiées, il s'agit d'un probleme [NP-complet](https://fr.wikipedia.org/wiki/Probl%C3%A8me_NP-complet). (wikipedia)

Le TP utilisera la carte des régions de France:

{{< img src="../images/france-region.jpg" >}}

Ce TP est inspiré du sujet de bac Am Nord J1 2025: [sujet](https://www.education.gouv.fr/media/227287/download)

La correction se trouve ici: [correction](https://www.math93.com/images/pdf/annales_bac/Bac_NSI/bac_NSI_2025/BACNSI2025_AmeriqueNord_Sujet1_corr.pdf). (Ne pas consulter avant d'avoir cherché par vous même)

Les dessins du graphe seront réalisés avec la librairie networkx.

# Sources
* Page sur les graphes: [zonensi.fr](https://www.zonensi.fr/NSI/Terminale/C09/graphe_python/#__tabbed_6_1)
