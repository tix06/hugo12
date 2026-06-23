---
Title : programmation orientée objet
description: cours POO, classe, instanciation, accesseur getter et mutateur setter
weight: 16
---

Cette séquence comprend:

* un cours sur la POO: [Lien](../page3)
* une fiche d'exercices: [pdf](/pdf/NSI/POO_exercices.pdf)
* TP Jeu des 7 familles: [Lien](../page34/) *(Sans interface graphique)*
* TP sur trajectoires de projectiles: [Lien](../page31/) 
* TP sur la programmation d'un jeu de Dominos: [Lien](../page33/). *(Sans interface graphique)*

# Programmation objet

## Principe
En programmation orientée objet, on cherche à organiser les données avec la volonté de se rapprocher de l'architecture *d'objets physiques*.

Un *objet physique*, comme par exemple, une planche de skateboard, possède des caractéristiques propres. 

{{< img src="https://urbanart-paris.fr/wp-content/uploads/2016/04/12963624_1877786249114590_5321151849406456199_n.jpg" alt="chalk custom board" link="https://urbanart-paris.fr/event/chalk-custom-board-lart-dhabiller-skate/" caption="image: CHALK CUSTOM BOARD : L’ART D’HABILLER UN SKATE (urban art)" >}}
Une planche, malgré la diversité, est toujours constituée: 

* d'un deck (court, long)
* d'un tail (plat, relevé)
* de trucks (hauts, bas)
* de roues (à gommes tendres, dures)
* d'une décoration (image sous le deck)

C'est son **état**.

Cette planche peut repondre egalement à un ensemble de messages, qui forment ce que l'on appelle l'*interface* de l'objet. C'est au travers de ces méthodes que l'on peut interagir avec l'objet, ou que les objets peuvent interagir entre eux.

On peut lui associer une méthode `skateboard_pour_parc` qui renvoie `True` si la planche est de type *street* ou `False` si la planche est de type *cruising*, ou prevue pour la decoration.

Un objet comprend donc :

* une partie **figée** qui représente son **état**, et qui est constituée de champs ou **attributs**.
* une partie **dynamique** qui décrit son **comportement**, à l'aide de déclarations de **méthodes**, qui doivent répondre à des **messages**. 

## Classe et instance de classe
La structure interne des objets et les messages auxquels ils repondent sont définis dans une **classe**. Une *classe* décrit les méthodes de création d'objets de ce type (on parle d'*instance* de classe), et les méthodes auxquelles répondront les objets de ce type dans la reception des messages.

Avec l'exemple précédent, la **class**e Skateboard pourrait contenir:

* les méthodes de création des instances des différents skateboards. On y définit les attributs pour chaque nouvelle planche de skateboard que l'on créé. Chaque planche de skate constitue une *instance* de classe.
* les méthodes de la classe skateboard, qui repondent aux messages du genre: `skateboard_pour_parc`? Un *message* est constitué du nom de la méthode, et permet d'interagir avec celui-ci. Ces méthodes sont accessibles à tous les skates qui sont des instances de la classe skateboard.

En **python**, la création d'une classe commence par le mot clé **class** suivi du nom de la classe, de deux points et d'une indentation. 

```python
class Skateboard:
``` 

Toute la partie indentée contient les *méthodes de création* des *instances* de cette classe et les *méthodes* de cette classe.

Lors de la programmation, on devra faire référence à l'instance de l'objet sur lequel on travaille: le mot clé `self` permet ceci en python.

La méthode de création d'un objet est définie par `def __init__` suivi au minimum de l'argument `self`, et eventuellement d'autres arguments.

```python
class Skateboard:
    def __init__(self,deck='court',
                tail='releve',
                truck='bas',
                roues='dures',
                deco='None'):
        self.deck = deck
        self.tail = tail
        self.truck = truck
        self.roues = roues
        self.deco = deco
``` 

Les attributs des objets de cette classe sont définis dans cette méthode. Ils sont codés sous la forme `self.attribut`, et peuvent faire référence aux arguments passés lors de l'instanciation.

Enfin, chaque méthode de classe est définie à l'aide de: `def nom_de_la_methode`. Celle-ci prend aussi au minimum, l'argument `self`.

*Script complet:*

```python
class Skateboard:
    def __init__(self,deck='court',tail='releve',truck='bas',roues='dures',deco='None'):
        self.deck = deck
        self.tail = tail
        self.truck = truck
        self.roues = roues
        self.deco = deco
        
    def skateboard_pour_parc(self):
        if self.deck == 'court' and self.tail == 'releve' and self.roues == 'dures':
            return True
        else:
            return False
```

On instancie alors un premier skateboard de la manière suivante:

```python
>>> mon_premier_skate = Skateboard()
```

Le programme interprete alors l'instruction: `Skateboard.__init__(mon_premier_skate)`, c'est à dire qu'il execute la méthode de classe `Skateboard.__init__`, avec le paramètre `self=mon_premier_skate`.

{{< img src="../images/sk8_classic.jpg" alt="skateboard classic" caption="un premier skateboard bien classique" >}}
Et on envoie le message suivant:

```python
>>> mon_premier_skate.skateboard_pour_parc()
True
```

Le programme interprete alors l'instruction: `Skateboard.skateboard_pour_parc(mon_premier_skate)`,

Instanciation d'un second skateboard:

{{< img src="../images/sk8_sector9.jpg" alt="skateboard cruiser" caption="un skateboard cruiser" >}}
```python
>>> mon_sector_9 = Skateboard('long','plat','haut','molles','Marley')
>>> mon_sector_9.skateboard_pour_parc()
False
```

## La méthode `__repr__()` 
Cette méthode `__repr__` s'utilise pour donner une représentation plus lisible de l'objet lorsqu'on veut l'afficher avec la fonction `print`.

*Exemple 1:* On essaie d'afficher notre instance de classe `mon_sector_9` créée plus haut:

```python
>>> print(mon_sector_9)
<__main__.Skateboard object at 0x7fc6b0847550>
``` 

Ce n'est pas très explicite pour un humain. On préfèrera souvent choisir un descriptif personnalisé. Nous allons programmer la chaine de caractères qui sera renvoyée lors du `print`.

On ajoute maintenant à la classe `Skateboard` la méthode `__repr__()` qui sera appelée lorsque l'on utilise `print(objet)`: 

```python
class Skateboard:
    def __init__(...
    ...

    def __repr__(self):
        if self.skateboard_pour_parc():
            return "skateboard de type {} qui permet de rider en parc".format(self.deck)

        else:
            return "skateboard de type {} qui ne permet pas de rider en parc".format(self.deck)
```

On construit à nouveau l'instance de classe `mon_sector_9`, et on fait `print(mon_sector_9)`:

```python
>>> mon_sector_9 = Skateboard('long','plat','haut','molles','Marley')
>>> print(mon_sector_9)
skateboard de type long qui ne permet pas de rider en parc
``` 

*Remarquer* que l'appel à la méthode `skateboard_pour_parc` se fait en identifiant l'objet qui possède cette méthode: `self.skateboard_pour_parc()`. Et ici, on n'ajoutera pas de nouvel argument. (On ne met pas `self` en argument lors du *message* envoyé à cet objet).

*Surcharge d'une fonction de la librairie standard:* Ce que l'on vient de réaliser est une surcharge de la fonction `print` de la librairie standard. 

Mais il existe d'autres méthodes de surcharge, prévues pour les **opérateurs**, ainsi que pour certaines **fonctions**. On pourra se référer au [lien suivant](https://riptutorial.com/fr/python/example/7334/surcharge-de-l-operateur) pour approfondir le sujet.

# Encapsulation: *getter* et *setter* 
## Lire un attribut: accesseur ou *getter*

L'utilisateur du programme ne devrait pas utiliser la méthode *pointée* précédente `nom_objet.nom_attribut`, permettant d’accéder aux valeurs des attributs: on ne veut pas forcement que l’utilisateur ait accès à la représentation interne des classes. 

Pour utiliser ou modifier les attributs, on utilisera de préférence des **méthodes dédiées** dont le rôle est de faire l’**interface** entre l’utilisateur de l’objet et la représentation interne de l’objet (ses attributs).

Les **attributs** sont alors en quelque sorte **encapsulés** dans l’objet, c’est à dire non accessibles directement. la liste des **méthodes** devient une sorte de mode d’emploi de la classe.

Pour obtenir la valeur d’un attribut nous utiliserons la méthode des accesseurs (ou "getters") dont le nom est généralement : `getNom_attribut()`.

*Exemple:*


```python
class Skateboard:
    def __init__(...
    ...
    
    def getTail(self):
      return self.tail
```

En console, une fois l'instance de classe `mon_sector_9` définie, on fait:

```
>>> mon_sector_9.getTail()
`long`
```

## Modifier des attributs : les mutateurs ou *setters*
De la même manière, pour modifier la valeur d'un attribut, on devrait utiliser une méthode dédiée. Le nom de cette méthode commence en principe par `set`:

*Exemple:*

```python
class Skateboard:
    def __init__(...
    ...
    
    def setDeco(self, deco):
      self.deco = deco
```

En console:

```
>>> mon_sector_9.setDeco = 'repeinte'

```

## Docstrings
Chaque classe définit ses propres manières de stocker, d'acceder et de manipuler les données. C'est le Docstring qui permettra de prendre connaissance des détails, comme par exemple celui de la classe `Sept_Familles`:

```python
class Sept_Familles:
    """
    NAME
        Sept_Familles
    DESCRIPTION
        constructeur pour les cartes du jeu
    PARAMETERS
        famille (str): nom de la famille
        qui(str): membre de la famille 
            choix parmi ('Grand-père','Grand-mère','Pére','Mère','Fils','Fille')
    FUNCTIONS
        get_Attributs
    """
```

On peut alors prendre connaissance du docstring en faisant:

```
>>> help(Sept_Familles)
```

# Interface
L'interface d'une classe est représentée par le diagramme suivant:

{{< img src="../images/UML.png" caption="Une représentation d'une classe" >}}

<!--
# L'essentiel
<h2> Classe et Objet</h2>
Un <b>objet</b> est construit à partir d'une <b>classe</b>, et comporte des attributs (les variables) et des méthodes (fonctions).


<ul>
<li>Les <b>attributs</b> renvoient aux variables contenues dans l’objet : ce sont les données. Ces données peuvent varier au cours du programme. Il s'agit donc de l'état de cet objet à un instant t.</li>
<li>Les <b>méthodes</b> sont les éléments qui permettent d’interagir avec les attributs. Les méthodes sont des fonctions internes à une classe, qui doivent répondre à des <b>messages</b>.</li>
</ul>

<em>Exemple:</em><br>
<pre><code>
class Sept_Familles:
    def __init__(self,famille,qui):
        self.famille = famille
        self.qui = qui   
    def get_Attributs(self):
        return self.famille,self.qui

carte1 = Sept_Familles('Jongleurs','Grand-père')
</code></pre>

<h2>Instanciation</h2>
<p>
<b>Un objet est une <em>instance</em> de classe.</b>
</p>
<p>
On instancie un objet en appelant le nom de sa classe comme s'il s'agissait d'une fonction. Instancier, c'est définir un nouvel objet, donc définir son <b>nom</b>, et la valeur de ses attributs.
</p>
<p>
Par exemple, à l'aide de l'instruction <code>carte1 = Sept_Familles('Jongleurs','Grand-père')</code> lorsque l'on veut créer un nouvel objet <code>carte1</code> à partir de la classe <code>Sept_Familles</code>.
</p>
<p>
C'est alors la méthode <code>__init__(self,attribut1,...);</code> qui est automatiquement appelée pour initialiser l'objet. Cette méthode déclare les attributs associés à <code>Sept_Familles</code>.
</p>
<h2> Definir une méthode de classe</h2>
Les méthodes de classe peuvent modifier l'état de l'objet (ses attributs), ou retourner une valeur.

Une méthode possède au minimum, comme attribut, self. Les autres seront ajoutés après:

<pre><code>
  def age(self,an_actuelle):
    """
    calcule l'age en fonction de l'année de naissance
    et de la date actuelle
    Params:
    self.an_de_naissance (int): attribut de l'objet
    an_actuelle (int) : date actuelle
    """
    return an_actuelle - self.an_de_naissance
</code></pre>
<h2>Notation pointée</h2>
<h3>Attributs</h3>
<p>
Les attributs sont accessibles au sein de la classe à l'aide d'une notation pointée, du type <code>self.attribut</code>. Le mot-clé <code>self</code> correspondra à l'objet instancié.
</p>
<p>
<em>En dehors de la classe:</em>
<br>
On pourrait acceder aux attributs en faisant `objet.attribut`:

<pre><code>
carte1.famille
</code></pre>
</p>

<p>
En principe, il vaudra mieux éviter cette notation pointée en dehors de la classe, et éviter de faire référence aux attributs en faisant <code>objet.attribut</code>. On préfèrera utiliser un mécanisme d'<b>encapsulation</b>.
</p>
<h3>Méthodes</h3>
Les méthodes de classe sont accessibles en faisant 

<pre><code>
objet.methode(arg)
</code></pre>

<h2>L'encapsulation</h2>
<p>
L'<b>encapsulation</b> consiste à rassembler les données et les méthodes au sein d'une structure en cachant l'implémentation de l'objet, c'est-à-dire en empêchant l'accès aux données par un autre moyen que les services proposés. (getters et setters par exemple).
</p>
<p>
On peut, par exemple, accéder à la description de carte1 à l'aide de la méthode <code>get_Attributs()</code>, ce qui donne:

<pre><code>
>>> carte1.get_Attributs()
('Jongleurs', 'Grand-père')
</code></pre>

</p>

-->



<!--
## Exercice 3: Classe Pile créée à partir d'une liste chaînée
La notion de *classe* permet de créer de nouveaux types de structure. Nous allons créer à la main une structure de liste chaînée; pour ce faire, nous allons utiliser une premiere classe *Maillon*; et une deuxième classe Pile, qui se servira de cette structure. Cette nouvelle structure n'utilise pas le type *List* de python.

On rappelle qu'une liste chaînée est une structure linéaire, constituée de cellules. [voir cours sur les listes chainees](/docs/NSI/structure/page21/#listes)

1. Compléter la méthode `push` fournie dans la fenêtre de l'editeur.
2. Créer une méthode `pop`.
3. Créer la méthode `__repr__(self)` qui va être appelée lors de l'affichage d'une pile `P` à l'aide de l'instruction `print(P)`.

-->

**La suite en TP**

* TP Jeu des 7 familles: [Lien](../page34/) *(Sans interface graphique)*
* TP sur trajectoires de projectiles: [Lien](../page31/) 
* TP sur la programmation d'un jeu de Dominos: [Lien](../page33/). *(Sans interface graphique)*

# Liens
* cours sur [python.developpez.com](https://python.developpez.com/cours/apprendre-python-3/?page=la-programmation-orientee-objet): compléments sur les méthodes spéciales de [surcharge des opérateurs](https://python.developpez.com/cours/apprendre-python-3/?page=la-programmation-orientee-objet#L7-4), d'[héritage et polymorphisme](https://python.developpez.com/cours/apprendre-python-3/?page=la-programmation-orientee-objet#L7-5)
* références : [Classes sur docs.python.org](https://docs.python.org/fr/3.6/tutorial/classes.html)
* prolongement sur les heritages et polymorphismes [python doctor POO - debutants](https://python.doctor/page-apprendre-programmation-orientee-objet-poo-classes-python-cours-debutants)
* Resumé de cours : [Lyceum.fr > POO](https://lyceum.fr/tg/nsi/4-langages-et-programmation/6-programmation-objet)
* Autres exercices : [Lyceum.fr > POO > Exercices](https://lyceum.fr/tg/nsi/4-langages-et-programmation/6-programmation-objet/exo)


