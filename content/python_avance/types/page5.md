---
Title: TP3a tableau Excel
description: tableaux représentés par un tableur, export en csv
hidden: true
weight: 13
---

{{< img src="../images/exc17.png" width="600" >}}

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


{{< img src="../images/exc10.png" width="600" caption="" >}}

Ajouter la fonction $arrondi$ pour limiter à une seule décimale.

{{< img src="../images/exc11.png" width="600" caption="=arrondi(alea..." >}}

Cliquer-glisser avec le curseur vers la droite et vers le bas 

{{< img src="../images/exc12.png" caption="" >}}

... pour obtenir un tableau de valeurs aleatoires:

{{< img src="../images/exc13.png" caption="tableau de valeurs aleatoires" >}}

Puis sauvegarder le tableau avec l'extension $.csv$

{{< img src="../images/exc14.png" width="600" caption="classe.csv" >}}

Ce format est echangeable entre logiciels et peut être traité en langage python (Partie 2). 

Si vous l'ouvrez avec un editeur textuel (notepad++, ...), vous devriez obtenir à peu près ceci:

{{< img src="../images/exc15.png" caption="contenu du fichier classe.csv" >}}

Un fichier dans lequel les lignes représentent les $eleves$. Les valeurs sont separées par des points virgules ";"






# Suite
##### {{% button href="../page10" icon="bullhorn" style="caution" %}}Cours{{% /button %}} 
##### {{% button href="../page5" icon="palette" style="tip" %}}TP3a{{% /button %}} Tableur
##### {{% button href="../page51" icon="palette" style="tip" %}}TP3b{{% /button %}} Tableau de notes et algorithmes (Visualisation)
##### {{% button href="../page52" icon="palette" style="tip" %}}TP3c{{% /button %}} Systemes scolaires européens

