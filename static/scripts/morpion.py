morpion = [
    [' ', 'X', ' '],
    ['O', 'X', 'X'],
    ['X', 'O', ' ']
]

def affiche(grille):
    for ligne in grille:
        for case in ligne:
            print(case, '|', end=' ')
        print()
        
def compteur(grille,car,liste_X,liste_Y):
    c = 0
    for i in range(len(liste_X)):
            # à completer 
            x = liste_X[i]
            y = liste_Y[i]
            if grille[x][y] == car:
                c = c + 1
    return c

def victoire(grille,car):
    b1 = compteur(grille, car, [0,0,0],[0,1,2]) == 3
    b2 = compteur(grille, car, [1,1,1],[0,1,2]) == 3
    b3 = compteur(grille, car, [2,2,2],[0,1,2]) == 3
    b4 = compteur(grille, car, [0,1,2],[0,0,0]) == 3
    b5 = compteur(grille, car, [0,1,2],[1,1,1]) == 3
    b6 = compteur(grille, car, [0,1,2],[2,2,2]) == 3
    b7 = compteur(grille, car, [0,1,2],[0,1,2]) == 3
    b7 = compteur(grille, car, [2,1,0],[0,1,2]) == 3
    return b1 or b2 or b3 or b4 or b5 or b6 or b7 or b8

def cherche_car(grille,car,liste_X,liste_Y):
    for i in range(len(liste_X)):
        x = liste_X[i]
        y = liste_Y[i]
        if grille[x][y] == car:
            return x,y
        
def jouer(grille,car,x,y):
    grille[x][y] = car
                    
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
    elif compteur(grille,car_attaquant,
                [2,2,2],[0,1,2]) == 2 and cherche_car(grille,' ',
                [2,2,2],[0,1,2]) != None:
        # jouer dans une case vide de la ligne 2
        jouer_case = cherche_car(grille,' ',
                [2,2,2],[0,1,2])
    elif compteur(grille,car_attaquant,
                [0,1,2],[0,0,0]) == 2 and cherche_car(grille,' ',
                [0,1,2],[0,0,0]) != None:
        # jouer dans une case vide de la colonne 0
        jouer_case = cherche_car(grille,' ',
                [0,1,2],[0,0,0])
    elif compteur(grille,car_attaquant,
                [0,1,2],[1,1,1]) == 2 and cherche_car(grille,' ',
                [0,1,2],[1,1,1]) != None:
        # jouer dans une case vide de la colonne 1
        jouer_case = cherche_car(grille,' ',
                [0,1,2],[1,1,1])
    elif compteur(grille,car_attaquant,
                [0,1,2],[2,2,2]) == 2 and cherche_car(grille,' ',
                [0,1,2],[2,2,2]) != None:
        # jouer dans une case vide de la colonne 2
        jouer_case = cherche_car(grille,' ',
                [0,1,2],[2,2,2])
    elif compteur(grille,car_attaquant,
                [0,1,2],[0,1,2]) == 2 and cherche_car(grille,' ',
                [0,1,2],[0,1,2]) != None:
        # jouer dans une case vide de la diagonale descendante
        jouer_case = cherche_car(grille,' ',
                [0,1,2],[0,1,2])
    elif compteur(grille,car_attaquant,
                [2,1,0],[0,1,2]) == 2 and cherche_car(grille,' ',
                [2,1,0],[0,1,2]) != None:
        # jouer dans une case vide de la diagonale montante
        jouer_case = cherche_car(grille,' ',
                [2,1,0],[0,1,2])
    else:
        jouer_case = None
    return jouer_case

# si jeu_de_defense retourne None:
# la premiere case vide possible

if jeu_de_defense(morpion,'X') == None:
    x,y = cherche_car(morpion,' ',[0,0,0,1,1,1,2,2,2],
                                  [0,1,2,0,1,2,0,1,2])
else: 
    x,y = jeu_de_defense(morpion,'X')