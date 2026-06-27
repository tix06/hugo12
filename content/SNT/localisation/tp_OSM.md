---
Title: TP openstreetmap
---

Ce TP va permettre d'explorer la zone du lycée d'Estienne d'Orves, à Nice, grace aux applications de cartes numériques.

{{< img src="../images/LEO.png" caption="Lycée H. d'Estienne d'Orves, GoogleMap" >}}


# Utiliser Geoportail
Aller sur le site Geoportail.

## Plan cadastral
* Utiliser le fond de carte *IGN*. Localisez vous sur le lycée H. d'Estienne d'Orves à Nice.

* Ajouter maintenant un calque: aller sur le menu *CARTES* puis choisir *parcelles cadastrales*


{{< img src="../images/geoportail.png" caption="choix d'un fond de carte" >}}

> **Question a:** **retrouvez les numéros de parcelles** correspondant au lycée. 



## Surface
Le menu de droite permet diverses actions comme ajouter des marqueurs, mesure des distances, etc...

{{< img src="../images/geoportail2.png" caption="outils divers de Geoportail" >}}

A l'aide de l'outil mesures > mesurer une surface:

> **Question b:** mesurer la surface totale du lycée (toutes les parcelles cadastrales)

> **Question c:** mesurer la surface de la cour

{{< img src="../images/LEO_surf.png" caption="" >}}

## Distances
* à l'aide des outils de Geoportail, **ajouter des marqueurs** sur les lycée d'Estienne d'Orves et sur celui du Parc Impérial.

{{< img src="../images/geoportail3.png" caption="carte avec marqueurs" >}}

> **Question d:** **Mesurer alors la distance** *à vol d'oiseau* entre ces 2 marqueurs. (outil MESURES)

> **Question e:** **déterminer l'itinéraire** à pied entre ces 2 marqueurs (outil ITINERAIRE)



# Planifier un itinéraire
A l'aide des outils vus plus haut, choisir le mode *calcul d'itinéraire*.

Placer les étapes suivantes, dans un ordre quelconque:

* lycée d'Estienne d'Orves
* lycée du Parc Impérial
* Avenue François Mitterand
* 4 rue de Rivoli
* 6 Place Charles Pasqua
* 5 boulevard Victor Hugo
* 31 avenue Jean Médecin


* 16 place Garibaldi

{{< img src="../images/LEO_iti2.png" caption="itineraire avec plusieurs étapes" >}}

> **Question f:** Calculer alors l'itinéraire pieton qui relie tous ces points.

Ce n'est peut être pas le meilleur itinéraire. Faites alors une recherche simplifiée du parcours à vol d'oiseau, en traçant un nouvel itinéraire depuis *mesure de distance*, et en joignant les différents marqueurs dans ordre que vous aurez choisi.

{{< img src="../images/LEO_iti.png" caption="Un exemple d'itinéraire, pas forcement le plus court ;-)" >}}

> **Question g:** Quel est l'itinéraire le plus court? Quel est le plus long?

*Le calcul de l'itinéraire le plus court, tout en visitant tous les lieux marqués est un problème d'optimisation, qui peut être résolu avec un ordinateur, à condition que le nombre d'étapes ne soit pas trop important. Sinon, le temps de calcul peut être TRES long, même pour une machine actuelle.*

# Remonter le temps
Aller sur le site [remonterletemps.ign.fr](https://remonterletemps.ign.fr/telecharger?x=7.265133&y=43.696776&z=14&layer=GEOGRAPHICALGRIDSYSTEMS.PLANIGNV2&demat=DEMAT.PVA$GEOPORTAIL:DEMAT;PHOTOS&missionId=missions.6491585) et repérer le lycée sur le fond de carte.

{{< img src="../images/remonterletemps.png" link="https://remonterletemps.ign.fr/telecharger?x=7.265133&y=43.696776&z=14&layer=GEOGRAPHICALGRIDSYSTEMS.PLANIGNV2&demat=DEMAT.PVA$GEOPORTAIL:DEMAT;PHOTOS&missionId=missions.6491585" caption="photographies anciennes de Nice 1919 à 2023" >}}

Les petits points verts mènent vers l'image aerienne choisie. Les limites de l'image aerienne sont données par les frontières blanches déssinées sur le fond de carte. Pour ouvrir la photographie aerienne, il faut rechercher le point vert au centre de la figure (polygone).

> **Question h**: A partir de quelle année le lycée a-t-il été construit?


<!--
# Calcul d'isochrone


**Peut-on atteindre la gare SNCF en 5 min à pied?**

Sur le site [openrouteservice.org](https://maps.openrouteservice.org/directions?a=null,null,null,null&b=0&c=0&k1=fr&k2=km#/place/Lycée%20Honoré%20d'Estienne%20d'Orves,Nice,France/@7.248312,43.699588,6/data/55,130,32,102,9,96,46,4,32,246,5,112,29,128,76,12,226,1,113,64,78,8,41,128,52,33,175,128,134,56,12,96,5,150,184,28,101,249,37,62,57,106,0,54,101,69,128,44,1,56,1,208,5,96,8,192,1,128,95,62,197,57,32,14,101,128,7,16,128,236,0,216,213,72,11,236,64,23,156,56,1,108,176,107,150,64,39,155,44,32,1,187,48,34,17,162,22,57,46,216,6,35,140,146,38,32,116,128), ouvrir le bandeau de menu à gauche (flèche `>`). Renseigner le lien *à atteindre* (il s'agit en réalité du lieu de *départ*): Votre lycée.

{{< img src="../images/isochrone1.png" caption="atteindre..." >}}

Puis paramétrer le logiciel en *temps* pour obtenir les surfaces de la ville atteignables en 1 à 5 min, à pied.

{{< img src="../images/isochrone.png" caption="parametrage" >}}

Peut-on atteindre la gare **à pied, en vélo, en voiture**?

{{< img src="../images/isochrone2.png" caption="isochrones en voiture" >}}


# Présentation du projet Openstreetmap

{{< img src="../images/osm.png" link="https://www.youtube.com/watch?v=zJSGOpqa9ew" caption="video presentation OSM" >}}

video presentation OSM: https://www.youtube.com/watch?v=zJSGOpqa9ew


## Utiliser Openstreetmap, contribuer
* Sur le site [Openstreetmap](https://www.openstreetmap.org/edit#map=16/43.6991/7.2509), repérez votre lycée.

* Identifiez-vous avec le compte de la classe pour contribuer à la carte publique:

compte: (adresse academique)

mot de passe: classe_snt_LEO

* Avec l'**editeur**, dans la partie **MODIFIER**, renseigner certains points de la carte (lycée ou autres) que vous connaissez parfaitement. (rampe accès chaise roulante, parking 2 roues, entrées du lycée, de la cantine, ...). Vous pouvez aussi ajouter des informations manquantes à certains points déjà ajoutés à la carte publique.
-->
# Liens
* [guide pour la classe de snt](https://www.openstreetmap.fr/les-bonnes-pratiques-pour-contribuer-a-openstreetmap-en-snt/)
* [tutoriel version texte, sur educosm](https://educosm.openstreetmap.fr/?ModeEmploi)
* [tutoriel pour le mode uMap](https://docs.framasoft.org/fr/umap/2-premiere-carte.html)
