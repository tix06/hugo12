---
Title: TD reduction chaine
hidden: true
weight: 37
---

# Exercice 1 : implementer une pile
On donne les fonctions qui implémentent la *pile*: `Pile`,`est_vide`,`empile`,`depile`,`sommet`:

```python

L = ['a',1,'b',2,'c',3,'d',4]

def Pile():
    return []

def est_vide(pile):
    return pile == []

def depile(pile):
    return pile.pop()

def empile(a,pile):
    pile.append(a)

def sommet(pile):
    return pile[-1]

```

> Utilisez les fonctions de cette interface pour resoudre l'exercice suivant: 

    * Soit une liste L = ["a",1,"b",2,"c",3,"d",4]
    * Parcourir les éléments de la liste L avec une boucle bornée
    * empiler tous les **nombres entiers** dans une pile `p`.
    * afficher `p`

```python
L = ['a',1,'b',2,'c',3,'d',4]
```

On pourra utiliser la fonction `isinstance(a,int)` qui retourne `True` si `a` est de type `int`.

<!--<iframe width='100%' height='500' allowfullscreen frameborder='0' style='border:1px #d6d6d6 solid;' src="https://fr.vittascience.com/python/?link=5f9d36caf37c6&mode=code"></iframe>-->

<!--
{{< vitta 5f9d36caf37c >}} 
-->

# Exercice 2 : lever des exceptions
Certaines des fonctions que vous avez écrites vont générer des erreurs dans le cas où la pile est vide.

1. Pour les fonctions `est_vide` et `depile`, ajouter un test d'assertion pour lever les exceptions dans le cas où la pile est vide.
2. Tester ces fonctions avec une pile vide.


# Exercice 3 : déverser une pile
## Déverser une pile
Ecrire une fonction `deversepile` qui déverse une pile `p1` dans une pile `p2`.

Pour que `p2` soit identique à `p1`, il faudra utiliser une pile intermédaire `p3` de la manière suivante: 

```python
p1,p2,p3=Pile(),Pile(),Pile()
deversepile(p1,p3)
deversepile(p3,p2)
```

*Les fonctions que vous pourrez utiliser pour les piles seront celles définies dans l'exercice 1 : `Pile,est_vide,empile,depile,sommet`.*

## Visualiser sur Pythontutor
Ouvrir l'editeur pythontutor et executer le script pas à pas. 

{{< img src="../images/pythontutor2.png" link="https://pythontutor.com/render.html#code=def%20deverse%28p_1,p_2%29%3A%0A%20%20%20%20while%20p_1%20!%3D%20%5B%5D%3A%0A%20%20%20%20%20%20%20%20p_2.append%28p_1.pop%28%29%29%0A%0Ap1,p2%20%3D%20%5B%5D,%5B%5D%0Ap1%20%3D%20%5B1,2,3,4%5D%0Adeverse%28p1,p2%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false" caption="cliquer pour ouvrir sur pythontutor" >}}

*Remarquez-vous?*

* La pile `p1` est-elle vide à la fin du *dépilement*?
* Les listes `p1` et `p2` sont-elles modifiées par effet de bord, dans la fonction?
* Les éléments se rangent-ils en sens inverse dans `p2`?



# Exercice 4 : Evaluation d'une opération en notation polonaise inversée
## Principe 
la notation polonaise inversée permet d'écrire une opération sans utiliser de parenthèses. Il faut alors écrire les 2 opérandes avant l'opérateur. L'opérateur se trouve à droite des 2 opérandes.

En parcourant l'expression `L` de gauche à droite (boucle `for`):

* chaque fois que l'on rencontre un opérateur: 
    * on dépile 2 fois la pile `p` pour rechercher les 2 opérandes (nombres)
    * on empile le resultat de l'opération.

* chaque fois que l'on rencontre un entier, on l'empile dans `p`


On peut utiliser une pile pour réaliser la séquence de calculs.

Exemple : `1 2 + 4 * 3 +`

{{< img src="../images/npi.png" >}}

{{< img src="../images/video_NPI.png" alt="video notation polonaise inversée" link="https://www.youtube.com/watch?v=Ak8I7o-rXKg" caption="Arnaud Bodin : Calculatrice polonaise - les piles" >}}
La liste L contient les caractères de l'expression POSTFIXE à calculer.

## Problème simplifié: Opérations d'addition seulement
Dans un premier temps, on ne va considérer que des expressions contenant des entiers et l'opérateur `+`. 

Par exemple, `L = [7, 8, '+', 6, '+', 10, '+', 3, '+']`

Cette expression sera évaluée à 34.

```python
L = [7, 8, '+', 6, '+', 10, '+', 3, '+']

def Pile():
    return []

def est_vide(pile):
    return pile == []

def depile(pile):
    assert pile != [], 'impossible de depiler : pile vide'
    return pile.pop()

def empile(a,pile):
    pile.append(a)

def sommet(pile):
    assert pile != [], 'la pile n_a pas de sommet : pile vide'
    return pile[-1]

def evalNPI(L):
    """evalue l'expression postfixe de type 
    notation polonaise inversee
    :Params:
    L : list of str and int: liste contenant les caracteres et les nombres entiers
    :Returns:
    p[0]: int, le resultat de l'evaluation de L, seul element restant de la pile p
    :variables:
    p : list of int: les entiers stockés pour leur evaluation
    :Exemple:
    >>> evalNPI([7, 8, '+', 6, '+', 10, '+', 3, '+'])
    34
    """
    p=[]    
    # à completer #
    return p[0]
```
## Calculatrice complète
On donne le script python à compléter:

```python
L = [7, 8, '-', 6, '*', 10, 3, '+', '*']


def Pile():
    return []

def est_vide(pile):
    return pile == []

def depile(pile):
    assert pile != [], 'impossible de depiler : pile vide'
    return pile.pop()

def empile(a,pile):
    pile.append(a)

def sommet(pile):
    assert pile != [], 'la pile n_a pas de sommet : pile vide'
    return pile[-1]



def add(x,y):
    # à completer #

def soust(x,y):
    # à completer #

def multip(x,y):
    # à completer #

dicoP = {'+' : add,
        '-' : soust,
        '*' : multip
}


def evalNPI(L):
    """evalue l'expression postfixe de type 
    notation polonaise inversee
    :Params:
    L : list of str and int: liste contenant les caracteres et les nombres entiers
    :Returns:
    p[0]: int, le resultat de l'evaluation de L, seul element restant de la pile p
    :variables:
    p : list of int: les entiers stockés pour leur evaluation
    :Exemple:
    >>> evalNPI([7, 8, '-', 6, '*', 10, 3, '+', '*'])
    -78
    """
    p=[]    
    # à completer #
    return p[0]
```

1. Compléter les fonctions `add`, `soust`, et `multip` qui doivent additionner, soustraire, et multiplier les arguments x et y.
2. Testez vos fonctions à l'aide du tableau associatif: Executer en console l'instruction: `dicoP['-'](3,4)` qui doit renvoyer ... -1
3. Compléter la fonction evalNPI: Dans une boucle bornée qui parcourt tous les éléments de la liste L: `for a in L:`

* si `a` est un entier: empiler a dans une liste `p` qui sera utilisée comme une *pile*.
* si `a` est un opérateur présent dans le tableau associatif `dicoP`:
    * depiler `p` deux fois et stocker les valeurs dans les opérandes x et y. 
    * empiler la valeur calculée dans la pile `p`
* retourner la valeur finale stockée dans `p`

<!--
<iframe width='100%' height='500' allowfullscreen frameborder='0' style='border:1px #d6d6d6 solid;' src="https://fr.vittascience.com/python/?link=5f9d305edd765&mode=code"></iframe>

{{< vitta 5f9d305edd765 >}}
-->

## Variante utilisant les fonctions lambda
On peut racourcir l'écriture du script en utilisant des fonctions lambda. Elles utilisent des paramètres pour calculer une valeur de retour, comme une fonction. Elles ne peuvent contenir qu'une expression.

On les déclare de la manière suivante:

```python
lambda arguments: expression
```

*Exemple 1:*

```python  
sum = lambda a,b : a+b
```

Ces fonctions peuvent ne pas être nommées. On les place alors dans une liste, ou un dictionnaire.


```python
dico = {'+' : lambda x,y : x+y,
        '-' : lambda x,y : x-y,
        '*' : lambda x,y : x*y
        }
```

On calcule alors avec cette fonction en faisant: `dico[a](3,4)` par exemple:

*Exemple 2:*

```python
a = '+'
if a == '+':
    r = dico[a](3,4)
    print(r)
# affiche 7
```

L'interêt des fonctions *lambda* est surtout de **rendre le script plus lisible**. Cela donne une autre option d'écriture.

# Exercice 5 (Projet): Reduction d'une chaine de caractères
On utilisera pour cet exercice l'implementation d'un pile avec les definitions suivantes:

```python
def Pile():
    return []

def est_vide(pile):
    return pile == []

def depile(pile):
    assert pile != [], 'impossible de depiler : pile vide'
    return pile.pop()

def empile(a,pile):
    pile.append(a)

def sommet(pile):
    assert pile != [], 'la pile n_a pas de sommet : pile vide'
    return pile[-1]
```


## Enoncé basique
Certains jeux comme par exemple *Candie Crush* reposent sur l'*élimination de motifs adjacents*. Je vous propose ici d'utiliser une chaine de caractères dans laquelle les motifs vont être éliminé de la manière suivante:


![méthode de reduction](../images/reduction.PNG)

> Programmez la fonction `reduction` qui va permettre de réaliser ceci.

*On se limitera aux caractères 'a', 'A', 'b', 'B', 'c', 'C', 'd', 'D' pour cette chaine.*

> Testez votre fonction avec les arguments suivants:

```
reduction(['d','D','a','A','a'])
-> ['d','D','a']
reduction(['d','a','a','b','A','a','A','a'])
-> ['d','a','a','b']
reduction(['d','a','c','a','A','a','A','a','C'])
-> ['d', 'a', 'a', 'b']
reduction(['B','a','A','c','A','a','A','a','C','b'])
-> []
```

[correction](../page23)

## Enoncé difficile
On modifie maintenant la règle du jeu: les motifs peuvent être réduits par groupe de 2, comme précédemment, mais aussi par groupe de 3 si ceux-ci présentent une  alternance minuscule-majuscule-minuscule ou bien majuscule-minuscule-majuscule:

```
reduction(['b','D','a','A','a'])
-> ['b','D']
reduction(['d','D','a','A','a'])
-> ['d','D'] puis []
reduction(['b', 'D', 'a','a','A','a'])
-> ['b','D','a']
```

Par contre, il n'y aura pas de reduction lorsque la séquence ne présente pas d'alternance:

```
> reduction(['d','a','a','b','A','a','A','a'])
['d','a','a','b']
```




<!--
## Enoncé progressif
On va chercher un solution qui ressemble à celle de la notation polonaise inversée, utilisant une Pile.

On donne 2 fonctions qui seront utiles pour la resolution:

```python
def deversePile(pile1,pile2):
    while not est_vide(pile1):
        empile(depile(pile1),pile2)
        
def motif(pile):
    p2 = Pile()
    i = 0
    if not est_vide(pile):
        c1 = depile(pile)
        empile(c1,p2)
    while not est_vide(pile) and sommet(pile) in dicoS and c1 == dicoS[sommet(pile)]:
        c2 = depile(pile) # c2 est le sommet
        empile(c2,p2)
        i = i + 1
        c1 = c2
    deversePile(p2,pile)
    #return i, p2, pile
    return i
```

**Partie 1**: fonction `motif(pile)`

cette fonction retourne le nombre de motifs consecutifs comptés à partir du sommet de la pile:

Pour ['z','a',**'a','A','a'**]

* la fonction compte un motif pour ['z','a','a',**'A','a'**]
* puis un motif pour ['z','a',**'a','A'**,'a']

Ce qui fait 2 motifs consécutifs.

> Testez la fonction avec les arguments suivants:

```
> motif(['z','a','a','A','a'])
> motif(['z','a','a','b','A','a','A','a'])
> motif(['z','a','c','a','A','a','A','a','C'])
> motif(['z','a','c','a','A','a','A','a','C'])
```

**Partie 2**: fonction recursive `destruction_pile`

```python
def destruction_recur(pile):
    if motif(pile) == 0:
      # a completer
    else:
        return destruction_recur(pile[:-1])
```

Completer la fonction `destruction_pile` avec pour paramètre `pile`.

Les 2 conditions d'arrêt seront:

* retourne `pile` si le nombre de motifs à partir du sommet est égal à zero
* retourne `pile` dont on supprime les 2 éléments du sommet si le nombre de motifs à partir du sommet est égal à 1
* appel recursif avec pour argument `pile` dont on a supprimé l'élément du sommet.

> Completer le script et tester la fonction avec les différents exemples de piles donnés plus haut.

**Partie 3**:  fonction `simplifier`
Dans la fonction `simplifier`:

* on utilise un dictionnaire pour mettre les caractères en correspondance 'a' : 'A', ...
* on parcours chaque caractères `c` d'une chaine `s` 
* on utilise une pile pour stocker des caractères au fur et à mesure du parcours de `s`
* si p n'est pas vide, si le caractere au sommet de la pile `p` est une clé du dictionnaire `dicoS`, et si ce caractère correspond à `c` selon la regle établie pour l'énoncé du problème ('a' : 'A', ...):
 * empiler `c` dans `p`
* sinon si `p` non vide, mais `c` et le sommet de `p` ne correspondent pas:
 * appel recursif de `destruction_recur`
 * empiler `c` dans `p`
 * nouvel appel recursif de `destruction_recur`
* sinon: empiler `c` dans `p`



```python
def simplifier(s):
    dicoS = {'a':'A','b':'B','c':'C','d':'D','A':'a','B':'b','C':'c','D':'d'}
    p = Pile()
    for c in s:
        ...
```
-->
<!--
# Correction des exercices
## Exercice 1

```python
# exercice 1
L = ['a',1,'b',2,'c',3,'d',4]

def Pile():
    return []

def est_vide(pile):
    return pile == []

def depile(pile):
    assert pile != [], 'impossible de depiler : pile vide'
    return pile.pop()

def empile(a,pile):
    pile.append(a)

def sommet(pile):
    assert pile != [], 'la pile n_a pas de sommet : pile vide'
    return pile[-1]



p = Pile()
for a in L:
    if isinstance(a,int):
        empile(a,p)
print(p)
```



## Exercice 2
Les modifications ont été faites directement dans le corrigé de l'exercice 1.

Tester le script suivant à la suite de celui de l'exercice 1:

```python
# exercice 2
p2 = Pile()
depile(p2)
```

## Exercice 3
Ajouter la fonction `deversePile` suivante à la suite de celles de l'exercice 1. (Les fonctions `est_vide`, `depile` et `empile` doivent être définies)


```python
# exercice 3
def deversePile(p1,p2):
    while not(est_vide(p1)):
        a = depile(p1)
        empile(a,p2)
    return p2
```

## Exercice 4
Il faut commencer par définir le dictionaire `dicoP` ainsi que les différentes fonctions des opérations:

```python
def add(x,y):
    return x+y

def soust(x,y):
    return x-y

def multip(x,y):
    return x*y

dicoP = {'+' : add,
        '-' : soust,
        '*' : multip
}
```

On peut tester une opération à l'aide de `dicoP`:

```python
>>> dicoP['-'](3,4)
-1
```

Puis on programme la fonction `evalNPI`.

On donne une autre version (plus avancée) de la fonction `evalNPI` utilisant des fonctions lambda, ce qui raccourcit le script:

```python
def evalNPI(L):
    dico = {'+' : lambda x,y : x+y,
            '-' : lambda x,y : x-y,
            '*' : lambda x,y : x*y
    }
    p=[]    
    for a in L:
        if a in dico:
            deuxieme = depile(p)
            premier = depile(p)
            r = dico[a](premier,deuxieme)
            empile(r,p)
        elif isinstance(a,int) : 
            empile(a,p)
    return p

evalNPI(L)
```

> A vous de jouer: Ecrire la liste d'instructions relatives au calcul de g, puis utiliser votre calculatrice en notation polonaise inversée pour résoudre:

> $$g = (3+6)*7 - (10-24)*4$$



<i>Aide: rappelez vous que l'instruction ne contient pas de parenthèses, alors il faudra bien respecter l'ordre des opérations à realiser, de gauche à droite. Le dernier caractère à saisir sera alors le symbole **-**. Relire la video si vous en avez besoin (énoncé de l'Ex 4).</i>


-->


