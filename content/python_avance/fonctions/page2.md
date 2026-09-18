---
Title : TP4 - fonctions
hidden: true
description: travaux dirigés sur la valeur par défaut, les annotations de type, les arguments positionnés
weight: 10
---

# TD : Fonctions en Python

*Ce TD s'appuie sur le [cours sur les fonctions](../page1/). Pour chaque script, tu dois répondre aux 3 questions dans l'ordre, sans exécuter le code avant d'avoir répondu à la question 1.*

**Consignes de rédaction :**
- Question 1 : écris précisément ce que le programme affiche (ou l'erreur qu'il produit), ligne par ligne si nécessaire.
- Question 2 : justifie ta prédiction en t'appuyant sur une notion précise du cours (nomme-la).
- Question 3 : propose une version corrigée ou modifiée du script, puis explique en une phrase ce que tu as changé et pourquoi.

---

## Script 1 — Valeur par défaut

```python
def ajouter_eleve(nom, liste=[]):
    liste.append(nom)
    return liste

classe_A = ajouter_eleve('Alice')
classe_B = ajouter_eleve('Bob')

print(classe_A)
print(classe_B)
```

**Q1.** Que produit l'exécution de ce script ?

**Q2.** Explique précisément ce qui se passe, en citant la notion du cours concernée.

**Q3.** Modifie `ajouter_eleve` pour que chaque appel de la fonction sans préciser `liste` reparte d'une liste **vide et indépendante**, de sorte que `classe_A` ne contienne que `'Alice'` et `classe_B` que `'Bob'`.

---

## Script 2 — Annotations de type

```python
def double(x: int) -> int:
    """renvoie le double de x"""
    return x * 2

resultat = double(2.5)
print(resultat)
print(type(resultat))
```

**Q1.** Que produit l'exécution de ce script ?

**Q2.** Explique précisément ce qui se passe, en citant la notion du cours concernée.

**Q3.** Modifie `double` pour qu'elle signale clairement une erreur si l'argument reçu n'est pas un `int`, de façon à garantir réellement ce que l'annotation ne fait que suggérer. Tu pourras utiliser la fonction `isinstance(objet, type)`, qui renvoie `True` si `objet` est bien une instance de `type`. Choisis entre une instruction `assert` et une instruction `raise`, et justifie ton choix en une phrase.

---

## Script 3 — Arguments positionnés

```python
def publier_msg(message, user):
    """publie le message d'un utilisateur"""
    return f'{user} : {message}'

annonce = publier_msg('Le Directeur', 'Les cours reprennent lundi')
print(annonce)
```

**Q1.** Que produit l'exécution de ce script ?

**Q2.** Explique précisément ce qui se passe, en citant la notion du cours concernée.

**Q3.** Corrige l'appel de `publier_msg` (sans modifier la définition de la fonction) pour que l'annonce affichée ait effectivement du sens : le directeur est bien l'auteur du message, et le message est bien « Les cours reprennent lundi ». Propose deux solutions : une où tu réordonnes simplement les arguments, une autre où tu utilises des **arguments nommés** pour que l'appel reste correct même si l'ordre des paramètres venait à changer dans la définition de la fonction.

## Script 4 — Chaînage de fonctions

```python
def extraire_prix(ligne):
    """extrait le prix d'une ligne du type 'Livre;12.50'"""
    _, prix = ligne.split(';')
    return prix

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
```

**Q1.** Que produit l'exécution de ce script ?

**Q2.** Explique précisément ce qui se passe, en citant la notion du cours concernée.

**Q3.** Modifie `extraire_prix` pour que l'enchaînement `extraire_prix` → `appliquer_remise` → `afficher_ticket` fonctionne correctement, en veillant à ce que le type de la valeur renvoyée par chaque fonction soit bien compatible avec le type attendu par la fonction suivante.

---

##### {{% button href="../page1" icon="bullhorn" style="caution" %}}Cours{{% /button %}} les fonctions
##### {{% button href="../page2" icon="palette" style="tip" %}}TP4{{% /button %}} 

{{% button href="" icon="lightbulb" style="tip" %}}Corrigé du TP4{{% /button %}}


<!--
{{% button href="../page3" icon="lightbulb" style="tip" %}}Corrigé du TP4{{% /button %}}
-->

---

# TD : Fonctions en Python

*Ce TD s'appuie sur le [cours sur les fonctions](../page1/). Pour chaque script, tu dois répondre aux 3 questions dans l'ordre, sans exécuter le code avant d'avoir répondu à la question 1.*

**Consignes de rédaction :**
- Question 1 : écris précisément ce que le programme affiche (ou l'erreur qu'il produit), ligne par ligne si nécessaire.
- Question 2 : justifie ta prédiction en t'appuyant sur une notion précise du cours (nomme-la).
- Question 3 : propose une version corrigée ou modifiée du script, puis explique en une phrase ce que tu as changé et pourquoi.

---

## Script 1 — Valeur par défaut

```python
def ajouter_eleve(nom, liste=[]):
    liste.append(nom)
    return liste

classe_A = ajouter_eleve('Alice')
classe_B = ajouter_eleve('Bob')

print(classe_A)
print(classe_B)
```

**Q1.** Que produit l'exécution de ce script ?

**Q2.** Explique précisément ce qui se passe, en citant la notion du cours concernée.

**Q3.** Modifie `ajouter_eleve` pour que chaque appel de la fonction sans préciser `liste` reparte d'une liste **vide et indépendante**, de sorte que `classe_A` ne contienne que `'Alice'` et `classe_B` que `'Bob'`.

---

## Script 2 — Annotations de type

```python
def double(x: int) -> int:
    """renvoie le double de x"""
    return x * 2

resultat = double(2.5)
print(resultat)
print(type(resultat))
```

**Q1.** Que produit l'exécution de ce script ?

**Q2.** Explique précisément ce qui se passe, en citant la notion du cours concernée.

**Q3.** Modifie `double` pour qu'elle signale clairement une erreur si l'argument reçu n'est pas un `int`, de façon à garantir réellement ce que l'annotation ne fait que suggérer. Tu pourras utiliser la fonction `isinstance(objet, type)`, qui renvoie `True` si `objet` est bien une instance de `type`. Choisis entre une instruction `assert` et une instruction `raise`, et justifie ton choix en une phrase.

---

## Script 3 — Arguments positionnés

```python
def publier_msg(message, user):
    """publie le message d'un utilisateur"""
    return f'{user} : {message}'

annonce = publier_msg('Le Directeur', 'Les cours reprennent lundi')
print(annonce)
```

**Q1.** Que produit l'exécution de ce script ?

**Q2.** Explique précisément ce qui se passe, en citant la notion du cours concernée.

**Q3.** Corrige l'appel de `publier_msg` (sans modifier la définition de la fonction) pour que l'annonce affichée ait effectivement du sens : le directeur est bien l'auteur du message, et le message est bien « Les cours reprennent lundi ». Propose deux solutions : une où tu réordonnes simplement les arguments, une autre où tu utilises des **arguments nommés** pour que l'appel reste correct même si l'ordre des paramètres venait à changer dans la définition de la fonction.

##### {{% button href="../page1" icon="bullhorn" style="caution" %}}Cours{{% /button %}} les fonctions
##### {{% button href="../page2" icon="palette" style="tip" %}}TP4{{% /button %}} 

{{% button href="" icon="lightbulb" style="tip" %}}Corrigé du TP4{{% /button %}}


<!--
{{% button href="../page3" icon="lightbulb" style="tip" %}}Corrigé du TP4{{% /button %}}
-->
