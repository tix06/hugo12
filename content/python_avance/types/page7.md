---
Title : TD - types simples (corrigé)
description: corrigé du TD sur int, float, str, bool
hidden: true
weight: 6
---

# Corrigé — TD : Types simples en Python



---

## Script 1 — Conversions de types

**Q1.** Le script lève une erreur :
```
ValueError: invalid literal for int() with base 10: '19.9'
```
Aucun prix ne s'affiche.

**Q2.** `str(19.90)` produit la chaîne `'19.9'` (le zéro final disparaît). Or `int()` appliqué à une chaîne n'accepte que des chaînes représentant un **entier** — il ne fait pas d'arrondi, contrairement à `int()` appliqué à un float qui, lui, **tronque**. Convertir en chaîne puis en entier n'est donc pas équivalent à arrondir un flottant.

**Q3.** Version attendue :
```python
def preparer_etiquette(prix):
    prix_arrondi = round(prix)
    print("Prix à afficher :", prix_arrondi, "euros")

preparer_etiquette(19.90)
# Prix à afficher : 20 euros
```
Point clé à observer : utilisation de `round()` directement sur le float, sans passer par `str`. Une réponse utilisant `int(prix + 0.5)` peut être acceptée (mais ne fonctionne pas pour les négatifs) ; c'est l'occasion de rappeler que `round()` est la fonction adaptée pour arrondir.

---

## Script 2 — Chaînes de caractères

**Q1.** Le script lève une erreur :
```
TypeError: 'str' object does not support item assignment
```

**Q2.** Les chaînes de caractères sont des objets **immuables** en Python : une fois créées, elles ne peuvent pas être modifiées caractère par caractère via l'affectation indexée (`nom[0] = ...`). Toute transformation doit produire une **nouvelle** chaîne.

**Q3.** Version attendue, par exemple :
```python
def anonymiser(nom):
    return '*' * (len(nom) - 2) + nom[-2:]

print(anonymiser('Dupont'))
# ****nt
```
Points clés à valoriser :
- usage du slicing `nom[-2:]` (index négatif vu dans le cours) pour récupérer les deux derniers caractères ;
- construction d'une nouvelle chaîne avec `*` (répétition) et `+` (concaténation), sans tentative de modification en place ;
- une solution utilisant `nom[:-2]` remplacé caractère par caractère dans une boucle est correcte mais moins élégante.

---

## Script 3 — Booléens et nombres flottants

**Q1.**
```
Erreur de caisse
<class 'bool'>
```

**Q2.** `0.1 + 0.1 + 0.1` ne vaut pas exactement `0.3` en mémoire à cause de la représentation limitée des flottants (norme IEEE 754, mentionnée dans le cours) : le résultat réel est légèrement différent de `0.3` (par exemple `0.30000000000000004`), donc `compte == 0.3` renvoie `False`. La seconde ligne affichée confirme que le résultat d'une comparaison est bien de type `bool`.

**Q3.** Version attendue :
```python
if round(compte, 2) == 0.3:
    print("Le compte est bon")
else:
    print("Erreur de caisse")
```
Point clé à valoriser : on ne compare pas deux flottants directement avec `==`, on arrondit d'abord à une précision raisonnable avec `round()` (fonction déjà vue dans le cours). Une solution utilisant `math.isclose` peut être acceptée en bonus si l'élève l'a rencontrée ailleurs, mais n'est pas exigée puisqu'elle n'est pas dans le cours fourni.

---

## Grille de correction indicative

| Question | Compétence évaluée | Barème indicatif |
|---|---|---|
| Q1 (×3) | Lire du code et prédire un résultat / une erreur sans exécuter | 1 pt chacune |
| Q2 (×3) | Mobiliser la notion exacte du cours pour expliquer | 2 pts chacune |
| Q3 (×3) | Modifier le code en respectant une contrainte précise | 3 pts chacune |

Total : 18 points.
