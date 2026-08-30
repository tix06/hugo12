---
Title: TP3 boucles
description: boucles bornées et non bornées, notion d'itérable
hidden : true
weight: 8
---

## Exercices
Pour chaque exercice **résolu**, **recopier** le script dans votre cahier.

1. **Sélection des valeurs paires**

Placer les 5 instructions suivantes, dans le bon ordre, et avec la bonne indentation pour afficher tous les nombres pairs entre 0 et 100:


```python
if i % 2 == 0:
range(100):
for i 
in 
print(i)
```

Le programme devra afficher les valeurs:

```
0
2
...
100
```



2. **Table de 7**

* version a: Réaliser un programme utilisant une boucel bornée `for`, qui affiche (fonction `print`) les 10 premières valeurs de la table de 7

* version b: Ecrire un nouveau programme, utilisant cette fois une boucle non bornée `while` pour afficher  les 10 premières valeurs de la table de 7:



*Rappel:*

> La construction en bloc vous est déjà familière si vous avez utilisé un langage de blocs comme scratch ou blocky.  L’instruction while montre cette même disposition avec l'indentation.


{{< img src="../images/bloc4.png" caption="blocs python à compléter" >}}

> Pensez à ...:

* Utiliser un variant `i`, et une condition d'execution `while i < ...:`
* Dans la boucle, augmenter la valeur du variant `i`, avec `i = i+1` 


3. **Parcourir des éléments de liste**

L'équipe de France a remporté les trophées suivants: Coupe des Confédérations (2001, 2003), Jeux olympiques (1984), son championnat continental (1984, 2000)

Ecrire un script python qui utilise des listes et des boucles bornées pour afficher tous les trophées remportés par l'équipe de France:

```
l'equipe de France a remporté un trophée en 1984
...
l'equipe de France a remporté un trophée en 2000
```

4. **Division euclidienne**

*On rappelle que l'utilisation d'une boucle bornée `for` nécessite de connaitre le nombre d'itérations (`for .. in range(n)`). Si ce nombre d'itérations n'est pas connu, il faudra utiliser une boucle `while`*.

Le quotient de la division de a par b est égal au nombre de fois N qu'il faut soustraire b à a jusqu'à ce que l'on ait a < b.

a. D'après cet énoncé, va t-on utiliser une boucle bornée, ou bien un boucle non bornée?

b. Compléter le script de la division euclidienne de a par b

```python
a = int(input('entrer la valeur de a :'))
b = int(input('entrer la valeur de b :'))
N = 0
while a >=b:
  ...
  ...
print(f"a = {a}, N = {N}")
``` 

c. Quel est le quotient entier de la division de 2024 par 7? Quel est le reste?

5. **Compter** le nombre de **a** dans *abracadabra*:

Utiliser la variable `i` pour compter les **a**. L'itérable sera la chaine de caractères `mot`.

a. Compléter le programme pour qu'il affiche le nombre de **a** minuscules.

```python
i = 0
mot = "Abracadabra"
for caractere in mot:
	if ...:
		i = ...
print(f"...")
```

b. Modifier le programme pour qu'il compte aussi les **A** majuscules.

# Les fonctions natives du langage python
Tous les langages de programmation fournissent un large ensemble de fonctions prêtes à être utilisées. Nous avons déjà rencontré diverses fonctions prédéfinies, de la librairie standart : `print`, `input`, `range`.

> Tester dans un notebook, ou en console les fonctions natives suivantes:

```python
> bin(129)
..
> int('0b10000001',2)
..
```

Dans ces 2 exemples, on a utilisé un ou plusieurs arguments, positionnés entre les parenthèses.

* pour `bin(129)`, c'est l'argument 129 qui est passé à la fonction, afin que celle-ci réalise la conversion de 129 en binaire.
* pour `int('0b10000001',2)`, ce sont 2 arguments qui sont passés à la fonction `int`: Le binaire '0b10000001', ainsi que l'argument 2 précisant qu'il s'agit d'un code binaire à convertir en entier.

*Remarquer que ces arguments sont séparés par une virgule.*

## Exercices
1. **Convertir en binaire**

Utiliser la fonction `bin` pour convertir les nombres suivants: 65400, 31654, 1026

*Astuce pour **automatiser** le calcul*: On pourra placer ces valeurs dans une liste et utiliser une boucle bornée `for`:

```python
L = [65400, 31654, 1026]
for nombre in L:
    print(..)
```

2. **Convertir en ascii**

La fonction `chr` retourne le caractère ascii correspondant à l'entier (0..127) placé en argument:

```python
> chr(97)
'a'
```

> Utiliser cette fonction `chr` pour décoder le message, et trouver le tresor derrière l'une de ces portes...

{{< img src="../images/miniature.png" link="/pdf/NSI_1/D1_les_3_portes_ascii.pdf" caption="cliquer pour agrandir" >}}

On pourra s'aider du script suivant:

```python
L = [110, 39, 111]
for n in L:
    print(...)
```

# Liens

##### {{% button href="../page5" icon="bullhorn" style="caution" %}}Cours{{% /button %}} 
##### {{% button href="../page6" icon="palette" style="tip" %}}TP3{{% /button %}} Boucles bornées et non bornées