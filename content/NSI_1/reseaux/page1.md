---
title: modele OSI
description: modele en couches, encapsulation, numeros et adresses
weight: 6
---

* cours sur le modèle OSI: [Lien](../page1)
* cours sur les protocoles du modele OSI: [Lien](../page2)
* cours sur le protocole HTTP: [Lien](../page7)
* exemple de scénario montrant les failles de securité: [Lien](../page8)
* TP simulation de reseau (../TP_reseau) avec Filius
* TP sur la lecture des en-tête pour les methode GET et POST (HTTP): [Lien](../TP_GET_POST)
* TP sur la conception de pages web avec serveur python et gestion de formulaire: [Lien](../../ihm_web/html_page6) avec module Flask, et [projet web](../../ihm_web/html_page7)
* TP utilisant le module python requests: [Lien](../TP_requests)

# Le modèle OSI
Introduction: 

* voir [page SNT](/docs/SNT_2nde/pages/page3/fonctionnement/)
* [Les protocoles internet](/docs/SNT_2nde/pages/page3/protocoles/)


{{< img src="../images/video_OSI.png" caption="VIDEO: modèles OSI et TCP IP" >}}
[chaine Cookie connecté](https://www.youtube.com/watch?v=26jazyc7VNk)

<!--
*source: comprendre les modèles OSI et TCP/IP - [chaine Cookie connecté](https://www.youtube.com/watch?v=26jazyc7VNk)*
*
-->

## Les données qui circulent sur internet
*Internet manipule deux types d’information : les contenus envoyés et les adresses du destinataire et de l’émetteur. Ces deux types d’information sont regroupés dans des paquets de taille fixe, de façon uniforme et indépendante du type de données transportées : texte, images, sons, vidéos, etc.*

## Principe du modèle OSI
On peut rentrer un peu plus dans le détail du modèle OSI et en particulier de la communication TCP/IP.
Le modèle OSI est une norme qui préconise comment les ordinateurs devraient communiquer entre eux avec 4 *couches* technologiques adjacentes, numérotées selon leur *distance* au support d'emission (la couche n°1). On peut rassembler les couches 5, 6 et 7 en une seule.

Les couches forment une hiérarchie qui va de l'application (HTTP, FTP etc...) jusqu'au support physique (cable coaxial, ondes etc...).

Ce modèle OSI (un modèle theorique) a été conçu pour cloisonner les différents processus, langages et technologies employés. 

> *Combien de couches?*:

Selon le degré de description, on parle plutôt du modèle TCP/IP en 4 couches.

{{< img src="../images/OSI3.png" caption="illustration du TCP/IP" >}}
*image issue de la chaine [youtube - Cookie connecté](https://www.youtube.com/watch?v=26jazyc7VNk)*

> *Quelles applications pour quelle couche?:*

Les 2 schémas ci-contre illustrent le découpage couche-application.

{{< img src="../images/OSI2.png" >}}
*tableau issu de la page [wikipedia - TLS, SSL](https://fr.wikipedia.org/wiki/Transport_Layer_Security)*

SSH et SSL sont deux technologies qui permettent de chiffrer et d’authentifier les données qui passent entre deux ordinateurs. Ce sont des applications de la couche 5. Ces données sont chiffrées avant leur mise en forme pour le transport. Pour approfondir: [différence entre SSH et SSL](https://kinsta.com/fr/base-de-connaissances/ssh-vs-ssl/).

> *Quelles sont les liens entre couches?*

Le modèle OSI ajoute deux règles plus générales entre les couches :

> * chaque couche est indépendante ;
> * chaque couche ne peut communiquer qu'avec une couche adjacente.

Lors de l'émission d'une requête par une application, celle-ci doit traverser toutes les couches, depuis la 7 (application), puis de la 4 vers la 1; durant le trajet les données subiront des modifications et chaque couche rajoutera ce qu'elle voudra (généralement des en-têtes) pour mieux exercer sa fonction, mais pas seulement (la couche 1, de transport concerne... le transport). 

Ce mécanisme s'appelle l'encapsulation : la trame de données numériques est constituée de plusieurs parties distinctes et mises dans un ordre particulier. *L'encapsulation, en informatique et spécifiquement pour les réseaux informatiques, est un procédé
consistant à inclure les données d'un protocole dans un autre protocole.*

Au final, ce qui va circuler sur le réseau est une trame de couche 1, qui contient le datagramme de couche 2 (qui lui-même contiendra le segment de couche 3)

{{< img src="../images/encapsulation.png" alt="encapsulation" caption="encapsulation" >}}
Lors de la réception c'est exactement l'inverse qui se produit (désencapsulation).

{{< img src="../images/desencapsulation.png" alt="desencapsulation" caption="desencapsulation" >}}
**Prenons un exemple simple,** vous demandez à votre navigateur de charger votre site préféré www.informatix.fr. Vous êtes reliés à un modem par un câble à paires torsadées. 




{{< img src="../images/OSI1.png" >}}







## *couche application*
Le navigateur demande au système d'envoyer une requête HTTP (couche 7). Dans cette couche, le logiciel lui même n'en fait pas partie. Cette couche concerne *l'interface* entre le logiciel est la couche de transport, et transporte l'information du **protocole application** utilisé (ici http par exemple, c'est à dire le protocole lié à l'affichage des pages html)

> Sortie : `[requête HTTP]`

## *couche de transport*
La requête arrive dans TCP qui ajoute son en-tête. Le protocole TCP va mettre en forme les données à envoyer et ajouter son en-tête. Ici, les numeros d'identification sont les **port source et le port destination**, qui identifient les **applications** qui entrent en jeu dans la communication. Parmi les informations, on trouve aussi le numéro de séquence initial, **ISN**, appelé aussi **SYN** (pour dire à la machine en face combien de données elle est censée avoir reçues) et celui d'acquitement **ACK** (le numéro du prochain octet des données attendues). Ces numéros vont permettre d'établir une communication avec accusés de reception (pour TCP, pas UDP) et de s'assurer, en principe, de l'identité de la machine avec qui les données sont échangées (avec le numéro de séquence, nécessaire pour l'accusé de reception). L'en-tête contient aussi un *checksum.* Pour résumer, on appelera cette en-tête le **PDU** (Protocol Data Unit).

> Sortie : `[en-tête PDU][requête HTTP]`

fragmentation TCP: [cours sur openclassroom](https://openclassrooms.com/fr/courses/2340511-maitrisez-vos-applications-et-reseaux-tcp-ip/5677997-fragmentez-vos-paquets)

## *couche réseau*
Le segment TCP arrive dans IP qui ajoute aussi son en-tête (qui contient entre autres votre **adresse IP**  (pour le **routage**) et celle du serveur demandé). La couche 3 indique à la couche 2 quel protocole a été utilisé (TCP, UDP...). Il y a aussi un numéro de connexions établies (IPID) sur le port en question et d'autres informations qui servent à l'eventuelle fragmentation du datagramme (les données ne peuvent pas exceder 1500 octets.  
Une autre valeur transportée est le **TTL** (time to live) qui evite que le paquet ne circule indefiniment sur les reseaux.

> Sortie : `[en-tête IP][en-tête PDU][requête HTTP]`


{{< img src="../images/dataIP.png" caption="modèle simplifié du datagramme" >}}
## *couche physique*
Le paquet IP arrive dans Ethernet qui ajoute un en-tête (qui contient entre autres votre **adresse MAC** - pour le **switch** -  et celle du modem) et un checksum (vérification d'erreurs CRC). La couche 2 peut alors former la trame et l'envoyer sur le réseau.

Il va ajouter l'adresse MAC de l'emetteur et du destinataire, qu'il aura résolu grâce aux tables de routage et la *table arp* (côté serveur). 

> Sortie : `[en-tête Ethernet][en-tête IP][en tête PDU][requête HTTP][checksum Ethernet]`

{{< img src="../images/entete.png" alt="en-tête" caption="en-tête Ethernet" >}}


Le document complet sur la structure d'une trame: [Lien](/pdf/NSI/reseau_trame.pdf). *document est issu du cours en ligne du lycee de Taaone, série technologique.*

Lors du transport, chaque machine va désencapsuler les informations de la partie Ethernet et les remplacer par de nouvelles informations pour assurer le transport jusqu'à la prochaine étape.

{{< img src="../images/OSI4.png" >}}

Seule la machine de destination va acceder au contenu.


# Liens
* Complements sur la fragmentation TCP: [cours sur openclassroom](https://openclassrooms.com/fr/courses/2340511-maitrisez-vos-applications-et-reseaux-tcp-ip/5677997-fragmentez-vos-paquets)
* Feuille d'exercices sur les reseaux:{{< a link="/pdf/NSI/R3_exercices.pdf" caption="Lien" >}}
* {{< a link="../circulation/" caption="Retour vers la page Reseaux" >}}
* {{< a link="/docs/SNT_2nde/pages/page3/protocoles/" caption="Compléments sur les protocoles TCP et IP" >}}
* {{< a link="../securite/index.html" caption="Sécurité des communications (1ere NSI)" >}}
* {{< a link="../TP_reseau/index.html" caption="TP simulation d'un reseau avec Filius" >}}
* [TP Filius et cours sur les protocoles, GLasius](https://glassus.github.io/premiere_nsi/T3_Architecture_materielle/3.4_Protocoles_de_communication/cours/)
* Protocole DNS, cours de NSI sur [infoforall.fr](https://www.infoforall.fr/act/snt/protocole-dns/)

