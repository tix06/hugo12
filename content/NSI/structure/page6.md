---
Title: TP implementation python graphes
description: module networkx, interagir avec l'objet graphe, dessiner, parcourir
hidden: true
weight: 41
---





# Traitement des graphes en Python
## Implémenter le graphe avec la librairie networkx
Dans un [notebook python/capytale](https://capytale2.ac-paris.fr/web/c/1b0b-2960109), executer les scripts suivants et repondre aux questions.

**Rappel:**

* Anglais: *Node*; Français: Sommet (noeud)
* Anglais: *Edge*; Français: Arête

Avec la librairie *networkx*, le graphe `G` est un objet de la classe `nx.Graph`

Il se manipule avec l'attribut `nodes` et les méthodes de classe `add_node`, et `add_edge`.

Voici un exemple de graphe avec 4 noeuds, numérotés de 0 à 3:


{{< img src="../images/g5.png" >}}

```python
import matplotlib.pyplot as plt
import networkx as nx
from numpy import array
G = nx.Graph()
# definition des noeuds
G.add_node(0,label='A',col='white')
G.add_node(1,label='B',col='blue')
G.add_node(2,label='C',col='yellow')
G.add_node(3,label='D',col='red')

# definition des aretes
G.add_edge(0,1)
G.add_edge(0,2)
G.add_edge(2,3)
```

### structures de données
Pour faciliter l'interaction avec les données du graphe, on créé de nouvelles structures de données:

* `pos`, utile pour le tracé
* `edge_color`: list
* `colorNodes`: list
* `label_nodes`: dict

```python
# calcul des positions pour repartir les sommets du graphe
pos = nx.spring_layout(G)  
# sommets et couleur des sommets
L = list(G.nodes())
edge_color = list(G.nodes(data='col'))
colorNodes = [node[1] for node in edge_color]
# Afficher les etiquettes: labels
labels_nodes={node:label for node,label in G.nodes(data='label')}
```

**Question a:** Explorer chacune des séquences `L`, `edge_color`, `colorNodes` et `labels_nodes` et recopier leur valeur.



### Dessiner
Le script suivant va dessiner le graphe à partir de l'objet `G`.

```python
# nodes
plt.clf()
nx.draw_networkx_nodes(G, pos, node_size=700,node_color=colorNodes,alpha=0.9)
# labels
nx.draw_networkx_labels(G, pos, labels=labels_nodes, \
                        font_size=20, \
                        font_color='black', \
                        font_family='sans-serif')
# edges
nx.draw_networkx_edges(G, pos)

plt.axis('off')
plt.show()
```

{{< img src="../images/g5.png" >}}

**Question b**: interpreter la figure obtenue. Celle-ci était elle prévisible d'après les informations données pour implémenter le graphe?

**Question c:** Modifier maintenant la déclaration du graphe (cellule 1) pour dessiner le graphe suivant: 

{{< img src="../images/g3.png" >}}

### Interragir avec les attributs du graphe
**Question d:** On créé une liste d'adjacence à partir de l'instruction suivante:

```
liste_adjacence = [list(nx.neighbors(G,node)) for node in L]
```

* Expliquer/commenter: comment est écrite cette instruction

**Question e:** Compléter le script pour obtenir le dictionnaire représentant ce graphe: 

```python
D = {}
for node in ...:
    D[node] = ...
print (D)
```
 
*affiche:*

```
{0: [1, 2, 4],
 1: [0, 4],
 2: [0, 4, 3],
 3: [4, 2, 5],
 4: [0, 1, 2, 3, 5],
 5: [4, 3]}
 ```

 *astuce: prévoir un parcours par indice `for node in range(len(liste_adjacence))`*

 **Question f:** Créer une fonction `degre_max` qui retourne un tuple constitué du noeud de plus haut degré, et de la valeur de plus haut degré dans le graphe. Cette fonction prend pour unique paramètre le dictionnaire `D` défini plus haut.

```python
def degre_max(D):
    ...
```

*astuce: rappelez vous l'algorithme de recherche du max dans une liste, puis adaptez ce script pour le dictionnaire D. Ici, la valeur qui doit être maximale, c'est `len(D[node])`, où `node` est une clé du dictionnaire `D`*

**Question g:** L'instruction suivante génère un affichage des caractéristiques du graphe. 

```
for node in list(G.nodes()):
    print(node,'->',list(nx.neighbors(G,node)),G.nodes(data='col')[node])
```

```
0 -> [1, 2] white
1 -> [0] blue
2 -> [0, 3] yellow
3 -> [2] red
```

Obtenez le même affichage, mais cette fois en utilisant les séquences construites plus haut: `L`, `edge_color`, `colorNodes`, `labels_nodes` et `D`.

```python
for node in L:
    print(node,'->',...,...
```

# Compléments
## Caractéristiques du graphe - librairie networkx
L'objet *graphe* `G` possède des méthodes de type *Getter* et *Setter*. Nous allons explorer celles-ci.

### Fonctions utiles de `networkx`
Pour connaitre la liste des sommets et des arêtes:

```python
print(list(G.nodes()))
print(list(G.edges()))
```



La [densité](https://networkx.org/documentation/stable/reference/generated/networkx.classes.function.density.html) du graphe:

```python
nx.density(G)
``` 

Pour connaitre la liste des [voisins](https://networkx.org/documentation/stable/reference/generated/networkx.classes.function.neighbors.html) d'un sommet:

```python
nx.neighbors(G,node)
```

Pour connaitre la liste des voisins de TOUS les sommets, ainsi que leur couleur:

```python
for node in list(G.nodes()):
    print(node,'->',list(nx.neighbors(G,node)),G.nodes(data='col')[node])
```

> **Q.a:** Compléter le script pour obtenir le dictionnaire représentant ce graphe:

```python
D = {}
for node in list(G.nodes()):
	# a completer
print (D)
```
 
*affiche:*

```
{0: [1, 2, 4],
 1: [0, 4],
 2: [0, 4, 3],
 3: [4, 2, 5],
 4: [0, 1, 2, 3, 5],
 5: [4, 3]}
 ```

### Getter
La documentation de la fonction se trouve [ici: networkx.org/documentation](https://networkx.org/documentation/stable/reference/generated/networkx.classes.function.get_node_attributes.html)

Tester dans une nouvelle cellule:

```python
color = nx.get_node_attributes(G, "col")
print('color',color)
```

> **Q.b:** Quel est le format de données retourné par `get_node_attributes`?

> **Q.c:** Afficher la seule couleur du sommet 0, en modifiant cette instruction.

> **Q.d:** Obtenir l'information des attributs *label* à l'aide d'une instruction similaire.

### Setter
La documentation de la fonction se trouve [ici: networkx.org/documentation](https://networkx.org/documentation/stable/reference/generated/networkx.classes.function.set_node_attributes.html)

Tester dans une nouvelle cellule:

```python
nx.set_node_attributes(G, {0:{"col":'blue'}})
color = nx.get_node_attributes(G, "col")
print('color',color)
```

> **Q.e:** Que remarque t-on? Pourquoi?

## Algorithmes de parcours de graphes
Pour une description illustrée de ces 2 parcours dans un graphe, on pourra consulter la page [suivante sur le site allophysique.com](/docs/SNT_2nde/pages/pages_algo/graphes/page2/).

La page [suivante du site marcarea.com](https://marcarea.com/weblog/2019/02/17/parcours-de-graphes-en-python) propose plusieurs implémentations pour les parcours en *largeur* et en *profondeur* d'un graphe.

* Pour utiliser l'une de ces fonctions, il faudra une structure de données de type *dictionnaire* pour le graphe: revoir le paragraphe *Fonctions utiles de networkx*.

* Ajouter une fonction pour dessiner et sauvegarder le graphe dans un fichier:

```python
def dessine(G,filename):
    plt.clf()
    L = list(G.nodes(data='col'))
    colorNodes = [node[1] for node in L]
    nx.draw_networkx_nodes(G, pos, node_size=700, node_color=colorNodes, alpha=0.9)

    # labels
    labels_nodes = {node: label for node, label in G.nodes(data='label')}

    nx.draw_networkx_labels(G, pos, labels=labels_nodes, \
                            font_size=20, \
                            font_color='black', \
                            font_family='sans-serif')

    nx.draw_networkx_edges(G, pos)
    plt.savefig(filename)
```

* Adapter ensuite la fonction de recherche pour tracer les graphes au fur et à mesure du parcours. Démarrer du sommet 0:

```python
plt.figure() # utile pour afficher TOUS les graphes
recursive_dfs(D,0)
```

{{< img src="../images/g4.png" >}}

# Correction




```python
import matplotlib.pyplot as plt
import networkx as nx
from numpy import array

def inverse(L):
    return [L[i] for i in range(len(L)-1,-1,-1)]

def dessine(G,filename):
    plt.clf()
    L = list(G.nodes(data='col'))
    colorNodes = [node[1] for node in L]
    nx.draw_networkx_nodes(G, pos, node_size=700, node_color=colorNodes, alpha=0.9)

    # labels
    labels_nodes = {node: label for node, label in G.nodes(data='label')}

    nx.draw_networkx_labels(G, pos, labels=labels_nodes, \
                            font_size=20, \
                            font_color='black', \
                            font_family='sans-serif')

    nx.draw_networkx_edges(G, pos)
    plt.savefig(filename)



G = nx.Graph()
# definition des noeuds
G.add_node(0, label='A', col='white')
G.add_node(1, label='B', col='white')
G.add_node(2, label='C', col='white')
G.add_node(3, label='D', col='white')
G.add_node(4, label='E', col='white')
G.add_node(5, label='F', col='white')
# definition des aretes
G.add_edge(0, 1)
G.add_edge(0, 2)
G.add_edge(0, 4)
G.add_edge(4, 1)
G.add_edge(4, 2)
G.add_edge(4, 3)
G.add_edge(2, 3)
G.add_edge(4, 5)
G.add_edge(3, 5)

# calcul des positions pour repartir les sommets du graphe
pos = nx.spring_layout(G)

# Dictionnaire du graphe
D = {}
for node in list(G.nodes()):
    D[node] = list(nx.neighbors(G, node))
print(D)

# Parcours en profondeur avec coloration des sommets
def dfs(graph, node, visited=None,stack=None):
    compteur_image=0
    if visited is None:
        visited = []
    if stack is None:
        stack = []
    stack.append(node)
    nx.set_node_attributes(G, {node: {"col": 'green'}})
    dessine(G, 'img/figure' + str(compteur_image) + '.png')
    compteur_image+=1
    while stack:
        node = stack.pop()

        if node not in visited :
            #and G.nodes()[node]['col'] != 'red':
            visited.append(node)

            #plt.show()
            unvisited = [n for n in graph[node] if n not in visited]
            stack.extend(inverse(unvisited))
            for n in unvisited :
                nx.set_node_attributes(G, {n: {"col": 'green'}})
            dessine(G, 'img/figure' + str(compteur_image) + '.png')
            compteur_image += 1
            nx.set_node_attributes(G, {node: {"col": 'red'}})
            dessine(G,'img/figure'+str(compteur_image)+'.png')
            compteur_image += 1
    #plt.show()

    return visited


# appel de dfs depuis le sommet 0 et affichage graphique
#plt.figure()
visited = dfs(D, 0)

print(visited)
```


# Liens
* Documentation de [python networkx](https://networkx.org)
* Programmes python pour le parcours [en largeur et en profondeur d'un graphe](https://marcarea.com/weblog/2019/02/17/parcours-de-graphes-en-python)





