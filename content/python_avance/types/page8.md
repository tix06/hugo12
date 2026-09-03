---
Title : Fiche d'exercices - variables et types
titleHidden: true
hidden: true
description: exercices courts sur None, bool, math, references, methodes de chaines
weight: 6
---

# Fiche d'exercices : variables et types natifs

*Cette fiche s'appuie sur le [cours avancé](../page1/) ainsi que certaines notions du cours [python débutant](/python_bases/). Chaque exercice est court et peut se faire au stylo (en prédisant le résultat) avant vérification à l'IDE.*

---

## Exercice 1 — `None`

```python
def verifier_age(age):
    if age >= 18:
        return "majeur"
    # pas d'instruction return si age < 18

resultat = verifier_age(15)
print(resultat)
print(type(resultat))
```

Sans exécuter : que vont afficher les deux `print` ? Justifie en une phrase.

---

## Exercice 2 — `bool`, un sous-type de `int`

Sans exécuter, donne la valeur de chacune des expressions suivantes :

```python
True + True
False + 10
True == 1
True * 5
```

---

## Exercice 3 — bibliothèque `math`

Calcule à la main (ou vérifie à l'IDE) :

```python
import math
math.sqrt(16)
math.floor(7.9)
math.ceil(7.1)
math.pow(2, 10)
```

*Indications : `math.floor` -> arrondit vers le bas (plancher). `math.ceil` arrondit vers le haut.*

---

## Exercice 4 — `round`

Donne le résultat de :

```python
round(2.5)
round(3.5)
round(3.14159, 3)
```

*Remarque : `round(2.5)` te surprendra peut-être — Python utilise l'arrondi "au pair le plus proche", pas l'arrondi classique. Cherche pourquoi si le résultat ne correspond pas à ton intuition.*

---

## Exercice 5 — typage dynamique et affectation multiple

```python
a = 5
print(type(a))
a = "cinq"
print(type(a))

x, y = y, x = 1, 2
print(x, y)
```

1. Que produisent les deux premiers `print` ? Quelle notion du cours cela illustre-t-il ?
2. La ligne `x, y = y, x = 1, 2` est syntaxiquement valide : il s'agit d'une **affectation chaînée** (`cible1 = cible2 = expression`), combinée à l'affectation multiple vue dans le cours. Sans exécuter, prédis ce qu'affiche `print(x, y)`. *Indice : l'expression `1, 2` n'est évaluée qu'une seule fois, puis affectée à chaque cible.*
3. Ecris cette expression de manière plus conventionnelle, en 2 lignes.

---

## Exercice 6 — références, `id`, `is` et `==`

```python
a = "bonjour"
b = "bonjour"
c = a

print(a == b)
print(a is c)
```

1. Prédis le résultat des deux `print`.
2. Explique avec tes mots la différence entre `==` et `is`.
3. Que donnent les tests `id(a) == id(b)`, et `id(a) == id(c)` ? Expliquer.

---

## Exercice 7 — méthodes de chaînes

Pour la chaîne `phrase = "  Les Chaines De Caracteres En Python  "`, écris (au stylo) le code Python qui permettrait de :

1. supprimer les espaces inutiles au début et à la fin ;
2. mettre toute la phrase en minuscules ;
3. remplacer `"python"` par `"NSI"` ;
4. découper la phrase nettoyée en une liste de mots (séparateur : l'espace) ;
5. recoller cette liste de mots avec un tiret `-` comme séparateur.


---

## Exercice 8 — f-strings

Réécris chacun des `print` suivants en utilisant une f-string :

```python
nom = "Turing"
annee = 1912
print("Nom : " + nom + ", né en " + str(annee))
print("{} a {} ans".format(nom, 2024 - annee))
```

---

## Exercice 9 — parser une chaîne

On dispose de la chaîne suivante, représentant une date au format ISO :

```python
d = "2024-09-02"
```

1. En utilisant le **slicing** `d[a:b]`, extrais séparément l'année, le mois et le jour dans trois variables `annee`, `mois`, `jour`.
2. Propose une seconde solution utilisant la méthode `split`.
3. Laquelle des deux méthodes te semble la plus robuste si le format de date changeait (par exemple un jour à un seul chiffre) ? Justifie.

# Suite
##### {{% button href="../page1" icon="bullhorn" style="caution" %}}Cours{{% /button %}} 
##### {{% button href="../page6" icon="palette" style="tip" %}}TP1{{% /button %}} Types simples
{{% button href="../page7" icon="lightbulb" style="tip" %}}Corrigé du TP1{{% /button %}}
##### {{% button href="../page8" icon="palette" style="important" %}}TD1{{% /button %}} Variables et types natifs
