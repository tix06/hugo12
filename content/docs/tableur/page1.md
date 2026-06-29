---
Title: Utiliser Tableur
---

# Tableau de notes
## Tableurs
Les tableurs sont des logiciels de présentation et de traitement de données. 

les suites Microsoft Office et LibreOffice proposent les mêmes logiciels, mais les formats de fichiers différent.


| Logiciel | LibreOffice   | Extension   | Microsoft   | Extension |
|--- |--- |--- |--- |--- |
| Traitement de textes | Writer  | `odt` | Word  | `docx`  |
| Tableur   | Calc   | `ods`   | Excel   | `xlsx`  |
| Présentations  | Impress | `odp`  | PowerPoint  | `pptx`   |

Les fonctionnalités de ces logiciels sont identiques. Pour les tableurs, la page est un tableau de cellules, repérées par leurs coordonnées (A1, A2, ...). La mise en forme du tableau demande une certaine maitrise des différents curseurs.

## Les curseurs pour manipuler les cellules
Il existe 3 sortes de curseur dans la page: "main", "croix blanche", "croix noire". C'est en faisant glisser celui-ci dans la cellule que l'on peut passer d'un curseur à l'autre.

### Main: déplacer une cellule
* Ouvrir le logiciel Excel (document vierge). Ecrire Le nom de l'école.
* Choisir alors le curseur "main" et déplacer la cellule dans `A1`.

{{< img src="../images/calc1.png" >}}

### Croix blanche: sélection étendue
La croix blanche permet de selectionner plusieurs cellules, ou de selectionner une *plage de cellule* (utile pour les formules de calcul)

* Glisser le curseur au centre de la cellule. Lorsque l'on obtient une croix blanche, cliquer-glisser sur plusieurs colonnes pour faire une sélection étendue.

{{< img src="../images/calc2.png" >}}

On peut alors *fusionner les cellules*: clic droit > *format de cellule*

{{< img src="../images/calc3.png" >}}

* Cocher la case "fusionner (merge)". Puis aligner le texte au centre.

* Compléter alors le tableau selon l'image suivante:

{{< img src="../images/calc4.png" >}}

### Croix noire: reproduire une mise en forme
* Ecrire pour nom du premier élève: *Elève 1*. 
* Glisser le curseur dans le coin inférieur droit de la cellule pour obtenir une croix noire.
* cliquer-glisser le long de la colonne, sur 3 lignes.

{{< img src="../images/calc5.png" >}}

Le tableur adapte alors le contenu. Ici, en numérotant les élèves.

{{< img src="../images/calc6.png" >}}

## Formules de calcul
Le traitement des données peut se faire à l'aide de fonctions ou bien de formules mathématiques.

Avant de commencer, compléter le tableau avec les notes des élèves.

{{< img src="../images/calc7.png" >}}

### Fonctions
Le nom des fonctions peut différer selon les logiciels tableurs utilisés. Il peut être prudent d'utiliser le concepteur de formule (bouton fx). 

{{< img src="../images/calc8.png" >}}

Une fois que vous avez saisi `=` ainsi que les premières lettres de la fonction, le concepteur de formule va vous proposer un choix parmi les fonctions existantes. 

> Pour calculer la moyenne de la classe obtenues pour les élèves au devoir 1:

* dans une cellule de la colonne B (devoir 1), commencer par écrire `=`
* Puis la fonction `MOYENNE(` 
* Ecrire le paramètre entre parenthèses: il faut placer les coordonnées de la plage de valeurs. Avec l'outil de sélection étendue (croix blanche), sélectionner toutes les cellules des devoir 1: `B6:B8`. Fermer la parenthèse.

{{< img src="../images/calc9.png" >}}

* Modifier le format de cellule pour afficher une valeur arrondie (1 ou 2 chiffres après la virgule): clic droit > Format de cellule

{{< img src="../images/calc10.png" >}}

On devrait obtenir maintenant le tableau suivant:

{{< img src="../images/calc11.png" >}}

* Reproduire la mise en forme dans les cellules voisines: croix noire dans la cellule `B9` puis cliquer-glisser jusqu'à *devoir 4*.

{{< img src="../images/calc12.png" >}}

C'est là l'une des fonctions magiques du logiciel. Observez les paramètres de chacune des fonctions reproduites. Pour le *devoir 2*, vous devriez voir `=MOYENNE(C6:C8)`. Le logiciel a adapté la mise en forme, dans la nouvelle colonne, à partir de celle adjacente!

### Ecrire une formule
* La formule non coefficientée, pour l'élève 1 s'écrira:

$$= (B6/B5+C6/C5+D6/D5+E6/E5) * 20 / 4$$

Il s'agit de la somme de ses notes, divisée par la somme de la ligne *"note sur:"* , Le tout, multiplié par 20. 


> Pour calculer la moyenne de l'élève 1, après ses 4 devoirs: Dans quelle cellule va t-on placer la formule?

> Saisir cette formule dans la cellule la plus adaptée. Puis modifier le format de cellule pour arrondir à 2 chiffres après la virgule.

> On souhaite *reproduire la mise en forme* afin de calculer la moyenne pour les autres élèves. Comment va-t-on s'y prendre?


* Reproduire la mise en forme du calcul de moyenne pour chaque élève. Les résultats vous paraissent-ils cohérents? D'où cela peut-il provenir?

Nous allons corriger ce problème dans le paragraphe suivant...

### Références relatives ou absolues
Le problème précédent vient de la manière avec laquelle nous avons écrit les coordonnées de cellules. Le calcul doit être reproduit pour chaque élève, mais avec des coordonnées pour les valeurs *note sur:* qui doivent rester fixes. Pour cela, à la place d'écrire $= (B6/B5+C6/C5...$ dans la formule de calcul pour l'élève 1, nous allons écrire: `= (B6/B$5+C6/C$5...` 

Cela ne change rien au calcul de la moyenne de l'élève 1. Par contre, si vous faites une *reproduction de la mise en forme* pour les autres élèves, leur moyenne est cette fois-ci correctement calculée: *La copie de la formule ne modifie pas la reference de cellule de la ligne 5.*

## Finir le tableau
Il vous reste maintenant:

* à tenir compte des coefficients pour chaque matière. Cela va vous obliger à modifier la formule de calcul de moyenne par élève:

`= (B6/B$5*B$4+C6/C$5*C$4+D6/..*..+E6/..*..) * 20 / (B$4+C$4+D$4+E$4)`

* à ajouter le calcul de la moyenne de la classe pour le trimestre (semestre).

## Complément sur les références absolues
Les références absolues sont notées avec des `$`.

Il est possible de _bloquer_:

- La colonne. Exemple: `$B6`.
- La ligne. Exemple: `B$6`.
- Les deux. Exemple: `$B$6`.

Une vidéo pour mieux comprendre: <https://www.youtube.com/watch?v=6fMizCr1hpA>


