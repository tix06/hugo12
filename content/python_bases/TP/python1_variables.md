---
Title : jeu de rôle en console
---

# TP python: Jeu de Rôle
Le but de ce TP est de créer un jeu avec une interface TEXTUELLE
## Rappels de classe de 1ere NSI
### Les entrées et sorties
voir le cours à la page [https://lyceum.fr/1g/nsi/7-langages-et-programmation/3-entrees-et-sorties](https://lyceum.fr/1g/nsi/7-langages-et-programmation/3-entrees-et-sorties)


### texte formaté
On peut ajouter le contenu d'une variable dans du texte. Il faut pour cela utiliser un formatage. Les symboles `{}` devront se trouver à l'emplacement de la variable à disposer dans le texte : 

Exemple : (executer la cellule suivante)


```python
n = 18
texte = 'je viens d\'avoir {} ans'.format(n)
print(texte)
```

### Listes
Avec la liste suivante : 
```
mois = ['janvier','fevrier','mars','avril','mai','juin','juillet','aout']
```

1. compléter la liste des mois de l'année (utiliser l'une des méthodes de liste)


```python

```

2. Quelle instruction, utilisant un indice numerique va retourner le mois 'juin' ?


```python

```

3. Quelle instruction permettra de retourner la liste suivante, découpée à partir de celle `mois`? :

```
['juillet','aout']
```


```python

```

4. Utiliser une expression formatée utilisant `mois` pour afficher le texte : 

*Le mois de juin est celui du début de l'été.*  


```python

```

### Dictionnaire
Soit un dictionnaire : `dico = {1:2,3:4}` ayant pour couples:

* clé 1 : valeur 2
* clé 3 : valeur 4

Pour accéder à la valeur 2, il faut faire : 

```
dico[1]
```

Et pour accéder à la valeur 2, il faut faire : 

```
dico[3]
```

Le type des clés et des valeurs peut être différent d'un entier : il peut s'agit d'une chaine de caractère, mais aussi d'une liste, d'un tuple, d'un autre dictionnaire...

**Exercice :**
Avec le dictionnaire : 
```
dico = {1:2,3:{4:5}}
```
1. Trouver l'expression qui aura pour valeur : 5


```python

```

Même exercice, mais on dispose maintenant du dictionnaire : 
```
dico = {'1':'2','3':{'4':'5'}}`
```

2. Trouver l'expression qui aura pour valeur, **l'entier** 5


```python

```

On dispose d'un dictionnaire de nom `laby` contenant les données suivantes : 
```
laby = {1:{2:{3:9,5:6},7:8}}
```

3. Ecrire une série d'instructions qui permettent de parcourir les valeurs jusqu'à renvoyer la valeur 9.


```python

```

# Mini projet
Ecrire un programme qui permettra de parcourir la galerie de l'entrée (n°1) jusqu'à la sortie (n°9). 

![](../img/laby.png)

la galerie sera représentée par la structure : 
```
galerie = {1:{2:{3:9,5:6},7:8}}
```

Le programme demande à l'utilisateur de choisir une nouvelle direction à chaque nouvelle clé visitée.

Le programme affiche les choix possibles (valeurs) pour chacune des clés visitées.

L'utilisateur choisit alors une valeur numérique en rapport avec les valeurs possibles et la saisit dans une boite de dialogue générée par la fonction `input`.

Une boucle `while` permet de répéter cette séquence tant que la valeur saisie n'est pas 9.

Le texte affiché par le programme : 

```
vous etes au n°1
vous pouvez aller à : [2, 7]
quel est votre choix (1,..9) ? => 2
vous etes au n°2
vous pouvez aller à : [3, 5]
quel est votre choix (1,..9) ? => 3
vous etes au n°3
vous pouvez aller à : 9
quel est votre choix (1,..9) ? => 9
vous avez gagné `
```

{{< img src="../img/xyzzy1.GIF" caption="Xyzzy Blast, premier jeu de rôle sur ordinateur" >}}


# Extension du projet (term NSI)
Ce mini projet peut être étendu. On pourra utiliser des **classes** pour la gestion du (des) scenario(scenatii), du (des) joueur(s). 

On pourra également proposer une **interface** qui améliorera le confort de jeu.

Enfin, on pourra utiliser des **fichiers textes** (voire une **base de données**) pour une meilleure gestion des contenus, ou pour sauvegarder des éléments du jeu.

{{< img src="../img/xyzzy.GIF" caption="Xyzzy Blast, Computer History Museum" >}}

# Aides
## lire/ ecrire dans un fichier texte
Consulter la page [Entrees/Sorties](/docs/python/pages/ES/page1/) en python

## gestion de base de données en python
* Le [TP de term NSI](/docs/NSI/bases/page5/) sur la gestion de Base de Données en Python

* Le [TP serveur Flask](/docs/NSI/HTML/page6/) de 1ere NSI
