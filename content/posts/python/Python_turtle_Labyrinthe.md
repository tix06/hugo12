---
author: "Eric Tixidor"
date: 08-25-2020
linktitle: Python turtle Labyrinthe
menu:
  main:
    parent: 
next: 
prev: 
title: Python turtle Labyrinthe
weight: 13
---

# Utiliser le module turtle
Le script suivant présente les classes et fonctions utiles pour : 

* tracer un labyrinthe complet
* parcourir le labyrinthe selon une méthode de parcours en profondeur
* tracer ce parcours animé avec turtle

**Utilisation :**

```python
tab=labyrinthe(5,6)

L = parcours((len(tab)-1,0),(0,len(tab[0])-1),tab)

afficheTurtle(tab,L)
```

## librairies


```python
from numpy.random import randint
import matplotlib.pyplot as plt
import turtle
```

## classes utiles


```python
class Pile:
    def __init__(self):
        self.lst = [] 
    
    def empty(self):
        return self.lst == [] 
    
    def push(self, x):
        self.lst.append(x)

    def pop(self):
        if self.empty():
            raise ValueError("pile vide") 
        return self.lst.pop()
"""    
def explorer(laby): 
    pile = Pile()
    pile.push((0, laby.q - 1)) 
    laby.tab[0][laby.q - 1].etat = False 
    while True:
        i, j = pile.pop()
        if i == laby.p - 1 and j == 0:
            break
        if j > 0 and laby.tab[i][j].S and laby.tab[i][j-1].etat:
            pile.push((i, j)) 
            pile.push((i, j-1)) 
            laby.tab[i][j-1].etat = False
        elif i < laby.p-1 and laby.tab[i][j].E and laby.tab[i+1][j].etat: 
            pile.push((i, j))
            pile.push((i+1, j))
            laby.tab[i+1][j].etat = False
        elif j < laby.q-1 and laby.tab[i][j].N and laby.tab[i][j+1].etat: 
            pile.push((i, j))
            pile.push((i, j+1))
            laby.tab[i][j+1].etat = False
        elif i > 0 and laby.tab[i][j].W and laby.tab[i-1][j].etat: 
            pile.push((i, j))
            pile.push((i-1, j))
            laby.tab[i-1][j].etat = False
    return pile.lst
"""    
class Case:
    def __init__(self):
        self.N = False 
        self.W = False 
        self.S = False 
        self.E = False 
        self.etat = False

class Labyrinthe:
    def __init__(self, p, q):
        self.p = p
        self.q = q
        self.tab = [[Case() for j in range(q)] for i in range(p)]
    
    def show(self):
        plt.plot([0, 0, self.p, self.p, 0], [0, self.q, self.q, 0, 0], linewidth=2) 
        for i in range(self.p-1):
            for j in range(self.q):
                if not self.tab[i][j].E:
                    plt.plot([i+1, i+1], [j, j+1], 'b') 
        for j in range(self.q-1):
            for i in range(self.p):
                if not self.tab[i][j].N:
                    plt.plot([i, i+1], [j+1, j+1], 'b') 
        
        plt.axis([-1, self.p+1, -1, self.q+1])
        plt.show()
    """
    def solution(self):
        sol = explorer(self) 
        X, Y = [], []
        for (i, j) in sol:
            X.append(i+.5)
            Y.append(j+.5) 
        X.append(self.p-.5)
        Y.append(.5)
        plt.plot(X, Y, 'r', linewidth=2) 
        self.show()
    """
def creation(p, q):
    laby = Labyrinthe(p, q)
    pile = Pile()
    i, j = randint(p), randint(q) 
    pile.push((i, j)) 
    laby.tab[i][j].etat = True 
    while not pile.empty():
        i, j = pile.pop()
        v = []
        if j < q-1 and not laby.tab[i][j+1].etat:
            v.append('N')
        if i > 0 and not laby.tab[i-1][j].etat:
            v.append('W')
        if j > 0 and not laby.tab[i][j-1].etat:
            v.append('S')
        if i < p-1 and not laby.tab[i+1][j].etat:
            v.append('E') 
        if len(v) > 1:
            pile.push((i, j)) 
        if len(v) > 0:
            c = v[randint(len(v))] 
            if c == 'N':
                laby.tab[i][j].N = True
                laby.tab[i][j+1].S = True
                laby.tab[i][j+1].etat = True 
                pile.push((i, j+1))
            elif c == 'W':
                laby.tab[i][j].W = True 
                laby.tab[i-1][j].E = True 
                laby.tab[i-1][j].etat = True 
                pile.push((i-1, j))
            elif c == 'S':
                laby.tab[i][j].S = True 
                laby.tab[i][j-1].N = True 
                laby.tab[i][j-1].etat = True 
                pile.push((i, j-1))
            else:
                laby.tab[i][j].E = True 
                laby.tab[i+1][j].W = True 
                laby.tab[i+1][j].etat = True 
                pile.push((i+1, j))
    return laby
```

## autres definitions utiles


```python
def directions(laby,i,j):
    """les directions possibles pour la case courante
    i : int numero de ligne
    j : numero de la colonne
    
    retourne une liste (tuple) des points cardinaux possibles
    """
    L = []
    if laby.tab[j][i].N == True: L.append('N')
    if laby.tab[j][i].S == True: L.append('S')
    if laby.tab[j][i].E == True: L.append('E')
    if laby.tab[j][i].W == True: L.append('W')
    return tuple(L)

def labyrinthe(lines,col):
    """
    Params : 
    --------
    lines : int : nombre de lignes du labyrinthe
    col : int : nombre de colonnes
    
    Returns : 
    ---------
    tab2 : list : tuples de 1 à 4 éléments correspondants aux directions libres ('N', 'S', E', 'W')
    sortie : tracé du labyrinthe
    
    Variables :
    -----------
    p : nombre de colonnes (=largeur)
    q : nombre de lignes (=hauteur)
    """
    laby = creation(col, lines)
    tab2 = [[0]*laby.p for i in range(laby.q)]
    for i in range(laby.q):
        for j in range(laby.p):
            tab2[i][j] = directions(laby,i,j)
    Labyrinthe.show(laby)
    return tab2

def nexto(c,direc):
    """retourne les coordonnées lors du deplacement
    selon la position actuelle et la direction
    Params :
    --------
    c : tuple (ligne,colonne) correspondant à (y,x) dans le plan cartesien
    direct : str : 'N', 'S', E', 'W'
    
    Returns :
    ---------
    tuple : (int,int) correspondant à (ligne,colonne)
    """
    i,j = c[0],c[1]
    if direc=='N' : return (i+1,j)
    if direc=='S' : return (i-1,j)
    if direc=='E' : return (i,j+1)
    if direc=='W' : return (i,j-1)

def visited(c,L,couleur):
    """retourne la couleur du noeud de coord c et 
    de liste de directions possibles L selon celle de ses voisins
    
    Params : 
    --------
    c : tuple : (ligne,colonne) correspondant à (y,x) dans le plan cartesien
    L : list : tuples de 1 à 4 éléments correspondants aux directions libres ('N', 'S', E', 'W')
    couleur : List dimension 2 contenant des elements str
              'white' si noeud non visité, 
              'green' si le noeud est en cours de visite, 
              'red' si tous les noeuds ont été visités autour de lui
    Returns : 
    ---------
    couleur : str : 'green' si le noeud est en cours de visite, 'red' si tous les noeuds 
              ont été visités autour de lui
    """
    i,j = c[0],c[1]
    coul='red'
    for direc in L:
        coord = nexto(c,direc)
        if couleur[coord[0]][coord[1]]=='white':coul='green'
    #print(c,coul)
    return coul
    
def parcours(start,end,tab):
    """trouve la solution au labyrinthe et trace ce chemin
    p : Pile() utile pour la recherche du parcours
    pchemin : Pile() utile pour memoriser tout le chemin
    on insère dans le chemin toutes les arêtes empruntées : 
    pour le chemin entre c1 et c2, on insère c1 puis c2
    """
    p = Pile()
    pchemin = Pile()
    p.push(start)
    c = start
    couleur = [['white']*len(tab[0]) for i in range(len(tab))]
    
    
    while (not p.empty()) and (not c == end):
        c = p.pop()
        pchemin.push(c) # chaque fois que l'on depile, on rempile dans pchemin
        L = tab[c[0]][c[1]]
        couleur[c[0]][c[1]]=visited(c,L,couleur) # c est retiré de la pile et coloré en green ou red
        
        
            
        for direc in L:
            coord = nexto(c,direc)
            if couleur[coord[0]][coord[1]]=='white': # le noeud fils est coloré en blanc dans la direction D
                    p.push(c) # on remet le noeud parent afin de reconsidérer sa couleur à chaque fois que l'on depile
                    # et le chemin arriere CONTINU pour le tracé
                    p.push(coord) 
                    # alors on ajoute le noeud fils dans la direction D au sommet de la pile
                    
    return pchemin.lst
```

## fonctions particulières au module turtle


```python
def turtleWall(dir,i,j):
    """trace les murs des directions fermées
    dir est un tuple contenant les directions libres
    """
    larg = len(tab[0])
    haut = len(tab)

    fenX = 600
    fenY = fenX*haut/larg

    scaleX = (fenX-20)/larg
    scaleY = (fenY-20)/haut

    x0=-fenX/2+10
    y0=-fenY/2+10
    
    if not('N' in dir[i][j]) :
        turtle.penup()
        turtle.setpos(x0+j*scaleX,y0+(i+1)*scaleY)
        turtle.setheading(0)
        turtle.pendown()
        turtle.forward(scaleX)
    if not('S' in dir[i][j]) : 
        turtle.penup()
        turtle.setpos(x0+j*scaleX,y0+i*scaleY)
        turtle.setheading(0)
        turtle.pendown()
        turtle.forward(scaleX)
    if not('E' in dir[i][j]) : 
        turtle.penup()
        turtle.setpos(x0+(j+1)*scaleX,y0+i*scaleY)
        turtle.setheading(90)
        turtle.pendown()
        turtle.forward(scaleY)
    if not('W' in dir[i][j]) : 
        turtle.penup()
        turtle.setpos(x0+j*scaleX,y0+i*scaleY)
        turtle.setheading(90)
        turtle.pendown()
        turtle.forward(scaleY)
        
def turtleLab(tab):
    for i in range(len(tab)):
        for j in range(len(tab[i])):
            turtleWall(tab,i,j)
    #plt.plot([0, 0, len(tab[0]), len(tab[0]), 0], [0, len(tab), len(tab), 0, 0], 'blue',linewidth=10)
    #plt.savefig('laby.png')

def turtlePath(tab,L):
    """tracé du parcours dans le labyrinthe à l'aide de la tortue
    Params:
    -------
    tab : Liste de liste contenant des str : 'N','S','W','E' = le labyrinthe
    L : Liste de tuples correspondant aux cases visitées
    sortie : 
    --------
    le dessin du parcours animé
    """
    larg = len(tab[0])
    haut = len(tab)

    fenX = 600
    fenY = fenX*haut/larg

    scaleX = (fenX-20)/larg
    scaleY = (fenY-20)/haut

    x0=-fenX/2+10
    y0=-fenY/2+10
    
    turtle.penup()
    turtle.pencolor("red")
    turtle.setpos(x0+scaleX/2,y0+scaleY*4+scaleY/2) # depart
    turtle.showturtle()
    turtle.pendown()
    start = L[0]
    for c in L[1:]:
        #angle = 90*(c[0]-start[0]) # si deplacement uniquement vertical
        if c[0]!=start[0] : 
            depl = scaleY # vertical
            angle = 90*(c[0]-start[0])
        else : 
            depl = scaleX # horizontal
            angle = 90 - 90*(c[1]-start[1])
        if c[1]<start[1] : angle = 180 # deplacement à gauche
        turtle.setheading(angle)
        turtle.forward(depl)
        start = c
```

## fonction principale pour affichage de l'animation turtle


```python
def afficheTurtle(tab,L):
    larg = len(tab[0])
    haut = len(tab)

    fenX = 600
    fenY = fenX*haut/larg

    scaleX = (fenX-20)/larg
    scaleY = (fenY-20)/haut
    turtle.setup(fenX, fenY)  #Largeur : 600px, Hauteur : 400px

    turtle.bgcolor((0.9, 0.9, 0.9))
    turtle.hideturtle()
    turtle.penup()
    turtle.setpos(-fenX/2+10,-fenY/2+10)
    turtle.setheading(90)

    turtle.pendown()
    #turtle.speed(0)
    turtle.tracer(False) # tracer le Laby avant de demarrer l'animation avec la tortue
    turtle.pensize(2)

    turtle.forward(fenY-20)
    turtle.left(-90)
    turtle.forward(fenX-20)
    turtle.left(-90)
    turtle.forward(fenY-20)
    turtle.left(-90)
    turtle.forward(fenX-20)
    turtle.left(-90)

    turtleLab(tab)

    turtle.tracer(True) # fin du tracé du Laby

    turtle.speed(6)

    turtlePath(tab,L) # animation du parcours par la tortue




    #calling for the mainloop()
    turtle.mainloop()
```

## Programme


```python
tab=labyrinthe(5,6)

L = parcours((len(tab)-1,0),(0,len(tab[0])-1),tab)

afficheTurtle(tab,L)
```


![gif](../images/turt.gif)


