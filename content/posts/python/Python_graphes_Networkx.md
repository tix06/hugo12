---
author: "Eric Tixidor"
date: 08-25-2020
linktitle: Python graphes Networkx
menu:
  main:
    parent: 
next: Python graphe et NPI
prev: 
title: Python graphes Networkx
weight: 11
---

# tracé de graphes avec Networkx
Les scripts suivants permettent de choisir entre plusieurs types de configuration pour tracer un graphe avec Networkx, module Python.

On pourra choisir de personaliser :

* la couleur d'un noeud
* l'etiquette des noeuds
* l'étiquette des arêtes
* le type de trait (plein ou en pointillés) des arêtes


## Déclaration du graphe



```python
import matplotlib.pyplot as plt
import networkx as nx
from numpy import array

G = nx.Graph()
# definition des noeuds
G.add_node(0,label='A',col='pink')
G.add_node(1,label='B',col='red')
G.add_node(2,label='C',col='white')
G.add_node(3,label='D',col='white')
G.add_node(4,label='E',col='white')
G.add_node(5,label='F',col='blue')
# definition des aretes
G.add_edge(0,1,weight=6,styl='dashed')
G.add_edge(0,2,weight=5,styl='solid')
G.add_edge(0,4,weight=1,styl='solid')
G.add_edge(4,1,weight=5,styl='solid')
G.add_edge(4,2,weight=1,styl='solid')
G.add_edge(4,3,weight=3,styl='solid')
G.add_edge(2,3,weight=8,styl='solid')
G.add_edge(4,5,weight=6,styl='dashed')
G.add_edge(3,5,weight=9,styl='solid')
```

## Exploration de la structure de données
### couleur des noeuds


```python
liste = list(G.nodes(data='col'))
colorNodes = {}
for noeud in liste:
    colorNodes[noeud[0]]=noeud[1]
colorNodes
```




    {0: 'pink', 1: 'red', 2: 'white', 3: 'white', 4: 'white', 5: 'blue'}



Pour les couleurs des noeuds, le format doit être en **liste** (de la taille du nombre de noeuds)


```python
colorList=[colorNodes[node] for node in colorNodes]
colorList
```




    ['pink', 'red', 'white', 'white', 'white', 'blue']



### etiquettes de noeuds
Pour les étiquettes de noeuds, le format doit être un **dictionnaire**.


```python
liste = list(G.nodes(data='label'))
labels_nodes = {}
for noeud in liste:
    labels_nodes[noeud[0]]=noeud[1]
labels_nodes
```




    {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F'}



ou bien : 


```python
labels={node:label for node,label in G.nodes(data='label')}
labels
```




    {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F'}



### labels des arêtes
format : dictionnaire. 

Utile pour les applications de type algorithme de Dijkstra.

Dans les autres cas, on pourra remplir la liste avec des guillemets : `labels_edges = {edge:'' for edge in G.edges}` 


```python
labels_edges = {}
labels_edges = {edge:G.edges[edge]['weight'] for edge in G.edges}
#labels_edges = {edge:'' for edge in G.edges}
labels_edges
```




    {(0, 1): 6,
     (0, 2): 5,
     (0, 4): 1,
     (1, 4): 5,
     (2, 4): 1,
     (2, 3): 8,
     (3, 4): 3,
     (3, 5): 9,
     (4, 5): 6}



### style du trait de l'arête
format : liste


```python
liste = list(G.edges(data='styl'))
edges_style = {}
edges_style = {edge:G.edges[edge]['styl'] for edge in G.edges}
edges_style
```




    {(0, 1): 'dashed',
     (0, 2): 'solid',
     (0, 4): 'solid',
     (1, 4): 'solid',
     (2, 4): 'solid',
     (2, 3): 'solid',
     (3, 4): 'solid',
     (3, 5): 'solid',
     (4, 5): 'dashed'}




```python
edg_style = [edges_style[node] for node in edges_style]
edg_style
```




    ['dashed',
     'solid',
     'solid',
     'solid',
     'solid',
     'solid',
     'solid',
     'solid',
     'dashed']



### Tracé du graphe


```python
# positions for all nodes
pos = nx.spring_layout(G)  

# nodes
nx.draw_networkx_nodes(G, pos, node_size=700,node_color=colorList,alpha=0.9)
               
# labels
nx.draw_networkx_labels(G, pos, labels=labels_nodes, \
                        with_labels=True,font_size=20, \
                        font_color='black', \
                        font_family='sans-serif')

# edges
nx.draw_networkx_edges(G, pos,width=1)
nx.draw_networkx_edge_labels(G, pos,width=1, edge_labels=labels_edges, style='dashed', font_color='red')



plt.axis('off')
plt.savefig('datas/fig1.png')
plt.show()
```


![png](../images/output_21_0.png)


# Utilisation d'une fonction multitracés
## fonction multigraphes


```python
def multigraphe(G,pos,name,edg=True,dashed=False):
    """
    tracé d'un graphe G à partir des options obligatoires : 
    label et col pour G.nodes : 
    G.add_node(0,label='A',col='pink')
    weight et styl pour G.edges :
    G.add_edge(0,1,weight=6,styl='dashed')
    
    Params :
    --------
    G : graphe
    
    pos : un dictionnaire qui contient les positions des différents noeuds
    obtenu à partir de : pos = nx.spring_layout(G)
          
    name : chaine de caractères finissant par l'extension .png par ex monfichier.png
    
    edg : option pour affichage des etiquettes sur les aretes
    par defaut edg vaut 'True' et l'etiquette EST affichée ('False' sinon)
    
    dashed : option pour tracer un graphe en solid + en pointillé avec l'option styl de G.edges
    """
    # liste de couleurs pour les noeuds
    liste = list(G.nodes(data='col'))
    colorNodes = {}
    for noeud in liste:
        colorNodes[noeud[0]]=noeud[1]
    colorList=[colorNodes[node] for node in colorNodes]
    # Dict d'etiquette des noeuds
    liste = list(G.nodes(data='label'))
    labels_nodes = {}
    for noeud in liste:
        labels_nodes[noeud[0]]=noeud[1]
    # Dict d'etiquette des aretes
    labels_edges = {}
    
    if edg : 
        labels_edges = {edge:G.edges[edge]['weight'] for edge in G.edges}
    else :
        labels_edges = {edge:'' for edge in G.edges}
    
    # Division en 2 des aretes : solid et dashed
    elarge = [(u, v) for (u, v, w) in G.edges(data=True) if w['styl'] == 'solid']
    esmall = [(u, v) for (u, v, w) in G.edges(data=True) if w['styl'] == 'dashed']
    
    # positions for all nodes : 
    # à mettre en parametre pour que chaque graphe ait la même disposition
    # pos = nx.spring_layout(G)  

    # nodes
    nx.draw_networkx_nodes(G, pos, node_size=700,node_color=colorList,alpha=0.9)
               
    # labels
    nx.draw_networkx_labels(G, pos, labels=labels_nodes, \
                        with_labels=True,font_size=20, \
                        font_color='black', \
                        font_family='sans-serif')

    # edges
    if dashed:
        nx.draw_networkx_edges(G, pos, edgelist=elarge,width=3)
        nx.draw_networkx_edges(G, pos, edgelist=esmall,width=3, alpha=0.5, edge_color='b', style='dashed')
        
    else :
        nx.draw_networkx_edges(G, pos,width=1)
        nx.draw_networkx_edge_labels(G, pos,width=1, edge_labels=labels_edges, font_color='red')

    plt.axis('off')
    fichier='datas/'+ name
    plt.savefig(fichier)
    plt.show()
```

## Exemples


```python
pos = nx.spring_layout(G)
pos
```




    {0: array([ 0.27974646, -0.89916229]),
     1: array([ 0.92773482, -0.4219083 ]),
     2: array([-0.56455338, -0.41641877]),
     3: array([-0.64887674,  0.39760485]),
     4: array([0.2899486 , 0.33988451]),
     5: array([-0.28399977,  1.        ])}




```python
multigraphe(G,pos,'fig1.png')
```


![png](../images/output_21_0.png)



```python
multigraphe(G,pos,'fig2.png',False)
```


![png](../images/output_22_0.png)



```python
multigraphe(G,pos,'fig3.png',False,True)
```


![png](../images/output_23_0.png)



```python
G.add_node(1,label='B',col='blue')
multigraphe(G,pos,'fig3.png',False,True)
```


![png](../images/output_24_0.png)



