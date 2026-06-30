---
Title : TP table de routage
description: TP Filius simulation d'un reseau, table de routage
weight: 50
---

# Rappels de NSI 1ere: logiciel Filius
Ce TP a été vu en 1ere NSI à la [seance suivante](/NSI_1/reseaux/TP_reseau/).
On cherche à créer un système de 2 sous-réseaux locaux. Ces reseaux auront pour adresses: 198.168.0.0 et 192.168.2.0

*C'est à dire que toutes les machines du réseau 198.168.0.0 auront en commun les 3 octets 198.168.0 et toutes les machines du reseau 198.168.2.0 auront en commun les octets 198.168.2.* 

* Le sous-réseau 192.168.0.0 comportera un switch et 3 ordinateurs M1, M2 et M3. Ces machines auront pour adresses IP:
  * 192.168.0.1
  * 192.168.0.2
  * 192.168.0.3

* Le sous-réseau 192.168.2.0 comportera un switch et 3 ordinateurs M4, M5 et M6. Ces machines auront pour adresses IP:
  * 192.168.2.1
  * 192.168.2.2
  * 192.168.2.3

Votre système devrait ressembler à l'image suivante:


{{< img src="../images/reseauSansrouteur.png" alt="systeme de 2 sous-reseaux sans routeur" caption="systeme de 2 sous-reseaux sans routeur" >}}
* Tester alors la commande `ping` depuis la machine M1 vers celle M6 du 2e sous-reseau. 

* Installer les logiciels utiles sur les machine M1 et M6 pour faire communiquer les machines. Pour faire cela: Démarrer la simulation:

{{< img src="../images/logiciels.png" alt="démarrer" >}}

* Puis faire un *double clic* sur chacune des machines, et installer le logiciel *ligne de commandes*.

{{< img src="../images/instal.png" alt="console installation logiciel" caption="console d'installation de logiciels" >}}
  

* tester alors les commandes suivantes depuis la machine M1:

  * `ipconfig` : vérifier la correspondance de l'adresse IP de la machine M1
  * `ping 192.168.0.2` : pour établir et tester une connexion avec la machine M2 
  * `traceroute 192.168.0.2` : pour établir le trajet qui mène jusqu'à M2

  * Tester alors les commandes `ping` et `traceroute` vers une adresse de machine inexistante dans le réseau. Par exemple `192.168.0.4`

> **Qu.1a:** Quels messages indiquent que la communication M1->M2 est possible, alors que M1-> `192.168.0.4` ne l'est pas?

> **Qu.1b:** La machine M6 est-elle accessible depuis M1? Pourquoi?

*Vous constatez que l'accès à M6 n'est pas possible. En effet, votre système doit disposer d'un routeur, une machine capable de faire interface entre 2 reseaux...*


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

> **Qu.1c:** Pourquoi le routeur de votre système informatique possède t-il 2 adresses IP?

> **Qu.1d:** Démarrer le système et tester alors la commande `ping` de M1 vers M6, puis de M6 vers M1. Que constatez-vous? Pourquoi?



*En cas de difficultés: on pourra consulter la{{< a link="https://www.youtube.com/watch?v=xyK6ThdQeR0" caption="video Filius 2 de David Roche" >}}*


# Simulation d'un reseau avec Filius (version term NSI): Routage statique

**1.** Avec le logiciel Filius, construire les réseaux ci-dessous :


{{< img src="../images/filius_routage.png"   caption="système 2" >}}

**2.** Vous devrez renseigner les adresses IP des machines, ainsi que les masques de sous-reseau. 

* Tester avec un ping si un ordinateur du réseau R1 peut communiquer avec un autre ordinateur du réseau R1. Conclure.
* Tester avec un ping si un ordinateur du réseau R1 peut communiquer avec un autre ordinateur du réseau R2. Conclure.

*Remarque : Toutes les machines appartenant au même réseau devront posséder la même adresse réseau sinon elles ne pourront pas communiquer ensemble, même si elles sont bien physiquement reliées.*

**3.** *Ne pas utiliser le routage automatique*. Compléter les adresses IP des passerelles. Tester à nouveau avec un ping si un ordinateur du réseau R1 peut communiquer avec un autre ordinateur du réseau R2. Puis avec  avec un ordinateur du réseau R3. Conclure.

**4.** Mettre en place le réseau R4. (Adresse IP et passerelle). Tester avec un ping si un ordinateur du réseau R1 peut communiquer avec un ordinateur du réseau R3.

**5.** Comment modifier la table de routage du routeur A ?

**6.** Comment modifier est la table de routage du routeur G ?

# Aide pour renseigner la table de routage
On cherche à renseigner pour le routeur A la route à prendre pour acheminer un paquet vers le reseau 192.168.4.0
{{< img src="../images/filius_R1.png"   caption="exemple de systeme à 2 routeurs" >}}

Dans la table de routage du routeur A, il faudra ajouter une nouvelle entrée, et renseigner la passerelle pour rejoindre ce reseau éloigné:

{{< img src="../images/filius_R2.png"   caption="exemple de nouvelle entrée dans la table de routage du routeur A" >}}

Alors, à condition de renseigner également le routeur B, avec la passerelle vers le reseau 192.168.0.0, les ordinateurs des 2 reseaux devraient communiquer ensemble.

{{< img src="../images/filius_R3.png"   caption="exemple de nouvelle entrée dans la table de routage du routeur B" >}}

# Liens
* Le TP de 1ere NSI se trouve à l'adresse [suivante](/docs/SNT_2nde/pages/page3/TP_reseau/)
* Ce TP est inspiré de la fiche d'exercices [http://bfourlegnie.com/Tnsi_2020/cours/Chap4_routage/TaleNSI_routage.pdf](http://bfourlegnie.com/Tnsi_2020/cours/Chap4_routage/TaleNSI_routage.pdf)