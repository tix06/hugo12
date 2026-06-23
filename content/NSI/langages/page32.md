---
Title: correction des exercices en ligne sur POO
hidden: true
weight: 19
--- 

# Correction des exercices
## Exercice 1

```python
class Sept_Familles:
    """
    NAME
        Sept_Familles
    DESCRIPTION
        constructeur pour les cartes du jeu
    PARAMETERS
        famille (str): nom de la famille
            choix parmi ('Jongleurs','Acrobates','Dresseurs','...')
        membre_famille(str): membre de la famille 
            choix parmi ('Grand-père','Grand-mère','Pére','Mère','Fils','Fille')
    FUNCTIONS
        get_Attributs
    """
    def __init__(self,famille,qui):
        self.famille = famille
        self.membre_famille = qui
        
    def get_Attributs(self):
        return self.famille,self.membre_famille
    
    def __repr__(self):
        return "La carte est de la famille des {} C'est le {}".format(self.famille,self.membre_famille)
    

carte1 = Sept_Familles('Jongleurs','Grand-père')
carte2 = Sept_Familles('Jongleurs','Fille')
carte3 = Sept_Familles('Musiciens','Père')
carte4 = Sept_Familles('Musiciens','Fille')
```

En console:

```
>>> print(carte1)
la carte est de la famille des Jongleurs. C'est le Grand-père
```

## Exercice 2
Compléter la classe Joueur avec les méthodes:

```python
class Joueur:
    def __init__(self,*args):
        self.C = []
        for i in args:
            self.C.append(i.get_Attributs())
    
    def possede(self,carte):
        return carte in self.C
    
    def donne(self,carte):
        self.C.remove(carte)
    
    def demande(self, joueur, carte):
        if joueur.possede(carte):
            self.C.append(carte)
            joueur.donne(carte)
            print("Il a la carte "+str(carte)+ " et la donne")
            print(joueur1)
            print(joueur2)
        else:
            return "pioche"
    
    def __repr__(self):
        return "joueur possède les cartes :"+str(self.C)
    
```

Puis tester en console:

```
>>> joueur1 = Joueur(carte1,carte2)
>>> joueur2 = Joueur(carte2,carte3)
>>> print(joueur1)
le joueur possède les cartes : [('Jongleurs', 'Grand-père'), ('Jongleurs', 'Fille')]
>>> joueur2.demande(joueur1,('Jongleurs','Grand-père'))
Il a la carte ('Jongleurs', 'Grand-père') et la donne
joueur possède les cartes :[('Jongleurs', 'Fille')]
joueur possède les cartes :[('Jongleurs', 'Fille'), ('Musiciens', 'Père'), ('Jongleurs', 'Grand-père')]
>>> joueur2.demande(joueur1,('Jongleurs','Grand-mère'))
pioche
>>> joueur2.demande(joueur1,carte2.get_Attributs())
Il a la carte ('Jongleurs', 'Fille') et la donne
joueur possède les cartes :[]
joueur possède les cartes :[('Jongleurs', 'Fille'), ('Musiciens', 'Père'), ('Jongleurs', 'Grand-père'), ('Jongleurs', 'Fille')]
```