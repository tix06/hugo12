---
Title : Files et Listes
description: autres structures lineaires, File, listes chainees
weight: 36
---

*Ce cours comporte 2 chapitres prérequis:*

* Cours sur les{{< a link="/docs/NSI/structure/page1/" caption="types abstraits" >}} et les tableaux statiques.
* {{< a link="/docs/NSI/structure/page3/" caption="Programmation orientée objets" >}}

*Et plusieurs parties:*

* les types abstraits: [Lien](../page1)
* les Piles: une structure linéaire: [Lien](../page2)
* exercices en ligne (TP) sur les Piles: [Lien](../page22)
* autres structures linéaires: [Lien](../page21)

*Et plusieurs notebooks:*

* Piles, Files, exercices issus de la banque de sujets d'EP: [Lien capytale.fr](https://capytale2.ac-paris.fr/web/c/0a47-1458602)
* Listes chainées sur [capytale2.ac-paris.fr](https://capytale2.ac-paris.fr/web/c/e3b8-4712390)

# Structures de données: rappels
Les piles, files et listes sont des structures de données **linéaires**. Ce sont des types **abstraits**.

Structure de données **linéaire** : les données sont rangées sur un ligne ou une colonne.

Un **type abstrait** décrit essentiellement une interface, indépendamment du  langage de programmation.


# Files
## Definition et interface
Une file (queue ou FIFO pour first in, first out) est une collection d’objets munie  des opérations suivantes:  
 
* savoir si la file est vide (is_empty);  
* ajouter un élément dans la file (enfiler ou enqueue) en temps constant;  
* retirer et renvoyer l’élément le plus ancien de la file (defiler ou dequeue). 

C'est une structure de données utilisée en informatique pour par exemple gérer la file d'attente lors de la gestion des impressions.

{{< img src="../images/file_ex.png" caption="exemple de gestion d'une file d'attente" >}}

## Implémentations en python natif
L'implementation d'une File est imparfaite avec une liste en python pour l'opération de *defiler*. On peut utiliser l'instruction `file.pop(0)`:

```python
> F = []
> F.append(1)
> F.append(2)
> F.append(3)
> print(F)
[1,2,3]
> F.pop(0)
> print(F)
[2,3]
```

Le problème est que celle-ci ne s'effectue pas en temps constant.

## Implémentation avec l'extension `deque`
La *bibliothèque standard* possède toutefois un module nommé `collections`  qui contient quelques structures de données supplémentaires, dont le type `deque`, qui est une implémentation de file:

```python
from collection import deque
f = deque()
f.append("Premier")
f.append("Deuxieme")
print(f.popleft())
f.append("Troisieme")
while f:
  print(f.popleft())
```

affiche:

```
Deuxieme
Troisieme
```


# Listes
## Principe
Le types abstrait *Liste* ne concerne pas le type *list* en python. C'est une liste *chaînée* (ou liste *liée*): une structure de données composées d’une séquence d’*éléments* de liste.

Ces éléments sont aussi appelés *noeuds* ou *maillons*.

La **tête** d’une liste est son premier *maillon*. La **queue** d’une liste, son dernier.

Chaque maillon **M** contient:

* une valeur, de n'importe quel type.
* un lien (ou pointeur) vers le maillon suivant de la séquence.

Il s'agit d'une structure *linéaire*, mais dans laquelle les éléments n'occupent pas *à priori*, des positions contigües dans la mémoire:

*illustration:*

{{< img src="../images/listeElem.png" alt="elements d" caption="elements dans une liste" >}}

Pour relier ces éléments ensembles, dans une même structure de données, il faut alors utiliser des *pointeurs*.

{{< img src="../images/listeElemPoint.png" alt="liste chainée grâce aux pointeurs" caption="liste chainée grâce aux pointeurs" >}}
L'élément **A** pointe sur **B**, qui pointe sur **C**, qui pointe sur **D**. **D**, lui, ne pointe sur ... **rien**!

La plupart du temps, le lien du dernier maillon a pour valeur *None* en python, signifiant un pointeur sur *rien*.




## Interface
On trouve en général les opérations suivantes pour l'interface d'une *Liste*:

* `est_vide` : renvoie `True` si Liste vide
* `taille` : renvoie le nombre de *maillons* de la séquence
* `get_dernier_maillon`  
* `get_maillon_indice`  
* `ajouter_debut`  
* `inserer_apres` 
* `ajouter_fin`  
* `supprimer_apres`  
* ...

## Implémentation en POO
L'implémentation est plus naturelle en *programmation orientée objet* {{< a link="/docs/NSI/structure/page3/" caption="voir le chapitre POO" >}}
> Un maillon est une instance de la classe `Maillon`

```python
class Maillon:
  def __init__(self):
    self.val = None
    self.suiv = None
```

> Une *Liste* est une instance de la classe `Liste`

```python
class Liste:
  def __init__(self):
    self.tete = None
```

Son attribut `tete`  est de type `Maillon` , ou bien vaut `None` si la liste est vide.

Cette classe ne comporte pour l'instant que sa définition de la variable `tete`, mais elle est créée pour contenir, plus tard, l'implementation des différentes méthodes prévues par l'interface.

{{< img src="../images/listeC.png" alt="liste chainée" caption="illustration d'une liste chainée" >}}
On peut alors créer une liste ainsi :

```python
ma_liste = Liste()
M1, M2, M3 = Maillon(), Maillon(), Maillon()
M1.val = 'A'
M2.val = 'C'
M3.val = 'D'
M1.suiv = M2
M2.suiv = M3
M3.suiv = None
ma_liste.tete = M1
```

> **Questions:** à votre avis, que vaut `L.tete.val` ?

> et que vaut `L.tete.suiv.val`?


## Interêt et inconvenient par rapport aux listes en python
L'interface d'une liste chainée fournit des méthodes plus efficaces que la *Pile*, la *File* ou le *tableau*, lorsque l'on veut par exemple: **insérer**, ou **supprimer** un élément dans la séquence.

{{< img src="../images/listeC2.png" alt="insertion liste chainée" caption="insertion dans une liste" >}}
Cette opération est prévue par l'interface d'une liste chainée => O(n): `inserer_apres(i)`, où `i` est l'indice de l'élément après lequel on veut *insérer*.

Avec une liste python, qui implémente la Pile (voir cours) cela necessite de décaler toutes les valeurs de rang supérieur à `i `. C'est une opération qui est évaluée en O($n^2$) pour sa complexité asymptotique.

Il s'agit du même problème lorsque l'on veut *supprimer après `i`*.

Un autre avantage est la possibilité de faire pointer le dernier élément sur le premier de la liste. On créé ainsi une liste *périodique*.

**Inconvénient:** Pour accéder à un *maillon* de rang `i` dans une liste chainée, il faut remonter la liste depuis le premier élément (celui de tête), jusqu'à celui de rang `i`. Et cela se fait avec une complexité asymtotique O(n).



# Exercices

Editeur sur [capytale2.ac-paris.fr](https://capytale2.ac-paris.fr/web/c/e3b8-4712390)

## Exercice 1: Créer une liste chainée
**1.** Completer le script ci-dessous pour créer une liste chainée appelée `ma_liste` qui contiendra la éléments suivants:

`'Premier', 'Troisieme'`, `'Quatrieme'`

Vous devrez créer les maillons `M1`, `M2`, `M3` et renseigner leur contenu `M.val`:

```python
class Maillon:
  def __init__(self):
    self.val = None
    self.suiv = None
    
class Liste:
  def __init__(self):
    self.tete = None

# a compléter
```

<!--
<iframe width='100%' height='500' allowfullscreen frameborder='0' style='border:1px #d6d6d6 solid;' src="https://fr.vittascience.com/python/?link=5faa722d44d4d&mode=code"></iframe>

{{< vitta 5faa722d44d4d >}}
-->

**2.** Tester dans la console les instructions suivantes:

```python
>>> ma_liste.tete.val
>>> ma_liste.tete.suiv.val
>>> ma_liste.tete.suiv.suiv.val
```

**3.** Rendez-vous sur{{< a link="http://pythontutor.com/visualize.html#mode=edit" caption="pythontutor.com" >}}
{{< img src="../images/pythontutor.png" alt="liste chainée et pythontutor" caption="liste chainée et pythontutor" >}}

Dans la fenêtre d'edition de *pythontutor*: Coller les lignes ci-dessous et executer le script *pas à pas*

```python
class Maillon:
  def __init__(self):
    self.val = None
    self.suiv = None
    
class Liste:
  def __init__(self):
    self.tete = None
    
L = Liste()
M1, M2, M3 = Maillon(), Maillon(), Maillon()
M1.suiv = M2
M2.suiv = M3
M1.val = 'A'
M2.val = 'C'
M3.val = 'D'
L.tete = M1
```

**4.** Ajouter les lignes suivantes et dérouler le programme ligne par ligne:

```python
s = L.tete
s.val = '1'
print(L.tete.val)
print(M1.val)
```

> Qu'affiche la console? Ce résultat était-il prévisible? Pourquoi? (la copie `s = L.tete` se fait-elle par valeur ou bien par référence)

## Exercice 2: afficher les éléments de liste
On cherche à parcourir les éléments d'une liste chainée `L`.

On propose un premier algorithme itératif. Celui-ci stocke l'élément de tête de `L` dans une variable `M`.

Puis une boucle non bornée parcourt les différents maillons de `L` jusqu'à ce que `M.suiv` soit `None`, marquant le maillon de *queue*.

On affiche alors les valeurs `M.val` de ces maillons avec `print`.

Et on passe au maillon suivant: `M = M.suiv`

**1.** Ecrire le script itératif.

**2.** Adapter ce script pour en faire une fonction **recursive** qui prend en paramètre un maillon M, et affiche toutes les valeurs jusqu'à la fin de la liste. La condition d'arrêt (Base) sera `M.suiv is None`. 

La fonction doit renvoyer une chaine de caractères fabriquée de la manière suivante : `A => ... => ... => D`

Compléter après le return: 

```python
class Maillon:
  def __init__(self):
    self.val = None
    self.suiv = None
    
class Liste:
  def __init__(self):
    self.tete = None
    
L = Liste()
M1, M2, M3 = Maillon(), Maillon(), Maillon()
M1.suiv = M2
M2.suiv = M3
M1.val = 'A'
M2.val = 'C'
M3.val = 'D'
L.tete = M1

def affiche(M):
    if M.suiv is None:
        return str(M.val)  # affiche la valeur de queue
    else:

    .....
```



<!--
<iframe width='100%' height='500' allowfullscreen frameborder='0' style='border:1px #d6d6d6 solid;' src="https://fr.vittascience.com/python/?link=5faa752e1c9a3&mode=code"></iframe>

{{< vitta 5faa752e1c9a3 >}}
-->

**3.** Comment appeler cette fonction afin qu'elle affiche TOUS les éléments de la liste L, du premier (*tête*) au dernier? Tester avec la liste **ACD** décrite dans le cours.

## Exercice 3: Insertion d'un élément

{{< img src="../images/listeC2.png" alt="insertion liste chainée" caption="insertion dans une liste" >}}

Soit la liste chainée `L`: 'A' => 'C' => 'D'

On souhaite maintenant modifier la séquence de `L` créée dans l'exercice 2. On va insérer un élément de valeur `B` à la $2^e$ position:

A => B => C => D


Ajouter dans votre programme les instructions qui permettront de:
 
**1.** Créer un nouveau maillon `M2`.

**2.** Affecter 'B' comme valeur à `M2`.

**3.** Modifier le lien `M2.suiv` pour que celui-ci pointe vers le 3<sup>e</sup> élément de `ma_liste`. 

**4.** Modifier le lien `L.tete.suiv` pour recréer la liste chainée. (ou bien celui de `M1`, ce qui revient à la même chose).

**5.** Utiliser la fonction `affiche` pour afficher les éléments de `L`.

**6.** Que se passerait-il avec cette fonction `affiche` si on mettait `M4.suiv = M1`? (liste chainée circulaire).

# Correction des exercices
## Exercice 1

```python
# correction de l'exercice 1
class Maillon:
  def __init__(self):
    self.val = None
    self.suiv = None
    
class Liste:
  def __init__(self):
    self.tete = None
    
ma_liste = Liste()
M1, M2, M3 = Maillon(), Maillon(), Maillon()
M1.val = 'Premier'
M2.val = 'Troisieme'
M3.val = 'Quatrieme'
M1.suiv = M2
M2.suiv = M3
M3.suiv = None
ma_liste.tete = M1

print(ma_liste.tete.val)
print(ma_liste.tete.suiv.val)
print(ma_liste.tete.suiv.suiv.val)

s = ma_liste.tete
s.val = '1'
print(ma_liste.tete.val)
print(M1.val)
```


## Exercice 2

```python
# Correction de l'exercice 2 en ligne question 2.1
M = L.tete
while not M.suiv is None:
    print(M.val)
    M = M.suiv
print(M.val)
```

Pour le script recursif:

```python
# Correction de l'exercice 2.2 en ligne

def affiche(M):
    if M.suiv is None:
        return str(M.val)
    else:
        return str(M.val) + '=>' + affiche(M.suiv)


# Correction question 2.3 en ligne
>>> print(affiche(L.tete))
'A=>B=>C=>D'
```

## Exercice 3
(à venir)

# Liens
* Retour vers la page [introduction aux structures de données: les Piles](../page2/)


