---
Title: TP 7 Familles
description: POO et jeu des 7 familles, interaction entre objets de 2 classes
hidden: true
weight: 18
---

# Exercice: Jeu de cartes des 7 familles
Lien vers le notebook: [CAPYTALE](https://capytale2.ac-paris.fr/web/c/d57c-8003286)

## Les cartes
On donne la declaration de la classe `Sept_Familles`

```python
class Sept_Familles:
    """
    NAME
        Sept_Familles
    DESCRIPTION
        constructeur pour les cartes du jeu
    PARAMETERS
        famille (str): nom de la famille
            choix parmi ('Jongleurs','Acrobates','Dresseurs','...')
        membre_famille(str): membre de la famille 
            choix parmi ('Grand-père','Grand-mère','Pére','Mère','Fils','Fille')
    FUNCTIONS
        get_Attributs
    """
    def __init__(self,famille,qui):
        self.famille = famille
        self.membre_famille = qui
```

**Question 1**: créer (instancier) l'objet `carte1` de la famille des *Jongleurs*, le *Grand-père*.

**Question 2**: Compléter la classe Sept_Familles avec la fonction `get_Attributs`. Cette fonction ne prend pas d'autre paramètre que `self`.
Celle-ci devra retourner un tuple constitué des 2 attributs de classe.

Exemple d'utilisation dans le programme:

```
>>> carte1.get_attribut()
('Jongleurs','Grand-père')
```

**Question 3**: Consulter le *Docstring*  de la classe:

```
>>> help(Sept_Familles)
```

**Question 4**: Définir les objets-cartes suivantes:

```
carte1 = Sept_Familles('Jongleurs','Grand-père')
carte2 = Sept_Familles('Jongleurs','Fille')
carte3 = Sept_Familles('Musiciens','Père')
carte4 = Sept_Familles('Musiciens','Fille')
```

Puis tester la méthode de classe:

```
>>> carte2.get_Attributs()
```

Ajouter les autres membres de l’une des familles (carte5, carte6,…). Une famille est constituée de Grand-père, Grand-mère, Père, Mère, Fils, Fille.

**Question 5**: Ajouter la méthode `__repr__` qui permettra de décrire la carte:

Exemple de message attendu:

```
>>> print(carte1)
La carte est de la famille des Jongleurs. C'est le Grand-père.
```

Testez votre fonction pour quelques unes des cartes.

## Classe joueur
Le joueur est un objet qui possède, pour attributs, les cartes qu'il a en main.

Chaque joueur est une instance de la classe `Joueur`, et sera construit avec `joueur1 = Joueur(carte1,...)`

*Difficulté à venir:* On ne connait pas le nombre de cartes que le joueur peut avoir en main à l'instant t. 

Python permet d'appeler une fonction avec un nombre inconnu d'arguments: il faut ajouter le paramètre `*args` dans la déclaration de la fonction. On parcourt alors les arguments de la manière suivante:

```
for i in args:
  ...
```

La fonction `__init__` aura alors pour arguments `self` (qui est obligatoire), et `*args`. On y definit une liste vide, `self.C`, et on y ajoute des tuples constitués des attributs pour chacune des cartes du joueur. Cette fonction est donnée dans l'editeur, plus bas...

**Question 1**: Dans la classe `Joueur`: Ecrire une méthode de classe `get_cartes` qui retourne la liste `self.C`, afin de pouvoir accéder à la liste des cartes du joueur.

```python
class Joueur:
    def __init__(self,*args):
        self.C = []
        for i in args:
            self.C.append(i.get_Attributs())
    
    # à compléter


carte1 = Sept_Familles('Jongleurs','Grand-père')
carte2 = Sept_Familles('Jongleurs','Fille')
carte3 = Sept_Familles('Musiciens','Père')
carte4 = Sept_Familles('Musiciens','Fille')
```

**Question 2**: Créer l’objet `joueur1`. Celui-ci devra posséder les cartes `carte1` et `carte2` définies plus haut: `joueur1 = Joueur(carte1,carte2)`

Tester alors la méthode : joueur1.get_cartes() pour afficher la liste.

**Question 3**: Créer une méthode de classe `__repr__` pour afficher cette liste dans un message, comme par exemple:

```
>>> print(joueur1)
le joueur possède les cartes : [('Jongleurs', 'Grand-père'), ('Jongleurs', 'Fille')]
``` 

**Question 4**: On souhaite maintenant avoir une interaction plus poussée avec le `Joueur`, selon les règles du jeu. 

L’idée est de créer une méthode `possede` qui prend en paramètre un tupple `(famille,membre_famille)`, et qui retourne un booleen selon la main du joueur, comme par exemple:

```
>>> joueur1.possede(('Jongleurs','Fils'))
False
>>> joueur1.possede(('Jongleurs','Fille'))
True
>>> joueur1.possede(carte1.getAttributs())
True
```

**Question 5**: Quelles fonctionnalités du jeu reste t-il à programmer pour avoir un jeu complet?

**Question 4:** On souhaite maintenant avoir une interaction plus poussée avec le `Joueur`, selon les règles du jeu. 

L’idée est de créer une méthode `possede` qui prend en paramètre un tupple `(famille,membre_famille)`, et qui retourne un booleen selon la main du joueur, comme par exemple:

```
>>> joueur1.possede(('Jongleurs','Fils'))
False
>>> joueur1.possede(('Jongleurs','Fille'))
True
>>> joueur1.possede(carte1.getAttributs())
True
```

**Question 5:** Quelles fonctionnalités du jeu reste t-il à programmer pour avoir un jeu complet?

**Question 6:** **(mini projet)** Programmer tout ou partie de ces fonctionnalités.

* Exemple 1: programmer une fonction `donne`, de la classe `Joueur` qui retire la carte de la liste du joeur. On pourra utiliser la méthode de liste `remove`, qui supprime un élément X de la liste:

```python
>>> L = ['a','b','c']
>>> L.remove('b')
>>> L
['a','c']
```

* Exemple 2: programmer une fonction `demande` de la classe `Joueur` telle que:

```
>>> joueur1 = Joueur(carte1,carte2)
>>> print(joueur1)
le joueur possède les cartes : [('Jongleurs', 'Grand-père'), ('Jongleurs', 'Fille')]
>>> joueur2.demande(joueur1,('Jongleurs','Grand-père'))
le joueur a la carte
>>> joueur2.demande(joueur1,('Jongleurs','Grand-mère'))
pioche
>>> joueur2.demande(joueur1,carte2.get_Attributs())
le joueur a la carte
```

Lorsque le joueur a la carte, il la donne au joueur qui la lui demande. Elle est retirée de son jeu et s'ajoute au jeu de l'adversaire.



# Liens

**Correction de l'exercice** sur le jeu des `Sept_Familles`: [Lien](../page32)

**La suite en TP**

* TP Jeu des 7 familles: [Lien](../page34/) *(Sans interface graphique)*
* TP sur trajectoires de projectiles: [Lien](../page31/) 
* TP sur la programmation d'un jeu de Dominos: [Lien](../page33/). *(Sans interface graphique)*