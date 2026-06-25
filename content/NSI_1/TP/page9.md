---
Title: projet bases en python
description: chaines str, types simples, boucles, conditions, random
weight: 9
---

# Rire aléatoire
La fonction `random` de la bibliothèque `random` produit un nombre aleatoire entre 0 et 1.

```python
> from random import random
> random()

0.8324575544825609
```

On peut egalement demander un entier aleatoire entre 0 et 100 avec la fonction `int`:

```python
> int(100*random())

62
```

1. Ecrire un programme qui affiche de manière aléatoire la chaine de phonèmes "Ke", "KeKe", "KeKeKe" ou "KeKeKeKe", ..., avec "Ke" répété un nombre aléatoire de fois, entre 1 et 10.
2. On veut maintenant que le programme affiche un texte aléatoire pouvant aussi comporter des séquences de "Ki", "Di", "Bi" comme par exemple: "KeKiDiBiBi". La séquence devra avoir une longueur inférieure ou egale à 10 phonèmes et pourra comporter des repetitions.
3. Programmer une fonction `texte_aleatoire` qui prend en paramètres les 4 phonèmes `son1`, 'son2', `son3`, `son4`. La fonction retourne un texte aleatoire de 10 sons maximum. Lors de l'appel de cette fonction avec `texte_aleatoire("Ke","Ki","Di","Bi")`, cette fonction pourrait retourner par exemple : "KeKiDiBiBi"


# Calendrier
**1.** Ecrire un programme qui indique si une année **a** est bissextile. Une année est bissextile si elle est divisible par 4.

**2.** Compléter le programme pour calculer le nombre de jours du mois **m**. **m** étant un entier compris entre 1 et 12. De janvier à juillet, les mois impairs ont 31 jours, les autres 30. Sauf le mois de fevrier a 29 ou 28 selon que l'année est bissextile ou non. Pour les autres mois, du mois d'aout à décembre c'est l'inverse (31 jours pour les **m** pairs).

**3.** Ecrire une fonction `jour_semaine` qui détermine le jour de la semaine à une date donnée. On représente les jours par les nombres 0 = lundi, 1 = mardi, ... 6 = dimanche.

```python
def jour_semaine(jour,mois,annee,jour0):
  """retourne le jour de la semaine à une 
  date donnée. jour0 est le code du premier
  jour de l'année"""

```

**4.** Vérifier que le 14 juillet 2022 tombe un jeudi.

# Fonction sin
**1.** Ecrire un programme qui utilise une boucle pour afficher les valeurs de la fonction `sin` pour `x` entre 0 et &#960;
<br>On découpera l'intervale [0; &#960;] de façon à afficher 15 valeurs de `sin(x)`. 
<br>Pour utiliser la fonction `sin`, il faudra l'importer avec la librairie math:

*Exemple d'import de la fonction sin et de la constante PI en console:*

```python
> from math import sin,pi
> sin(pi/2)

1.0
```

*Exemple de valeurs obtenue pour sin(x), où x est dans [0; &#960;]*

```
0.0
0.20791169081775931
0.40673664307580015
0.5877852522924731
0.7431448254773941
0.8660254037844386
0.9510565162951535
0.9945218953682733
0.9945218953682734
0.9510565162951536
0.8660254037844388
0.7431448254773945
0.5877852522924732
0.40673664307580004
0.2079116908177593
5.66553889764798e-16
```

**2.** Pour afficher le graphe de la fonction `sin`, on peut remplacer chaque valeur calculée précédement par une barre horizontale de longueur proportionnelle à sa valeur.<br>
On pourra par exemple multiplier le résultat de `sin(x)` par 30, et utiliser la fonction `int` pour transformer le nombre en entier, afin d'afficher un nombre de barres entre 0 et 30: `int(30 * sin(x))`
<br>Utiliser le programme pour afficher un graphique qui aura l'allure suivante:

```

=====
===========
================
=====================
========================
===========================
============================
============================
===========================
========================
=====================
================
===========
=====
```

**3.** *(difficile)* Modifier le programme pour afficher maintenant la courbe entière de `sin` sur une période entière, c'est à dire pour x compris dans l'intervale [0, 2&#960;]

```
                              ======
                              ============
                              =================
                              ======================
                              =========================
                              ============================
                              =============================
                              =============================
                              ============================
                              =========================
                              ======================
                              =================
                              ============
                              ======
                              
                        ======
                  ============
             =================
        ======================
     =========================
  ============================
 =============================
 =============================
  ============================
     =========================
        ======================
             =================
                  ============
                        ======
```


# Jeu de hasard
**1.** Ecrire un programme qui, étant donné un nombre entre 2 et 12, affiche toutes les combinaisons possibles permettant d'obtenir ce nombre avec 2 dés.

Par exemple, pour obtenir 7, il pourrait afficher:

```
'1 ET 6 , 2 ET 5 , 3 ET 4 , 4 ET 3 , 5 ET 2 , 6 ET 1 , '
```

*Aide:* Pour faire une boucle bornée, avec un variant qui va de 1 à 6, on peut faire:

```python
for i in range(1,7):
  ...
``` 

**2.** Etendre ce programme pour afficher, pour chaque nombre entre 2 et 12, toutes les combinaisons possibles permettant d'obtenir ce nombre avec les 2 dés.

Par exemple:

```
Pour obtenir 2, on peut faire 1 ET 1 , 
Pour obtenir 3, on peut faire 1 ET 2 , 2 ET 1 , 
Pour obtenir 4, on peut faire 1 ET 3 , 2 ET 2 , 3 ET 1 , 
Pour obtenir 5, on peut faire 1 ET 4 , 2 ET 3 , 3 ET 2 , 4 ET 1 , 
Pour obtenir 6, on peut faire 1 ET 5 , 2 ET 4 , 3 ET 3 , 4 ET 2 , 5 ET 1 , 
Pour obtenir 7, on peut faire 1 ET 6 , 2 ET 5 , 3 ET 4 , 4 ET 3 , 5 ET 2 , 6 ET 1 , 
Pour obtenir 8, on peut faire 2 ET 6 , 3 ET 5 , 4 ET 4 , 5 ET 3 , 6 ET 2 , 
Pour obtenir 9, on peut faire 3 ET 6 , 4 ET 5 , 5 ET 4 , 6 ET 3 , 
Pour obtenir 10, on peut faire 4 ET 6 , 5 ET 5 , 6 ET 4 , 
Pour obtenir 11, on peut faire 5 ET 6 , 6 ET 5 , 
Pour obtenir 12, on peut faire 6 ET 6 ,
``` 

**3.** Modifier le programme pour faire la même chose avec 3 dés.



