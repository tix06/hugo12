---
Title: TP3c Systemes scolaires en Europe 
description: tableau python, recherche du maximum, tri avec une clé (sort et sorted), passer d'une liste à un dictionnaire
hidden: true
weight: 14
---


# Manipuler une table de données (liste de listes et dictionnaires)

On dispose de la table suivante, qui donne, pour 4 pays européens, le nombre d'élèves scolarisés dans le secondaire, le nombre de jours de vacances scolaires par an, et la durée des études secondaires (collège-lycée ou équivalent) :

```python
table = [
    ["Pays", "Nb élèves secondaire", "Jours de vacances/an", "Durée secondaire (ans)"],
    ["France", 5660000, 112, 7],
    ["Allemagne", 6900000, 65, 9],
    ["Espagne", 3500000, 105, 6],
    ["Grèce", 700000, 119, 6],
]
```

La première ligne contient les **étiquettes de colonnes**, les lignes suivantes les **données** proprement dites, un pays par ligne.

---

## 1. Copier les données sans l'en-tête

On souhaite travailler uniquement sur les données (sans la ligne d'étiquettes), dans une nouvelle variable `donnees`, tout en conservant `table` intacte.

* Écrire une instruction qui construit `donnees` par une **copie par valeur** de `table`, en excluant la première ligne.
* Vérifier que modifier `donnees` (par exemple en ajoutant une ligne avec `append`) ne modifie pas `table`.

*Remarque à garder en tête pour la suite du cours :* cette copie protège la liste `table` elle-même, mais les lignes qu'elle contient (par exemple `donnees[0]`) restent les **mêmes objets** que ceux de `table`. Modifier un élément d'une ligne de `donnees` (comme `donnees[0][1] = 0`) modifierait donc bien la ligne correspondante dans `table`. On appelle cela une copie *de surface* (shallow copy).

---

## 2. Rechercher le pays ayant le plus grand nombre d'élèves

En parcourant `donnees` avec une boucle bornée, écrire un script qui détermine le pays possédant le plus grand nombre d'élèves du secondaire (colonne d'indice 1).

Le script devra afficher le nom du pays et le nombre d'élèves correspondant. On procèdera comme pour une recherche de maximum : une variable mémorise le meilleur pays trouvé jusqu'ici, mise à jour à chaque fois qu'une ligne fait mieux.

---

## 3. Trier la table par nombre d'élèves décroissant

Python permet de trier une liste avec la fonction `sorted` (qui renvoie une copie triée) ou avec la méthode `sort` (qui trie en place). Toutes deux acceptent un paramètre optionnel `key`, qui indique **selon quel critère** comparer les éléments.

*Documentation (extrait) :*
```
sorted(iterable, key=None, reverse=False)
    - key : fonction appliquée à chaque élément avant comparaison
    - reverse=True : tri décroissant plutôt que croissant
```

Pour trier `donnees` selon le nombre d'élèves (2e colonne de chaque ligne), la fonction `key` doit indiquer comment extraire cette valeur d'une ligne. Par exemple, pour trier selon le nom du pays (1re colonne), on écrirait :

```python
tri_par_pays = sorted(donnees, key=lambda ligne: ligne[0])
```

* Écrire l'instruction qui construit `tri_par_effectif`, une copie de `donnees` triée par nombre d'élèves, du **plus grand au plus petit**.
* Vérifier que `donnees` n'a pas été modifiée.

---

## 4. Construire un dictionnaire par pays

On souhaite représenter chaque pays par un dictionnaire, dont les clés sont les étiquettes de colonnes de la table d'origine. Voici le script pour la France :

```python
etiquettes = table[0]
ligne_france = table[1]

France = {
    etiquettes[0]: ligne_france[0],
    etiquettes[1]: ligne_france[1],
    etiquettes[2]: ligne_france[2],
    etiquettes[3]: ligne_france[3],
}
```

* Adapter ce script pour construire, de la même manière, les dictionnaires `Allemagne`, `Espagne` et `Grece`.
* Afficher chacun des 4 dictionnaires pour vérifier leur contenu.

---

## 5. Construire un dictionnaire de dictionnaires, automatiquement

Le script de la question 4 doit être réécrit à la main pour chaque pays : ce n'est pas satisfaisant si la table contient un jour 50 pays. On souhaite maintenant construire, **à partir de la liste `table` d'origine et à l'aide d'une boucle**, un dictionnaire unique `pays_dict` qui rassemble tous les pays, de la forme :

```python
{
    'France': {'Nb élèves secondaire': 5660000, 'Jours de vacances/an': 112, 'Durée secondaire (ans)': 7},
    'Allemagne': {...},
    ...
}
```

* Écrire un script qui construit `pays_dict` automatiquement, en parcourant les lignes de `table` (sans la ligne d'en-tête) avec une boucle bornée. On pourra s'appuyer sur `etiquettes = table[0]` et parcourir, pour chaque pays, les indices de colonnes avec une seconde boucle bornée imbriquée.
* Vérifier que `pays_dict['France']` donne bien le même contenu que le dictionnaire `France` construit à la question 4.

*Pour aller plus loin :* la fonction native `zip` permet d'associer deux listes élément par élément et simplifie beaucoup ce genre de construction (`dict(zip(etiquettes[1:], ligne[1:]))`). Si le temps le permet, cherchez sa documentation et proposez une version de `pays_dict` qui l'utilise.

# Suite
##### {{% button href="../page10" icon="bullhorn" style="caution" %}}Cours{{% /button %}} 
##### {{% button href="../page5" icon="palette" style="tip" %}}TP3a{{% /button %}} Tableur
##### {{% button href="../page51" icon="palette" style="tip" %}}TP3b{{% /button %}} Tableau de notes et algorithmes (Visualisation)
##### {{% button href="../page52" icon="palette" style="tip" %}}TP3c{{% /button %}} Systemes scolaires européens
