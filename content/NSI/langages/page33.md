---
Title: Jeu de dominos
description: POO, jeu de dominos, liste chainee,  interaction entre objets de 2 classes
hidden: true
weight: 20
---

**Editeur**: Notebook sur [CAPYTALE](https://capytale2.ac-paris.fr/web/c/e3a0-4866533)

# jeu de Dominos et POO - version classique
Le jeu de *Dominos* est un jeu très simple, ou, pour gagner, il faut être le premier joueur à avoir posé tous ses dominos.
Une fois le premier domino placé sur la table, le joueur suivant doit à son tour poser un domino ayant le même nombre de points sur au moins un côté du domino précédemment posé. Voir la règle du jeu [ici](https://www.agoralude.com/blog/la-regle-du-jeu-de-dominos-n33)

Un domino est constitué de côtés, droite/gauche ou haut/bas selon comment la pièce sera disposée.



{{< img src="../images/domino1.jpg" caption="un début de partie" >}}

La disposition importe peu: il faut que la chaine reste ouverte.



{{< img src="../images/domino2.png" caption="Exemple de disposition juste (à gauche) et fausse (à droite)" >}}

Dans cette simulation de jeu, on supposera: 

* que le joueur joue seul
* et qu'il est possible d'insérer un Domino en l'intercalant entre 2 Dominos déjà posés, à condition qu'il s'agisse d'un Domino double. (1:1) par exemple peut être posé entre (5:1) et (1:6)

On utilise la définition de classes suivantes:

```python
class Domino:
    def __init__(self,val1,val2):
        self.val1 = val1
        self.val2 = val2
        self.suiv = None

    
class Partie:
    def __init__(self,first):
        self.first = first
        
    def last(self):
        """parcours de la liste chainee jusqu'a la fin
        return: str, valeurs du dernier domino sous la forme
        val1:val2
        """
        M = self.first
        while not M.suiv is None:
            M = M.suiv
        return '{}:{}'.format(M.val1,M.val2)
        
    def atteindre_domi(self,val2):
    	"""docstring a ajouter
    	"""
        D = self.first
        while not D.suiv is None and D.val2 != val2:
            D = D.suiv
        if D.val2 == val2:
            # domino trouve
            return D
        else:
            # domino non trouve, retourne False
            return False   
            
    def inserer(self,D_a_inserer):
    		"""insere le domino D_a_inserer a la premiere place possible
            dans le jeu
            param:
            D_a_inserer est une instance de la classe Domino. Il s'agit d'un domino double: D_a_inserer.val1 == D_a_inserer.val2

            exemple d'utilisation:
            etat de la partir avant insertion
            4:3=>3:2=>2:1
            on insere le domino D4 de valeur 3:3 en trouvant sa place
            dans la partie
            >>> partie.inserer(D4)
            etat de la partie apres insertion
            4:3=>3:3=>3:2=>2:1
            """
            #à completer

    def __repr__(self):
        M = self.first
        s = '{}:{} '.format(M.val1,M.val2)
			# à completer
        return s
```

**Qu a.** On cherche à modéliser la partie de l'image de gauche (voir plus haut).
Les dominos seront instanciés à l'aide des noms D1, D2, D3, ... Ecrire les instructions qui instancient tous les dominos de la partie, avec, pour chacun, leurs valeurs et le domino suivant.

**Qu b.** Ecrire l'instruction qui doit créer l'objet `partie1` à partir de ce plateau de jeu. (classe `Partie`)

**Qu c.** Compléter la méthode de classe `__repr__` qui surcharge la fonction `print`

**Qu d.** Commenter la méthode de classe `atteindre_domi`. A quoi sert-elle? Quelle est sa complexité asymtotique?

**Qu e.** Imaginons que l'état de la partie soit celui-ci:

```python
print(partie1)
4:4 => 4:6 => 6:1 => 1:5 => 5:4 => 4:2 => 2:1 => 1:3 
```

> Compléter la méthode de classe `inserer` qui permet d'insérer un domino (double) dans la chaine de dominos à partir des instructions suivantes:

```python
D = partie1.atteindre_domi(2)
D10 = Domino(2,2)
partie1.inserer(D10)
```

> Le nouvel état de la partie devrait alors être :

```python
print(partie1)
4:4 => 4:6 => 6:1 => 1:5 => 5:4 => 4:2 => 2:2 => 2:1 => 1:3 
```

**Qu f.** Insérer le domino `1:1` à sa place, dans la partie.

**Qu g.** Ajouter une méthode de classe `poser` qui pose un domino à la suite du dernier domino posé dans la partie, à condition que celui-ci soit bien en correspondance. La fonction va alors retourner l'état de la partie (si le nouveau domino peut être posé), ou bien un message signifiant que la pose est interdite. Tester votre methode de classe `poser` en choisissant un domino correct, puis un domino non correct.

# Corrections

## Jeu de dominos *classique*

```python
class Domino:
    def __init__(self,val1,val2):
        self.val1 = val1
        self.val2 = val2
        self.suiv = None

    
class Partie:
    def __init__(self,first):
        self.first = first
        
    def last(self):
        """parcours de la liste chainee jusqu'a la fin
        return: str, valeurs du dernier domino sous la forme
        val1:val2
        """
        M = self.first
        while not M.suiv is None:
            M = M.suiv
        return '{}:{}'.format(M.val1,M.val2)
        
    def atteindre_domi(self,val2):
        """docstring a ajouter
        """
        D = self.first
        while not D.suiv is None and D.val2 != val2:
            D = D.suiv
        if D.val2 == val2:
            # domino trouve
            return D
        else:
            # domino non trouve, retourne False
            return False   
            
    def inserer(self,D_a_inserer):
            """insere le domino D_a_inserer a la premiere place possible
            dans le jeu
            param:
            D_a_inserer est une instance de la classe Domino. Il s'agit d'un domino double: D_a_inserer.val1 == D_a_inserer.val2

            exemple d'utilisation:
            etat de la partir avant insertion
            4:3=>3:2=>2:1
            on insere le domino D4 de valeur 3:3 en trouvant sa place
            dans la partie
            >>> partie.inserer(D4)
            etat de la partie apres insertion
            4:3=>3:3=>3:2=>2:1
            """
            if self.atteindre_domi(D_a_inserer.val2):
                D = self.atteindre_domi(D_a_inserer.val2)
                D_a_inserer.suiv = D.suiv
                D.suiv = D_a_inserer
                return self.__repr__()
            else:
                return "insertion impossible"

    def poser(self,D_a_poser):
            D = self.first
            while not D.suiv is None:
                D = D.suiv 
            if D.val2 == D_a_poser.val1:
                D.suiv = D_a_poser
                return self.__repr__()
            else:
                return "pose impossible"

    def __repr__(self):
        M = self.first
        s = '{}:{} '.format(M.val1,M.val2)
        while not M.suiv is None:
            M = M.suiv
            s += '=> {}:{} '.format(M.val1,M.val2)
        return s

                
D1 = Domino(4,4)
D2 = Domino(4,6)
D3 = Domino(6,1)
D4 = Domino(1,5)
D5 = Domino(5,4)
D6 = Domino(4,2)
D7 = Domino(2,1)
D8 = Domino(1,3)
D9 = Domino(1,1) # domino double pour insertion
D10 = Domino(3,6) # domino correct pour pose apres D8
D11 = Domino(5,3) # domino incorrect pour pose
D1.suiv = D2
D2.suiv = D3
D3.suiv = D4
D4.suiv = D5
D5.suiv = D6
D6.suiv = D7
D7.suiv = D8
partie1 = Partie(D1)
```

puis les différents tests des méthodes de Partie:

```python
>>> partie1.inserer(D9)
>>> partie1.poser(D10)
>>> partie1.poser(D11)
```


**La suite en TP**

* TP Jeu des 7 familles: [Lien](../page34/) *(Sans interface graphique)*
* TP sur trajectoires de projectiles: [Lien](../page31/) 
* TP sur la programmation d'un jeu de Dominos: [Lien](../page33/). *(Sans interface graphique)*
* TP (projet) jeu de Dominos avec interface graphique: [Lien](/docs/NSI/projet/page4/)

