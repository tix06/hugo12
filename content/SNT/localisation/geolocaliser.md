---
Title : geolocaliser
---

# Géolocaliser
*Prérequis:* La lumière, transport d'une information par modulation [cours de PC 2nde](/docs/PC_2nde/physique/pages/page3/)

## Traquer un telephone portable
Dans la série *Person Of Interest*, le personnage principal, *Finch*, utilise une entité numérique, la *machine* pour effectuer une surveillance globale de la population, qu'il a lui même mise en place pour les États-Unis. La série soulève de nombreuses questions quant au respect de la vie privée.

{{< img src="../images/POIS2E3.png" caption="voir extrait du film S2E3 13'" >}}

*Questions:* 

* *Cet extrait, vous parait-il réaliste?*
* *Dans ce passage du film, quel dispositif détermine la position de Sophia? (le film evoque une antenne, mais c'est plus probablement le mobile de Sophia)*
* *Quel dispositif partage cette position?*

## Mesurer le temps pour determiner une distance
Les systèmes américains GPS et européens Galiléo permettent la *géolocalisation* par satellite d'un recepteur.

La *géolocalisation* est le calcul de la position sur Terre.


Le récepteur va recevoir en continu 2 types d'informations de la part de chacun des satellites:

* la position du satellite
* l'heure d'envoi du signal depuis le satellite t0

Le recepteur va utiliser ces informations pour réaliser un calcul de positionnement. D'abord en calculant sa distance au satellite: Il utilise les temps t0 d'emission du signal et t1, celui de reception:

{{< img src="../images/Ti-9-SNT-2.png" >}}

Le signal se deplaçant à la vitesse de la lumière, c = 300 000 km/s.

{{< img src="../images/Ti-9-SNT-1.png" >}}
Cette durée, t1 - t0 est calculée à partir des temps t1 et t0, mesurés par deux horloges différentes, et qu’il faudra synchroniser au mieux. 

> Exercice: Calculer la distance satellite-recepteur si le temps de transit t1-t0 est egal à 70ms. 

{{< img src="../images/Ti-9-SNT-4.png" >}}
L’horloge du récepteur nécessite d’être régulièrement synchronisée avec celle des satellites émetteurs. C’est grâce à un algorithme calculant sur  les écarts de positionnement, que l’horloge du récepteur se met à l’heure des émetteurs. Cela nécessite de capter les signaux ﻿d’au moins 4 satellites GPS.

## Principe de la trilatération
**1964 :** Le premier système de positionnement par satellites est développé par les États-Unis, à usage uniquement militaire 

**1995 :** ouverture mondiale au reseau GPS, le Global Positioning System

GNSS est l’appellation du groupement de systèmes de positionnements par satellites qui *envoie des données de localisation et d’horaire* depuis leur orbite. Le système GNSS comprend le célèbre système de positionnement GPS (Global Positioning System), le système de positionnement russe GLONASS, le système de positionnement chinois BeiDou mais aussi le nouveau système de positionnement européen Galileo.

En équipant chaque satellite d'un émetteur radio, il est possible de réceptionner les signaux provenant d'appareils reconnus et d'estimer les délais de synchronisation.

{{< img src="../images/ConstellationGPS.gif" caption="Orbites de la constellation de satellites du système GPS - wikipedia" >}}



image issue de la page [GNNS-wikipedia](https://fr.wikipedia.org/wiki/Syst%C3%A8me_de_positionnement_par_satellites)

Pour déterminer la position précise du recepteur sur Terre, il faut utiliser le resultat du calcul de la distance à 4 satellites, et déterminer le point d'intersection de 4 sphères (video explicative).

{{< img src="../images/videoGPS.png" caption="KEZAKO: Comment fonctionne un GPS?" >}}

Pour optimiser le système, les satellites de navigation circulent sur une orbite moyenne à une altitude d'environ 20000 kilomètres. Compte tenu de cette donnée et de la nécessité que le récepteur puisse en permanence avoir quatre satellites visibles au-dessus de l'horizon, un système de navigation (GPS, Galileo, Beidou, Glonass) doit comporter environ 25 satellites de navigation opérationnels pour fournir une position, quelle que soit la position de l'utilisateur à la surface de la Terre. [GNNS-wikipedia](https://fr.wikipedia.org/wiki/Syst%C3%A8me_de_positionnement_par_satellites)


Observer les orbites de différents systèmes de satellites sur l'animation suivante: [wikipedia](https://upload.wikimedia.org/wikipedia/commons/b/b4/Comparison_satellite_navigation_orbits.svg)

## Coordonnées terrestres
La géolocalisation est un procédé qui permet de repérer une personne, un objet, un lieu sur une carte (le plus souvent numérique) à l’aide de ses coordonnées géographiques qui sont : 

* Sa latitude (en degrés) 
* Sa longitude (en degrés) 
* Son altitude par rapport au niveau moyen de la mer (en mètres) 

{{< img src="../images/france.png" >}}
{{< img src="../images/latlongitude.png" >}}
Le format numérique de la longitude est différent de celui de la latitude avec un chiffre significatif supplémentaire. Ceci s’explique par la valeur de l’angle qui ne dépasse pas 90° pour une latitude et qui peut atteindre 180° pour une longitude. 

Les coordonnées géographiques sont traditionnellement exprimées dans le système sexagésimal, parfois noté DMS : degrés minutes secondes. 
De nos jours, les notations équivalentes en degrés minutes décimales (DM) ou degrés décimaux (DD) sont également utilisées : 

* DMS : Degré : Minute : Seconde (49°30’00”) ;
* DM : Degré : Minute (49°30,0’) ;
* DD : Degré décimal (49,5000°), généralement avec quatre décimales 

| norme | exemple |
|--- |--- |
| Degrés DD | 48.225833 |
| Degrés, minutes DM | 48°13,54998' |
| Degrés, minutes, secondes | 48°13'32.9988'' |



{{< img src="/images/video.png" link="https://www.youtube.com/watch?v=Mo0IMbcg8DM" caption="Video sur les conversions DD<->DMS" >}}

# Trame NMEA
Protocole NMEA 0183 : (National Marine Electronics Association): protocole utilisé par les récepteurs GPS pour fournir la localisation sous une forme de trame normalisée facilement décodable. Ces données sont mises dans un format standard :

{{< img src="../images/nmea.png" >}}
Sur cette trame:

* Quel est le caractère de début de la trame?
* Quel est le séparateur entre les données?
* Que signifient les lettres N, E, M?
* Comment convertit-on 4836.5375 en 48°36’32.25’’? *Aide: il s’agit d’une conversion DD vers DMS.* 


# Positionner
Voici une trame affichée sur votre smartphone (utilisation de l’appli nmeaGPS):

$GPGGA,093642.126,4342.1254,N,00103.2814,O,1,04,3.2,200.2,M,,,,0000*0E$

* Déterminer l'heure de réception de la trame. On précisera les heures, les minutes et les secondes.
* Déterminer les coordonnées géographiques envoyées par la trame NMEA (DM)
* Convertir ces données en format DD.
* Positionner le point sur la carte

{{< img src="../images/carte.png" >}}
# Liens
* activité de SNT sur la synchronisation des horloges: [vittasciences.fr](https://fr.vittascience.com/learn/tutorial.php?id=253/9.-synchroniser-des-horloges)

# Suite du cours
[services de geolocalisation](../services)