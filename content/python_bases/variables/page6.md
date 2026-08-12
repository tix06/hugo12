---
Title: TP2 variables
hidden: true
weight: 4
---

# Travaux pratiques
Ouvrir dans *winpython > python QTConsole*


{{< img src="/images/qtconsole.png" >}}



## Opérations sur les nombres

> Tester les scripts suivants dans l'editeur Python. Pour cela, recopier dans l'ordre, et dans la même cellule, chacune des instructions du script, et executer celle-ci. Repondre ensuite aux questions.

### Script 1
Incrémenter une variable...

```python
age = 0
age = age + 1
age
```

* **Question a:** quelle est la valeur de `age` à la fin du script? 

### Script 2
Le programme suivant permet de connaitre en quelle année un enfant, né en 2022, aura 17 ans

```python
age = 0
annee = 2022
age = age + 17
annee = annee + age
annee
```

* **Question b:** en quelle année aura-t-il 17 ans?

### Script 3
On veut réaliser les opérations suivantes:

```python
nombre=2*nombre
nombre=nombre-10
nombre=nombre**2
nombre=nombre-5
```

* **Question c:** Quel est le résultat (c'est à dire la valeur finale de `nombre`) pour une valeur de depart `nombre = 5`?

### Script 4
Écrire un programme dans l’éditeur qui :

- affecte 3 à la variable `nombre` 
- Ajoute 7 au triple du nombre.
- Multiplie le résultat par le nombre lui-même.
- Soustrait au résultat le nombre 1 ;
- Affiche le résultat obtenu.

Ne pas utiliser de nouvelles variables pour les résultats intermédiaires. Seulement `nombre`

* **Question d:** Quel est le résultat?

### Script 5: permuter la valeur de 2 variables
On veut mettre la valeur de `a` dans `b` et celle de `b` dans `a`. Le problème est que lorsque l'on fait...

```python
b = a
a = b
```

... on se retrouve avec les mêmes valeurs pour `b` et pour `a`. Il n'y a pas eu d'echange. 

L'idée est d'utiliser une troisième variable `c` pour stocker la valeur de `b`, échanger `a` et `b`, puis affecter `c` à `a`:

On fait alors `c <- b`, `b <- a`, puis `a <- c`.


* **Question e:** Ecrire la série d'instructions correspondantes. Puis vérifier qu'il y a bien eu échange entre les variables: `print(f"a={a}, b={b}")`

## Opérations sur les chaines de caractères

### Script 6
Associer des chaines de caractères.

```python
debut = "bonne annee"
milieu = " "
fin = "grand mere"
message = debut + milieu + fin
message
```

Cet exemple vous rappelle que l'opérateur `+` est l'opérateur de *concaténation* avec les chaines de caractères. 

* **Question f:** Ecrire un nouveau script qui construit le message suivant: `Ho Ho Ho Ho Ho Ho Ho Ho Ho Ho`, où le nombre de `Ho` est stocké dans une variable N. 

*Astuce: utiliser l'opérateur* `*`

### Script 7
Associer des valeurs numériques et des chaines de caractères

```python
age = 21
nom = "Kevin"
message = "mon nom est " + nom + ", et j'ai " + age + " ans"
message
```

* **Question g:** Le script s'execute t-il, ou bien renvoie-t-il une erreur? Quelle erreur le cas écheant?
* **Question h:** Modifier l'avant derniere ligne par: `message = "mon nom est " + nom + ", et j'ai " + str(age) + " ans"`. Le script fonctionne t-il? Que renvoie t-il?

*Remarque:* La fonction `str` va tranformer la valeur numerique `age` en une chaine de caractères (les caractères "2" et "1").

*Tester également les méthodes:* 

```python
# methode 1: separer les arguments evec des virgules
print("mon nom est ",nom ," et j'ai ",age, "ans")
# methode 2: utiliser un f-string
print(f"mon nom est {nom} et j'ai {age} ans")
```

*Que constatez-vous?*

### Script 8
Afficher avec la fonction `print`

```python
a = 45
b = 26
q = a // b
r = a % b
print(f'le quotient de la division entiere de {...} par {...} vaut {...} et le reste vaut {...}')
```

* **Question i:** Completer la derniere ligne du script pour afficher la phrase entière. Vous ne devrez pas écrire les chiffres 45, 26 et 19 dans le message. Seulement utiliser les variables.


Nous avons vu qu'une chaine de caractère pouvait être construite comme une association de plusieurs chaines de caractères. Une chaine de caractères est de type *string* (ou `str`) en python.

Pour vérifier le type d'une variable, on utilise la fonction `type`

> Testez chacune des instructions suivantes pour vérifier le type des différentes variables

```python
a = 45
type(a)
b = 26
type(b)
type(a//b)
c = a % b
type(c)
d = a / b
type(d)
m = str(a)
type(m)
```

* **Question j:** Compléter le tableau

| x= | valeur |  type(x) |
| --- | --- | --- |
| 45 |  |  |
| "45" + "45" |   |   |
| "45" * 3 |   |   |
| 45%26 | |   |
| 45/26 |  |   |
| 45//26 |  |   |
| str(45) |  |  |
| 2**8 |   |  |
| 6.02e-3 |   |   |



### Script 9
Calculer en physique

Dans une cellule Python, 

* commencez par attribuer 100 à la variable `m`, et 20 à la variable `v`
* calculer puis afficher E, l'energie cinetique pour un systeme de masse 100kg et de vitesse $20m.s^{-1}$, selon la loi:

$$Ec = \tfrac{1}{2}m.v^2$$

* **Question j:** Quelle est l'expression que vous avez saisie en langage Python? Quelle est la valeur calculée pour l'énergie cinetique?

* **Question k:** Construire une chaine de caractères, en utilisant un f-string et précisant les conditions initiales, les valeurs pour m et pour v, et le résultat du calcul de l'énergie cinétique. Recopier ici cette instruction en python.


### Script 10
Voici un exemple de fonction en python:

```python
# on créé une fonction avec def
def calcule_somme_carres(a,b):
	return a**2 + b**2

# on appelle cette fonction avec les arguments placés pour a et b
> calcule_somme_carres(3,4)
25
```

* **Question l:** créer une fonction `Ec` qui prend pour paramètres `m` et `v` et retourne le resultat de $Ec = \tfrac{1}{2}m.v^2$. Appeler cette fonction avec les valeurs 100kg et $20m.s^{-1}$

# Portfolio
* Comment se nomment *en python* les 4 types primitifs que l'on a vus lors de ces premieres séances?
* Le changement de type entre variables se fait grace aux fonctions `str`, 'float', `int`, et `bool`
  * Comment transformer la chaine "12" en une valeur entière égale à 12? "12" => 12
  * Comment réaliser l'opération inverse? 12 => "12"
  * Comment transformer la chaine "12" en un nombre flottant? "12" => 12.0
  * Comment transformer l'information 1 en un booléen `True`?
  * Comment réaliser l'opération inverse?
* Qu'est-ce qu'une affectation multiple, en une seule ligne d'instruction?
* Comment échange t-on la valeur de 2 variables `a` et `b`?
* Pourquoi l'instruction: `print("aujourd'hui j'ai "+ 18 +"ans")` ne fonctionne t-elle pas? Corriger cette expression (donner 2 moyens).
* Donner un exemple d'utilisation d'une expression formatée pour écrire le résultat du calcul de la force de gravitation $F=G\times m_1 \times m_2/d^2$, à partir des différentes variables.
* Quel sera le type associé à `F` si l'on réalise le calcul?
* Comment définir une fonction `F_gravitation` pour réaliser le calcul de `F`?
* Comment utiliser cette fonction pour calculer la force de gravitation Terre-Lune?

$M_T = 5.972\times 10^{24}kg$, 

$M_L = 7.348\times 10^{22}kg$, 

$d = 3.844\times 10^{8}m$, 

$G = 6.67\times 10^{-11}SI$