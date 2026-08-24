---
Title: TD2b listes, indices, méthodes
description: parcours de liste, compréhension de liste, méthodes de listes et dictionnaires, tracé graphique
hidden: true
weight: 10
---

  








## Ex 0: Parcours d'une liste


Une boucle bornée utilise le mot `for`. La structure suit le schéma suivant:

```
for variant in iterable:
    # traitement sur le variant
```

L'*itérable* est un ensemble de valeurs prises successivement par le *variant*. A chaque *itération*, le variant passe à la valeur suivante.

Cet itérable peut être une liste, ou une sequence de nombre entiers (`range(n)`, `range(len(L))`, ...)

On souhaite afficher les valeurs de l'iterable avec la fonction `print`. On donne les 2 scripts suivants:

* script 1

```python
L = [1, 10, 100, 1000]
for x in L:
  print(x)
```
* script 2

```python
L = [1, 10, 100, 1000]
for i in range(len(L)):
  print(i)
```
* **Question:** Lequel des 2 scripts précédents affiche `1 10 100 1000`? Lequel des 2 affiche `0 1 2 3`? Préciser dans chaque cas:

  * quel est le variant
  * quel est l'itérable
  * quelles sont les valeurs successives prises par le variant


## Ex 1: table de 3
On peut créer une liste VIDE, en faisant `L = []`, puis lui ajouter des valeurs. C'est ce qui doit être réalisé par ce programme.

```python
L = []
for  i in  range(11):
  L.append(...)
```

> Recopier et compléter le programme. Celui-ci doit compléter la liste avec les valeurs de la table de 3.

* **Question a1:** Que vaut la liste `L` après ce programme? Quelles sont les valeurs prises par l'iterable `i`? 

* **Question a2:** Comment avez vous complété les `...`? Comment feriez-vous pour compléter les valeurs de la table de 7?

> Ecrire l'instruction en compréhension de liste qui construit la liste L. (voir cours sur les types sequentiels > listes > [comprehension de liste](/docs/python/pages/variables/page2/))

## Ex 2: Energie en sciences physiques
On donne les listes de relevés du temps et de la vitesse pour un mobile. 

La vitesse `vitesse[0]`est relevée au temps `t[0]`, `vitesse[1]`est relevée au temps `t[1]`, etc...

```python
t = [0,0.04,0.08,0.12,0.16,0.2,0.24]
vitesse = [5.2,4.8,4.41,4.02,3.63,3.23,2.84]
```

Dans une cellule Python, 

* Recopiez les 2 listes et leur contenu
* commencez par attribuer 100 à la variable `m`.
* créez une liste vide pour l'énergie: `E = []`
* calculer les éléments de la liste `E`, l'energie cinetique pour un systeme de masse 100kg et de vitesse v, selon la loi:

`E = 1/2 * m * v**2`

> Pour réaliser cela, vous completerez la boucle bornée sur les valeurs de `vitesse`:

```python
for v in vitesse:
  E.append(...)
```

> Ecrire l'instruction en compréhension de liste qui construit la liste E. (voir cours sur les types sequentiels > listes > [comprehension de liste](/docs/python/pages/variables/page2/))

* **Question b:** Recopier le script sur votre feuille.


* **Question c:** Afficher le graphique de l'Energie cinétique E au cours du temps. (abscisses: t, ordonnées: E). Recopier le script entier dans votre cahier. Identifier dans le script les parties qui servent à:
  * déclarer des variables et des listes
  * calculer les termes d'une liste avec une boucle bornée
  * importer un module
  * tracer un graphique


## Ex 3: algorithmes simples utilisant une boucle bornée
Le script suivant calcule la somme des 99 premiers entiers:

$$0 + 1 + 2 + 3 + ...99$$

> Tester le script suivant et lire le résultat.

```python
somme = 0
for n in range(100):
  somme = somme + n
somme
```

* **Question d:** adapter ce script pour que celui-ci calcule la somme des termes $2^i$ pour `i` variant de 0 à 99: $$2^0 + 2^1 + 2^2 + ... + 2^{99}$$

* **Question e:** adapter ce script pour calculer le nombre de boules de la pyramique à 7 étages suivante. Quel est ce nombre? Quel serait ce nombre pour une pyramide à 99 étage?

{{< img src="../images/pyramide.jpeg" caption="ID 32142797 © [Ekostsov](https://fr.dreamstime.com/ekostsov_info) | Dreamstime.com" >}}

## Ex 4: Autres types construits
### Tuple
Soit le tuple `T` suivant:

```python
T = (("A",1),("B",2),("C",3))
```

L'interpreteur python construit l'objet `T` de la manière suivante:

{{< img src="../images/tuple1.png" caption="image - pythontutor" >}}

Lorsque l'on utilise la boucle bornée:

```python
for elem in T:
```

...cela créé un itérable (un ensemble), comme sur l'image suivante:

{{< img src="../images/tuple2.png" caption="en orange: ensemble des itérables" >}}

Ainsi, avec le programme suivant:

```python
T = (("A",1),("B",2),("C",3))
for elem in T:
  print(elem)
```

On affiche:

```
("A",1)
("B",2)
("C",3)
```



> A vous de jouer: Ecrire un programme qui parcourt les éléments de `T`, et affiche le caractère lu à la première position: 

```
"A"
"B"
"C"
```

*On utilisera la même boucle `for` que dans l'exemple précédent.*

### Dictionnaire
On souhaite construire un dictionnaire python `D` à partir du tuple `T`.

Les caractères seront les clés du dictionnaire, et les entiers, les valeurs correspondantes.

On souhaite que `D` soit constitué de: `{"A":1,"B":2,"C":3}`

> Adapter le script précédent pour construire `D` à partir des éléments de `T`.

On peut aussi construire un dictionnaire par compréhension, en une seule ligne.

*Exemple:*

```python
>>> L1 = ("a","b","c")
>>> dico = {i:L1[i] for i  in range(len(L1))}
>>> dico
{0: 'a', 1: 'b', 2: 'c'}
```

> Construire le dictionnaire `D` par compréhension de dictionnaire.


## Ex 5: Méthodes de listes — gérer un plan de vols
On reprend l'exemple du cours sur les aéroports :

```python
aeroports = ['CDG', 'ORY', 'LIS']
```

* **Question a:** Un nouveau vol dessert New-York. Ajouter `'JFK'` **en fin** de liste, avec la méthode adéquate.

* **Question b:** Un vol vers Londres-City doit être inséré **juste après** `'ORY'` (en 3e position), sans reconstruire toute la liste. Quelle méthode utiliser ? Écrire l'instruction.

* **Question c:** Le vol vers `'LIS'` est annulé : supprimer cet aéroport de la liste (méthode `remove`).

* **Question d:** Quel est l'index de `'JFK'` dans la liste actuelle ? Écrire l'instruction qui permet de l'obtenir sans le compter à la main.

* **Question e:** Le dernier aéroport ajouté à la liste doit être retiré, et son nom doit être annoncé à l'écran. Quelle méthode permet de faire les deux à la fois ? Écrire l'instruction correspondante.

* **Question f:** Une compagnie partenaire propose également les aéroports `['AMS', 'BRU']`. Fusionner cette liste à la fin de `aeroports`, en une seule instruction (sans boucle `for`).

* **Question g (bilan):** Recopier le script complet, dans l'ordre des questions a à f, puis afficher `aeroports` à la fin. Vérifier votre résultat à l'IDE.


## Ex 6: Trier une liste — classement de notes
On donne la liste de notes suivante :

```python
notes = [12, 8, 15, 10, 20, 6, 14]
```

* **Question a:** Utiliser `sorted(notes)` pour obtenir une **copie** triée par ordre croissant, stockée dans une nouvelle variable `notes_triees`. Vérifier ensuite que `notes` n'a pas changé.

* **Question b:** Utiliser la méthode `sort()` pour trier `notes` **en place**. Vérifier que `notes` a bien changé cette fois.

* **Question c — piège classique:** Que se passe-t-il si on exécute `notes = notes.sort()` ? Tester à l'IDE, afficher `notes`, et expliquer le résultat obtenu en une phrase (aide : que renvoie une méthode qui trie « en place » ?).

* **Question d:** En consultant `help(list.sort)` ou `help(sorted)`, trouver le paramètre optionnel qui permet de trier une liste par ordre **décroissant**. Trier `notes` par ordre décroissant, avec `sort()` puis avec `sorted()`.


## Ex 7: Copier une liste — le piège de la référence
On exécute le script suivant :

```python
original = [1, 2, 3]
copie = original
copie.append(4)
print(original)
print(copie)
```

* **Question a:** Sans exécuter, prédire ce qu'affichent les deux `print`. Vérifier ensuite à l'IDE.

* **Question b:** Le résultat de `original` vous étonne-t-il ? Expliquer, en une ou deux phrases, pourquoi modifier `copie` a également modifié `original` (aide : que fait réellement l'instruction `copie = original` ?).

* **Question c:** Réécrire le script pour que `copie` soit une liste réellement indépendante de `original` (deux façons sont possibles — en écrire au moins une). Vérifier qu'après modification de `copie`, `original` reste bien `[1, 2, 3]`.


## Ex 8: Méthodes de dictionnaires — le carnet de capitales
On reprend l'exemple du cours :

```python
capitales = {'France': 'Paris', 'Italie': 'Rome', 'Allemagne': 'Berlin'}
```

* **Question a:** Afficher, une par ligne, toutes les **clés** du dictionnaire (méthode `keys`).

* **Question b:** Afficher, une par ligne, toutes les **valeurs** du dictionnaire (méthode `values`).

* **Question c:** Afficher, une par ligne, chaque pays suivi de sa capitale sur la même ligne, par exemple `France Paris` (méthode `items`).

* **Question d:** Le Portugal doit être ajouté au dictionnaire, avec Lisbonne pour capitale. Écrire l'instruction.

* **Question e:** Une erreur s'est glissée : la capitale associée à `'Allemagne'` doit être modifiée en `'Berlin'` si ce n'est pas déjà le cas, sinon laissez comme c'est. Écrire l'instruction qui modifierait cette valeur si nécessaire.

* **Question f:** Le pays `'Italie'` ne doit plus figurer dans le dictionnaire : le supprimer avec `del`.

* **Question g:** Faire une copie indépendante de `capitales` dans une nouvelle variable `mes_capitales` (attention à ne pas faire une simple affectation). Ajouter `'Espagne': 'Madrid'` uniquement à `mes_capitales`, puis vérifier que `capitales` n'a pas changé.

* **Question h (compréhension de dictionnaire):** Construire, **en une seule ligne**, un nouveau dictionnaire `capitales_maj` qui contient les mêmes clés que `capitales`, mais avec les valeurs (les noms de villes) tout en majuscules. On utilisera la méthode `upper()` sur les chaînes de caractères, dans une compréhension de dictionnaire.

# Suite
##### {{% button href="../page2" icon="bullhorn" style="caution" %}}Cours{{% /button %}} 
##### {{% button href="../page9" icon="palette" style="tip" %}}TP2{{% /button %}} decouverte du cours
##### {{% button href="../page3" icon="palette" style="important" %}}TD2a{{% /button %}} les types construits, les copies par valeur et reference sur Pythontutor
##### {{% button href="../page4" icon="palette" style="important" %}}TD2b{{% /button %}} le parcours de liste, compréhension de liste et tracé graphique
##### {{% button href="../page5" icon="palette" style="tip" %}}TP3{{% /button %}} les tableaux
