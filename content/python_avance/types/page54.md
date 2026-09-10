---
Title: TP3c correction
hidden: true
weight: 15
---

## Question 1

```python
donnees = table[1:]
donnees.append(["Pays-Bas", 919813,77,6])
print(donnees)
print(table)
```

## Question 2

```python
meilleure_ligne = donnees[0]
# meilleure_ligne vaut ["France", 5660000, 112, 7]
for ligne in donnees:
    if ligne[1] > meilleure_ligne[1]:
        meilleure_ligne = ligne

print(meilleure_ligne[0], meilleure_ligne[1])
# affiche Allemagne 6900000
```


## Question 3

```python
tri_par_effectif = sorted(donnees, key=lambda ligne: ligne[1], reverse=True)
print(tri_par_effectif)
```

## Question 4

```python
# Question 4
etiquettes = table[0]
ligne_france = table[1]

France = {
    etiquettes[0]: ligne_france[0],
    etiquettes[1]: ligne_france[1],
    etiquettes[2]: ligne_france[2],
    etiquettes[3]: ligne_france[3],
}

ligne_allemagne = table[2]
Allemagne = {
    etiquettes[0]: ligne_allemagne[0],
    etiquettes[1]: ligne_allemagne[1],
    etiquettes[2]: ligne_allemagne[2],
    etiquettes[3]: ligne_allemagne[3],
}
print(Allemagne)
```

## Question 5

```python
# Question 5
pays_dict = {}
etiquettes = table[0]

for ligne in donnees:
    nom_pays = ligne[0]
    pays_dict[nom_pays] = {}
    """
    for j in range(1, len(etiquettes)):
        pays_dict[nom_pays][etiquettes[j]] = ligne[j]
    """

print(pays_dict)
# Affiche
# {'France': {}, 'Allemagne': {}, 'Espagne': {}, 'Grèce': {}, 'Pays-Bas': {}}
```


