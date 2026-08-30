---
Title: TP5a fonctions python
description: TP sur les fonctions python, et les boucles
hidden: true
weight: 11
---



## Ex 1: fonction sans paramètre
La fonction suivante va retourner un dessin réalisé à partir de symboles ascii du clavier:

```
def figure_petit_chat():
  fig = "^----^"
  print(fig)
  fig = "_00_"
  print(fig)
  fig = "|-==-|"
  print(fig)
```

* Saisir le script dans une cellule python et executer.
* Dans une nouvelle cellule/interpreteur python: appeler la fonction. Ecrire: `figure_petit_chat()`

```python
>>> figure_petit_chat()

 ^----^
  _00_
 |-==-|
```


*La plupart du temps, on evitera d'utiliser la fonction `print` à l'intérieur d'une fonction. Sauf cas particulier comme ci-dessus.*

La fonction suivante va justement utiliser le mot clé `return` prévu pour qu'il y ait une *sortie*.

```python
def dessine():
  n = 3
  dessin = ""
  for i in range(n):
    dessin = dessin + "x*x"
  return dessin
```

* **Question a:** Executer la fonction du 2e script: `>>> print(dessine())` 

Quel est le motif dessiné? Pourquoi?

## Ex 2: fonction avec paramètre

> Ecrire une fonction `salut` qui prend pour paramètre `nom` et qui retourne une chaine de caractères `bonjour + "nom"`. 

Exemples d'appels de la fonction `salut`:

```python
salut("John")
# affiche
bonjour John
salut("Paul")
# affiche
bonjour Paul
salut("Ringo")
# affiche
bonjour Ringo
salut("George")
# affiche
bonjour George
```  

* **Question b:** Citer l'un des avantages d'utiliser une fonction. (répétition)

## Ex 3: fonction pour calculer
1. Écrire une fonction `cube` qui retourne le `cube` de son argument: `x**3`
2. Écrire une fonction `volumeSphere` qui calcule le volume d’une sphère de rayon r fourni en argument et qui utilise la fonction cube.

*Donnée:*

$$V = \tfrac{4}{3}\times\pi\times R^3$$

3. Calculer le volume en $cm^3$ d'une sphere de rayon 10cm (à l'aide de la fonction `volumeSphere`)

## Ex 4: Importer des fonctions
Importer les fonctions `degrees` et `radians` du module `math` et completer le tableau:

| angle degrés | angle radians |
|--- |--- |
| 45 |    |
| 35 |    |
|    | 0.657 |
|    | 0.1 |

# Liens
##### {{% button href="../page2" icon="bullhorn" style="caution" %}}Cours{{% /button %}} 
##### {{% button href="../page3" icon="palette" style="tip" %}}TP5a{{% /button %}} Fonctions, applications
##### {{% button href="../page52" icon="palette" style="tip" %}}TP5b{{% /button %}} fonctions utiles pour calculer
##### {{% button href="../page51" icon="palette" style="tip" %}}TP5c{{% /button %}} boucles et fonctions, traitements automatisés
