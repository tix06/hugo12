---
Title: exercices sur la recursivité
description: exercices recursivite
hidden: true
weight: 23
---

[RETOUR au cours sur la recursivité](../page2/)

# Ex 1: Fonction `impair`

La fonction récursive impair accepte un paramètre, N, entier positif. A chaque appel récursif, la fonction s'appelle elle-même avec l'argument N-2.

1. La condition de base est que N == 1 au bout d'un certain nombre d'appels.

> Completez le script de cette fonction. 

<!--
<iframe width='100%' height='500' allowfullscreen frameborder='0' style='border:1px #d6d6d6 solid;' src="https://fr.vittascience.com/python/?link=5f87256293a25&mode=code"></iframe>

{{< vitta 5f87256293a25 >}}
-->

```python
def impair(N):
    """retourne True si N est impair
    Param:
    N: int positif
    Exemple:
    >>> impair(5)
    True
    >>> impair(4)
    False
    >>> assert impair(4) == False
    >>> assert impair(5) == True
    """
```

2. Cette condition de base est-elle suffisante ou bien faut-il en ajouter une autre? Complétez votre script.

> Une fois que vous obtenez les bons résultats aux tests, recopiez le script sur votre cahier d'exercices.

# Ex 2: Suite de Fibonacci
On définit la suite (f<sub>n</sub>) des nombres de Fibonacci par :
$$\left\\{\begin{matrix}\begin{align}f\_0 & =0\\\f\_1 & =1\\\f\_{n+1} & =f\_{n}+f\_{n-1}, \forall n \in \mathbb{N}^+\end{align}\end{matrix}\right.$$

```python
def fibo(n):
    """
    algo recursif
    Exemple:
    >>> assert fibo(1) == 1
    >>> assert fibo(10) == 55
    """
    if (n==0) : return 0
    if (n==1) : return 1
    return fibo() + fibo()
```


1. Compléter la dernière ligne de la fonction `fibo` avec les bons arguments
2. Ajouter quelques lignes au script pour placer dans une liste `L` tous les nombres de la suite de Fibonacci, du rang 0 au rang n=10 (inclus).


<!--
<iframe width='100%' height='500' allowfullscreen frameborder='0' style='border:1px #d6d6d6 solid;' src="https://fr.vittascience.com/python/?link=5f8726ff0f497&mode=code"></iframe>

{{< vitta 5f8726ff0f497 >}}
-->

> Une fois que vous obtenez les bons résultats aux tests, recopiez le script sur votre cahier d'exercices.

# Ex 3: Les tours de Hanoï
Le problème des tours de Hanoi est présenté en détails dans le cours sur la recursivité [ici](/docs/NSI/langages/page22/#application-les-tours-de-hanoï)


1. Dans l'editeur ci-dessous: Executer le script. Puis aller dans la console et tester l'exemple proposé dans le prototypage de la fonction.

> Représenter dans votre cahier d'exercice les différents déplacements. S'aider du schéma:

{{< img src="../images/page2/hanoi_3p.png" >}}

2. Tester egalement avec 4 disques. Noter le nombre de deplacements effectués pour N=1 à 4.





*3.* Proposez une loi de recurence entre le nombre de déplacements T(N) pour N disques, et le nombre de déplacements T(N-1) pour N-1 disques. 

> Cette loi, est-elle prévisible à partir de l'énoncé de la solution (pour déplacer N disques du piquet 1 à 3, il faut deplacer N-1 disques de 1 à 2, puis ...).

*Aide: on pourra consulter la page [accromath](https://accromath.uqam.ca/2016/02/les-tours-de-hanoi-et-la-base-trois/).*

# Ex 4: Nombre d'occurences dans une chaine de caractères
il s'agit d'écrire une fonction recursive nombre_r(lettre, phrase) qui renvoit le nombre de fois où la lettre apparaît dans la phrase. 

* Dans le cas de base: on retourne 0 si la phrase est vide `""`.
* Pour l'heredité: On réduit la phrase en eliminant le premier caractère après chaque appel recursif: on met comme argument `phrase[1:]` à la place du paramètre `phrase`.

    * Si le caractère `phrase[0]` est identique à `lettre`: on applique la formule de recurence suivante: $u_n = 1 + u_{n-1}$ que l'on adapte ici en: `return 1 + nombre_r(lettre,phrase[1:])`

    * sinon, on adapte la formule de recurence : $u_n = u_{n-1}$

> Compléter le script et testez votre fonction avec, par exemple les arguments: `u` et `lustucru`

```python
def nombre_r(lettre, phrase):
    """
    Exemples:
    >>> assert nombre_r('a','lustucru') == 0
    >>> assert nombre_r('u','lustucru') == 3
    """
    if len(phrase)==0: # si la phrase est vide
        return 0
    # SINON
    if phrase[0]==lettre:
```

<!--
<iframe width='100%' height='500' allowfullscreen frameborder='0' style='border:1px #d6d6d6 solid;' src="https://fr.vittascience.com/python/?link=5f872924a7977&mode=code"></iframe>

{{< vitta 5f872924a7977 >}}
-->

> Une fois que vous obtenez les bons résultats aux tests, recopiez le script sur votre cahier d'exercices.

# Ex 5: Retournement d'une liste
La fonction suivante realise un retournement d'une chaine de caractères. 




```python
def reverse_iterative(seq): 
    """
    Return the reverse of a string 
    Example:
    >>> reverse_iterative('abcd')
    dcba
    >>> assert reverse_iterative('abacab') = 'bacaba'
    """
    reversed_seq = ""
    for i in range(1,len(seq)+1):
        reversed_seq = reversed_seq + seq[-i] 
    return reversed_seq
```


1. Programmer et tester la fonction itérative.
2. Compléter le script de la fonction `reverse_recur`. S'aider du schéma suivant:

```
f('abc') = f('bc') + 'a'
         = f('c') + 'b' + 'a'
         = f('') + 'c' + 'b' + 'a'
         = 'cba'
```

*Fonction recursive, script à compléter*:

```python
def reverse_recur(seq):
    """
    >>> assert reverse_iterative('abacab') = 'bacaba'
    """
    if seq == "":
        return ""
    return ...
```

> Une fois que vous obtenez les bons résultats aux tests, recopiez le script sur votre cahier d'exercices.

# Exercice 6: algorithme d'Euclide 
Euclide propose l’algorithme suivant:

1. Calculez le reste r dans la division de a par b
2. Si r est nul alors le pgcd est b
3. Sinon recommencer l’étape 1 avec a = b et b = r


{{< img src="../images/page2/euclide.png" >}}
> Exemple d’exécution : a = 32, b = 12 :

– 32 = (2 x 12) + 8

– 12 = (1 x 8) + 4

– 8 = (2 x 4) + 0

On a donc pgcd(32, 12) = 4

La page dédiée sur [wikipedia](https://fr.wikipedia.org/wiki/Algorithme_d%27Euclide) propose une illustration géométrique de cette méthode. *Un couple d'entiers est vu comme un rectangle, dont le PGCD est la longueur du côté du plus grand carré permettant de carreler entièrement ce rectangle:*

{{< img src="../images/page2/euclide2.png" caption="Explication géométrique de l'algorithme d'Euclide sur les entiers 21 et 15. - source wikipedia" >}}

```python
def euclide(a,b):
    """
    a et b sont des entiers, a > b
    euclide retourne un entier qui est le PGCD de a et b
    """
    r = a % b
    while r>0 :
        a = b
        b = r
        r = a % b
    return b
```

1. Tester l'algorithme itératif avec un couple de valeurs de votre choix.

Le PGCD d'Euclide calcule une suite définie par une récurence à 2 termes:

$r_0 = a$

$r_1 = b$

$r_2 = r_0 \\% ~r_1$

$r_{n+1} = r_{n-1} \\% r_n$

```python
def PGCD(a,b):
  """
  PGCD : entier correspondant au plus grand diviseur commun de a par b
  a et b : entiers tels que a > b
  b correspond à r_n, a correspond à r_{n-1}, r à r_{n+1}
  return:
  -------
  appel recursif avec b et r
  -------
  Exemples:
  >>> PGCD(28,12)
  4
  >>> assert PGCD(24,18) == 6
  """
  if b == 0 : return a
  else:
    r = .. % ..
    return PGCD(...,...)
```

2. Compléter la fonction recursive du calcul du PGCD

> vérifier son (bon) fonctionnement grâce aux tests proposés dans le docstring.



[RETOUR au cours sur la recursivité](../page2/)
# Ressources
* L'editeur en ligne est proposé par [https://fr.vittascience.com/python/](https://fr.vittascience.com/python/)
