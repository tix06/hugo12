---
Title: correction probleme reduction
hidden: true
weight: 38
---

# Reduction de chaines, Piles

*Exemples*

```
assert reduc('aAbB') == list('')
assert reduc('baAB') == list('')
assert reduc('abBaAa') == list('aa')
assert reduc(['d','a','a','b','A','a','A','a']) == ['d', 'a', 'a', 'b']
assert reduc('abBaAa') == ['a', 'a']
```

*Implémentation*

```python
def Pile():
    return []

def est_vide(pile):
    return pile == []

def depile(pile):
    assert pile != [], 'impossible de depiler : pile vide'
    return pile.pop()


def empile(pile,a):
    pile.append(a)

def sommet(pile):
    assert pile != [], 'pile vide: impossible de consulter le sommet'
    return pile[-1]

def deversepile(pile1,pile2):
    while not est_vide(pile1):
        empile(pile2,depile(pile1))
        
def inversepile(p1):
    p2 = []
    while not est_vide(p1):
        empile(p2,depile(p1))
    return p2
```

*Programme itératif*

```python
# iteratif

D = {'a':'A','b':'B','A':'a','B':'b','c':'C','C':'c','d':'D','D':'d'}
def reduc(chaine):
    if isinstance(chaine,str):
        chaine = list(chaine)
    if len(chaine) == 0:
        return []
    while not est_vide(chaine):
        x = depile(chaine) 
        if not est_vide(L2) and x == D[sommet(L2)]:
            depile(L2)
            try:
                empile(chaine,depile(L2))
            except:
                pass
        else:
            empile(L2,x)
    return inversepile(L2)

L2 = [] 
print(reduc(['d','a','a','b','A','a','A','a']))
L2 = []
print(reduc('abBaAa'))
```

*Programme recursif*

```python
# recursif

D = {'a':'A','b':'B','A':'a','B':'b','c':'C','C':'c','d':'D','D':'d'}
def reduc_recur(chaine):
    if isinstance(chaine,str):
        chaine = list(chaine)
    if len(chaine) > 0:
        x = depile(chaine) 
        if not est_vide(L2) and x == D[sommet(L2)]:
            depile(L2)
            try:
                empile(chaine,depile(L2))  
            except:
                pass
        else:
            empile(L2,x)
        reduc_recur(chaine)
    return L2
L2 = [] 
print(inversepile(reduc_recur(['d','a','a','b','A','a','A','a'])))
# ['d', 'a', 'a', 'b']
L2 = []
print(inversepile(reduc_recur('abBaAa')))
# ['a', 'a']
```

[Retour à l'énoncé](../page22)
