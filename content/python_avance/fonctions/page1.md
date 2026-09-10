---
Title : Fonctions
titleHidden: true
description: arguments, valeur par defaut d'un argument, annotations de type, modules, docstring, lambda fonction
weight: 9
---

* Un cours de niveau débutant sur les fonctions se trouve à la page suivante: [Lien](/python_bases/fonctions/page2/)

# Fonctions
Les fonctions permettent de rendre le script plus efficace, plus facile à lire et à vérifier. Une bonne pratique est de faire régulièrement du *remaniement* de son code : c'est-à-dire ré-écrire les parties du programme qui *fonctionnent* et les mettre dans une fonction ou un module. Cela évite aussi les répétitions. On remplace alors le code par un appel à une fonction.

## Généralités
Tous les langages de programmation fournissent un large ensemble de fonctions prêtes à être utilisées. Nous avons déjà rencontré diverses fonctions prédéfinies, de la librairie standard : `print`, `input`, `range`, `len`.


> *Définition :* Une fonction est un bloc de code auquel on donne un nom en vue de le réutiliser. L'appel de son nom exécute tout le bloc de code que cette fonction contient.

Pour créer une fonction, il faut la définir avec le mot clé `def`, suivi du nom de la fonction, d'une paire de parenthèses suivies de `:`.

## Return
La fonction peut retourner une valeur. Celle-ci est alors mise après le mot clé `return`.

```python
def salut():
  """Accueillir tout le monde"""
  return 'bonjour tout le monde'
```

On appelle cette fonction à l'aide de son nom, suivi des parenthèses : 

```python
salut()
# retourne (et affiche) 'bonjour tout le monde'
```

## Fonction python et fonction mathématique
On peut programmer une fonction pour qu’elle retourne la valeur y = f(x).

Exemple: soit la fonction mathématique $f : x \mapsto 3x^2+2$

Le script python correspondant sera:

```python
def f(x):
    return 3*x**2+2
```

Pour exécuter la fonction avec x=5, on fait: `f(5)`

Et cela retourne … $3\times 5^2+2$, soit 77.

Le mot-clé `return` joue, dans le script, un rôle analogue à celui du signe `=` dans l'écriture mathématique $y = f(x)$.


## Docstring
Il est d'usage, dans les *bonnes* pratiques, d'ajouter une chaîne de documentation, à la première ligne de la fonction : le *Docstring*.

Le *Docstring* est accessible à l'aide de la fonction `help` : 

```python
help(salut)
# affiche
Help on function salut in module __main__:

salut()
    Accueillir tout le monde
```

Pour plus d'informations sur le *Docstring*, et principalement le *Prototypage*, consulter la page [mise au point](/docs/NSI/langages/page5/#prototypage-d-une-fonction)

# Passage d'argument
## Définitions
> Un **paramètre** est une information dont la fonction a besoin pour s'exécuter.
> Un **argument** est une valeur transmise à une fonction.

Les paramètres sont placés à l'intérieur des parenthèses dans la définition de la fonction.

```python
def salut(nom):
  """Accueillir tout le monde par son nom"""
  return f'bonjour {nom}'
```

Lors de l'appel de la fonction, on place l'argument entre parenthèses : 

```python
salut('Brendon')
# retourne (affiche) 'bonjour Brendon'
```

## Portée des variables 
### internes
Lors de l'exécution de la fonction, la valeur `'Brendon'` est affectée à la variable `nom` : `nom = 'Brendon'`.

Seulement, la variable `nom` est une **variable interne** à la fonction, et n'existe que dans celle-ci. Elle n'est pas définie en dehors.

```python
>>> salut('Brendon')
'bonjour Brendon'
>>> nom
NameError: name 'nom' is not defined
```

La portée des paramètres et des variables déclarées dans la fonction est limitée à la fonction elle-même. Ce sont des variables **locales**.

### externes
Les variables déclarées dans le *main* sont accessibles à l'intérieur d'une fonction, en lecture.

Pour les modifier depuis l'intérieur de la fonction, deux cas se distinguent :

* si la variable désigne un objet **mutable** (une liste, un dictionnaire...), on peut modifier son *contenu* par un *effet de bord*, sans rien déclarer de particulier ;
* pour **réaffecter** la variable elle-même — qu'elle soit mutable ou non — il faut la déclarer explicitement avec le mot-clé `global` à l'intérieur de la fonction (voir le cours sur les [types construits](../../variables/page2/#portée-des-variables), qui détaille ce mécanisme).

**Exemple**:

```python
x = 9

def ajouter_un():
  global x
  x = x + 1
  return x

ajouter_un()
print(x)
# affiche 10
```

## Arguments positionnés

> Lorsqu'une fonction a besoin de plusieurs valeurs, ces dernières doivent correspondre aux paramètres qu'elle attend. Les arguments doivent être placés dans l'ordre des valeurs reçues.

```python
def publier_msg(message,user):
  """publier le message de l'utilisateur"""
  return f'{user} : {message}'
```

Que l'on appelle en renseignant les 2 arguments : 

```python
publier_msg('Ok pour moi','Branda')
# retourne (affiche) 'Branda : Ok pour moi'
```

*Rq : il existe aussi la possibilité d'utiliser des arguments non positionnés, et nommés. Une petite recherche sur le net devrait vous permettre d'en prendre connaissance si besoin.*

## Valeur par défaut
> Définir la *valeur par défaut* d'un paramètre dans une fonction permet à l'appel de la fonction d'utiliser cette valeur, sauf si une autre valeur est spécifiée à l'appel. 

Lorsqu'il y a plusieurs arguments, il faudra mettre les paramètres avec valeur par défaut à la fin : 

```python
def servir_cafe(client,nombre=1):
  """servir le nombre de cafés voulus au client"""
  return f'{client} commande {nombre} café(s)'
```

*Exemple d'utilisation :*

```python
servir_cafe('George')
# retourne 'George commande 1 café(s)'
servir_cafe('Jean',2)
# retourne 'Jean commande 2 café(s)'
```

## Annotations de type (paramètres et valeur de retour)
Depuis Python 3.5, on peut préciser, dans la définition d'une fonction, le type attendu pour chaque paramètre ainsi que le type de la valeur renvoyée. On parle d'**annotations de type** (*type hints*).

```python
def nom_fonction(parametre: type_attendu) -> type_de_retour:
    ...
```

*Exemple :*

```python
def f(x: float) -> float:
    return 3 * x ** 2 + 2
```

Ces annotations rendent la fonction plus facile à comprendre et à utiliser correctement (on sait, sans lire le corps de la fonction, ce qu'elle attend et ce qu'elle renvoie). Elles sont également exploitées par des outils externes (éditeurs de code, vérificateurs de type comme `mypy`) pour détecter des erreurs avant l'exécution.

**Attention, piège classique :** ces annotations sont purement indicatives. Python ne les **vérifie pas** et ne convertit **pas** automatiquement les arguments reçus vers le type annoncé.

```python
f(5)
# affiche 77   (un int, pas un float !)
```

Rien n'empêche d'appeler `f` avec un entier alors que `x` est annoté `float` : aucune erreur, aucune conversion, le calcul se fait simplement avec la valeur reçue. L'annotation est une indication à l'intention du programmeur (et des outils d'analyse), pas une contrainte imposée par l'interpréteur.

On peut combiner une annotation de type avec une valeur par défaut :

```python
def servir_cafe(client: str, nombre: int = 1) -> str:
    """servir le nombre de cafés voulus au client"""
    return f'{client} commande {nombre} café(s)'
```

*Pour aller plus loin :* les annotations d'une fonction sont accessibles via son attribut `__annotations__`, un peu comme le Docstring est accessible via `help` :

```python
f.__annotations__
# affiche {'x': <class 'float'>, 'return': <class 'float'>}
```

## Vérifier réellement les préconditions : `assert` et `raise`
Puisque les annotations de type ne sont pas contrôlées par Python, il faut, si l'on veut réellement **garantir** qu'une fonction reçoit des arguments valides, écrire ce contrôle soi-même. Deux outils permettent de le faire, avec un usage différent.

**`assert`** vérifie qu'une condition est vraie, et interrompt le programme avec une `AssertionError` si ce n'est pas le cas :

```python
def double(x: int) -> int:
    assert isinstance(x, int), "x doit être un entier"
    return x * 2

double(2.5)
# AssertionError: x doit être un entier
```

`assert` est surtout destiné à vérifier des conditions qui **ne devraient jamais être fausses si le programme est correct** — des invariants internes, utiles pendant le développement et les tests. Un détail important : les instructions `assert` peuvent être **désactivées globalement** au lancement de Python (option `-O`), auquel cas elles ne sont plus exécutées du tout. Il ne faut donc jamais s'appuyer sur `assert` pour une vérification qui doit rester active en toutes circonstances, en particulier pour valider une donnée saisie par un utilisateur.

**`raise`** lève explicitement une exception, d'un type que l'on choisit, et reste **toujours actif**, quelles que soient les options de lancement :

```python
def double(x: int) -> int:
    if not isinstance(x, int):
        raise TypeError("x doit être un entier")
    return x * 2

double(2.5)
# TypeError: x doit être un entier
```

**En résumé :** on préfère `assert` pour des vérifications de mise au point (aides au débogage, à retirer mentalement de la logique du programme), et `raise` pour valider de façon fiable les entrées d'une fonction destinée à être réellement utilisée — par exemple par d'autres personnes, ou dans un programme final. La fonction `isinstance(objet, type)`, qui renvoie `True` si `objet` est bien une instance de `type`, est l'outil le plus courant pour ce genre de vérification.

# Importer des fonctions
## Modules : fonctions dans un fichier séparé
Une fonction peut être placée dans un autre fichier. On a alors:

* un fichier principal (le programme main)
* un ou plusieurs fichiers annexes (modules)

Ces fonctions ne deviennent accessibles que si on les **importe**.

> Utiliser le mot clé `import` pour importer un module et accéder à toutes ou partie de ses fonctions.

Le programme principal doit alors faire référence aux modules.
On utilise l’une des 3 manières proposées ci-dessous:

```python
import module
from module import *
import module as alias
```

Il est préconisé de ne charger que les fonctions utiles du module:

```python
from module import fonction
```




La manière avec laquelle on utilise la fonction dépend de l'import du module.

Les exemples suivants sont issus du cours [https://www.courspython.com/modules.html](https://www.courspython.com/modules.html)

| import | appel de la fonction | commentaire |
| --- | --- | --- |
| import puissance | u = puissance.carre(a)  |  |
| from puissance import carre, cube | u = carre(a)  | on importe uniquement les fonctions nécessaires |
| from puissance import * | u = carre(a)  | déconseillée car elle "pollue" l'espace de nom |
|   `import puissance as pu`| u = pu.carre(a) | import du module avec un alias |
|  `from puissance import carre as ca`| u = ca(a) | import d'une fonction d’un module et on lui donne un alias |
| `import package1.module1`| u = package1.module1.carre(a) | import d'une partie du package (le dossier) |


## Modules
Dans un projet plus grand, les fonctions peuvent être mises dans des **modules** (des fichiers séparés). On doit alors les importer pour bénéficier d'une extension du langage. Certains modules très utiles: `math`, `turtle`, `random`, …

Tout fichier Python peut être importé. C'est particulièrement facile lorsque les fichiers sont dans le même répertoire. Supposons que `A.py` et `B.py` le soient, on peut mettre dans `B.py` l'instruction `from A import *` : toute fonction (ou variable) déclarée dans `A.py` sera alors utilisable dans `B.py`.

## `if __name__ == "__main__"`
Cette syntaxe idiomatique de Python permet de n'exécuter du code présent dans un fichier/module que si ce fichier/module est directement exécuté. Ce code N'est PAS exécuté lorsque ce fichier/module est importé. Cette approche est généralement utilisée pour inclure du code de test dans un module.

```python
def ma_fonction():
    ...

if __name__ == "__main__":
    # Ce bloc n'est exécuté que si on lance ce fichier, pas s'il est importé depuis un autre module
    ma_fonction()
```

# Lambda fonction: fonctions anonymes
On peut avoir recours aux fonctions anonymes pour des tâches ponctuelles qui ne nécessitent pas la création d'une fonction complète.

La syntaxe est la suivante:

```
lambda arguments : expression
```

Les arguments sont les paramètres de la fonction et l'expression calcule la valeur de retour. 

Remarquez l'absence d'utilisation du mot-clé `return`, contrairement à une fonction classique.

Exemple:

```python
>>> square = lambda x : x ** 2
>>> square(2)
4
```

Les fonctions *lambda* peuvent être utilisées pour trier une liste selon une clé spécifique: [doc officielle](https://docs.python.org/3/howto/sorting.html)

```python
nodes = [('A', 20), ('B', 15), ('C', 12), ('D', 10), ('E', 8), ('F', 5), ('G', 2)]
nodes.sort(key= lambda x: x[1])
nodes
```

résultat:

```python
[('G', 2), ('F', 5), ('E', 8), ('D', 10), ('C', 12), ('B', 15), ('A', 20)]
```

# Liens

##### {{% button href="../page1" icon="bullhorn" style="caution" %}}Cours{{% /button %}} les fonctions
##### {{% button href="../page2" icon="palette" style="tip" %}}TP4{{% /button %}} 

