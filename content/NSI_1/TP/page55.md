---
Title: exos tableaux listes python
description: TP listes, tableaux, matrices
weight: 14
---

# Partie 1 : Tableaux 1D - Accès par indice

## Exercice 1.1 : Gestion d'un inventaire de jeu vidéo

Vous développez un jeu de rôle où le personnage possède un inventaire de 10 emplacements. Chaque emplacement contient un objet représenté par une chaîne de caractères.

```python
inventaire = ["épée", "potion", "bouclier", "vide", "clé", "vide", "arc", "carte", "vide", "torche"]
```

**Exemple 1 : Accéder à un élément**

```python
# Pour afficher l'objet à l'indice 2
print(inventaire[2])  # Affiche : bouclier
```

**Exemple 2 : Modifier un élément**

```python
# Pour remplacer l'objet à l'indice 3
inventaire[3] = "diamant"
print(inventaire[3])  # Affiche : diamant
```

**Exemple 3 : Échanger deux éléments**

```python
# Pour échanger les éléments aux indices 1 et 5
temp = inventaire[1]
inventaire[1] = inventaire[5]
inventaire[5] = temp
```

**Questions :**

1. Affichez l'objet situé à l'emplacement 4 de l'inventaire.
2. Le joueur ramasse un "parchemin". Remplacez le premier emplacement "vide" par "parchemin".
3. Le joueur utilise sa potion (indice 1). Remplacez-la par "vide".
4. Échangez les objets aux emplacements 0 et 6 (épée et arc).
5. Créer une fonction `echange` qui prend une liste `L` ainsi que 2 indices `i` et `j` pour paramètres, et qui modifie la liste `L` en permutant les objets aux rangs `i` et `j`. Cette fonction n'aura pas de valeur de retour.
6. Ecrire l'instruction qui échange les objets aux emplacements 0 et 6, mais cette fois-ci, en utilisant la fonction `echange`.

## Exercice 1.2 : Thermomètre intelligent

Un thermomètre enregistre les températures de chaque heure de la journée (24 valeurs).

```python
temperatures = [12, 11, 10, 10, 9, 9, 11, 14, 17, 20, 23, 25, 27, 28, 27, 25, 22, 19, 17, 15, 14, 13, 13, 12]
```

**Exemple : Calculer un écart**

```python
# Pour calculer l'écart entre deux températures
ecart = temperatures[10] - temperatures[3]
print("L'écart est de", ecart, "degrés")
```

**Exemple : Augmenter une valeur**
```python
# Pour augmenter de 3 degrés la température à l'indice 5
temperatures[5] = temperatures[5] + 3
# ou plus court :
temperatures[5] += 3
```

**Questions :**

1. Affichez la température à 14h (indice 14).
2. Une erreur de capteur s'est produite à 8h. Modifiez la valeur à l'indice 8 pour la remplacer par 16. 
3. Pourrait-on utiliser la fonction `echange`? Si oui, écrire l'instruction correspondante.
3. Calculez l'écart entre la température maximale (indice 13) et minimale (indice 5).
4. Augmentez de 2 degrés la température de minuit (indice 0).

---

# Partie 2 : Tableaux 1D - Parcours par élément et par indice

## Exercice 2.1 : Analyse d'une partie de Scrabble

Un joueur de Scrabble possède les lettres suivantes dans son chevalet :

```python
chevalet = ['A', 'E', 'R', 'T', 'I', 'N', 'S']
```

**Exemple 1: Parcours par élément**

```python
# Afficher chaque lettre
for lettre in chevalet:
    print(lettre)
```

**Exemple 2: Compter des éléments**

```python
# Compter les 'E' dans le chevalet
compteur = 0
for lettre in chevalet:
    if lettre == 'E':
        compteur += 1
print("Il y a", compteur, "lettre E")
```

**Exemple 3: Vérifier une condition**

```python
# Vérifier si le chevalet contient un 'A'
if 'A' in chevalet:
    print("Il y a un A !")
else:
    print("Pas de A")
```

**Questions avec parcours par élément :**

1. Affichez toutes les lettres du chevalet, une par ligne, en utilisant une boucle `for lettre in chevalet`.
2. Comptez combien de voyelles (A, E, I, O, U, Y) se trouvent dans le chevalet.
3. Affichez "BINGO!" si le chevalet contient au moins une lettre 'S', sinon affichez "Pas de S".
4. Ecrire une fonction `compte` qui prend une liste `L` ainsi qu'une lettre `V` en paramètre, et qui retourne le nombre de fois où cette lettre est présente dans la liste.
5. Ecrire l'instruction qui appelle cette fonction pour déterminer le nombre de `E` dans le chevalet `['A', 'E', 'R', 'T', 'I', 'N', 'S']`

## Exercice 2.2: Parcours par indice
**Exemple 1: afficher l'indice et l'élément**

```python
# Afficher chaque lettre avec sa position
for i in range(len(chevalet)):
    print("Position", i, ":", chevalet[i])
```

**Exemple 2: Modifier en parcourant**

```python
# Remplacer tous les 'A' par des '*'
for i in range(len(chevalet)):
    if chevalet[i] == 'A':
        chevalet[i] = '*'
```

**Exemple 3: Créer un nouveau tableau**

```python
# Créer un tableau avec uniquement les voyelles
voyelles_trouvees = []
for i in range(len(chevalet)):
    if chevalet[i] in ['A', 'E', 'I', 'O', 'U', 'Y']:
        voyelles_trouvees.append(chevalet[i])
print(voyelles_trouvees)
```

**Questions avec parcours par indice :**

4. Affichez chaque lettre avec sa position : "Position 0 : A", "Position 1 : E", etc.
5. Remplacez toutes les voyelles par des '*' en parcourant le tableau par indice.
6. Créez un nouveau tableau contenant uniquement les consonnes en utilisant les indices.


# Partie 3 : Tableaux 2D - Parcours par élément et par indice

## Exercice 3.1 : Grille de Morpion
### Parcours par élément 
Une grille de morpion est représentée par un tableau 2D de 3×3 :

```python
morpion = [
    ['X', 'O', 'X'],
    ['O', 'X', ' '],
    [' ', ' ', 'O']
]
```

**Exemple 1: afficher les éléments**

```python
for ligne in morpion:
    for case in ligne:
        print(case, end=' ')
    print()  # retour à la ligne
# Affiche toutes les valeurs ligne par ligne:
X | O | X | 
O | X |   | 
  |   | O |
````


**Exemple 2: Compter les éléments**

```python
# Compter les 'X'
compteur = 0
for ligne in morpion:
    for case in ligne:
        if case == 'X':
            compteur += 1
print("Nombre de X :", compteur)
```

**Questions:**

1. Affichez tous les 'X' de la grille, ligne par ligne en utilisant deux boucles `for`.
2. Comptez le nombre de cases vides (contenant ' ').
3. Déterminez qui a le plus de coups joués (X ou O).



### parcours par indice :

**Exemple 1: Parcours par indice (tableau 2D)**

```python
# Afficher la grille avec les indices
for i in range(len(morpion)):
    for j in range(len(morpion[i])):
        print(morpion[i][j], end=' ')
    print()
```

**Exemple 2: Accéder à un élément précis**

```python
# Afficher et modifier un élément
print("Case [0][1] :", morpion[0][1])  # Affiche 'O'
morpion[0][1] = 'X'  # Modifier la case
```

**Exemple 3: Vérifier une ligne**

```python
# Vérifier si la ligne 0 contient trois symboles identiques
ligne = morpion[0]
if ligne[0] == ligne[1] == ligne[2] and ligne[0] != ' ':
    print("La ligne 0 est gagnante !")
```

**Questions:** 

1. Le joueur O joue en position [1][2] (ligne 1, colonne 2). Ecrire l'instruction qui modifie la grille.
2. Quelles sont les coordonnées `morpion[i][j]` pour chacune des cases? Dessinez sur votre cahier une matrice pour placer les coordonnées `[i][j]`dans chaque case..
2. Ecrire les instructions qui verifient si la première ligne contient trois symboles identiques (condition de victoire).
3. Ecrire une fonction `ligne_X` qui prend pour paramètre une matrice `M` comme la grille de morpion (3*3). `M` contient dans chaque case `'X'`, `'O'`, ou `''`. Cette fonction retournera `True` si l'une des lignes est remplie avec trois `'X'`. 

## Exercice 3.2 : Grille de Sudoku (9×9)

Voici une grille de Sudoku partiellement remplie :

```python
sudoku = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]
```

Les cases vides sont représentées par 0.

**Exemple : Compter les cases vides**

```python
# Compter les 0 dans toute la grille
compteur = 0
for i in range(len(sudoku)):
    for j in range(len(sudoku[i])):
        if sudoku[i][j] == 0:
            compteur += 1
print("Nombre de cases vides :", compteur)
```

**Exemple : Afficher une ligne**

```python
# Afficher la ligne 0
for j in range(len(sudoku[0])):
    print(sudoku[0][j], end=' ')
print()
```

**Exemple : Afficher une colonne**

```python
# Afficher la colonne 2
for i in range(len(sudoku)):
    print(sudoku[i][2], end=' ')
print()
```

**Exemple : Modifier une case**

```python
# Remplacer le 0 en position [0][2] par 4
sudoku[0][2] = 4
print("Nouvelle valeur :", sudoku[0][2])
```

**Exemple : Extraire un bloc 3×3**

```python
# Extraire le bloc en haut à gauche (lignes 0-2, colonnes 0-2)
bloc = []
for i in range(0, 3):  # lignes 0, 1, 2
    ligne_bloc = []
    for j in range(0, 3):  # colonnes 0, 1, 2
        ligne_bloc.append(sudoku[i][j])
    bloc.append(ligne_bloc)
print(bloc)
```

**Exemple : Vérifier les doublons dans une ligne**

```python
# Vérifier si la ligne 1 contient des doublons (sans compter les 0)
ligne = sudoku[1]
nombres = []
for valeur in ligne:
    if valeur != 0:
        if valeur in nombres:
            print("Doublon détecté !")
        else:
            nombres.append(valeur)
```

**Questions avec parcours par indice :**

1. Comptez le nombre de cases vides (valeur 0) dans toute la grille.
2. Affichez tous les chiffres de la première ligne (ligne d'indice 0).
3. Affichez tous les chiffres de la cinquième colonne (colonne d'indice 4).
4. Remplacez le 0 en position [0][2] par le chiffre 4.
5. Ecrire une fonction `doublons`, qui prend en paramètre une grille de sudoku `G`, ainsi qu'un numero de ligne `i`, et qui retourne un booléen `True`/`False`. selon si la ligne `i` contient des *doublons*. (sans compter les 0).
6. Appeler la fonction `doublons` pour vérifier si la première ligne contient des *doublons*.
7. Créez une fonction `bloc` qui extrait l'un des 9 blocs 3×3, n'importe où dans la grille. (par exemple, le bloc en haut à gauche : lignes 0-2, colonnes 0-2), à partir des indices `i,j` de départ (coin supérieur gauche du bloc).


## Conseils généraux

- **Testez votre code progressivement** : ne cherchez pas à tout résoudre d'un coup.
- **Utilisez des fonctions** pour organiser votre code et le rendre réutilisable.
- **Affichez des résultats intermédiaires** avec `print()` pour vérifier votre logique.
- **N'oubliez pas** : les indices commencent à 0 en Python !

[COURS python sur les tableaux](/docs/python/pages/boucles/page2/)

**Suite en projet:**

[Liste des projets](../page551)
