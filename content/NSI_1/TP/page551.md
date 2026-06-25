---
Title: Jeu du Morpion
description: projet utilisant les tableaux python
weight: 15
---

# Projet 1: jeu du Morpion
Le jeu du Morpion est un jeu de réflexion se pratiquant à deux joueurs au tour par tour et dont le but est de créer le premier un alignement sur une grille (3x3).

Vous allez programmer le jeu du Morpion contre l'ordinateur. L'ordinateur devra repondre à chacun des coups du joueur et, si possible, remporter la partie.

Pour traiter ce projet, il est fortement recommandé de bien maitriser l'exercice 3.1, vues dans le [TD](../page55) sur les tableaux.

On donne la fonction d'affichage de la grille:

```python
def affiche(grille):
    for ligne in grille:
        for case in ligne:
            print(case, '|', end=' ')
        print()
```

**Exemple: Afficher la grille**

```python
morpion = [
    ['X', ' ', ' '],
    ['O', 'X', ' '],
    [' ', 'O', ' ']
]

affiche(morpion)

# affiche
X |   |   | 
O | X |   | 
  | O |   |
```

Afin d'analyser la partie, et prevoir les prochains coups à jouer, l'ordinateur utilisera les fonctions suivantes, que vous devrez programmer:

* `compteur`
* `victoire`
* `cherche_car`

Prévoir ensuite le prochain coup à partir des informations fournies, et créez un jeu, où l'ordinateur ne sera jamais perdant.

## Compteur du nombre de caractères identiques
Lire et tester le programme suivant:

**Exemple: Compte le nombre de X dans une ligne, colonne ou diagonale**



```python
# Vérifier si la ligne 0 contient trois symboles identiques
liste_X = [0,0,0]
liste_Y = [0,1,2]
compteur = 0
for i in range(len(liste_X)):
    x = liste_X[i]
    y = liste_Y[i]
    if morpion[x][y] == 'X':
        compteur +=1
print("il y a ", compteur, "cases X dans la ligne 0")
```

Dans la boucle `for`, l'indice i varie de 0 à 2.

Pour `i=0`, `x` a pour valeur `liste_X[0] -> 0` et `y` a pour valeur `liste_Y[0] -> 0`. Le couple x,y vaut alors 0,0. 

On utilise ces coordonnées pour relever le symbole de la case `morpion[0][0]`. C'est un `X`. On augmente alors le compteur d'une unité (on compte les `X`).

On continue dans la boucle `for` avec les cases 0,1 puis 0,2.

> Etape 1: Créer une fonction `compteur` qui prend une `grille`, un caractère `car`, une liste `liste_X` et une liste `liste_Y` en paramètres. Cette fonction devra retourner le nombre de fois que ce caractère `car` apparait.

**Exemple: utiliser la fonction compteur**

```python
# Etape 1
morpion = [
    ['X', 'O', 'X'],
    ['O', 'X', ' '],
    [' ', 'O', 'O']
]

def compteur(grille,car,liste_X,liste_Y):
	c = 0
	for i in range(len(liste_X)):
			# à completer 
			x = ...
			y = ...
			if grille[][]...
				c = c + ...
		
	return c

compteur(morpion,'X',[0,0,0],[0,1,2])
# retourne:
2
```

{{< img src="../images/compteur.png" caption="premiere étape de la boucle for" >}}


La fonction retourne 2: à la premiere ligne, il y a bien 2 caractères 'X'.

## Utilisez votre fonction
> Etape 2: utilisez votre fonction pour déterminer le nombre de  'X' dans chacune des lignes, dans chacune des colonnes, et dans chacune des diagonales (8 appels de la fonction). Placer chaque valeur dans une liste `L`, puis afficher celle-ci.


```python 
# Etape 2
L = []
L.append(compteur(morpion,'X',[0,0,0],[0,1,2]))
L.append(compteur(...
...
print(L)
```

## Victoire
> Etape 3: Créer une fonction `victoire`, qui prend une grille de morpion en paramètre, ainsi qu'un caractère `car` (qui vaut X ou O), et vérifie si la condition de victoire est réalisée pour le joueur X ou O. La fonction retournera un booléen True/False.

**Exemple: Victoire des X**

```python
# Etape 3
morpion = [
    ['X', 'O', 'X'],
    ['O', 'X', ' '],
    [' ', 'O', 'X']
]

def victoire(grille,car):
	b1 = compteur(grille, car, [0,0,0],[0,1,2])
	b2 = compteur(grille, car, [1,1,1],[0,1,2])
	# a completer
	b8 = compteur(grille, ...)
	return b1 == 3 or ...

victoire(morpion,'X')
# retourne:
True
victoire(morpion,'O')
# retourne:
False
```



## Interface joueurs
> Etape 4: Vous allez maintenant programmer l'interface  joueurs, en demandant alternativement, à chacun d'entre eux les coordonnées x,y pour placer son pion: 'X' puis 'O', puis 'X', puis 'O', ...

```python
# Etape 4
Fin_de_partie = False
while not victoire(morpion,'X') and not victoire(morpion,'O') and not Fin_de_partie:
    afficher(morpion)
    print('Joueur X:')
    x = int(input("jouer à la ligne (0,1,2), 3=Fin: "))
    y = int(..)
    ...
```

*Puis...*

* Si le joueur 'X' n'est pas vainqueur, demander à l'adversaire où il veut jouer.
* Le joueur 'O' est-il gagnant?
* Afficher la grille modifiée après ce tour de jeu
* Recommencer s'il n'y a pas de vainqueur.


# Phase 2: Comment jouer contre l'ordinateur?
> Dans cette phase du projet, nous allons remplacer les choix du joueur 'O' par ceux de l'ordinateur. Ce sera lui qui essaiera de vous bloquer lorsque vous avez deux pions 'X' alignés, et que vous risquez de gagner à la partie suivante.

Nous aurons besoin de 2 nouvelles fonctions:

* `cherche_car`: fonction qui recherche la première case vide dans un ensemble de cases du morpion, et retourne les coordonnées x,y de cette case
* `jeu_de_defense`: qui retourne les coordonnées x,y de la case qui doit bloquer le joueur (si celui-ci a une ligne avec deux 'X' et peut gagner au prochain tour)

## Detection case vide 
> Etape 1: Ecrire une fonction `cherche_car(grille,car,liste_X,liste_Y)` qui verifie si les cases de coordonnées `(liste_X[0], liste_Y[0]), (liste_X[1], liste_Y[1]), (liste_X[2], liste_Y[2])` contiennent au moins un symbole `car`, et retourne les coordonnées de la première case contenant le caractère `car`.

**Exemple: recherche d'un espace ' ' dans la ligne 2**

```python
# Etape 1
morpion = [
    ['X', 'O', 'X'],
    ['O', 'X', ' '],
    [' ', 'O', 'O']
]

def cherche_car(grille,car,liste_X,liste_Y):
    for i in range(len(liste_X)):
        x = liste_X[..
        y = liste_Y[..
        if grille[..][..] == ...:
            return x,y

cherche_car(morpion,' ',[2,2,2],[0,1,2])
# retourne:
(2,0)
```

La fonction retourne (2,0), car à la case de coordonnées `[2][0]`, il y a un symbole `' '`.


{{< img src="../images/cherche_car.png" caption="recherche d'un caractère espace ' ' dans la dernière ligne" >}}

**Exemple: recherche du premier espace ' ' dans tout la grille**

```python
morpion = [
    ['X', 'O', 'X'],
    ['O', 'X', ' '],
    [' ', 'O', 'O']
]

cherche_car(grille,' ',[0,0,0,1,1,1,2,2,2],
                       [0,1,2,0,1,2,0,1,2])
(1,2)
```

Lorsque l'on recherche un caractère dans TOUTE la grille, il y a 9 coordonnées à renseigner pour chacune des listes.

> Etape 2: créer une fonction `jeu_de_defense`, qui prend pour paramètre `grille`, et `car_attaquant`, qui vaudra 'X' ou 'O'.

Cette fonction va permettre de programmer le jeu complet, pour jouer contre l'ordinateur.

Pour chacune des lignes, puis pour chacune des colonnes, et enfin chaque diagonale:

Si la ligne contient 2 caractères 'X' (fonction `compteur`, et que la ligne contient un espace (`cherche_car` ne retourne pas `None`), alors retourner les coordonnées x,y retournées par la fonction `cherche_car`.

Sinon, retourner `None`



```python
def jeu_de_defense(grille,car_attaquant):

    if compteur(grille,car_attaquant,
                [0,0,0],[0,1,2]) == 2 and cherche_car(grille,' ',
                [0,0,0],[0,1,2]) != None:
        # jouer dans une case vide de la ligne 0
        jouer_case = cherche_car(grille,' ',
                [0,0,0],[0,1,2])
    elif compteur(grille,car_attaquant,
                [1,1,1],[0,1,2]) == 2 and cherche_car(grille,' ',
                [1,1,1],[0,1,2]) != None:
        # jouer dans une case vide de la ligne 1
        jouer_case = cherche_car(grille,' ',
                [1,1,1],[0,1,2])
    elif (...)
    (...)

    elif compteur(grille,car_attaquant,
                [0,1,2],[0,0,0]) == 2 and cherche_car(grille,' ',
                [0,1,2],[0,0,0]) != None:
        # jouer dans une case vide de la colonne 0
        jouer_case = cherche_car(grille,' ',
                [0,1,2],[0,0,0])
    (...)
	else:
		jouer_case = None
    return jouer_case
```

Pour appeler la fonction, et bloquer l'adversaire 'X', faire:

```python
if jeu_de_defense(morpion,'X') == None:
    x,y = cherche_car(grille,' ',[0,0,0,1,1,1,2,2,2],
                                  [0,1,2,0,1,2,0,1,2])
else: 
    x,y = jeu_de_defense(morpion,'X')
```

Ainsi, si aucune des lignes, colonnes, diagonale ne correspond ne contient deux caratères 'X' alignés, retourner la premiers case vide trouvée dans la grille: ce sera l'emplacement où l'ordinateur 'O' peut jouer.

L'ordinateur peut alors jouer:

```python
def jouer(grille,car,x,y):
    grille[x][y] = car

jouer(morpion,'O',x,y)
affiche(morpion)
```

## Jouer contre l'ordinateur
Pour cette dernière phase du projet, vous pourrez télécharger le script python contenant toutes les fonctions nécéssaires: [telecharger](/scripts/morpion.py)

Pour élaborer une stratégie plus avancée de l'ordinateur, on pourra consulter la page dédiée: site [tictactoe.com](https://tictactoefree.com/fr/astuces/comment-gagner-au-morpion-si-vous-jouez-en-second)

{{< img src="../images/morpion.png" link="https://tictactoefree.com/fr/astuces/comment-gagner-au-morpion-si-vous-jouez-en-second" caption="site TICTACTOEFREE.COM" >}}





* pour jouer contre l'ORDINATEUR. (utiliser la fonction `jeu_de_defense` pour prevoir la case dans laquelle il devra jouer). 
* Organisez au mieux votre script. Commentez vos fonctions.

**Pour les élèves de Terminale:**

* Prévoir et anticiper toutes les erreurs possibles de saisie du joueur, tous les defauts possibles qui peuvent survenir dans la partie (plus de O que de X, erreurs avec les coordonnées saisies, terminaison de la boucle while, ...). On pourra ajouter des structures conditionnelles supplémentaires, ou bien des tests d'**assert**ion, ou autres mécanismes. (**try.. except**, **raise**,...): Voir cours sur la mise au poin d'un programme: [python avancé](/docs/NSI/langages/page5/)
* Utiliser une structure de données **Pile** pour permettre un retour en arriere (le joueur efface ses coups précédents).



