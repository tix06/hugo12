---
Title: TP3 tableaux python
description: tableaux représentés par un tableur, tableau python, import csv
hidden: true
weight: 13
---

{{< img src="../images/exc17.png" >}}

Prérequis:

* Cours sur les tableaux et listes Python

# Partie 1: Tableaux et traitement sur Excel
Commencer par remplir les notes de l'élève comme sur l'image ci-dessous (cellules $C2$ à $K2$)

{{< img src="../images/exc1.png" caption="tableau de données" >}}

Ajouter une fonction pour calculer la moyenne de ces notes. Dans la cellule $B2$, ecrire le signe `=` puis le nom de la fonction $= moyenne($ 


{{< img src="../images/exc2.png" caption="saisie de la fonction moyenne" >}}

Compléter avec la plage de cellule contenant les valeurs: 

$$= moyenne(C2:K2)$$ 

{{< img src="../images/exc3.png" caption="plage de valeurs de C2 à K2" >}}

La valeur moyenne comprend trop de décimales...

{{< img src="../images/exc4.png" caption="" >}}

Ajouter une fonction d'arrondi:

$$= arrondi(moyenne(C2:K2);1)$$

{{< img src="../images/exc5.png" caption="arrondir à 1 ou 2 décimale-s" >}}

Ajouter des etiquettes aux colonnes. Commencer par ecrire $note1$ dans la cellule $C1$.

{{< img src="../images/exc6.png" caption="etiquette note1" >}}

Puis positionner le curseur en bas à droite dans la cellule. Et cliquer-glisser vers la droite pour *reproduire la mise en forme*.

{{< img src="../images/exc7.png" caption="remplissage automatique des noms des colonnes" >}}

Faire la même manipulation pour obtenir des etiquettes aux lignes (eleve1, eleve2,...)

{{< img src="../images/exc9.png" caption="" >}}

Dans la cellule $C3$, mettre une note aleatoire entre 0 et 20 avec:

$$= alea() * 20$$

{{< img src="../images/exc8.png" caption="ajout d'une valeur aleatoire" >}}

La valeur contient trop de décimales. 


{{< img src="../images/exc10.png" caption="" >}}

Ajouter la fonction $arrondi$ pour limiter à une seule décimale.

{{< img src="../images/exc11.png" caption="=arrondi(alea..." >}}

Cliquer-glisser avec le curseur vers la droite et vers le bas pour obtenir un tableau de valeurs aleatoires:

{{< img src="../images/exc12.png" caption="" >}}

{{< img src="../images/exc13.png" caption="tableau de valeurs aleatoires" >}}

Puis sauvegarder le tableau avec l'extension $.csv$

{{< img src="../images/exc14.png" caption="classe.csv" >}}

Ce format est echangeable entre logiciels et peut être traité en langage python (Partie 2). 

Si vous l'ouvrez avec un editeur textuel (notepad++, ...), vous devriez obtenir à peu près ceci:

{{< img src="../images/exc15.png" caption="contenu du fichier classe.csv" >}}

Un fichier dans lequel les lignes représentent les $eleves$. Les valeurs sont separées par des points virgules ";"



# Partie 2: Tableaux python
## Traitement sur une liste
Le script suivant calcule la moyenne sur une liste de notes. La première valeur de la liste est reservée pour y placer une valeur, à la fin du programme. Les notes commencent donc à partir de l'indice 1 de cette liste:

```python
list1 = ["",12.0,14.5,10.0,18.5]

def moyenne(L):
    s = 0
    for x in L:
        s+=x
    return s/len(L)
    
m = moyenne(list1[1:])
print(m)
```

> 1. Voir l'animation sur Pythontutor: visualiser le parcours et traitement sur une liste de notes `list1`:

Lien: [pythontutor](https://pythontutor.com/render.html#code=list1%20%3D%20%5B%22%22,12.0,14.5,10.0,18.5%5D%0A%0Adef%20moyenne%28L%29%3A%0A%20%20%20%20s%20%3D%200%0A%20%20%20%20for%20x%20in%20L%3A%0A%20%20%20%20%20%20%20%20s%2B%3Dx%0A%20%20%20%20return%20s/len%28L%29%0A%20%20%20%20%0Am%20%3D%20moyenne%28list1%5B1%3A%5D%29%0Aprint%28m%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=311&rawInputLstJSON=%5B%5D&textReferences=false)

{{< img src="../images/pythontutor_list.png" caption="nom et valeur des variables dans pythontutor - liste" >}}

> 1a. Commenter le schéma ci-dessus: que signifient les flèches? Que signifient les cases bleues et jaunes?

> 1b. Pourquoi écrit-on l'instruction `m = moyenne(list1[1:])` et non `m = moyenne(list1)`?

> 1c Modifier le script (faire *edit* dans pythontutor) pour que le programme place la 
valeur `m` dans la case `list1[0]`. Noter ici l'instruction utilisée. Comment voit-on la modification dans pythontutor?


## Traitement sur une table (liste de listes)  et effet de bord
> 2. Animation sur Pythontutor: visualiser le parcours et traitement sur une liste

Execution du script suivant sur [Pythontutor](https://pythontutor.com/render.html#code=classe%20%3D%20%5B%5B'%5Cufeff','moyenne','note1','note2','note3','note4','note5',%0A%20%20'note6','note7','note8','note9'%5D,%0A%20%5B'eleve1',%20'12,5',%2010.0,%208.9,%209.9,%2012.3,%2011.1,%2012.3,%2013.1,%2014.5,%2020.0%5D,%0A%20%5B'eleve2',%20'',%204.2,%202.1,%2016.5,%2015.0,%2019.6,%207.5,%2010.3,%2018.8,%2017.4%5D%5D%0A%0Adef%20moyenne%28tab%29%3A%0A%20%20%20%20s%20%3D%200%0A%20%20%20%20for%20note%20in%20tab%3A%0A%20%20%20%20%20%20%20%20s%20%2B%3D%20note%0A%20%20%20%20return%20s%20/%20len%28tab%29%0A%0Aeleve%20%3D%20classe%5B2%5D%0Am%20%3D%20round%28moyenne%28eleve%5B2%3A%5D%29,2%29%0Aprint%28%22nom%20eleve%3A%20%7B%7D%20moyenne%3A%20%7B%7D%22.format%28eleve%5B0%5D,m%29%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=311&rawInputLstJSON=%5B%5D&textReferences=false)

```python
classe = [['\ufeff','moyenne','note1','note2','note3','note4','note5',
  'note6','note7','note8','note9'],
 ['eleve1', '12,5', 10.0, 8.9, 9.9, 12.3, 11.1, 12.3, 13.1, 14.5, 20.0],
 ['eleve2', '', 4.2, 2.1, 16.5, 15.0, 19.6, 7.5, 10.3, 18.8, 17.4]]

def moyenne(tab):
    s = 0
    for note in tab:
        s += note
    return s / len(tab)

eleve = classe[2]
m = round(moyenne(eleve[2:]),2)
print(m)
```

{{< img src="../images/pythontutor_notes.png" caption="nom et valeur des variables dans pythontutor - tableau" >}}

> 2a. Commenter le schéma ci-dessus: que signifient les flèches? Que signifient les cases bleues et jaunes?

> 2b. Que contient la liste `eleve`? Recopier ici son contenu.

> 2c. Pourquoi écrit-on l'instruction `m = moyenne(eleve[2:])` et non `m = moyenne(eleve))`?

> 2d. Ajouter une instruction au programme pour placer la valeur m dans la case `eleve[1]`. Noter ici l'instruction utilisée. Comment voit-on la modification dans pythontutor?

> 2e. La table a t-elle été modifiée? Expliquer.

> 2f. Ecrire une fonction `ajoute_colonne_moyenne` qui prend en paramètre une table `classe` et un numero de colonne `c`. Le fonction devra ajouter la moyenne pour chaque élève, dans la colonne `c`. La table `classe` aura le format proposé dans l'énoncé vu plus haut.


# Prolongement
## Traitements sur le fichier csv importé du tableur



Telecharger et placer dans le même dossier: 

* [tableur_vers_python.ipynb](/scripts/notebooks/tableur_vers_python.ipynb)
* fichier [classe.csv](/scripts/notebooks/classe.csv)
* fichier [utilitaire_notes.py](/scripts/notebooks/utilitaire_notes.py)

Deux options sont possibles pour organiser votre dossier et vos fichiers:

* Vous pouvez placer *classe.csv* dans le même dossier que le notebook: Depuis le script python, ouvrez le alors avec l'instruction `with open('classe.csv', newline='') as csvfile:`
* ou bien dans un sous dossier `datas`. Ouvrir alors avec `with open('datas/classe.csv', newline='') as csvfile:` 

{{< img src="../images/exc16.png" >}}

Utiliser une distribution python (*jupyter notebook*) en *local*.

> 1. Traiter la partie 1 du notebook

> 2. Traiter la partie 2 du notebook

> 3. Traiter la feuille d'exercices sur les tableaux en python: [lien vers le pdf](/pdf/NSI_1/TP_excel_vers_python.pdf)

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

