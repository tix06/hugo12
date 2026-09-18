---
Title : TP4 - fonctions (corrigé)
hidden: true
description: corrigé du TD sur la valeur par défaut, les annotations de type, les arguments positionnés
weight: 11
---

# Corrigé — TD : Fonctions en Python

*Ce corrigé est destiné à l'enseignant.*

---

## Script 1 — Valeur par défaut

**Q1.**
```
['Alice', 'Bob']
['Alice', 'Bob']
```
Les deux `print` affichent la **même** liste, contenant les deux prénoms.

**Q2.** La valeur par défaut `liste=[]` n'est évaluée **qu'une seule fois**, au moment de la définition de la fonction — pas à chaque appel. Comme une liste est un objet **mutable**, cette même liste par défaut est réutilisée (et modifiée par `append`) à chaque appel où `liste` n'est pas précisé. `classe_A` et `classe_B` finissent donc par désigner le même objet, qui contient les deux prénoms. C'est un piège classique de Python, à mi-chemin entre la notion de « valeur par défaut » et celle de mutabilité vue dans le cours sur les types construits.

**Q3.** Version attendue :
```python
def ajouter_eleve(nom, liste=None):
    if liste is None:
        liste = []
    liste.append(nom)
    return liste

classe_A = ajouter_eleve('Alice')
classe_B = ajouter_eleve('Bob')

print(classe_A)  # ['Alice']
print(classe_B)  # ['Bob']
```
Point clé: on ne met jamais un objet mutable comme valeur par défaut si on veut un comportement indépendant à chaque appel ; le motif `liste=None` puis `if liste is None: liste = []` est la solution standard, qui force la création d'une nouvelle liste à **chaque appel**.

---

## Script 2 — Annotations de type

**Q1.**
```
5.0
<class 'float'>
```

**Q2.** Les annotations `x: int` et `-> int` sont purement indicatives : Python ne les vérifie pas et ne convertit rien automatiquement. Rien n'empêche donc d'appeler `double` avec un `float` (`2.5`) : le calcul `2.5 * 2` se fait normalement et renvoie `5.0`, un `float`, alors que l'annotation de retour promettait un `int`. C'est le piège signalé dans le cours sur les annotations de type.

**Q3.** Version attendue, avec `raise` :
```python
def double(x: int) -> int:
    """renvoie le double de x"""
    if not isinstance(x, int):
        raise TypeError("x doit être un entier")
    return x * 2

double(2.5)
# lève TypeError: x doit être un entier
double(3)
# renvoie 6
```
Une version avec `assert` est également acceptable sur le plan technique :
```python
def double(x: int) -> int:
    assert isinstance(x, int), "x doit être un entier"
    return x * 2
```
Point clé: `double` est une fonction destinée à être **appelée avec des données externes** (par un autre programme, un autre élève, un utilisateur...), donc `raise` est le choix le plus fiable, car une instruction `assert` peut être désactivée globalement (option `-O` de Python) et ne serait alors plus jamais exécutée. `assert` reste pertinent pour des vérifications internes de mise au point, mais pas pour garantir durablement le contrat d'une fonction. Une solution qui se contente de convertir avec `int(x * 2)` doit être écartée : elle masque l'erreur au lieu de la signaler (`int(2.5 * 2)` donnerait silencieusement `5`).

---

## Script 3 — Arguments positionnés

**Q1.**
```
Les cours reprennent lundi : Le Directeur
```

**Q2.** Les arguments sont transmis **par position** : le premier argument de l'appel (`'Le Directeur'`) est affecté au premier paramètre (`message`), et le second (`'Les cours reprennent lundi'`) au second paramètre (`user`) — quel que soit le sens que ces valeurs semblent avoir pour un lecteur humain. Le nom du paramètre dans la définition ne « devine » jamais ce que représente la valeur reçue : seul l'ordre compte pour les arguments positionnés.

**Q3.** Deux solutions possibles :
```python
# Solution 1 : réordonner les arguments positionnés
annonce = publier_msg('Les cours reprennent lundi', 'Le Directeur')

# Solution 2 : utiliser des arguments nommés, indépendants de l'ordre
annonce = publier_msg(user='Le Directeur', message='Les cours reprennent lundi')
```
Point clé: la solution 2 est plus robuste — elle reste correcte même si l'ordre des paramètres dans la définition de `publier_msg` changeait un jour, contrairement à la solution 1 qui redevient fausse si l'ordre change. C'est l'occasion de relier ce script à la remarque du cours sur les arguments nommés.

---

## Script 4 — Chaînage de fonctions

**Q1.**
```
TypeError: can't multiply sequence by non-int of type 'float'
```
L'exécution s'arrête sur une erreur au moment de l'appel à `appliquer_remise`.

**Q2.** `ligne.split(';')` renvoie deux chaînes de caractères (`str`) ; `extraire_prix` renvoie donc `prix` sous forme de **chaîne** (`'12.50'`), et non de nombre. Or ce retour devient directement l'argument reçu par `appliquer_remise`, qui essaie de calculer `prix * taux`, c'est-à-dire une multiplication entre un `str` et un `float`. Python autorise `str * int` (répétition de la chaîne) mais pas `str * float`, d'où l'erreur. C'est le piège central du **chaînage de fonctions** : le type de la valeur renvoyée par une fonction doit être compatible avec le type attendu par les paramètres de la fonction suivante — ici, une conversion de type a été oubliée entre les deux étapes.

**Q3.** Version attendue :
```python
def extraire_prix(ligne):
    """extrait le prix d'une ligne du type 'Livre;12.50'"""
    _, prix = ligne.split(';')
    return float(prix)

def appliquer_remise(prix, taux=0.9):
    """applique un taux de remise (10 % par défaut)"""
    return prix * taux

def afficher_ticket(article, prix_final):
    """affiche la ligne de ticket de caisse"""
    return f"{article} : {prix_final:.2f} €"

ligne = "Livre;12.50"
article, _ = ligne.split(';')

prix = extraire_prix(ligne)
prix_remise = appliquer_remise(prix)
print(afficher_ticket(article, prix_remise))
# Livre : 11.25 €
```
Point clé: il suffit de convertir `prix` en `float` **dès sa sortie** de `extraire_prix`, avant qu'il ne soit transmis à la fonction suivante. C'est l'occasion d'insister sur le fait que dans une chaîne `f1 → f2 → f3`, chaque maillon doit renvoyer une valeur du type que le maillon suivant sait exploiter : `split` renvoie toujours des `str`, jamais des nombres, même si la chaîne « ressemble » à un nombre.

---

## Grille de correction indicative

| Question | Compétence évaluée | Barème indicatif |
|---|---|---|
| Q1 (×4) | Lire du code et prédire un résultat / une erreur sans exécuter | 1 pt chacune |
| Q2 (×4) | Mobiliser la notion exacte du cours pour expliquer | 2 pts chacune |
| Q3 (×4) | Modifier le code en respectant une contrainte précise | 3 pts chacune |

Total : 24 points.
