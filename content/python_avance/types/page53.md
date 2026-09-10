---
Title: TP3b correction
hidden: true
weight: 15
---

## Ex 1.3

3a. Les flèches représentent les références vers les valeurs des objets dans la mémoire. En bleu, les varaibles globales et en jaune les valeurs placées dans les espaces mémoire.

3c. Les données sont mises dans les colonnes 2 et plus. On récupère ces données avec `eleve[2:]`

3d. `eleve[1] = m`

3e.

```python
def ajoute_colonne_moyenne(classe,c):
    for eleve in classe[1:]:
        m = round(moyenne(eleve[2:]),2)
        eleve[c] = m

# appel de la fonction
ajoute_colonne_moyenne(classe,1)
```

## Ex 2
3. `'12,5'.replace(',','.')` 
4. 5. script complet:

```python
import csv
with open('classe.csv', newline='') as csvfile:
    tab = csv.reader(csvfile, delimiter = ";")
    classe = []
    for row in tab:
        classe.append(row)


def somme(tab):
    """calcule la somme de la liste tab
    """
    s = 0
    for x in tab:
        s += x
    return s

def moyenne(tab):
    """calcule la moyenne des valeurs de la liste tab
    """
    return somme(tab)/len(tab)

def remplacer(tab):
    for i in range(1,len(tab)):
        for j in range(2,len(tab[i])):
            note = tab[i][j]
            tab[i][j] = float((note.replace(',','.')))

remplacer(classe)

for i in range(1,len(classe)):
    eleve = classe[i]
    # calcul de la moyenne des notes
    m = moyenne(eleve[2:])
    # arrondir avec 2 decimales
    m = round(m,2)
    # placer m dans la colonne moyenne
    eleve[1] = m
print(classe)
```
