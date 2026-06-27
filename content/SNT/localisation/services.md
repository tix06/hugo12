---
Title: GPS services
---

# Services sur smartphone
Sur Iphone: Réglages > Confidentialité > Services de localisation.

On peut paramétrer les permissions pour chacune des app de son smartphone.

{{< img src="../images/localisation_iphone.jpg" >}}
Lorsque l'on choisit une app, celle-ci précise à quoi serviront les données de localisation (celles de la{{< a link="http://localhost:1313/docs/SNT_2nde/pages/page18/geolocaliser/#trame-nmea" caption="trame NMEA" >}}


* Booking, Expedia: "pour trouver des hébergements et hôtels près de chez vous"
* Facebook, Instagram: "pour aider à indiquer votre présence dans un lieu, pour être notifié des évènements locaux, pour personnaliser du contenu"
* météo: "quand des épisodes de pluie ou de neige commencent"
* ...

Par défaut, de nombreuses applications sont susceptibles de traquer vos données de géolocalisation, afin d'étbalir au mieux votre profil. Voir la video ci-dessous: [Un espion dans ma poche?](https://www.francetvinfo.fr/internet/telephonie/video-un-espion-dans-la-poche_4507625.html)

{{< img src="../images/video_espion.png" link="https://www.francetvinfo.fr/internet/telephonie/video-un-espion-dans-la-poche_4507625.html" caption="Envoyé special, Francetvinfo.fr" >}}

Voici un exemple de la promesse faite à l'utilisateur: l'incrustation des recommandations en réalité augmentée...

{{< img src="../images/realite_augmentee.jpg" caption="realité augmentée. fiction ou réalité?" >}}

# Les cartes numériques
Les services de cartographie numérique, comme *geoportail* ou *openstreetmap* mettent à disposition des images géoréférencées, avec plusieurs profondeur de zoom disponibles. A ces cartes sont ajoutés des repères avec des lieux d’intérêt.

*Comment gère t-on la profondeur de zoom?* Pour une même zone géographique, le service stocke des tuiles: ce sont les images assemblées, géoréférencées autour du point central, proposées à certaines échelles. Seules certaines échelles sont disponibles:

{{< img src="../images/pyramide.png" caption="*Les pyramides des caches d’images du Géoportail pour le WMTS comportent 21 niveaux de zoom.*" >}}

*images issue de [geoservices.ign.fr](https://geoservices.ign.fr/documentation/services/services-deprecies/images-tuilees-wmts-ogc)*


Une carte est donc constituée:
* d’un fond de carte constitué avec des tuiles: il s’agit d’images figurant un fragments de la carte, qui, rassemblées à la façon d’un puzzle, forment le fond de carte.
* des calques, qui ajoutent certaines informations pour enrichir la carte (altimétrie, cadastre,…). Ils ont une transparence.
* de POI: points of interest 
d’un repère de coordonnées, dont la norme est Dgrés décimaux (DD).

*Les calques* servent à regrouper des objets, par ordre d'empilement.

{{< img src="../images/zoom1.png" caption="détails sur geoservices.ign.fr" >}}

Dans ce dernier exemple, chaque tuile est une image **[matricielle](/docs/SNT_2nde/pages/page5/photo_num1/)**: elle peut être agrandie mais sans détails supplémentaires jusqu’au chargement d’une nouvelle tuile.
Alors que les quadrillages sont toujours aussi nets: ce sont des images **vectorielles** ajoutées.

*image issue de: [geoservices.ign.fr](https://geoservices.ign.fr/documentation/services/services-deprecies/images-tuilees-wmts-ogc)*

Voir l'activité compléte ici: [Lien vers pdf](/pdf/SNT/carte_num.pdf)

## Géoportail
Les cartes de{{< a link="https://www.geoportail.gouv.fr/carte" caption="Géoportail" >}}
Elles permettent de zoomer, et ainsi de modifier dynamiquement l'echelle, mais aussi de mesurer une surface, créer un itinéraire, ... {{< a link="https://www.sport-nature.net/astuces-geoportail/" caption="voir ici" >}}
## Openstreetmap


Les fichiers d’itinéraires sont un autre exemple de données standardisées afin de pouvoir être échangées entre applis de cartes numériques: c’est le format .GPX

## Carte et image numérique
[Activité sur la structure des cartes numériques](/pdf/SNT/carte_num.pdf)

## Travaux pratiques
* [TP1 Cartographie numerique, marqueurs et cadastre](../tp_OSM)
* [TP2 itinéraire et croisière](../tp_croisiere)


# Calcul d'initéraire
L’ensemble des itinéraires peut être représenté à l’aide d’un graphe pondéré. Les noeuds sont des intersections, souvent des villes, croisements, points d’interêt. Les arêtes sont les routes.
Le calcul d'itinéraire se fait à l'aide d'algorithmes prenant de nombreux paramétres en compte. L’itinéraire est alors une liste de coordonnées de noeuds dans ce graphe.

*Exemple naïf:* 

```python
fonction recherche_itineraire(depart, arrivee, graphe):
  ville_courante <- depart
  itineraire.ajouter(ville_courante)
  tant que ville_courante != arrivee:
    ville_courante <- ville_voisine_plus_proche(ville_courante, graphe)
    itineraire.ajouter(ville_courante)
  retourner itineraire
```

{{< img src="../images/graphe1.png" caption="graphe" >}}
> Questions:

> 1. Quel itineraire est retourné par l'appel de la fonction avec les paramètres suivants: `recherche_itineraire("Montpellier", "Lyon", graphe)` ?
{{< img src="../images/graphe2.png" caption="Montpellier => Lyon" >}}2. Quel autre itineraire est retourné par l'appel de la fonction avec les paramètres suivants: `recherche_itineraire("Lyon", "Montpellier", graphe)` ?
{{< img src="../images/graphe3.png" caption="Lyon => Montpellier " >}}3. Cet algorithme donne t-il à coup sûr le chemin le plus court? Pourquoi?

## L'algorithme de Dijkstra
On a vu que l'algorithme précédent n'est pas efficace pour trouver le *meilleur* itineraire. Celui-ci n'assure pas non plus de trouver *un* itinéraire, car il n'y a pas de retour en arrière possible.

L'algorithme le plus efficace pour la recherche de l'itinéraire le plus court est l'[algorithme de Dijkstra (voir ici pour une description plus formelle)](/docs/SNT_2nde/pages/pages_algo/graphes/page4/).

L'idée de cet algorithme est de procéder comme pour un parcours de graphe en largeur. On tient à jour une liste de sommets adjacents, qu'il faudra visiter dans l'ordre. Pour un noeud N visité dans la liste, on ajoute les sommets adjacents à N en fin de liste. Puis on progresse dans la liste.

Mais ici:

* Le graphe est pondéré (les arêtes ont un poids qui correspond à la distance)
* La liste contient pour chaque sommet visité: le noeud et sa distance cumulée au sommet de départ.
* la liste des sommets à visiter est remise à jour, triée par ordre croissant de distance cumulée.

Une présentation en vidéo de cet algorithme:

{{< img src="../images/dijkstra.png" caption="video - Lelivrescolaire.fr" >}}

# Documents et liens
* Livre Delagrave, activité 5 page 89
Cartographie numérique pour débutant:  [blog](https://ig.hypotheses.org/1363)
* HTTP request make your own map: [geoservices.ign.fr](https://geoservices.ign.fr/documentation/services/services-deprecies/images-tuilees-wmts-ogc)


# Suite du cours
[principe de la geolocalisation](../geolocaliser)



