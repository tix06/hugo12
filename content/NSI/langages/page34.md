---
title: TP 7 Familles
description: POO et jeu des 7 familles, interaction entre objets de 2 classes
hidden: true
weight: 20
---

# Mini-projet : Jeu de cartes des 7 familles
<!--
Lien vers le notebook: [CAPYTALE](https://capytale2.ac-paris.fr/web/c/d57c-8003286)
-->

*Prérequis : TP « Fruits et paniers » (transition).*

## Les cartes
On donne la déclaration de la classe `Carte` :

```python
class Carte:
    """
    NAME
        Carte
    DESCRIPTION
        constructeur pour les cartes du jeu
    PARAMETERS
        famille (str) : nom de la famille
            choix parmi ('Jongleurs', 'Acrobates', 'Musiciens', 'Dresseurs', ...)
        membre_famille (str) : membre de la famille
            choix parmi ('Grand-père', 'Grand-mère', 'Père', 'Mère', 'Fils', 'Fille')
    METHODS
        get_attributs
    """
    def __init__(self, famille, membre_famille):
        self.famille = famille
        self.membre_famille = membre_famille

    def get_attributs(self):
        pass
```

> 1. Créer (instancier) l'objet `carte1` de la famille des *Jongleurs*, le *Grand-père*.

> 2. Compléter la classe `Carte` avec la méthode `get_attributs`. Cette méthode ne prend qu'un seul paramètre : `self`.
Elle doit **retourner** un tuple constitué des 2 attributs de l'objet.

Exemple d'utilisation dans le programme :

```
>>> carte1.get_attributs()
('Jongleurs', 'Grand-père')
```

**Question 1 :** (labo) recopier le script de cette méthode `get_attributs`.

> 3. Consulter le *docstring* de la classe :

```
>>> help(Carte)
```

> 4. Définir les objets-cartes suivants :

| nom | `famille` | `membre_famille`|
|--- |--- |--- |
| carte1 | 'Jongleurs' | 'Grand-père' |
| carte2 | 'Jongleurs' | 'Fille' |
| carte3 | 'Musiciens' | 'Père' |
| carte4 | 'Musiciens' | 'Fille' |

<!--
```
carte1 = Carte('Jongleurs','Grand-père')
carte2 = Carte('Jongleurs','Fille')
carte3 = Carte('Musiciens','Père')
carte4 = Carte('Musiciens','Fille')
```
-->

Puis tester la méthode :

```
>>> carte2.get_attributs()
```

**Question 2 :** Quelle instruction a permis d'instancier l'objet `carte2` ?

> 5. Ajouter les autres membres de la famille `Jongleurs` (carte5, carte6, …). Une famille est constituée de : Grand-père, Grand-mère, Père, Mère, Fils, Fille.

> 6. Ajouter la méthode `__repr__` qui permettra de décrire la carte.

Exemple de message attendu :

```
>>> print(carte1)
La carte est de la famille des Jongleurs : Grand-père.
```

*Rappel : `__repr__` doit **retourner** une chaîne de caractères (`return`), et non l'afficher avec `print`.*

Testez votre méthode pour quelques-unes des cartes.

**Question 3 :** recopier le script de votre méthode.

## Classe Joueur
Le joueur est un objet qui possède, pour attribut, la liste des cartes qu'il a en main.

Chaque joueur est une instance de la classe `Joueur`, et sera construit avec `joueur1 = Joueur(carte1, ...)`.

*Difficulté :* on ne connaît pas le nombre de cartes que le joueur a en main au moment de sa création.

Python permet d'appeler une fonction avec un nombre quelconque d'arguments : il faut ajouter le paramètre `*args` dans la déclaration de la fonction. On parcourt alors les arguments de la manière suivante :

```
for i in args:
  ...
```

La méthode `__init__` aura alors pour paramètres `self` (qui est obligatoire) et `*args`. On y définit une liste vide, `self.C`, à laquelle on ajoute chacune des cartes (objets de la classe `Carte`) passées en argument. Cette méthode est donnée dans l'éditeur, plus bas.

> 7. Dans la classe `Joueur` : écrire une méthode `get_cartes` qui retourne la liste `self.C`, afin de pouvoir accéder à la liste des cartes du joueur.

```python
class Joueur:
    def __init__(self, *args):
        self.C = []
        for carte in args:
            self.C.append(carte)

    def get_cartes(self):
        # à compléter
        pass

    def __repr__(self):
        pass


carte1 = Carte('Jongleurs', 'Grand-père')
carte2 = Carte('Jongleurs', 'Fille')
carte3 = Carte('Musiciens', 'Père')
carte4 = Carte('Musiciens', 'Fille')
```

**Question 4 :** recopier le script de votre méthode `get_cartes`.

> 8. Créer l'objet `joueur1`. Celui-ci devra posséder les cartes `carte1` et `carte2` définies plus haut : `joueur1 = Joueur(carte1, carte2)`.

Tester alors la méthode `joueur1.get_cartes()` pour afficher la liste.

*Que remarquez-vous ? Pourquoi l'affichage obtenu est-il celui-ci ?*

> 9. Écrire la méthode `__repr__` de la classe `Joueur` pour afficher la main du joueur dans un message, comme par exemple :

```
>>> print(joueur1)
le joueur possède les cartes : [('Jongleurs', 'Grand-père'), ('Jongleurs', 'Fille')]
```

*Remarque : il faudra utiliser la méthode `get_attributs` pour chaque objet de la liste `self.C`. Ce sont des objets `Carte`.*

> 10. On souhaite maintenant avoir une interaction plus poussée avec le `Joueur`, selon les règles du jeu.

L'idée est de créer une méthode `possede` qui prend en paramètre un tuple `(famille, membre_famille)`, et qui retourne un booléen selon la main du joueur, comme par exemple :

```
>>> joueur1.possede(('Jongleurs', 'Fils'))
False
>>> joueur1.possede(('Jongleurs', 'Fille'))
True
>>> joueur1.possede(carte1.get_attributs())
True
```

*Aide : parcourir la liste `self.C` et comparer `carte.get_attributs()` au tuple reçu.*

**Question 5 :** Quelles fonctionnalités du jeu reste-t-il à programmer pour avoir un jeu complet ?

**Question 6 :** **(mini-projet)** Programmer tout ou partie de ces fonctionnalités.

* Exemple 1 : programmer une méthode `donne` de la classe `Joueur`, qui prend en paramètre un tuple `(famille, membre_famille)`, retire la carte correspondante de la main du joueur et **retourne** cet objet `Carte`. On pourra utiliser la méthode de liste `remove`, qui supprime un élément X de la liste :

```python
>>> L = ['a', 'b', 'c']
>>> L.remove('b')
>>> L
['a', 'c']
```

*Attention : la liste `self.C` contient des objets `Carte`, et non des tuples. L'instruction `self.C.remove(('Jongleurs', 'Fille'))` provoque donc une erreur (`ValueError`). Il faut d'abord retrouver l'objet `Carte` correspondant au tuple, puis le retirer.*

* Exemple 2 : programmer une méthode `demande` de la classe `Joueur` telle que :

```
>>> joueur1 = Joueur(carte1, carte2)
>>> joueur2 = Joueur(carte3, carte4)
>>> print(joueur1)
le joueur possède les cartes : [('Jongleurs', 'Grand-père'), ('Jongleurs', 'Fille')]
>>> joueur2.demande(joueur1, ('Jongleurs', 'Grand-père'))
le joueur a la carte
>>> joueur2.demande(joueur1, ('Jongleurs', 'Grand-mère'))
pioche
>>> joueur2.demande(joueur1, carte2.get_attributs())
le joueur a la carte
>>> print(joueur1)
le joueur possède les cartes : []
```

Lorsque le joueur a la carte, il la donne au joueur qui la lui demande : elle est retirée de son jeu et s'ajoute au jeu de celui qui l'a demandée.

*Pistes pour aller plus loin : une classe `Pioche` (ou `Paquet`) qui crée les 42 cartes et les mélange (`random.shuffle`), la distribution des cartes, la détection d'une famille complète, le tour de jeu…*

# Liens

**Correction de l'exercice** sur le jeu des `Sept_Familles` : [Lien](../page32)

**La suite en TP**

* TP sur trajectoires de projectiles : [Lien](../page31/)
* TP sur la programmation d'un jeu de Dominos : [Lien](../page33/) *(Sans interface graphique)*
