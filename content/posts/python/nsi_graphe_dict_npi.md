---
author: "Eric Tixidor"
date: 08-26-2020
linktitle: Python graphe et NPI
menu:
  main:
    parent: 
next: 
prev: 
title: Python graphe et NPI
weight: 10
---
# tracer un arbre à partir d'une expression NPI
NPI : notation polonaise inversée

En particulier : on dispose d'une expression en NPI, du type :

`L3 = [7,8,'-',6,'*',10,3,'+','*']`

Et on veut créer et afficher le graphe correspondant : 
![](../images/output_3_0.png)

On utilisera le script : 

```
L3 = [7,8,'-',6,'*',10,3,'+','*']

D = makeTree(L3)
G = nx.Graph()
graphDict(D)
```

Dont l'instruction suivante va générer le dictionnaire à partir de l'expression NPI (fonction `npiTree` recursive): 

```
D = makeTree(L3)
D
# affiche {'*': ({'*': ({'-': (7, 8)}, 6)}, {'+': (10, 3)})}
```
Ce dictionnaire peut être alors parcouru avec des elgorithmes recursifs, comme par exemple celui de la fonction `createEdges` qui est un parcours en profondeur.

Le script permet aussi de créer une structure intermédiaire sous forme de dictionnaire, et permet d'afficher le graphe à partir de tout dictionnaire D : 

```
G = nx.Graph()
graphDict(D)
```

Le graphe est dans le format networkx. On pourra consulter la notice à l'adresse suivante :

* [différents algorithmes de parcours de graphe avec networkx](https://networkx.github.io/documentation/stable/reference/algorithms/traversal.html)
* [netwokx general](https://networkx.github.io/documentation/stable/reference/introduction.html)



```python
def hierarchy_pos(G, root=None, width=1., vert_gap = 0.2, vert_loc = 0, xcenter = 0.5):

    '''
    From Joel's answer at https://stackoverflow.com/a/29597209/2966723.  
    Licensed under Creative Commons Attribution-Share Alike 

    If the graph is a tree this will return the positions to plot this in a 
    hierarchical layout.

    G: the graph (must be a tree)

    root: the root node of current branch 
    - if the tree is directed and this is not given, 
      the root will be found and used
    - if the tree is directed and this is given, then 
      the positions will be just for the descendants of this node.
    - if the tree is undirected and not given, 
      then a random choice will be used.

    width: horizontal space allocated for this branch - avoids overlap with other branches

    vert_gap: gap between levels of hierarchy

    vert_loc: vertical location of root

    xcenter: horizontal location of root
    '''
    if not nx.is_tree(G):
        raise TypeError('cannot use hierarchy_pos on a graph that is not a tree')

    if root is None:
        if isinstance(G, nx.DiGraph):
            root = next(iter(nx.topological_sort(G)))  #allows back compatibility with nx version 1.11
        else:
            root = random.choice(list(G.nodes))

    def _hierarchy_pos(G, root, width=1., vert_gap = 0.2, vert_loc = 0, xcenter = 0.5, pos = None, parent = None):
        '''
        see hierarchy_pos docstring for most arguments

        pos: a dict saying where all nodes go if they have been assigned
        parent: parent of this branch. - only affects it if non-directed

        '''

        if pos is None:
            pos = {root:(xcenter,vert_loc)}
        else:
            pos[root] = (xcenter, vert_loc)
        children = list(G.neighbors(root))
        if not isinstance(G, nx.DiGraph) and parent is not None:
            children.remove(parent)  
        if len(children)!=0:
            dx = width/len(children) 
            nextx = xcenter - width/2 - dx/2
            for child in children:
                nextx += dx
                pos = _hierarchy_pos(G,child, width = dx, vert_gap = vert_gap, 
                                    vert_loc = vert_loc-vert_gap, xcenter=nextx,
                                    pos=pos, parent = root)
        return pos


    return _hierarchy_pos(G, root, width, vert_gap, vert_loc, xcenter)
```


```python
import matplotlib.pyplot as plt
import networkx as nx
import re





def deversepile(p1,p2):
    while p1!=[]:
        p2.append(p1.pop())
    return p2

def npiTree(L):
    """transforme l'expression NPI en un dictionnaire
    respectant les priorités de calcul
    Attention : la liste doit d'abord être mise à l'envers
    Utilise un algorithme recursif
    
    Params :
    --------
    L : list : expression NPI
    Returns : 
    ---------
    dictionnaire 
    
    exemple : 
    ---------
    [7,8,'-',6,'*',10,3,'+','*'] => {'*': ({'*': ({'-': (7, 8)}, 6)}, {'+': (10, 3)})}
    """
    #print('npiTree')
    if len(L)==1: # condition d'arret de l'appel recursif
        return L[0]
    fg = L.pop()
    fd = L.pop()
    pere = L.pop()
    #print('L : {}'.format(L))
    D={}
    if pere in ['*','+','-']: # données sous la forme : 'op',fg,fd
        D[pere]=fg,fd
        L.append(D)
    else : # données sous la forme : 'op0',('op1',fg1,fd1),fg0 => 'op0',fg0,fg0
        fg0 = fg
        fg1 = fd
        fd1 = pere
        pere1 = L.pop()
        D[pere1]=fg1,fd1
        L.append(D)
        L.append(fg0)
    #print('L : {}'.format(L))
    return npiTree(L)

def makeTree(L_NPI):
    """transforme liste issue d'une NPI
    en un dictionnaire D
    La liste est d'abord mise à l'envers avec deversepile
    puis on appelle la fonction npiTree
    Params :
    --------
    L_NPI : liste
    Returns :
    ---------
    D : dictionnaire à transformer en graphe
    """
    D={}
    p1 = []
    deversepile(L_NPI,p1) 
    D = npiTree(p1)
    return D

def decoupe(texte):
    """transforme la chaine de caractere correspondant au dictionnaire de l'arbre
    en une liste
    Params : 
    --------
    texte : string : la chaine à découper
    Returns :
    ---------
    texte_decoupe : la liste
    """
    texte_decoupe = list(re.findall('[{}():,*+-]|\w+',texte))
    return texte_decoupe

def creerNodes(D):
    """modifie la liste ou chaque item (valeur numerique ou operateur) est remplacé par le no de noeud
    on créé aussi le noeud et son etiquette à partir de l'item
    Params : 
    --------
    D : dict : dictionnaire correspondant a l'arbre
    Returns :
    ---------
    eval(chaine) : dict : dictionnaire avec les no de noeud à la place des items
    """
    texte = decoupe(str(D))
    index = 1
    for i,c in enumerate(texte):
        if c[0] in ['*','+','-','0','1','2','3','4','5','6','7','8','9']:
            G.add_node(index,label=c)
            texte[i]=str(index)
            index+=1
    chaine = ''.join(texte)        
    return eval(chaine)


def createEdges(D,key0=None):
    """créé une liste de tuple correspondant aux aretes de l'arbre
    l'algorithme utilise un parcours en profondeur recursif et ajoute la nouvelle arete
    à une liste LL
    Params : 
    --------
    D : dict : represente l'arbre à parcourir
    key0 : list ou int : le noeud parent
    Returns : 
    ---------
    LL[0] : contient un seul element : la liste de toutes le aretes
    tous les operateurs sont mis dans une liste de 1 élément. Il faudra sortir ces elements de la liste pour pouvoir 
    acceder au aretes seuls.
    """
    if not isinstance(D,dict):
        #print((key0,D))
        LL.append((key0,D))
        return LL[0]
    else:
        key = list(D.keys())
        #return key
        if key0!=None :
            #print((key0,key))
            LL.append((key0,key))

    createEdges(D[key[0]][0],key)
    createEdges(D[key[0]][1],key)
    



def graphDict(D):
    """construction du graphe G au format de la lib networkx
    et affiche le graphe
    Params : 
    --------
    D : dict issu de la chaine NPI ou autre
    Returns :
    ---------
    G : graphe format networkx
    
    
    """
    Dnum =creerNodes(D)
    

    global LL # necessaire pour utiliser LL dans la fonction createEdges recursive
    LL=[]
    createEdges(Dnum)

    # arranger le format des elements de la liste d'aretes (suprimer le format list de certains elements)
    for i,c in enumerate(LL):
        c0 = c[0]
        c1 = c[1]
        if isinstance(c0,list):c0=c[0][0]
        if isinstance(c1,list):c1=c[1][0]
        c = c0,c1
        LL[i]=c
    #print(LL)   

    # Dict d'etiquette des noeuds
    liste = list(G.nodes(data='label'))
    labels_nodes = {}
    for noeud in liste:
        labels_nodes[noeud[0]]=noeud[1]
    
    #labels_nodes
    G.root = 1
    G.add_edges_from(LL)
    #print(list(G.edges()))
    pos1 = hierarchy_pos(G,G.root)    
    nx.draw(G, pos=pos1, labels=labels_nodes, with_labels=True, font_size=15, font_family='sans-serif', node_color='pink',alpha=0.9)
    plt.savefig('datas/NPI1.png')
    plt.show()
    return G
    

```


```python
# expression NPI
L3 = [7,8,'-',6,'*',10,3,'+','*']

D = makeTree(L3)
G = nx.Graph()
graphDict(D)
```


![](../images/output_3_0.png)





    <networkx.classes.graph.Graph at 0x7fc60ce94a10>




```python
list(G.nodes(data='label'))
```




    [(1, '*'),
     (2, '*'),
     (3, '-'),
     (4, '7'),
     (5, '8'),
     (6, '6'),
     (7, '+'),
     (8, '10'),
     (9, '3')]




```python
list(G.edges())
```




    [(1, 2), (1, 7), (2, 3), (2, 6), (3, 4), (3, 5), (7, 8), (7, 9)]




```python
D
```




    {'*': ({'*': ({'-': (7, 8)}, 6)}, {'+': (10, 3)})}




```python
Dnum =creerNodes(D)
Dnum
```




    {1: ({2: ({3: (4, 5)}, 6)}, {7: (8, 9)})}




```python

```
