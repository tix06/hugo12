---
Title: algos essentiels
description: bases en python, listes, dictionnaires, recherche, min, max
weight: 71
---

# Exercices A de la BNS 2024
{{% badge icon="star" %}}chaine str{{% /badge %}} {{% badge icon="star" %}}tableau{{% /badge %}} {{% badge icon="star" %}}dictionnaire{{% /badge %}} {{% badge icon="star" %}}python bases{{% /badge %}} {{% badge icon="star" %}}compteur{{% /badge %}} {{% badge icon="star" %}}min max{{% /badge %}}

## parcours de chaine de caractères, mot à trou
On considère des chaînes de caractères contenant uniquement des majuscules et des carac-
tères `*` appelées *mots à trous*.

Par exemple `INFO*MA*IQUE`, `***I***E**` et
`*S*` sont des mots à trous.

**Programmer une fonction `correspond` qui :**

- prend en paramètres deux chaînes de caractères `mot` et `mot_a_trous` où
`mot_a_trous` est un mot à trous comme indiqué ci-dessus, 
- renvoie :
    - `True` si on peut obtenir `mot` en remplaçant convenablement les caractères
`'*'` de `mot_a_trous`.
    - `False` sinon.

Exemple :

```python
>>> correspond('INFORMATIQUE', 'INFO*MA*IQUE')
True
>>> correspond('AUTOMATIQUE', 'INFO*MA*IQUE')
False
>>> correspond('STOP', 'S*')
False
>>> correspond('AUTO', '*UT*')
True
```

## max d'une liste
Écrire la fonction `maximum_tableau`, prenant en paramètre un tableau non vide de nombres `tab` (de type
`list`) et renvoyant le plus grand élément de ce tableau.

Exemples :

```python
>>> maximum_tableau([98, 12, 104, 23, 131, 9])
131
>>> maximum_tableau([-27, 24, -3, 15])
24
```

## Rechercher
Programmer la fonction `recherche`, prenant en paramètres un tableau non vide `tab` (type `list`) d'entiers et un entier `n`, et qui renvoie l'indice de la **dernière** occurrence de l'élément cherché. Si l'élément n'est pas présent, la fonction renvoie `None`.

Exemples
```python
>>> recherche([5, 3], 1) # renvoie None
2
>>> recherche([2, 4], 2)
0
>>> recherche([2, 3, 5, 2, 4], 2)
3
```

## Tableau trié ou non
Écrire une fonction `verifie` qui prend en paramètre un tableau de valeurs numériques et qui renvoie `True` si ce tableau est trié dans l’ordre croissant, `False` sinon.

Un tableau vide est considéré comme trié.

Exemples :

```python
Exemples :
>>> verifie([0, 5, 8, 8, 9])
True
>>> verifie([8, 12, 4])
False
>>> verifie([-1, 4])
True
>>> verifie([])
True
>>> verifie([5])
True
```

## Compression. Codage par différence
Le codage par différence (*delta encoding* en anglais) permet de compresser un tableau
d’entiers dont les valeurs sont proches les unes des autres. Le principe est de stocker la
première donnée en indiquant pour chaque autre donnée sa différence avec la précédente
plutôt que la donnée elle-même.

On se retrouve alors avec un tableau de données plus petit, nécessitant
moins de place en mémoire. Cette méthode se révèle efficace lorsque les valeurs consécutives
sont proches.

Programmer la fonction `delta(liste)` qui prend en paramètre un tableau non vide de nombres entiers
et qui renvoie un tableau contenant les valeurs entières compressées à l’aide cette technique.

Exemples :

```python
>>> delta([1000, 800, 802, 1000, 1003])
[1000, -200, 2, 198, 3]
>>> delta([42])
[42] 
```

## Compteur d'espaces
Dans cet exercice, on considère des phrases composées de mots.

- On appelle « mot » une chaîne de caractères composée avec des caractères choisis
parmi les 26 lettres minuscules ou majuscules de l'alphabet,

- On appelle *phrase* une chaîne de caractères :
    - composée avec un ou plusieurs *mots* séparés entre eux par un seul
caractère espace `' '`,
    - se finissant :
        - soit par un point `'.'` qui est alors collé au dernier mot,
        - soit par un point d'exclamation `'!'` ou d'interrogation `'?'` qui est alors
séparé du dernier mot par un seul caractère espace `' '`.

Voici deux exemples de phrases :

- 'Cet exercice est simple.'
- 'Le point d exclamation est separe !'

Après avoir remarqué le lien entre le nombre de mots et le nombres de caractères espace
dans une phrase, programmer une fonction `nombre_de_mots` qui prend en paramètre une
phrase et renvoie le nombre de mots présents dans cette phrase.

```python
>>> nombre_de_mots('Cet exercice est simple.')
4
>>> nombre_de_mots('Le point d exclamation est séparé !')
6
>>> nombre_de_mots('Combien de mots y a t il dans cette phrase ?')
10
>>> nombre_de_mots('Fin.')
1
```
## Dictionnaire. Fusion
Écrire une fonction `ajoute_dictionnaires` qui prend en paramètres deux
dictionnaires `d1` et `d2` dont les clés sont des nombres et renvoie le dictionnaire `d` défini de
la façon suivante :

- Les clés de `d` sont celles de `d1` et celles de `d2` réunies.
- Si une clé est présente dans les deux dictionnaires `d1` et `d2`, sa valeur associée
dans le dictionnaire `d` est la somme de ses valeurs dans les dictionnaires `d1` et `d2`.
- Si une clé n’est présente que dans un des deux dictionnaires, sa valeur associée
dans le dictionnaire `d` est la même que sa valeur dans le dictionnaire où elle est
présente.

Exemples :

```python
>>> ajoute_dictionnaires({1: 5, 2: 7}, {2: 9, 3: 11})
{1: 5, 2: 16, 3: 11}
>>> ajoute_dictionnaires({}, {2: 9, 3: 11})
{2: 9, 3: 11}
>>> ajoute_dictionnaires({1: 5, 2: 7}, {})
{1: 5, 2: 7}
```
