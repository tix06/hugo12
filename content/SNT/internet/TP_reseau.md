---
Title : TP simulation d'un réseau
description: TP Filius, reseau a 2 machines et plus, adresses IP
weight: 16
---

# TP simulation reseau

Un reseau, c'est quoi? C'est un système constitué de machines reliées ensembles (machines de tout genre: ordinateur, imprimante,...). Elles ont une adresse IP. 

L'adresse IP (**Internet Protocol**) identifie un périphérique à l'intérieur d'un réseau. A l'intérieur de ce réseau elle est unique.

Les outils utilisés en simulation ne fonctionnent pas tous en mode réel, à partir de votre propre ordinateur du lycée, à cause de restrictions nécessaires pour des problèmes de sécurité.

# TP Filius 1 : faire communiquer 2 ordinateurs *(durée indicative: 10 min)*
Lancer le logiciel **Filius**.

On réalise un premier réseau simple de 2 ordinateurs reliés par une seule ligne.

On s'aidera de la video de présentation{{< a link="https://www.youtube.com/watch?v=nzuRSOwdF5I" caption="Filius 1 (David Roche)" >}}
* Disposer les 2 ordinateurs comme présenté sur la video. 

* Modifier les adresses IP de ces ordinateurs pour avoir, dans l'ordre:
  * 192.168.0.1
  * 192.168.0.2
  
  *Remarque: Souvent, dans un même reseau, les 3 premiers octets de l'adresse IP des machines sont identiques. (ici: 192.168.0). Seul le dernier octet change. Pour l'une des machines, ce sera .1, pour la suivante .2, etc...)* 

* Relier ces ordinateurs

* Installer les logiciels utiles pour faire communiquer ces machines. Pour faire cela: Démarrer la simulation:

{{< img src="../images/logiciels.png" alt="démarrer" >}}

* Puis faire un *double clic* sur chacune des machines, et installer le logiciel *ligne de commandes*.

{{< img src="../images/instal.png" alt="console installation logiciel" caption="console d'installation de logiciels" >}}
  

* tester alors les commandes suivantes depuis la machine M1:

  * `ipconfig` : vérifier la correspondance de l'adresse IP de la machine M1
  * `ping 192.168.0.2` : pour établir et tester une connexion avec la machine M2 
  * `traceroute 192.168.0.2` : pour établir le trajet qui mène jusqu'à M2

  * Tester alors les commandes `ping` et `traceroute` vers une adresse de machine inexistante dans le réseau. Par exemple `192.168.0.3`

> **Qu.1a**: comment voit-on si le chemin vers une machine du reseau existe? Quelle information lit-on dans la console?



* modifier le réseau et mettre 3 ordinateurs reliés à un *switch*  (un connecteur) :  *voir la vidéo pour explications*
  * revenir en mode *conception du reseau* (bouton avec le marteau)
  * commencer par supprimer le cable (clic Droit sur le composant => Supprimer)
  * ajouter l'ordinateur M3. Modifier son IP en 192.168.0.3. Relier ces machines à l'aide d'un switch.
  * tester alors la commande de `traceroute` entre M1 et M3

> **Qu.1b**: Pourquoi a-t-on besoin d'un *switch* dans un réseau à 3 ordinateurs?

# TP Filius 2 : créer un reseau de type lycée *(durée indicative: 20 min)*

On cherche maintenant à créer un système de 2 sous-réseaux locaux. Ces reseaux auront pour adresses: 198.168.0.0 et 192.168.2.0

*C'est à dire que toutes les machines du réseau 198.168.0.0 auront en commun les 3 octets 198.168.0 et toutes les machines du reseau 198.168.2.0 auront en commun les octets 198.168.2.* 

* Le sous-réseau 192.168.2.0 comportera un switch et 3 ordinateurs M4, M5 et M6. Ces machines auront pour adresses IP:
  * 192.168.2.1
  * 192.168.2.2
  * 192.168.2.3

Votre système devrait ressembler à l'image suivante:


{{< img src="../images/reseauSansrouteur.png" alt="systeme de 2 sous-reseaux sans routeur" caption="systeme de 2 sous-reseaux sans routeur" >}}
* Tester alors la commande `ping` depuis la machine M1 vers celle M6 du 2e sous-reseau. 

> **Qu.2a:**: La machine M6 est-elle accessible depuis M1? Pourquoi?
<!--
Vous constatez que l'accès à M6 n'est pas possible. En effet, votre système doit disposer d'un routeur, une machine capable de faire interface entre 2 reseaux...
-->

* Modifier le système en ajoutant **un routeur**:

  * clic droit sur le Switch2 : faire *supprimer tous les cables*
  * ajouter le routeur
  * paramétrer le routeur: 



  >  clic sur le routeur
  >
  >
  >
  > renseigner les adresses des 2 reseaux sur l'interface du routeur: 
  * 192.168.0.254 du côté du reseau 192.168.0.0 (à gauche)
  * 192.168.2.254 du côté du reseau 192.168.2.0 (à droite)


{{< img src="../images/interface.png" alt="adresses des reseaux" caption="adresses des reseaux" >}}

  > cocher routage automatique:


{{< img src="../images/routage.png" alt="option routage automatique" caption="option routage automatique" >}}

  * Pour chacun des ordinateurs du sous-reseau 1, M1, M2, M3, renseigner l'adresse de l'interface reseau 1 du routeur: mettre **192.168.0.254** dans le champs *passerelle*. Ce sera l'adresse IP de la carte reseau du routeur, du côté du reseau 192.168.0.0 (on met **254** à la place de **0** pour l'adresse routeur).

 

{{< img src="../images/passerelle.png" alt="renseigner l" caption="renseigner l'adresse reseau pour chaque ordinateur" >}}
  * Même travail pour M4, M5, M6: renseigner la passerelle **192.168.2.254**
  * refaire le cablage

> **Qu.2b:** Pourquoi le routeur de votre système informatique possède t-il 2 adresses IP?

> **Qu.2c:** Démarrer le système et tester alors la commande `ping` de M1 vers M6, puis de M6 vers M1. Que constatez-vous? Pourquoi?



*En cas de difficultés: on pourra consulter la{{< a link="https://www.youtube.com/watch?v=xyK6ThdQeR0" caption="video Filius 2 de David Roche" >}}*

# TP Filius 3 : système avec routage *(durée indicative: 20 min)*
On utilisera pour la suite un système informatique constitué de nombreux sous-reseaux:

* télécharger le fichier [filius_sim_reseau.fls](../images/filius_sim_reseau.fls)
* cliquer sur le fichier pour ouvrir avec *Filius*

{{< img src="../images/gros_reseau.png" >}}

## Premier contact avec le système
> **Qu.3a.** Représenter sur votre feuille le reseau en ne dessinant que les ordinateurs n°1 et n°15, ainsi que tous les routeurs traversé (plus court schemin entre M1 et M15). 


{{< img src="../images/reseau_simple.png" >}}

> **Qu.3b.** Indiquer sur le schéma, pour chaque routeur, l'adresse passerelle que le message de M1 vers M15 va emprunter.

Lancer la simulation 

1. Prendre connaissance de l'adresse IP de l'ordinateur n°15
2. Depuis l'ordinateur n°1: Lancer le logiciel *Ligne de commande*
3. Faire: `traceroute` suivi de l'adresse IP de la machine 15
4. Repérer alors quels sont les adresses passerelles empruntées par les données entre ces 2 ordinateurs. 

> **Qu.3c.** Quel est le nombre de sauts entre M1 et M15? Est-ce que le nombre de sauts effectués vous semble cohérent?

> **Qu.3d.** S'agit-il des mêmes adresses passerelles lorsque la machine M15 envoie un message à M1? Vérifiez le par une expérience.

## Table de routage
Revenir en *mode edition* (marteau) : cliquer sur le routeur A
Dans l’onglet *général* : *décocher* l’option : *routage automatique*

Aller dans l’onglet *table de routage (forwarding table)*:

{{< img src="../images/filius_routage_2.png" caption="table de routage du routeur A" >}}

> **Q3e** : cartes reseaux du routeur:
> * Hormis l’interface 127.0.0.1 : Combien d’interfaces différentes possède le routeur? (colonne NIC, next interface connection)
> * Quels sont les 3 réseaux auquel ce routeur est *directement* relié ? Donner leur adresse IP.

<!--
On souhaite ajouter l’information suivante: Depuis la machine M1, du reseau 192.168.1.1, on souhaite atteindre une machine du reseau 172.12.0.0. L'interface du routeur est 192.168.1.254 dans le reseau 192.168.1.0. 



> **Q3d** : nouvelle entrée dans la table:
> * Quelle sera l'adresse passerelle depuis la machine M1?
> * Quelle sera l'adresse de l'interface (table routage du routeur)?

*Remarque: il existe une différence entre l’adresse de passerelle et l’adresse de l’interface, qui sera expliquée avec le [cours de terminale](../TP_reseau_term/)* 

-->



# Compléments théoriques sur les adresses des machines

On pourra consulter la video sur les [adresses IP et masques de sous-reseau]( https://www.youtube.com/watch?v=RnpSaDSSjR4)


## Adresse IP
### IPv4
L'adresse IP(**Internet Protocol**) identifie un périphérique à l'intérieur d'un réseau. A l'intérieur de ce réseau elle est unique.

Une adresse (IPv4) est constituée de 4 nombres binaire de 8 bits chacuns (32 bits), comme par exemple:


$1100 0000.1010 1000. 0000 0000. 0000 0001$


Pour rendre la lecture plus facile, les séries de 8 bits seront traduites en leur valeur décimale correspondante, comprise entre 0 et 255 (voir le cours *codage des nombres*).


L'**adresse binaire** vue plus haut sera alors traduite en :


$192.168.0.1$

L'adresse possède 2 parties:


* une partie identifie la machine

* une autre partie identifie le reseau


### Masque de sous-reseau
**Masque de sous-reseau**: c'est une serie de valeurs avec des 255 ou 0, ou autre sur le(s) dernier(s) octet(s).

La valeur correspondante binaire début donc par une série de 1, marquant les positions relatives à l'adresse reseau dans l'adresse IP.

Par exemple: L'adresse machine suivante est constituée d'une première partie *reseau*, les 24 premiers bits, puis de l'adressage machine dans le reseau (8 derniers bits):

$1100 0000.1010 1000. 0000 0000. 0000 0001 / 24$

Le masque de sous-reseau est alors:

$1111 1111.1111 1111. 1111 1111. 0000 0000$

Que l'on peut aussi écrire:

$255.255.255.0$

### Machines appartenant à un même reseau
**Definition: Deux machines sont sur le même réseau si et seulement si, la partie réseau de leur adresse IP est identique.**

Les derniers caractères `/24` correspondent au **masque de sous-reseau**. Ils signifient que le reseau contenant la machine a une adresse codée sur les 24 premiers bits (192.168.0). Et que les 8 derniers bits constituent l'adresse de la machine dans ce reseau (il s'agit donc du **.1** final). 

### IPv6
Pour la norme IPv6, ce nombre est sur 128 bits, soit 16 octets.

*Exemple d'adresse IPv6 exprimée en hexadécimal (32 caractères):* `2001:0db8:3c4d:0015:0000:0000:1a2f:1a2b` 


## classes d'adresse IP

* classe A : adresses IP comprises entre 0.0.0.0 et 127.255.255.255 masque 255.0.0.0 : on ne peut avoir qu'une toute petite partie sous-reseau mais beaucoup d'adresses machines. Un petit reseau de beaucoup de machines.

* classe B : 128.0.0.0 à 191.255.255.255 masque sous-reseau de 2 octets : on met autant de machines que de sous reseaux.

* classe C : masque sous-reseau de 3 octets: beaucoup de sous-reseaux et peu de machines.

Sur un reseau, deux adresses sont deja reservés: l'adresse de broadcast (bit adresse mis à 255), ainsi que l'adresse de reseau (bit d'adresse mis à zero). La plage adressable se situe entre ces 2 valeurs.

## Adresse mac

Une adresse MAC (Media Access Control), parfois nommée adresse physique,
est un identifiant physique stocké dans une carte réseau ou une 
interface réseau similaire. Elle est unique au monde

Une adresse MAC est codée en hexadécimal, sur 6 octets (cf cours sur l'hexadécimal)

00-1E-33-1D-6A-79 est une adresse MAC


=> Ouvrir l'invite de commande windows et entrer la commande `ipconfig /all`. identifier l'adresse MAC de votre ordinateur.

# Suite
* Lien vers le [TP2: routage avec Filius](../TP_reseau_term)
* La suite du cours de Term NSI: [table de routage, protocole de routage](/docs/NSI/architecture/page3/)

# Liens

* Vidéo de prise en main du logiciel{{< a link="https://www.youtube.com/watch?v=nzuRSOwdF5I" caption="Filius 1 (David Roche)" >}}
* video [Ping et traceroute utility](https://www.youtube.com/watch?v=vJV-GBZ6PeM)
* detailler une trame: [openclassroom](https://openclassrooms.com/fr/courses/2340511-maitrisez-vos-applications-et-reseaux-tcp-ip/2927999-detaillez-len-tete-ip)
* detail trame [pixies informatique au lycée](https://pixees.fr/informatiquelycee/n_site/isn_modele_tcpip.html)
* Traceroute expliqué et autres commandes batch: [it-connect.fr](https://www.it-connect.fr/quest-ce-que-le-traceroute/)
* Créé ton propre fichier batch: [ionos.fr](https://www.ionos.fr/digitalguide/serveur/outils/creer-un-fichier-batch/#:~:text=Un%20fichier%20batch%20(fichier%20Bat,d'environnement%20d'ex%C3%A9cution.)







