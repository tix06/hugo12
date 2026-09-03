---
Title : TP variables
titleHidden: true
description: TP1 sur variables et types
hidden: true
weight: 5
---

# TP1 : Variables et types simples en Python

*Ce TD s'appuie sur le [cours sur les types simples](../page1/). Pour chaque script, tu dois répondre aux 3 questions dans l'ordre, sans exécuter le code avant d'avoir répondu à la question 1.*

**Consignes de rédaction :**
- Question 1 : écris précisément ce que le programme affiche (ou l'erreur qu'il produit), ligne par ligne si nécessaire.
- Question 2 : justifie ta prédiction en t'appuyant sur une notion précise du cours (nomme-la).
- Question 3 : propose une version corrigée ou modifiée du script, puis explique en une phrase ce que tu as changé et pourquoi.

---

## Script 1 — Conversions de types

```python
def preparer_etiquette(prix):
    prix_str = str(prix)
    prix_arrondi = int(prix_str)
    print("Prix à afficher :", prix_arrondi, "euros")

preparer_etiquette(19.90)
```

**Q1.** Que produit l'exécution de ce script ?

**Q2.** Explique précisément ce qui se passe, en citant la notion du cours concernée.

**Q3.** Modifie la fonction `preparer_etiquette` pour qu'elle affiche le prix arrondi à l'entier le plus proche (ici `20`), sans passer par une conversion en chaîne de caractères.

---

## Script 2 — Chaînes de caractères

```python
def anonymiser(nom):
    nom[0] = '*'
    return nom

resultat = anonymiser('Dupont')
print(resultat)
```

**Q1.** Que produit l'exécution de ce script ?

**Q2.** Explique précisément ce qui se passe, en citant la notion du cours concernée.

**Q3.** Réécris `anonymiser` pour qu'elle renvoie une **nouvelle** chaîne où seuls les deux derniers caractères du nom sont visibles, le reste étant remplacé par des `*` (par exemple `'Dupont'` devient `'****nt'`). Tu dois utiliser le slicing.

---

## Script 3 — Booléens et nombres flottants

```python
compte = 0.1 + 0.1 + 0.1

if compte == 0.3:
    print("Le compte est bon")
else:
    print("Erreur de caisse")

print(type(compte == 0.3))
```

**Q1.** Que produit l'exécution de ce script ? (les deux lignes affichées)

**Q2.** Explique précisément ce qui se passe, en citant la notion du cours concernée.

**Q3.** Modifie la condition du `if` pour que le programme affiche bien `"Le compte est bon"` lorsque `compte` vaut, à la précision voulue, `0.3`. Tu ne dois pas changer la ligne qui calcule `compte`.

# Suite
##### {{% button href="../page1" icon="bullhorn" style="caution" %}}Cours{{% /button %}} 
##### {{% button href="../page6" icon="palette" style="tip" %}}TP1{{% /button %}} Types simples
##### {{% button href="../page8" icon="palette" style="important" %}}TD1{{% /button %}} Variables et types natifs

