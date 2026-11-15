---
title: Programmation orientée objet
description: cours POO, classe, instance, attributs, méthodes, __repr__, objets qui interagissent, encapsulation
weight: 16
---

Cette séquence comprend :

* ce cours sur la POO ;
* une fiche d'exercices : [pdf](/pdf/NSI/POO_exercices.pdf) ;
* un TP de transition *Fruits et paniers* : [Lien](../page35/) ;
* le mini-projet Jeu des 7 familles : [Lien](../page34/) *(sans interface graphique)* ;
* un TP sur les trajectoires de projectiles : [Lien](../page31/) ;
* un TP sur la programmation d'un jeu de dominos : [Lien](../page33/) *(sans interface graphique)* ;
* une fiche *Les bonnes pratiques* en POO : [Lien](../fiche_POO).

# Programmation objet

## Principe
Jusqu'ici, nos programmes manipulaient des données (nombres, chaînes, listes, dictionnaires) d'un côté, et des fonctions qui agissent sur ces données de l'autre.

En **programmation orientée objet** (POO), on regroupe dans une même structure, appelée **objet**, des données et les fonctions qui agissent sur ces données. L'idée est de se rapprocher de la façon dont on décrit les *objets physiques*.

Prenons l'exemple d'une planche de skateboard : elle possède des caractéristiques qui lui sont propres.

{{< img src="../images/skates.png" caption="quelques exemples montrant la diversité des planches de skates" >}}

Malgré leur diversité, toutes les planches sont constituées :

* d'un deck (court, long) ;
* d'un tail (plat, relevé) ;
* de trucks (hauts, bas) ;
* de roues (à gomme tendre, dure) ;
* d'une décoration (l'image sous le deck).

L'ensemble de ces caractéristiques, à un instant donné, constitue l'**état** de la planche. Cet état peut évoluer : on peut changer les roues, repeindre la déco, la planche s'use…

Une planche peut aussi **répondre à des demandes** (on dit aussi des *messages*). Par exemple, on peut lui demander : *« es-tu adaptée au skatepark ? »*. Elle répond `True` pour une planche de type *street* (deck court, tail relevé, roues dures), et `False` pour une planche de type *cruiser*.

L'ensemble des demandes auxquelles un objet sait répondre s'appelle son **interface** : c'est par elle que l'on interagit avec l'objet, et que les objets interagissent entre eux.

Un objet comprend donc :

* des **attributs** : les données qui décrivent son **état** ;
* des **méthodes** : les fonctions qui décrivent son **comportement**, c'est-à-dire la façon dont il répond aux messages.

## Classe et instance

Toutes les planches ont la même structure, seules les valeurs changent. On décrit cette structure commune une seule fois, dans une **classe**.

* La **classe** `Skateboard` est le *plan de fabrication* (le moule) : elle indique quels attributs possède une planche, et quelles méthodes elle sait exécuter.
* Chaque planche fabriquée à partir de ce plan est un **objet**, appelé **instance** de la classe. Créer un objet s'appelle **instancier** la classe.

On peut fabriquer autant d'instances que l'on veut avec une même classe : chacune possède ses propres valeurs d'attributs.

## Définir une classe en Python

### Le mot-clé `class`
La définition d'une classe commence par le mot-clé `class`, suivi du nom de la classe (par convention avec une majuscule), de deux points et d'un bloc indenté :

```python
class Skateboard:
    ...
```

Tout le bloc indenté contient les **méthodes** de la classe.

### Le constructeur `__init__` et le paramètre `self`
La méthode `__init__`, appelée **constructeur**, est exécutée automatiquement à la création de chaque objet. Son rôle est de **créer les attributs** de l'objet et de leur donner une valeur initiale.

Toute méthode reçoit comme premier paramètre **`self`**, qui désigne l'objet sur lequel elle agit. Les attributs s'écrivent `self.nom_attribut` : `self.deck` signifie « le deck de *cette* planche ».

```python
class Skateboard:
    def __init__(self, deck='court', tail='relevé', truck='bas', roues='dures', deco=None):
        self.deck = deck
        self.tail = tail
        self.truck = truck
        self.roues = roues
        self.deco = deco
        self.km = 0       # attribut qui ne vient pas d'un paramètre
```

*Remarques :*

* Les paramètres ont ici des **valeurs par défaut** : `Skateboard()` crée une planche street classique, sans décoration (`None`).
* Un attribut ne vient pas forcément d'un paramètre. Ici, toute planche neuve a parcouru `0` km.
* Ne pas confondre le **paramètre** `deck` (une variable locale à `__init__`, qui disparaît ensuite) et l'**attribut** `self.deck` (qui reste attaché à l'objet).

### Les méthodes
Une méthode se définit comme une fonction, **à l'intérieur** de la classe, avec `self` comme premier paramètre. Une méthode peut :

* **retourner** une information sur l'objet, sans le modifier ;
* **modifier** l'état de l'objet, c'est-à-dire ses attributs.

*Script complet :*

```python
class Skateboard:
    def __init__(self, deck='court', tail='relevé', truck='bas', roues='dures', deco=None):
        self.deck = deck
        self.tail = tail
        self.truck = truck
        self.roues = roues
        self.deco = deco
        self.km = 0

    def skateboard_pour_parc(self):
        """retourne True si la planche est adaptée au skatepark"""
        if self.deck == 'court' and self.tail == 'relevé' and self.roues == 'dures':
            return True
        else:
            return False

    def rouler(self, distance):
        """ajoute distance (en km) au compteur de la planche"""
        self.km = self.km + distance
```

`skateboard_pour_parc` retourne une information, et `rouler` modifie l'état de la planche.

## Créer et utiliser des objets

### Instancier
On crée un objet en appelant la classe comme une fonction, **sans** donner l'argument `self` :

```python
>>> mon_premier_skate = Skateboard()
```

{{< img src="../images/sk8_classic.jpg" width="400" alt="skateboard classic" caption="un premier skateboard bien classique" >}}

Python crée un nouvel objet, puis exécute automatiquement `__init__` en donnant cet objet comme valeur à `self`. Les autres arguments sont passés aux paramètres suivants, dans l'ordre :

```python
>>> mon_sector_9 = Skateboard('long', 'plat', 'haut', 'molles', 'Marley')
```

{{< img src="../images/sk8_sector9.jpg" width="400" alt="skateboard cruiser" caption="un skateboard cruiser" >}}

### Appeler une méthode : la notation pointée
On envoie un message à un objet avec la **notation pointée** `objet.methode(arguments)` :

```python
>>> mon_premier_skate.skateboard_pour_parc()
True
>>> mon_sector_9.skateboard_pour_parc()
False
```

Python traduit `mon_sector_9.skateboard_pour_parc()` par `Skateboard.skateboard_pour_parc(mon_sector_9)` : l'objet placé **avant le point** devient `self`. C'est pour cela qu'on n'écrit jamais `self` lors de l'appel.

### Accéder aux attributs
La notation pointée permet aussi de lire un attribut :

```python
>>> mon_sector_9.deco
'Marley'
>>> mon_premier_skate.rouler(3)
>>> mon_premier_skate.rouler(2)
>>> mon_premier_skate.km
5
>>> mon_sector_9.km
0
```

Chaque instance a **ses propres attributs** : faire rouler `mon_premier_skate` ne change pas le compteur de `mon_sector_9`.

### Erreurs classiques

| Erreur | Ce qui se passe |
|--- |--- |
| oublier `self` dans la définition : `def rouler(distance):` | `TypeError` à l'appel : Python transmet l'objet en plus de l'argument |
| écrire `deck = deck` au lieu de `self.deck = deck` dans `__init__` | l'attribut n'est pas créé : `AttributeError` plus tard |
| oublier les parenthèses : `mon_sector_9.skateboard_pour_parc` | on obtient la méthode elle-même, sans l'exécuter |
| utiliser `print` au lieu de `return` dans une méthode qui doit renvoyer une valeur | la méthode renvoie `None` |

## La méthode `__repr__`
Essayons d'afficher une instance :

```python
>>> print(mon_sector_9)
<__main__.Skateboard object at 0x7fc6b0847550>
```

Python affiche seulement la classe et l'adresse mémoire de l'objet, ce qui n'est pas très lisible. On peut choisir un affichage personnalisé en écrivant, dans la classe, la **méthode spéciale** `__repr__`. Elle doit **retourner** une chaîne de caractères :

```python
class Skateboard:
    ...

    def __repr__(self):
        if self.skateboard_pour_parc():
            return f"skateboard {self.deck} qui permet de rider en parc"
        else:
            return f"skateboard {self.deck} qui ne permet pas de rider en parc"
```

Après avoir recréé l'instance :

```python
>>> mon_sector_9 = Skateboard('long', 'plat', 'haut', 'molles', 'Marley')
>>> print(mon_sector_9)
skateboard long qui ne permet pas de rider en parc
>>> [mon_premier_skate, mon_sector_9]
[skateboard court qui permet de rider en parc, skateboard long qui ne permet pas de rider en parc]
```

*Remarques :*

* À l'intérieur de la classe, une méthode en appelle une autre avec `self.skateboard_pour_parc()`, sans redonner `self` entre les parenthèses.
* `__repr__` est utilisée par `print`, par la console et pour afficher les éléments d'une liste. Python propose aussi la méthode `__str__`, utilisée en priorité par `print` si elle existe.
* Les méthodes dont le nom est entouré de `__` sont des **méthodes spéciales** : Python les appelle automatiquement dans certaines situations (`__init__` à la création, `__repr__` à l'affichage…). Il en existe aussi pour les opérateurs, par exemple `__eq__` pour `==` ou `__lt__` pour `<` (voir les liens en bas de page).

# Des objets qui interagissent

## Un objet comme attribut d'un autre objet
Un attribut peut contenir n'importe quelle valeur : un nombre, une liste… ou **un autre objet**. Définissons une classe `Skateur`, dont l'attribut `planche` est un objet `Skateboard` :

```python
class Skateur:
    def __init__(self, nom, planche):
        self.nom = nom
        self.planche = planche      # un objet Skateboard

    def peut_aller_au_parc(self):
        return self.planche.skateboard_pour_parc()

    def session(self, distance):
        self.planche.rouler(distance)
```

```python
>>> lea = Skateur("Léa", mon_premier_skate)
>>> lea.peut_aller_au_parc()
True
>>> lea.session(4)
>>> mon_premier_skate.km
9
```

`self.planche.skateboard_pour_parc()` se lit de gauche à droite : « la planche de ce skateur, à qui on demande si elle est adaptée au parc ». Le skateur **délègue** la question à sa planche.

On peut de même utiliser un attribut qui contient une **liste d'objets** : par exemple un magasin dont l'attribut `stock` est une liste de `Skateboard`, ou un joueur qui a une liste de cartes en main (voir le mini-projet *Jeu des 7 familles*).

## Variables et objets : attention aux références
Dans l'exemple précédent, `lea.session(4)` a modifié `mon_premier_skate.km`. En effet, `lea.planche` et `mon_premier_skate` désignent **le même objet** en mémoire, et non deux copies.

```python
>>> copie = mon_premier_skate      # pas de nouvelle planche : un second nom pour la même
>>> copie.rouler(1)
>>> mon_premier_skate.km
10
>>> copie is mon_premier_skate
True
>>> Skateboard() == mon_premier_skate   # même état, mais deux objets différents
False
```

Une variable contient une **référence** vers l'objet, comme pour les listes. Seul un appel à `Skateboard(...)` fabrique un nouvel objet.

# Encapsulation : *getters* et *setters*

## Le principe
Pour utiliser un objet, il suffit de connaître son **interface** (ses méthodes et ce qu'elles font), sans savoir comment il est programmé à l'intérieur. On dit que les attributs sont **encapsulés** : idéalement, on ne les manipule pas directement, mais à travers des méthodes prévues pour cela.

Avantage : la méthode peut **contrôler** les modifications. Par exemple, empêcher une distance négative dans `rouler`, ou un type de roues inconnu.

## Lire un attribut : accesseur ou *getter*
Un **accesseur** (*getter*) est une méthode qui retourne la valeur d'un attribut. Son nom commence généralement par `get_` :

```python
class Skateboard:
    ...

    def get_tail(self):
        return self.tail
```

```python
>>> mon_sector_9.get_tail()
'plat'
```

## Modifier un attribut : mutateur ou *setter*
Un **mutateur** (*setter*) est une méthode qui modifie la valeur d'un attribut. Son nom commence généralement par `set_` :

```python
class Skateboard:
    ...

    def set_deco(self, deco):
        self.deco = deco
```

```python
>>> mon_sector_9.set_deco('repeinte')
>>> mon_sector_9.get_deco()      # si l'on a aussi écrit cet accesseur
'repeinte'
```

*Attention :* `mon_sector_9.set_deco = 'repeinte'` ne modifie pas la déco. Cette instruction remplace la méthode `set_deco` de cet objet par une chaîne de caractères !

## En pratique, en Python
Contrairement à d'autres langages comme Java, Python n'empêche pas d'écrire `objet.attribut`. Par convention, un attribut dont le nom commence par `_` (par exemple `self._km`) signale qu'il ne doit pas être utilisé en dehors de la classe.

*Au baccalauréat*, les sujets utilisent souvent directement la notation `objet.attribut` (par exemple `carte.famille`). Il faut donc savoir lire et écrire les deux formes.

# Documenter une classe : le *docstring*
Une classe se documente par une chaîne placée juste après sa première ligne : le **docstring**. Il décrit les attributs et les méthodes, c'est-à-dire l'interface de la classe :

```python
class Skateboard:
    """
    NAME
        Skateboard
    DESCRIPTION
        planche de skateboard
    ATTRIBUTES
        deck (str) : 'court' ou 'long'
        tail (str) : 'plat' ou 'relevé'
        truck (str) : 'haut' ou 'bas'
        roues (str) : 'dures' ou 'molles'
        deco (str ou None) : décoration sous le deck
        km (float) : distance parcourue, 0 à la création
    METHODS
        skateboard_pour_parc() -> bool
        rouler(distance) -> None
        get_tail() -> str
        set_deco(deco) -> None
    """
```

On en prend connaissance avec :

```
>>> help(Skateboard)
```

# Représenter une classe
On représente souvent une classe par un diagramme en trois cases : le **nom** de la classe, ses **attributs**, puis ses **méthodes**.

{{< img src="../images/UML.png" caption="Une représentation d'une classe" >}}

Pour la classe `Skateboard` :

| `Skateboard` |
|--- |
| `deck`, `tail`, `truck`, `roues`, `deco`, `km` |
| `__init__(deck, tail, truck, roues, deco)`, `skateboard_pour_parc()`, `rouler(distance)`, `get_tail()`, `set_deco(deco)`, `__repr__()` |

# L'essentiel

* Une **classe** décrit un type d'objet. Un **objet** (ou **instance**) est fabriqué à partir d'une classe : `planche = Skateboard('long')`.
* Les **attributs** (`self.deck`) décrivent l'**état** de l'objet. Les **méthodes** décrivent son **comportement**.
* Le **constructeur** `__init__` est appelé automatiquement à la création de l'objet : il crée les attributs.
* **`self`** désigne l'objet sur lequel agit la méthode. Il est le premier paramètre de chaque méthode, mais on ne l'écrit pas lors de l'appel : `planche.rouler(3)`.
* Une méthode peut **retourner** une information ou **modifier** l'état de l'objet.
* `__repr__` **retourne** la chaîne utilisée pour afficher l'objet.
* Un attribut peut être un autre objet, ou une liste d'objets : les objets **interagissent**.
* Une variable contient une **référence** vers un objet : deux variables peuvent désigner le même objet.
* Les **accesseurs** (`get_...`) et **mutateurs** (`set_...`) font l'interface entre l'utilisateur et les attributs : c'est l'**encapsulation**.

<!--
## Exercice 3: Classe Pile créée à partir d'une liste chaînée
La notion de *classe* permet de créer de nouveaux types de structure. Nous allons créer à la main une structure de liste chaînée; pour ce faire, nous allons utiliser une premiere classe *Maillon*; et une deuxième classe Pile, qui se servira de cette structure. Cette nouvelle structure n'utilise pas le type *List* de python.

On rappelle qu'une liste chaînée est une structure linéaire, constituée de cellules. [voir cours sur les listes chainees](/docs/NSI/structure/page21/#listes)

1. Compléter la méthode `push` fournie dans la fenêtre de l'editeur.
2. Créer une méthode `pop`.
3. Créer la méthode `__repr__(self)` qui va être appelée lors de l'affichage d'une pile `P` à l'aide de l'instruction `print(P)`.

-->

*Pour la suite :* la POO sert aussi à programmer des **structures de données** (piles, files, listes chaînées, arbres) : l'interface (les méthodes `empiler`, `depiler`…) est séparée de l'implémentation (la manière de stocker les données). Voir le [cours sur les listes chaînées](/docs/NSI/structure/page21/#listes).

**La suite en TP**

* TP de transition *Fruits et paniers* : [Lien](../tp_fruits_paniers/)
* Mini-projet Jeu des 7 familles : [Lien](../page34/) *(sans interface graphique)*
* TP sur les trajectoires de projectiles : [Lien](../page31/)
* TP sur la programmation d'un jeu de dominos : [Lien](../page33/) *(sans interface graphique)*

# Liens
* Cours sur [python.developpez.com](https://python.developpez.com/cours/apprendre-python-3/?page=la-programmation-orientee-objet) : compléments sur les méthodes spéciales de [surcharge des opérateurs](https://python.developpez.com/cours/apprendre-python-3/?page=la-programmation-orientee-objet#L7-4), et sur l'[héritage et le polymorphisme](https://python.developpez.com/cours/apprendre-python-3/?page=la-programmation-orientee-objet#L7-5) (hors programme).
* Référence : [Classes sur docs.python.org](https://docs.python.org/fr/3/tutorial/classes.html)
* Prolongement sur l'héritage et le polymorphisme (hors programme) : [Python Doctor, POO pour débutants](https://python.doctor/page-apprendre-programmation-orientee-objet-poo-classes-python-cours-debutants)
* Résumé de cours : [Lyceum.fr > POO](https://lyceum.fr/tg/nsi/4-langages-et-programmation/6-programmation-objet)
* Autres exercices : [Lyceum.fr > POO > Exercices](https://lyceum.fr/tg/nsi/4-langages-et-programmation/6-programmation-objet/exo)
