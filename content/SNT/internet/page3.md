---
Title: circulation des données
description: protocoles, routage, modele client serveur, DNS, http et https, VPN
weight: 13
---

# Video SNT: les protocoles

{{< img src="/images/video.png" link="https://www.youtube.com/watch?v=s18KtOLpCg4" caption="Video SNT: Internet, TCP-IP un protocole universel ?" >}}

# Constitution du reseau internet
## Réseau local 
* Dans un réseau local, les ordinateurs sont interconnectés par un *switch* et peuvent communiquer entre eux par l'intermédiaire d'un *routeur*. C'est aussi le routeur qui fait passerelle vers *internet*.

{{< img src="../images/reseau-internet.png" alt="reseau internet" caption="reseau local et internet" >}}

## réseau internet
* Internet est un réseau de réseaux qui interconnecte toutes les machines à l'échelle mondiale.
En pratique, ce sont les routeurs des réseaux qui sont interconnectés. Lorsqu'un routeur reçoit une requête d'une des machines de son réseau, adressée à une machine qui n'appartient pas à son réseau, il se réfère à une table de routage d'internet pour expedier la requête. Il envoie alors la requête à un autre routeur. 


## Routeur et routage
Le **routeur**: c'est une machine qui a pour rôle de communiquer avec d'autres machines. 

Les routeurs s’occupent du routage sur internet, c’est à dire du meilleur choix de route selon les renseignements dans leur table de routage. Le but est de faire circuler les données, sans que celles-ci occupent trop longtemps le reseau, par les voies les plus rapides.

Chaque routeur est identifié par une adresse IP. Il possède une table de *routage* qui lui permet de choisir la bonne liaison entre les 2 machines qui veulent communiquer.

Cette table de routage identifie les ordinateurs de manière unique par leur *adresse IP* : Un code binaire à 32 bits (norme IPv4) ou 128 bits (norme IPv6).

> Dans l'exemple ci-dessous, les données qui circulent du *client* vers le *serveur* vont probablement emprunter des chemins différents : certains passeront par les reseaux d'accès E, A, B et D, alors que d'autres emprunteront les reseaux E, A, C et D. Les routeurs par lesquels passent ces données seront aussi différents dans un même réseau d'accès. Le calcul de l'itinéraire est réalisé de manière dynamique, par les routeurs eux-même, en fonction du trafic.

Le trajet possible entre les 2 machines n'est pas unique : 

{{< img src="../images/internet-fig1.png" alt="reseau internet" caption="des reseaux interconnectés" >}}

[source: interstices.info](https://interstices.info/internet-le-conglomerat-des-reseaux/)



Les données peuvent circuler en sous *plusieurs formes* et à travers **différents canaux**, ce qui modifie leur vitesse et leur *débit* :

* Fibre optique : 100 Mo/s
* Adsl : 5Mo/s
* 4G: 10 Mo/s
* Wifi : 10 Mo/s
* Bluetooth : 0,5 Mo/s


# Comment utiliser le reseau Internet?
Pour naviguer sur internet, votre machine va communiquer avec d'autres serveurs. Cette communication met en jeu plusieurs *protocoles*, dont les principaux sont **DNS, HTTP, IP et TCP**.

## Client – serveur
la description du reseau sous-entend un mode de fonctionnement client-serveur

* Client : demande une ressource
* Serveur : heberge et fournit la ressource

Il existe plusieurs niveaux de description des echanges entre client et serveur ce qui amène à utiliser un modèle en couches (TCP/IP).

Dans chaque couche de ce modèle, des algorithmes sont mis en œuvre et chaque couche s’occupe d’une partie de la transmission.

Par exemple, au niveau du client, le navigateur s’occupe de la resolution DNS puis de l’établissement du contact avec le serveur (HTTP)

Les autres couches vont s’occuper du routage et de sa fiabilisation.

**Algorithme** : une suite ordonnée et non ambigüe de commandes ou instructions. C'est une séquence d'ordres

## la resolution DNS
C'est l’une des étapes du protocole TCP/IP. Au cours de celle-ci, l’ordinateur client qui cherche à se connecter à un ordinateur serveur. Il va demander au serveur DNS de lui convertir l’adresse symbolique (URL) en une adresse IP, celle du serveur à joindre. Puis, une fois qu’il connaît l’adresse ip, il envoie une requête HTTP à l’ip correspondante afin que le serveur lui retourne la page.

Il y a une correspondance entre l’adresse symbolique et l’adresse IP. Lorsque l’on demande à notre machine de joindre celle d’adresse symbolique `musee-orsay.fr`, il y a un protocole qui se charge de renseigner l’adresse IP correspondante, afin que les machines puissent communiquer entre elles. C’est le protocole de résolution DNS.

Cette résolution DNS est réalisée :

1.	D’abord grâce au fichier host.txt de notre machine
2.	Puis, si l’adresse n’est pas dans le fichier, par le serveur DNS


## Le protocole HTTP
Ce **protocole HTTP** est initié par le *client*, le navigateur (Mozilla, Chrome, ...).
Une fois la connexion établie, vous allez pouvoir charger la page Web depuis l'ordinateur serveur.

## adresse IP et adresses symboliques
Les adresses IP identifient les machines par un numero (sur 32 bits pour l'IPV4, et 128 bits pour l'IPV6) et leur permet de communiquer entre elles. Le problème est que le format de cette adresse n'est pas très intelligible pour un humain. C'est pour cela que les sites et les programmes hébergés sur les serveurs possèdent aussi une adresse symbolique (nom d'hôte).

Par exemple, l'adresse IP 207.142.131.245 est celle de Wikilivres.com (son nom d'hôte correspondant).

Les tables de correspondance : nom d'hôte <=> adresse IP sont tenues par des serveurs appelés *DNS (domain name system)*. C'est à ce serveur DNS que votre routeur se réfère lorsque vous saisissez une adresse symbolique (une URL) dans la barre de navigation de votre navigateur.

Une fois la résolution DNS réalisée, les machines entrent en contact grâce à leurs adresses IP. Ce sont des étapes du **protocole IP**.

## Comment sont transmises les *informations numériques* ?
**Le protocole TCP** <br>
*Internet manipule deux types d’information : les contenus envoyés et les adresses du destinataire et de l’émetteur. Ces deux types d’information sont regroupés dans des paquets de taille fixe, de façon uniforme et indépendante du type de données transportées : texte, images, sons, vidéos, etc.*

Ces données sont rassemblées dans des trames de 1500 octets. La plupart du temps, les données à envoyer sont de taille supérieure à 1500 octets, et il faut plusieurs trames.

{{< img src="../images/segment.png" alt="trame" caption="decoupage de l'information numérique en plusieurs datagrammes" >}}
C'est le *protocole TCP* qui gère ce découpage, et rajoute des informations pour pouvoir renvoyer les paquets perdus en chemin (grâce à un accusé de reception), et remettre les paquets dans le bon ordre. Un code de vérification est également ajouté au paquet, pour vérifier s'il est conforme à l'original, et non *corrompu* en chemin.

# TP: comprendre le protocole TCP en jouant :
{{< img src="../images/packet-attack.png" alt="reseau internet" caption="reseau local et chemin entre routeurs : interstice.info" >}}> *Vous devez perturber le transport des paquets afin d'empêcher la reconstitution du message. Au fur et à mesure que vous passez les niveaux, l'ordinateur trouve de nouvelles stratégies pour y parvenir. Vous pouvez : retarder les paquets, les corrompre, ou les détruire.*

# Problème de libre accès au réseau internet et cybersécurité
## Utilité des noms de domaine
Une bonne pratique est de lire les noms de domaines dans la barre d’adresse afin de s’assurer que l’on navigue vers le BON site. Une des attaques les plus classiques sur le net est le Phishing

{{< img src="../images/phishing.png" >}}

On pourra consulter la video suivante:

{{< img src="../images/phishing_video.png" link="https://www.youtube.com/watch?v=iRf375BUIww" caption="phishing et noms de domaine - arsen.co" >}}

## Naviguer en https
https est la version securisée pour l’echange de données sur internet. Lorsque vous demandez à charger une page sur internet (on dit que vous demandez une ressource), les etapes sont les suivantes :

-	Resolution DNS
-	Contact avec le serveur grace à l’adresse IP et le nom de domaine du site internet
-	Echange des clés de chiffrement
-	*Le client demande la page web*
-	*Le serveur lui retourne la page*
-	*Le client envoie des données*
-	*Le serveur traite les données*
-	…

*En italique : les echanges chiffrés.*

**Risque (faible)**: si le flux de données est capturé: il est possible de connaitre le nom de domaine consulté, mais pas le contenu ni l'adresse de la page consultée sur le site.

<!--
## Attaque par dénis de service
DDoS : consiste à rendre un serveur incapable de répondre à des requêtes. En général, se fait en inondant de requêtes, le serveur n’est alors plus capable de répondre.
-->
## Censure sur internet
**Blocage DNS**

Le blocage DNS consiste à empêcher la résolution d’un nom de domaine en adresse ip. On peut vérifier depuis la France si certains sites sont inaccéssibles pour un pays qui pratique la censure d’internet. Sur le site [experte.com](https://www.experte.com/fr/censure-internet)

{{< img src="../images/censure.png" caption="page du site experte.com" >}}

Fonctionnement du site: envoi de l’URL sur l’un de ses serveurs hebergés dans les pays considérés. Test avec des pays pour lesquels l’internet est libre, afin de s’assurer que le domaine fonctionne bien.

{{< img src="../images/censure2.png" caption="page du site experte.com" >}}

{{< img src="../images/censure3.png" caption="exemple de blocages" >}}

Ce blocage est **facilement contournable** en utilisant un serveur DNS alternatif.

**Blocage par adresse IP**

Dans le cas d’un blocage ip, c’est directement l’adresse ip du site web qui est bloquée par le **FAI**, ou bien par un logiciel installé sur un noeud de routage (**Proxy**). 

Dans de nombreux pays, les FAI sont contraints par leur gouvernement d'effectuer régulièrement un filtrage et une censure d'Internet. Ce type de blocage n’est pas sans poser de problème puisque si plusieurs sites sont hébergés sur la même adresse ip, comme dans le cas d’un hébergement mutualisé, l’ensemble des sites se retrouvent inaccessibles.

Néanmoins, dans le cas d’un tel blocage, il existe des solutions, comme d’avoir recours à un tunnel chiffré, tel qu’un VPN.

## Utiliser un VPN
Le VPN assure un tunnel pour acheminer les données, chiffrées dès que la connexion est établie.
La procédure est la suivante:

-	Connection au serveur VPN
-	*Resolution DNS pour le site demandé*
-	*Contact avec le serveur..*
-	*Echange des clés*
-	 *;;;*

*En italique : les echanges chiffrés.*

La connexion au VPN ajoute une securité supplémentaire, avec un 2e chiffrement, et l’effacement du nom de domaine consulté.

