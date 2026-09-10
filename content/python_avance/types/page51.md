---
Title: TP3b tableaux python, visualisation et fichier csv
description: tableau python, effet de bord, import csv, algorithmes de moyenne, max et min
hidden: true
weight: 14
---

## Ex1: Visualiser les algorithmes
### 1. Moyenne
Le script suivant calcule la moyenne sur une liste de notes. La première valeur de la liste est reservée pour y placer une valeur, à la fin du programme. Les notes commencent donc à partir de l'indice 1 de cette liste:

```python{title="fonction moyenne", lineNos=true}
list1 = ["",12.0,14.5,10.0,18.5]

def moyenne(L):
    s = 0
    for x in L:
        s+=x
    return s/len(L)
    
m = moyenne(list1[1:])
print(m)
```

> Voir l'animation sur Pythontutor: visualiser le parcours et traitement sur une liste de notes `list1`:

Lien: [pythontutor](https://pythontutor.com/render.html#code=list1%20%3D%20%5B%22%22,12.0,14.5,10.0,18.5%5D%0A%0Adef%20moyenne%28L%29%3A%0A%20%20%20%20s%20%3D%200%0A%20%20%20%20for%20x%20in%20L%3A%0A%20%20%20%20%20%20%20%20s%2B%3Dx%0A%20%20%20%20return%20s/len%28L%29%0A%20%20%20%20%0Am%20%3D%20moyenne%28list1%5B1%3A%5D%29%0Aprint%28m%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=311&rawInputLstJSON=%5B%5D&textReferences=false)

{{< img src="../images/pythontutor_list.png" caption="nom et valeur des variables dans pythontutor - liste" width="400" >}}

> 1a. Commenter le schéma ci-dessus: que signifient les flèches? Que signifient les cases bleues et jaunes?

> 1b. Pourquoi écrit-on l'instruction `m = moyenne(list1[1:])` et non `m = moyenne(list1)`?

> 1c Modifier le script (faire *edit* dans pythontutor) pour que le programme place la 
valeur `m` dans la case `list1[0]`. Noter ici l'instruction utilisée. Comment voit-on la modification dans pythontutor?

### 2. Recherche du maximum

```python{title="fonction maximum", lineNos=true}
list1 = ["",12.0,14.5,10.0,18.5]
n = len(list1)

def maximum(L,a,b):
    # recherche du maximum de L entre les indices a et b
    maxi = L[a]
    for x in L[a:b]:
        if x > maxi:
            maxi = x
    return maxi
    
m = maximum(list1,1,n)
print(m)
```

> 2a. Voir l'animation sur Pythontutor: visualiser le parcours et traitement sur une liste de notes `list1`:

Lien: [Pythontutor](https://pythontutor.com/visualize.html#code=list1%20%3D%20%5B%22%22,12.0,14.5,10.0,18.5%5D%0An%20%3D%20len%28list1%29%0A%0Adef%20maximum%28L,a,b%29%3A%0A%20%20%20%20%23%20recherche%20du%20maximum%20de%20L%20entre%20les%20indices%20a%20et%20b%0A%20%20%20%20maxi%20%3D%20L%5Ba%5D%0A%20%20%20%20for%20x%20in%20L%5Ba%3Ab%5D%3A%0A%20%20%20%20%20%20%20%20if%20x%20%3E%20maxi%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20maxi%20%3D%20x%0A%20%20%20%20return%20maxi%0A%20%20%20%20%0Am%20%3D%20maximum%28list1,1,n%29%0Aprint%28m%29&curInstr=0&mode=display&origin=opt-frontend.js&py=311)

> 2.b. Dans l'animation, lorsque la boucle `for` est executée, à quel(s) moment(s) la valeur de `maxi` est elle corrigée?

### 3. Traitement sur une table (liste de listes)  et effet de bord
> 3. Animation sur Pythontutor: visualiser le parcours et traitement sur une liste

Execution du script suivant sur [Pythontutor](https://pythontutor.com/render.html#code=classe%20%3D%20%5B%5B'%5Cufeff','moyenne','note1','note2','note3','note4','note5',%0A%20%20'note6','note7','note8','note9'%5D,%0A%20%5B'eleve1',%20'12,5',%2010.0,%208.9,%209.9,%2012.3,%2011.1,%2012.3,%2013.1,%2014.5,%2020.0%5D,%0A%20%5B'eleve2',%20'',%204.2,%202.1,%2016.5,%2015.0,%2019.6,%207.5,%2010.3,%2018.8,%2017.4%5D%5D%0A%0Adef%20moyenne%28tab%29%3A%0A%20%20%20%20s%20%3D%200%0A%20%20%20%20for%20note%20in%20tab%3A%0A%20%20%20%20%20%20%20%20s%20%2B%3D%20note%0A%20%20%20%20return%20s%20/%20len%28tab%29%0A%0Aeleve%20%3D%20classe%5B2%5D%0Am%20%3D%20round%28moyenne%28eleve%5B2%3A%5D%29,2%29%0Aprint%28%22nom%20eleve%3A%20%7B%7D%20moyenne%3A%20%7B%7D%22.format%28eleve%5B0%5D,m%29%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=311&rawInputLstJSON=%5B%5D&textReferences=false)

```python{lineNos=true}
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

{{< img src="../images/pythontutor_notes.png" caption="nom et valeur des variables dans pythontutor - tableau" width="600" >}}

> 3a. Commenter le schéma ci-dessus: que signifient les flèches? Que signifient les cases bleues et jaunes?

> 3b. Que contient la liste `eleve`? Recopier son contenu. (fiche reponse)

> 3c. Pourquoi écrit-on l'instruction `m = moyenne(eleve[2:])` et non `m = moyenne(eleve))`?

> 3d. Ajouter une instruction au programme pour placer la valeur m dans la case `eleve[1]`. Noter ici l'instruction utilisée. Comment voit-on la modification dans pythontutor?

> 3e. La table a t-elle été modifiée? Expliquer.

> 3f. Ecrire une fonction `ajoute_colonne_moyenne` qui prend en paramètre une table `classe` et un numero de colonne `c`. Le fonction devra ajouter la moyenne pour chaque élève, dans la colonne `c`. La table `classe` aura le format proposé dans l'énoncé vu plus haut.


## Ex 2: Fichier de notes en csv
*But*: programmer un logiciel de traitement des notes des élèves, à la manière de *Pronotes*.

Dans votre IDE (Pyzo, IDLE), ouvrir un nouveau fichier python, et placer les 2 fonctions:

```python
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
```

Sauvegarder sur le disque dur. Avec le nom `prounotes.py` par exemple


Telecharger et placer dans le même dossier le fichier [classe.csv](/scripts/notebooks/classe.csv)

Deux options sont possibles pour organiser votre dossier et vos fichiers:

* Vous pouvez placer *classe.csv* dans le même dossier que le fichier python: Depuis le script python, ouvrez le alors avec l'instruction `with open('classe.csv', newline='') as csvfile:`
* ou bien dans un sous dossier `datas`. Il faudra adapter le script pour préciser le schemin.

{{< img src="../images/exc16.png" width="400" >}}


Ajouter le script suivant:

```python{title="import fichier csv", lineNos=true}
import csv
with open('datas/classe.csv', newline='') as csvfile:
    tab = csv.reader(csvfile, delimiter = ";")
    classe = []
    for row in tab:
        classe.append(row)
print(classe[:2])
```

1. Dans cet exemple, quelle option a été choisie pour placer le fichier *classe.csv*?
2. Que remarque t-on à propos du séparateur des valeurs décimales? 
3. Quelle instruction python va transformer `'12,5'` en un *float* égal à `12.5`?

La fonction `remplacer` va traiter chaque note du tableau pour qu'elle soit dans le bon format (float).

4. Compléter le script de cette fonction et l'ajouter à votre programme:


```python
def remplacer(tab):
    for i in range(1,len(tab)):
        for j in range(2,len(tab[i])):
            note = tab[i][j]
            tab[i][j] = ...(note. ... (',','.'))

remplacer(classe)
```

Pour chaque élève, vous allez calculer la moyenne de ses notes à l'aide de la fonction `moyenne` définie plus haut. Et placer la valeur dans la colonne d'indice 1:

```python
for i in range(1,len(classe)):
    eleve = classe[i]
    # calcul de la moyenne des notes
    m = moyenne(eleve[..:..])
    # arrondir avec 2 decimales
    m = round(...,...)
    # placer m dans la colonne moyenne
    eleve[..] = ...
```

5. Compléter et ajouter le script à votre programme.

<!--
> 3. Traiter la feuille d'exercices sur les tableaux en python: [lien vers le pdf](/pdf/NSI_1/TP_excel_vers_python.pdf)
-->

# Suite
##### {{% button href="../page10" icon="bullhorn" style="caution" %}}Cours{{% /button %}} 
##### {{% button href="../page5" icon="palette" style="tip" %}}TP3a{{% /button %}} Tableur
##### {{% button href="../page51" icon="palette" style="tip" %}}TP3b{{% /button %}} Tableau de notes et algorithmes (Visualisation)
##### {{% button href="../page52" icon="palette" style="tip" %}}TP3c{{% /button %}} Systemes scolaires européens