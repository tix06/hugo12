---
Title: reseaux
description: reseaux, adresses IP, blockchain
weight: 69
---


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

