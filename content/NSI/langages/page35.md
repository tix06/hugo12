---
title: TP Fruits et paniers
titleHidden: true
description: POO, transition vers le mini-projet 7 familles. Une classe, puis deux classes qui interagissent
hidden: true
weight: 17
---

# TP d'introduction à la POO : Fruits et paniers

*Durée : 45 min. Ce TP prépare le mini-projet [Jeu des 7 familles](../page34/) : on y retrouve exactement les mêmes notions, sur un exemple plus simple.*

**Objectifs :**

* écrire une classe avec un constructeur `__init__`, des attributs et des méthodes ;
* faire la différence entre **retourner** (`return`) et **afficher** (`print`) ;
* écrire une méthode `__repr__` ;
* écrire une classe dont un attribut est une **liste d'objets** d'une autre classe ;
* faire interagir deux objets entre eux.

**Méthode de travail :** après chaque étape, copier-coller les tests (`assert`) proposés à la fin de votre programme et l'exécuter. Si rien ne s'affiche, les tests sont réussis ! Si une `AssertionError` apparaît, c'est qu'un test échoue : corriger avant de passer à la suite.

---

## Partie 1 : la classe `Fruit` (10 min)

Un fruit est décrit par deux attributs : son `nom` (par exemple `"pomme"`) et sa `couleur` (par exemple `"rouge"`).

```python
class Fruit:
    def __init__(self, nom, couleur):
        # à compléter : créer les attributs nom et couleur
        pass

    def get_attributs(self):
        # à compléter
        pass
```

> 1. Compléter le constructeur `__init__`.

> 2. Créer l'objet `f1` : une pomme rouge.

Tests :

```python
assert f1.nom == "pomme"
assert f1.couleur == "rouge"
```

> 3. Compléter la méthode `get_attributs` : elle doit **retourner** le tuple `(nom, couleur)`.

```
>>> f1.get_attributs()
('pomme', 'rouge')
```

Test :

```python
assert f1.get_attributs() == ("pomme", "rouge")
```

> 4. Taper dans la console `print(f1)`. Que s'affiche-t-il ? Est-ce lisible ?

> 5. Ajouter à la classe `Fruit` la méthode `__repr__` ci-dessous et la compléter. Python l'appelle automatiquement lorsqu'on fait `print(f1)`, ou lorsqu'on affiche une liste qui contient `f1`.

```python
    def __repr__(self):
        return ...   # doit retourner une chaîne, par exemple "pomme (rouge)"
```

```
>>> print(f1)
pomme (rouge)
```

Test :

```python
assert str(f1) == "pomme (rouge)"
```

> 6. Créer deux autres fruits : `f2`, une banane jaune, et `f3`, un kiwi vert.

---

## Partie 2 : la classe `Panier` (15 min)

Un panier appartient à un `proprietaire` et possède un attribut `contenu` : une **liste d'objets `Fruit`**, vide au départ.

```python
class Panier:
    def __init__(self, proprietaire):
        self.proprietaire = proprietaire
        self.contenu = []

    def ajouter(self, fruit):
        # à compléter : ajoute l'objet fruit à la liste contenu
        pass

    def taille(self):
        # à compléter : retourne le nombre de fruits dans le panier
        pass

    def __repr__(self):
        # à compléter
        pass
```

> 7. Compléter les méthodes `ajouter` et `taille`.

Tests :

```python
p = Panier("Léa")
assert p.taille() == 0
p.ajouter(f1)
p.ajouter(f2)
assert p.taille() == 2
```

> 8. Compléter la méthode `__repr__` pour obtenir l'affichage suivant :

```
>>> print(p)
Panier de Léa : [pomme (rouge), banane (jaune)]
```

*Remarque : dans la liste, chaque fruit s'affiche grâce au `__repr__` de la classe `Fruit` écrit à la question 5. Essayer de mettre en commentaire le `__repr__` de `Fruit` : que se passe-t-il ?*

> 9. Écrire la méthode `contient(self, nom)` qui **retourne** `True` si le panier contient un fruit portant ce nom, `False` sinon.

*Aide : parcourir la liste `self.contenu` avec une boucle `for fruit in self.contenu:` et comparer `fruit.nom` au nom recherché.*

Tests :

```python
assert p.contient("banane") == True
assert p.contient("kiwi") == False
```

---

## Partie 3 : retirer un fruit (10 min)

> 10. Exécuter les instructions suivantes. Que se passe-t-il ? Pourquoi ?

```python
p.contenu.remove("pomme")
```

*La liste `p.contenu` ne contient pas la chaîne `"pomme"`, mais un **objet** `Fruit` dont l'attribut `nom` vaut `"pomme"`. Il faut donc d'abord retrouver cet objet dans la liste, puis le retirer.*

> 11. Écrire la méthode `retirer(self, nom)` qui :
>
> * cherche dans le panier le premier fruit portant ce nom ;
> * le retire de la liste avec `remove` ;
> * **retourne** l'objet `Fruit` retiré ;
> * retourne `None` si aucun fruit ne porte ce nom.

Tests :

```python
r = p.retirer("pomme")
assert r == f1
assert p.taille() == 1
assert p.retirer("fraise") == None
```

---

## Partie 4 : deux paniers qui interagissent (10 min)

**a) Un nombre quelconque d'arguments**

On voudrait pouvoir créer un panier déjà rempli : `Panier("Léa", f1, f2)` ou `Panier("Tom", f3)`, sans savoir à l'avance combien de fruits seront donnés.

Python le permet avec le paramètre `*args` : tous les arguments supplémentaires sont rangés dans `args`, que l'on peut parcourir avec une boucle `for`. Exemple :

```python
def somme(*nombres):
    total = 0
    for n in nombres:
        total = total + n
    return total
```

```
>>> somme(1, 2, 3)
6
>>> somme()
0
```

> 12. Modifier le constructeur de `Panier` pour qu'il ait l'en-tête `def __init__(self, proprietaire, *fruits):` et ajoute chacun des fruits reçus à `self.contenu`.

Tests :

```python
lea = Panier("Léa", f1, f2)
tom = Panier("Tom", f3)
assert lea.taille() == 2
assert tom.taille() == 1
```

**b) Donner un fruit à un autre panier**

> 13. Écrire la méthode `donner(self, autre, nom)` : si le panier `self` contient un fruit portant ce nom, ce fruit est retiré de `self` et ajouté au panier `autre`, et la méthode retourne `True`. Sinon, rien ne change et la méthode retourne `False`.

*Aide : utiliser les méthodes déjà écrites `contient`, `retirer` et `ajouter`. Le paramètre `autre` est lui-même un objet `Panier` : on peut donc écrire `autre.ajouter(...)`.*

```
>>> lea.donner(tom, "banane")
True
>>> print(lea)
Panier de Léa : [pomme (rouge)]
>>> print(tom)
Panier de Tom : [kiwi (vert), banane (jaune)]
>>> lea.donner(tom, "fraise")
False
```

Tests :

```python
assert lea.donner(tom, "banane") == True
assert lea.taille() == 1
assert tom.contient("banane")
assert lea.donner(tom, "fraise") == False
```

---

## Bilan : du panier aux 7 familles

| TP Fruits et paniers | Mini-projet 7 familles |
|--- |--- |
| classe `Fruit(nom, couleur)` | classe `Carte(famille, membre_famille)` |
| `Fruit.get_attributs()` | `Carte.get_attributs()` |
| classe `Panier`, attribut `contenu` (liste de `Fruit`) | classe `Joueur`, attribut `C` (liste de `Carte`) |
| `Panier(proprietaire, *fruits)` | `Joueur(*args)` |
| `contient(nom)` | `possede((famille, membre_famille))` |
| `retirer(nom)` | `donne((famille, membre_famille))` |
| `donner(autre, nom)` | `demande(autre_joueur, (famille, membre_famille))` |

**Questions de synthèse :**

1. Quelle est la différence entre une méthode qui **retourne** une valeur et une méthode qui l'**affiche** ?
2. Pourquoi `self.contenu.remove("pomme")` ne fonctionne-t-il pas ?
3. Dans la méthode `donner`, combien d'objets `Panier` sont modifiés ? Lesquels ?

**Suite :** [Mini-projet : Jeu des 7 familles](../page34/)

<!--
CORRECTION

def somme(*nombres):
    total = 0
    for n in nombres:
        total = total + n
    return total

class Fruit:
    def __init__(self, nom, couleur):
        self.nom = nom
        self.couleur = couleur

    def get_attributs(self):
        return (self.nom, self.couleur)

    def __repr__(self):
        return f"{self.nom} ({self.couleur})"

class Panier:
    def __init__(self, proprietaire, *fruits):
        self.proprietaire = proprietaire
        self.contenu = []
        for f in fruits:
            self.contenu.append(f)

    def ajouter(self, fruit):
        self.contenu.append(fruit)

    def taille(self):
        return len(self.contenu)

    def __repr__(self):
        return f"Panier de {self.proprietaire} : {self.contenu}"

    def contient(self, nom):
        for f in self.contenu:
            if f.nom == nom:
                return True
        return False

    def retirer(self, nom):
        for f in self.contenu:
            if f.nom == nom:
                self.contenu.remove(f)
                return f
        return None

    def donner(self, autre, nom):
        if self.contient(nom):
            autre.ajouter(self.retirer(nom))
            return True
        return False

Question 4 : print(f1) affiche <__main__.Fruit object at 0x...> (type + adresse mémoire).
Question 10 : ValueError: list.remove(x): x not in list
Synthèse 3 : deux objets Panier sont modifiés : self (perd le fruit) et autre (le reçoit).
-->
