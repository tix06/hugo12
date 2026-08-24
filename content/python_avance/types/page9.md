---
Title : TP2 - types construits
description: travaux dirigés sur listes, tuples, dictionnaires, mutabilité
hidden: true
weight: 8
---

# TD : Types construits en Python

*Ce TD s'appuie sur le [cours sur les types construits](../page2/). Pour chaque script, tu dois répondre aux 3 questions dans l'ordre, sans exécuter le code avant d'avoir répondu à la question 1.*

**Consignes de rédaction :**
- Question 1 : écris précisément ce que le programme affiche (ou l'erreur qu'il produit), ligne par ligne si nécessaire.
- Question 2 : justifie ta prédiction en t'appuyant sur une notion précise du cours (nomme-la).
- Question 3 : propose une version corrigée ou modifiée du script, puis explique en une phrase ce que tu as changé et pourquoi.

---

## Script 1 — Listes et aliasing

```python
def ajouter_note(notes, valeur):
    notes.append(valeur)
    return notes

classe_A = [12, 14, 9]
classe_B = classe_A
ajouter_note(classe_B, 18)

print(classe_A)
print(classe_B)
```

**Q1.** Que produit l'exécution de ce script ?

**Q2.** Explique précisément ce qui se passe, en citant la notion du cours concernée.

**Q3.** Modifie ce script pour que `ajouter_note(classe_B, 18)` ajoute bien `18` à `classe_B` sans que `classe_A` soit modifiée. Les deux listes doivent rester indépendantes dès leur création.

---

## Script 2 — Tuples et éléments mutables

```python
eleve = ("Dupont", [15, 12, 18])

def maj_notes(fiche, note):
    fiche[1].append(note)

maj_notes(eleve, 20)
print(eleve)

eleve[1] = [0]
```

**Q1.** Que produit l'exécution de ce script ? (distingue bien ce qui se passe avant et après la dernière ligne)

**Q2.** Explique précisément ce qui se passe, en citant la notion du cours concernée.

**Q3.** La dernière ligne (`eleve[1] = [0]`) provoque une erreur. Sans changer le type de `eleve` (qui doit rester un tuple contenant un nom et une liste de notes), écris une instruction qui **vide** la liste de notes de l'élève (elle doit devenir `[]`).

---

## Script 3 — Dictionnaires et portée des variables

```python
stock = {'pommes': 10, 'poires': 5}

def vendre(fruit, quantite):
    stock[fruit] -= quantite

def reinitialiser():
    stock = {}

vendre('pommes', 3)
print(stock)

reinitialiser()
print(stock)
```

**Q1.** Que produisent les deux `print` ?

**Q2.** Explique précisément pourquoi `vendre` et `reinitialiser` n'ont pas le même effet sur la variable globale `stock`, en citant la notion du cours concernée.

**Q3.** Propose **deux** façons différentes de corriger `reinitialiser` pour qu'elle vide réellement le dictionnaire global `stock`.

# Suite
##### {{% button href="../page2" icon="bullhorn" style="caution" %}}Cours{{% /button %}} 
##### {{% button href="../page9" icon="palette" style="tip" %}}TP2{{% /button %}} decouverte du cours
##### {{% button href="../page3" icon="palette" style="important" %}}TD2a{{% /button %}} les types construits, les copies par valeur et reference sur Pythontutor
##### {{% button href="../page4" icon="palette" style="important" %}}TD2b{{% /button %}} le parcours de liste, compréhension de liste et tracé graphique
##### {{% button href="../page5" icon="palette" style="tip" %}}TP3{{% /button %}} les tableaux


