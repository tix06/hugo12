---
Title: reseaux
description: reseaux, adresses IP, masque de sous-reseau, blockchain
weight: 69
---

# Exercice 3 25-NSIJ2ME1 
{{% badge icon="star" %}}binaire{{% /badge %}} {{% badge icon="star" %}}masque{{% /badge %}} {{% badge icon="star" %}}logique{{% /badge %}} {{% badge icon="star" %}}ping{{% /badge %}}

## Partie C - Réseaux
Bob et Marc travaillent pour une petite compagnie d’assurances.

Leurs postes de travail font partie d’un même réseau local géré par l’administratrice système qui dispose du bloc d’adresses IPv4 192.168.110.0/24.

La notation /24 situé à la suite de l’adresse 192.168.110.0 signifie que le masque de sous-réseau du réseau de cette entreprise est 255.255.255.0 : 

les trois premiers octets d’une adresse IP sur ce réseau permettent donc d’identifier la partie réseau de l’adresse, alors que le dernier octet permet d’identifier la partie hôte et est propre à chaque machine sur le réseau. 

Ce sous-réseau permet donc d’attribuer 256 adresses 
IPv4 différentes.

L’administratrice choisit alors d’attribuer, en représentation décimale, l’identifiant 115 pour la partie hôte du poste de travail de Bob et l’identifiant 153 pour celui de Marc.

Depuis son poste de travail, Marc souhaite tester la communication avec celui de Bob.

Pour cela, il exécute la commande ping 192.168.100.115 et obtient l’affichage
suivant :

```
--- 192.168.100.115 ping statistics ---
4 packets transmitted, 0 received, 100% packet loss, time
3060ms
```

14. Expliquer l’affichage obtenu et corriger l’erreur de Marc.

Afin d’améliorer les performances et la sécurité du réseau de l’entreprise,
l’administratrice système décide de séparer le réseau local en plusieurs sous-réseaux et de les relier entre eux par des routeurs. Pour cela, elle modifie le masque de sous-réseau qui devient 11111111.11111111.11111111.11100000, donné ici en représentation binaire.

15. Donner la représentation décimale de ce masque de sous-réseau.

Pour obtenir l’adresse IPv4 du sous-réseau auquel appartient une machine, il suffit
d’appliquer l’opérateur binaire ET, bit à bit, entre le masque de sous-réseau et
l’adresse IPv4 de la machine.

Par exemple, prenons le dernier octet de l’adresse IPv4 de Bob dont la représentation binaire est 01110011 : en appliquant bit à bit l’opérateur binaire ET entre cet octet et l’octet correspondant dans le masque, on obtient le dernier octet de l’adresse du sous-
réseau, soit 01100000.

{{< img src="../images/page7_3.png" width=300 >}}

Le poste de travail de Bob est donc sur le sous-réseau d’adresse 192.168.110.96.

16. Indiquer le nombre total d’adresses IPv4 pouvant être attribuées sur le sous-
réseau d’adresse 192.168.110.96 sur lequel se trouve Bob.

L’administratrice système attribue maintenant l’adresse IPv4 192.168.110.134 au
poste de travail de Zoé, nouvelle employée de la compagnie d’assurances.

17. Donner la représentation binaire du nombre 134.

Depuis son poste de travail, Zoé exécute les deux commandes suivantes :

* commande n°1 : `ping 192.168.110.115` ;
* commande n°2 : `ping 192.168.110.153`.

18. Indiquer, en justifiant, laquelle de ces deux commandes a produit l’affichage :
4 packets transmitted, 4 received, 0% packet loss, time
3002ms


# Bac 2022 Metropole1: Exercice 3
Cet exercice porte sur les représentations binaires et les protocoles de routage.

{{% badge icon="star" %}}binaire{{% /badge %}} {{% badge icon="star" %}}routage{{% /badge %}} {{% badge icon="star" %}}routage{{% /badge %}}

## Question 1
Une adresse IPv4 est représentée sous la forme de 4 nombres séparés par des
points. Chacun de ces 4 nombres peut être représenté sur un octet.

A.  Donner en écriture décimale l’adresse IPv4 correspondant à l’écriture binaire :

11000000.10101000.10000000.10000011

B.  Tous les ordinateurs du réseau A ont une adresse IPv4 de la forme :
192.168.128._ _ _ , où seul le dernier octet (représenté par _ _ _ ) diffère.
Donner le nombre d’adresses différentes possibles du réseau A.

## Question 2
On rappelle que le protocole RIP cherche à minimiser le nombre de routeurs
traversés (qui correspond à la métrique). On donne les tables de routage d’un
réseau informatique composé de 5 routeurs (appelés A, B, C, D et E), chacun
associé directement à un réseau du même nom obtenues avec le protocole RIP : 

{{< img src="../images/page6_5.png" caption="1234 × 916" >}}
A.  Donner la liste des routeurs avec lesquels le routeur A est directement
relié.

B.  Représenter graphiquement et de manière sommaire les 5 routeurs
ainsi que les liaisons existantes entre ceux-ci.

## Question 3
Le protocole OSPF est un protocole de routage qui cherche à minimiser la
somme des métriques des liaisons entre routeurs.

Dans le protocole de routage OSPF le débit des liaisons entre routeurs agit
sur la métrique via la relation : $metrique = \tfrac{10^8}{debit}$  dans laquelle le débit est exprimé en bit par seconde (bps).

On rappelle qu’un kbps est égal à $10^3$  bps et qu’un Mbps est égal à $10^6$  bps.

A. Recopier sur votre copie et compléter le tableau suivant : 

| Débit | 100 kbps | 500 kbps | ? | 100 Mbps |
|--- | --- | --- | --- | --- |
| Métrique associé | 1000 | ? | 10 | 1 |

{{< img src="../images/page6_6.png" caption="1230 × 644" >}}
Les nombres présents sur les liaisons représentent les coûts des routes avec le
protocole OSPF.

B.  Indiquer le chemin emprunté par un message d’un ordinateur du réseau F à
destination d’un ordinateur du réseau I.
Justifier votre réponse.

C.  Recopier et compléter la table de routage du routeur F.

D.  Citer une unique panne qui suffirait à ce que toutes les données des échanges de tout autre réseau à destination du réseau F transitent par le routeur G.
Expliquer en détail votre réponse. 

## Question 4 (sup hors bac)
A. Donner les caractéristiques du graphe de réseaux schématisé plus haut.

On donne cette fois le tableau constitué à partir de l'algorithme de Dijkstra, appliqué à ce même graphe de reseaux:

* le colonnes représentent les sommets à atteindre
* les lignes sont les sommets de départ
* On renseigne dans les cases la distance cumulée depuis le noeud **F**, jusqu'au noeud de la colonne, en passant par le noeud adjacent de la ligne. Par exemple, **I** peut être atteint en venant du noeud **K** avec une longueur de 13.

|  | G | H | I | J | K | L |
| --- | --- |--- |--- |--- |--- |--- |
| F |   | 5 |   |   |   |   |
| G |   |   |   |   |   |   |
| H |   |   | | 6 |   |   |
| I |   |   |   |   |   |   |
| J | 8 |   |   |   | 8 | 11|
| K |   |   |  13 |   |   |   |
| L |   |   |   |   |   |   |

B. Représenter le graphe des chemins pour explorer depuis **F** les autres noeuds, en suivant le chemin *le plus court*. 

C. Ce graphe représente l'arbre couvrant du graphe. Donner les caractéristiques de cet arbre. 

D. Quel est le chemin le plus court pour aller de F à G? 

E. Même question, mais cette fois pour aller de H à K.

# bac 2024 metropole1 exercice 2
Cet exercice traite de protocoles de routage, de sécurité des communications et de
base de données relationnelle.

{{% badge icon="star" %}}routage{{% /badge %}}

Une agence de voyage propose des croisières en bateau. Chaque croisière a un nom
unique et passe par quatre escales correspondant à des villes qui ont elles aussi des noms différents.
Pour gérer les réservations de ses clients, l’agence utilise une base de données. 

**Partie A**

L’agence de voyage possède deux bureaux distincts.
Elle passe par un prestataire de service qui héberge sa base de données et utilise un système de gestion de base de données relationnelle.
Vous trouverez ci-après un schéma du réseau entre les deux bureaux de l’agence de
voyage et le prestataire.
On peut y voir les différents routeurs (nommés de A à I) ainsi que le coût des liaisons entre eux.

{{< img src="../images/page6_9.png" caption="Topologie du réseau" >}}

1. Donner deux services rendus par un système de gestion de bases de données
relationnelles.

Le protocole RIP (Routing Information Protocol) est un protocole de routage qui
minimise le nombre de routeurs par lesquels les paquets transitent.

Le protocole OSPF (Open Shortest Path First) est un protocole de routage qui
minimise le coût du transit des paquets. Ce coût s'evalue grâce à la loi:

$$cout = \tfrac{18^8}{Debit}$$

2. Donner la route suivie par une requête issue du bureau numéro 1 jusqu’au
prestataire si on utilise le protocole RIP.
3. Le debit d'une liaison, utilisé pour le calcul du coût, s'exprime en bits par seconde. Donner une définition de ce qu'est le *débit*
4. Calculer le coût pour une liaison de débit 100 Mb par s. *(fast ethernet)*
5. Donner les deux routes que pourrait suivre une requête issue du bureau numéro
2 jusqu’au prestataire si on utilise le protocole OSPF. Donner le coût de chaque
route.


# Bac 2024 Amerique du Nord J2 exercice 3
*Cet exercice porte sur la programmation objet, les structures de données, les réseaux
et l’architecture matérielle.*

{{% badge icon="star" %}}poo{{% /badge %}} {{% badge icon="star" %}}adresses ip{{% /badge %}} {{% badge icon="star" %}}blockchain{{% /badge %}}

On considère un réseau local constitué des trois machines de Alice, Bob et Charlie
dont les adresses IP sont les suivantes :

* la machine d’Alice a pour adresse 192.168.1.1 ;
* la machine de Bob a pour adresse 192.168.1.2.

On rappelle que l’adresse 192.168.1.255 est l’adresse de diffusion qui sert à communiquer avec toutes les machines du réseau local et le masque de ce réseau local est 255.255.255.0. Cette adresse de diffusion est réservée et ne peut être attribuée à une machine.

## Partie A
1. Donner une adresse IP possible pour la machine de Charlie afin qu’elle puisse communiquer avec celles d’Alice et Bob dans le réseau local. Justifier votre réponse en donnant toutes les conditions à respecter dans le choix de cette adresse IP.

Ce réseau est utilisé pour effectuer des transactions financières en monnaie numérique nsicoin entre les trois utilisateurs. Pour cela, on crée la classe Transaction ci-dessous :

```python
class Transaction:
  def __init__(self, expediteur, destinataire, montant):
    self.expediteur = expediteur
    self.destinataire = destinataire
    self.montant = montant
```

2. Toutes les dix minutes, les transactions réalisées pendant cet intervalle de temps sont regroupées par ordre d’apparition dans une liste Python. Dans un intervalle de dix minutes, Alice envoie dix nsicoin à Charlie puis Bob envoie cinq nsicoin à Alice. Écrire la liste Python correspondante à ces transactions.

Pour garder une trace de toutes les transactions effectuées, on utilise une liste chaînée de blocs (ou blockchain) dont le code Python est fourni ci-dessous. Toutes les dix minutes un nouveau bloc contenant les nouvelles transactions est créé et ajouté à la blockchain.

```python
class Bloc:
  def __init__(self, liste_transactions, bloc_precedent):
    self.liste_transactions = liste_transactions
    self.bloc_precedent = bloc_precedent # de type Bloc

class Blockchain:
  def __init__(self):
    self.tete = self.creer_bloc_0()

  def self.creer_bloc_0(self):
    """
    Crée le premier bloc qui distribue 100 nsicoin à tous les utilisateurs
    (un pseudo-utilisateur Genesis est utilisé comme
    expéditeur)
    """
    liste_transactions = [
      Transaction("Genesis", "Alice", 100),
      Transaction("Genesis", "Bob", 100),
      Transaction("Genesis", "Charlie", 100)
      ]
    return Bloc(liste_transactions, None) 
```

3. La figure 1 représente les trois premiers blocs d’une Blockchain. Expliquer pourquoi la valeur de l’attribut `bloc_precedent` du bloc0 est None.

{{< img src="../images/page7_1.png" caption="Blockchain" >}}

4. À l’aide des classes Bloc et Blockchain, écrire le code Python permettant de créer un objet `ma_blockchain` de type Blockchain représenté par la figure 1.
5. Donner le solde en nsicoin de Bob à l’issue du bloc2.

6. On souhaite doter la classe Blockchain d’une méthode `ajouter_bloc` qui prend en paramètre la liste des transactions des dix dernières minutes et l’ajoute dans un nouveau bloc. Écrire le code Python de cette méthode cidessous.

```python
def ajouter_bloc(self, liste_transactions):
  # A compléter
```

8. Lorsqu’un utilisateur ajoute un nouveau bloc à la Blockchain, il l’envoie aux autres membres. Ainsi chaque utilisateur dispose sur sa propre machine d’une copie identique de la Blockchain. Donner le nom et la valeur de l’adresse IP à utiliser pour effectuer cet envoi.
9. On souhaite doter la classe Bloc d’une nouvelle méthode `calculer_solde` permettant de renvoyer le solde à l’issue de ce bloc. Recopier et compléter sur votre copie le code Python de cette méthode :

```python
def calculer_solde(self, utilisateur):
  if self.precedent is None: # cas de base
    solde = 0
  else:
    solde = ... # appel récursif : calcul du solde au bloc précédent
    for transaction in bloc.liste_transactions
      if ... == utilisateur:
        solde = solde - ....
      elif ... :
        ...
    return solde
```

10. Écrire l’appel à la fonction calculer_solde permettant de calculer le solde
actuel de Alice

## Partie B
Dans cette partie, on va améliorer la sécurité de la blockchain. Pour cela on enrichit la
classe Bloc comme indiqué ci-dessous:

```python
class Bloc:
  def __init__(self, liste_transactions, bloc_precedent):
    self.liste_transactions = liste_transactions
    self.bloc_precedent = bloc_precedent
    # Définition de trois nouveaux attributs
    self.hash_bloc_precedent = self.donner_hash_precedent()
    self.nonce = 0 # Fixé arbitrairement et temporairement à 0 
    # avant le minage du bloc
    self.hash = self.calculer_hash()

    # Définition de trois nouvelles méthodes
    def donner_hash_precedent(self):
      if self.bloc_precedent is not None:
        return self.bloc_precedent.hash
      else :
        return "0"

    def calculer_hash(self):
      """calcule et renvoie le hash du bloc courant"""
      # Le code python n'est pas étudié dans cet exercice

    def minage_bloc(self):
      """modifie le nonce d'un bloc pour que son hash commence
      par '00'"""
      # A compléter
```

La fonction calculer_hash produit une chaîne de caractères appelée hash qui
possède les propriétés suivantes :

* Le hash d’un bloc dépend de toutes les données contenues dans le bloc et uniquement de ces données ;
* Le calcul du hash d’un bloc est rapide et facile à calculer par une machine ;
* La moindre modification dans le bloc produit un hash complètement différent ;
* Il est impossible de déduire le bloc à partir de son hash.
* Si deux blocs ont le même hash, c’est qu’ils sont parfaitement identiques.

11. L’attribut nonce est de type entier. Miner un bloc signifie trouver une valeur de
nonce de telle façon que l’attribut hash du bloc commence par les deux
caractères “00”. Compte tenu des propriétés précédentes, la seule façon de
trouver cette valeur est de procéder à une recherche exhaustive. Expliquer en
quoi consiste le fait de trouver une valeur par recherche exhaustive.

Dans la suite de l’exercice, on considère que tous les utilisateurs cherchent à miner le
nouveau bloc. Le premier qui réussit, l’ajoute à la blockchain et gagne une récompense
en nsicoin.

12. En justifiant votre réponse, donner la valeur de l’attribut hash_bloc_precedent
du bloc0.
13. Sachant que le hash est écrit sur 256 bits, donner le calcul permettant d’obtenir
le nombre de hash possibles.
14. Recopier et compléter sur votre copie le code python de la méthode
minage_bloc.

```python
def minage_bloc(self):
  """modifie le nonce d'un bloc pour que son hash commence par
  '00' en énumérant tous les entiers naturels en partant de 0."""
  self.nonce = 0
  self.hash = self.calculer_hash()
  while ... :
    self.nonce = ...
    self.hash = ...
```

