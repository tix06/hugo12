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
for i in range(100):
print(i)
```

Le programme devra afficher les valeurs:

```
0
2
...
100
```

***question a:*** Recopier le script une fois que vous avez établi celui-ci.

2. **Table de 7**

* version a: Réaliser un programme utilisant une **boucle bornée** `for`, qui affiche, avec la fonction `print`, les 10 premières valeurs de la table de 7. 

*Astuce:* Utiliser le variant i pour faire `7*i`

* version b: Ecrire un nouveau programme, utilisant cette fois une boucle non bornée `while` pour afficher  les 10 premières valeurs de la table de 7:


<!--
*Rappel:*

> La construction en bloc vous est déjà familière si vous avez utilisé un langage de blocs comme scratch ou blocky.  L’instruction while montre cette même disposition avec l'indentation.
-->

{{< img src="../images/bloc4.png" width="400" caption="boucle while" >}}

> Pensez à ...:

* Utiliser un variant `i`, et une condition d'execution `while i < ...:`
* Dans la boucle, augmenter la valeur du variant `i`, avec `i = i+1` 


3. **Parcourir des éléments de liste**

L'équipe de France a remporté les trophées suivants: Coupe des Confédérations (2001, 2003), Jeux olympiques (1984), son championnat continental (1984, 2000)

On peut placer ces valeurs dans une liste `L = [1984,2000,...]`

> Ecrire un script python qui utilise une liste et une boucle bornée pour afficher tous les trophées remportés par l'équipe de France:

```
l'equipe de France a remporté un trophée en 1984
...
l'equipe de France a remporté un trophée en 2000
```

4. **Division euclidienne**

*On rappelle que l'utilisation d'une boucle bornée `for` nécessite de connaitre le nombre d'itérations (`for .. in range(n)`). Si ce nombre d'itérations n'est pas connu, il faudra utiliser une boucle `while`*.

Le quotient de la division de a par b est égal au nombre de fois N qu'il faut soustraire b à a jusqu'à ce que l'on ait a < b.

***question b.:*** D'après cet exercice, **la division euclidienne**, va t-on utiliser une boucle bornée, ou bien un boucle non bornée?



> Vous devrez écrire le programme de la division euclidienne de a par b, en utilisant uniquement des lignes de code choisies parmi les lignes suivantes. Les lignes ne sont pas toutes à utiliser et l’indentation est à adapter.

```python
a = int(input('entrer la valeur de a :'))
b = int(input('entrer la valeur de b :'))
N = 0
while a >= b:
while a > b:
a = a - b
b = b - a
N = N + 1
N = N - 1
print(f"La division de a={a}, par b={b}: quotient={N} et reste={a}")
print(f"La division de a={a}, par b={b}: quotient={a} et reste={N}")
``` 

***question c.:*** Quel est le quotient entier de la division de 2024 par 7? Quel est le reste?

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

***question d.:*** recopier le script lorsque vous l'avez obtenu.

## Les fonctions natives du langage python
Tous les langages de programmation fournissent un large ensemble de fonctions prêtes à être utilisées. Nous avons déjà rencontré diverses fonctions prédéfinies, de la librairie standart : `print`, `input`, `range`.

> Tester en console les fonctions natives suivantes:

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


1. **Convertir en binaire**

a. Dans le *shell python*: Utiliser la fonction `bin` pour convertir en binaire les nombres suivants: 65400, 31654, 1026

***question e.:*** Quel est le resultat obtenu pour 65400?

b. Automatiser le calcul: Placer ces valeurs dans une liste et utiliser une boucle bornée `for`:

```python
L = [65400, 31654, 1026]
for nombre in L:
    print(..)
```

***question f.:*** Recopier la ligne 3 que vous avez complétée.

2. **Convertir en ascii**
Le code ascii permet de représenter les caractères `"abcdef...z0123..9"` en un nombre entre 0 et 127. 

La fonction `ord()` permet de définir le nombre associé au caractère. Et la fonction `chr()` retourne le caractère ascii correspondant à l'entier (0..127) placé en argument:

```python
> ord('a')
97
> chr(97)
'a'
```

***question g.:*** Quel sont les caractère correspondants aux rangs ascii 110, puis 39 et enfin 111?

> Utiliser la fonction `chr` pour décoder le message, et trouver le tresor derrière l'une de ces portes...

{{< img src="../images/miniature.png" link="/pdf/NSI_1/D1_les_3_portes_ascii.pdf" caption="cliquer pour agrandir" >}}

```
message="110 39 111 117 118 114 101 122 32 115 117 114 116 111 117
116 32 112 97 115 32 108 97 32 112 111 114 116 101 32 100
101 32 103 97 117 99 104 101"
```

On pourra s'aider du script suivant:

```python
message = "110 39 111"
# decoupe du message pour créer une liste avec .split()
L = message.split()
# L = [110, 39, 111]
for n in L:
    print(...)
```

***question h.:*** Quel est le message?

# Liens

##### {{% button href="../page5" icon="bullhorn" style="caution" %}}Cours{{% /button %}} 
##### {{% button href="../page6" icon="palette" style="tip" %}}TP3{{% /button %}} Boucles bornées et non bornées