---
Title: TP fonctions python
description: TP sur les fonctions python, et les boucles
hidden: true
weight: 10
---

# Fonctions programmées
Les fonctions permettent de rendre le script plus efficace, plus facile à lire et à vérifier. Un bonne pratique est de faire régulierement du *remaniement* de son code : C'est à dire ré-écrire les parties du programme qui *fonctionnent* et les mettre dans une fonction ou un module. Cela evite aussi les répétitions. On remplace alors le code par un appel à une fonction.



> *Définition :* Une fonction est un bloc de code auquel on donne un nom en vue de le reutiliser. L'appel de son nom exécute tout le bloc de code que cette fonction contient.


## système def + return
Pour créer une fonction, il faut la definir avec le mot clé **`def`**, suivi du nom de la fonction, d'une paire de parenthèses suivies de `:`.


La fonction peut retourner une valeur. Celle-ci est alors mise après le mot clé `return`.

*Exemple:* 

```python
def salut():
  """Accueillir tout le monde"""
  return 'bonjour tout le monde'
```

## appeler la fonction
On appelle cette fonction à l'aide de son nom, suivi des parenthèses : 

```python
salut()
# retourne (et affiche) 
'bonjour tout le monde'
```

APPELLER = EXECUTER LA FONCTION

## placer la valeur retournée dans une variable
Souvent, cette donnée retournée doit être *affectée à une variable*:

```python
message = salut()
print(message)
# affiche: 
bonjour tout le monde
```

# Travaux pratiques 
## fonction sans paramètre
Un cours sur les fonctions se trouve à la page suivante: [Lien](/docs/python/pages/fonctions/page2/)

* *Question a*: Ecrire une fonction appelée `etoiles` en python qui écrit une série de 5 symboles `*`, séparés chacun par un espace:

```
* * * * * 
```

> Appeler (exécuter) la fonction: faire suivre le nom de la fonction par des parenthèses `()`: 

```
> etoiles()
```

Pour afficher la ligne, on peut placer l'instruction suivante dans le programme: 

```python
print(etoiles())
```

> Solution (ne pas regarder trop vite)

```python
def etoiles():
    return '* * * * *'

print(etoiles())
```

> utiliser une **boucle bornée** pour répéter 5 fois l'appel de la fonction et afficher l'image suivante:

```
* * * * * 
* * * * * 
* * * * * 
* * * * * 
* * * * * 
```

> Solution (ne pas regarder trop vite)

```python
for i in range(5):
   print(etoiles()) 
```


* *Question b*:  Recopier le script utilisé.

## Fonction avec paramètres
### Principe
Souvent, la fonction traite ou calcule sur un ou plusieurs paramètres qui lui sont passés lors de l'appel de la fonction.

Pour prévoir ceci, il faudra définir un ou plusieurs paramètres lors de la constuction de la fonction.

Par exemple, si l'on souhaite améliorer la fonction `salut` et personnaliser le message:

```python
def salut(nom):
  """Accueillir chacun par son nom"""
  return 'bonjour '+ nom
```

> Appeler cette fonction en plaçant le prenom 'John' entre les parenthèses: 

```python
def salut(nom):
  return 'bonjour '+ nom

print(salut("John"))
```

Vous devriez obtenir: *bonjour John*

### traitement automatisé avec une boucle `for`
> Utiliser cette fonction avec les prenoms de la liste `Beatles = ['John', 'Paul', 'Ringo', 'George']`

```python
Beatles = ['John', 'Paul', 'Ringo', 'George'] 
for name in Beatles:
    ...
```

Vous devriez obtenir l'affichage:

```
bonjour John
bonjour Paul
bonjour Ringo
bonjour George
``` 

*question c.* Recopier le script sur votre *feuille réponse*. 

> Solution (ne pas regarder trop vite)

```python
Beatles = ['John', 'Paul', 'Ringo', 'George'] 
for name in Beatles:
    print(salut(name))
```



## TP: ASCII-art
L'Ascii art consiste à représenter un dessin ou une image uniquement en utilisant des caractères ascii. La page suivante montre des créations artistiques par rubrique: [asciiart.eu](https://www.asciiart.eu/)

On cherche à realiser des figures à partir de caractères `*` ou `@`.

**ex1:** Ecrire le script d'une fonction que vous appelerez `ligne`, qui prend comme paramètre un entier `n`, et retourne une ligne de `n` caractères `@`.

*Exemple:*

```python
def ligne(n):
    return '@' * ...

> ligne(5)
@@@@@
```

**ex2:** Utilisez votre fonction `ligne`, et appelez celle-ci dans une boucle bornée pour créer l'image suivante:

```python
for i in range(...):
    print(ligne(...))
# affiche
@@@@@
@@@@@
@@@@@
@@@@@
@@@@@
```

**ex3:** Créez une fonction `carre` à partir du script précédent. Cette fonction devra créer un carré de `@` de la dimension `n` (paramètre). Cette fonction n'aura pas de valeur de *retour* (pas de return), les affichage seront produits par la fonction `print`

```python
def carre(n):
    for ... : 
        print(ligne(...))

> carre(5)
# affiche
@@@@@
@@@@@
@@@@@
@@@@@
@@@@@
```

**ex4:** Utiliser la fonction `carre` pour créer l'affichage suivant:

```python
for i in range (...):
    carre(...)
    print()

# affiche
@

@@
@@

@@@
@@@
@@@

@@@@
@@@@
@@@@
@@@@
```

**ex5:** Modifiez la fonction `etoiles` (ci-dessous) pour que celle-ci utilise un paramètre **(nb)**. Ce paramètre definit le nombre d'espaces entre les 2 symboles `*` de la ligne. La ligne n'affiche que 2 symboles `*`. 

Par exemple, `etoiles(5)` retourne `*     *` avec 5 espaces:

```python
def etoiles(nb):
    return '*' + ... + '*'

print(etoiles(5))
# affiche
*     *
``` 

**ex6:** afficher la figure suivante (un seul espace à chaque ligne entre 2 etoiles)

```python
for i in range(..):
  print(etoile(..))

# resultat
* *
* *
* *
* *
```



**ex7:** Vous appelerez ensuite cette fonction avec des arguments judicieusement choisis, afin de dessiner les figures suivantes:

figure 1:

```python
for i in range(..):
  print(etoile(..))

# resultat
**
* *
*  *
*   *
*    *
```

figure 2:

```
*    *
*   *
*  *
* *
**
```

figure 3:
```
**
* *
*  *
*   *
*    *
*    *
*   *
*  *
* *
**
```

*Astuce: avez vous fait en sorte d'utiliser au maximum des boucles bornées avec un variant de boucle?*

**ex8:** modifier la fonction ainsi que le programme pour afficher maintenant un sapin de Noel:

```
      **
     *  *
    *    *
   *      *
  *        *
      **
      **
```

**ex 9:** (a) Afficher une image à partir d'une Liste. Compléter le script:

```python
L1 = [' ^___^','" o o "', '===X===','   "  ']
for l in L1:
    print(...
```

(b) Afficher une image à partir d'une liste de listes de caractères.

```python
L2 = [[' ', '^', '_', '_', '_', '^'], ['"', ' ', 'o', ' ', 'o', ' ', '"'], ['=', '=', '=', 'X', '=', '=', '='], [' ', ' ', ' ', '"', ' ', ' ']]

for l in L2:
    s = ''
    for c in l:
        s += ...
    print(...
```


**ex 10:** Quelle est l'image cachée dans cette matrice?

```python
M = [['20', '2F', '5C', '5F', '2F', '5C', '20'],
     ['28', '20', '2E', '20', '2E', '20', '29'],
     ['3D', '5C', '5F', '76', '5F', '2F', '3D']]
```

*Solution partielle:*

```python
for l in M:
    s = ''
    for r in l:
        s += ...
    print(...
```

*Rappels:* 

* *Conversion valeur hexa -> decimal: utiliser `int(valeur,16)`*
* *Conversion decimal -> ascii: utiliser `chr`*


# Liens et sources
* notebook du site [clogique](https://clogique.fr/nsi/notebook/?from=/nsi/premiere/td_tp/TP_Art_Ascii.ipynb#Exercice-7)

# Suite
### Lecture - eciture dans un fichier: [Lien](../page54)
### Projet transformer image -> ASCII: [Lien](../page53)
### Utiliser des fonctions pour calculer: [Lien](../page52)

