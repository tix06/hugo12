---
Title: nobels
---

# Statistiques et prix Nobel

*Le [prix Nobel](https://fr.wikipedia.org/wiki/Prix_Nobel#Disciplines_r%C3%A9compens%C3%A9es) est une récompense de portée internationale. Remis pour la première fois en 1901, les prix sont décernés chaque année à des personnes « ayant apporté le plus grand bénéfice à l'humanité », par leurs inventions, découvertes et améliorations dans différents domaines de la connaissance, par l'œuvre littéraire la plus impressionnante, ou par leur travail en faveur de la paix, suivant ainsi les derniers vœux d'Alfred Nobel, inventeur de la dynamite.*

L'année 2023 a vu une féminisation des lauréats au prix Nobel. Mais depuis sa création, le nombre de femmes primées est-il comparable aux hommes? Faisons le bilan.

{{< img src="../images/femmesnobel_0.png" caption="Prix Nobel : une féminisation à tout petit pas - TV5 Monde" >}}

Narges Mohammadi, Claudia Goldin, Anne L'Huillier, Katalin Karikó. Quatre noms de femmes s'ajoutent en 2023 à la liste des "Nobélisé-es". Un seul en 2024, Han Kang, prix nobel de littérature.

## Fichier de données
Selon la version Excel installée:

###  méthode 1: avec Excel jusqu'à la version 16 (2019), *ou bien LibreOffice Calc*:
- **Fichier: Importer** le fichier de données [nobels.csv](../datas/nobels.csv). 

### méthode 2: Excel version plus récente
* **Données: Obtenir des données**, puis choisir "à partir d'un fichier", "fichier text ou csv", choisir le fichier [nobels.csv](../datas/nobels.csv). 

{{< img src="../images/excel3.png" >}}

Dans les 2 cas (méthode 1 ou 2): Bien sélectionner: 

* séparateur par point virgule
* Origine du fichier: unicode utf-8 afin de bien gérer les caractères avec accents.

{{< img src="../images/excel4.png" >}}

Puis **Enregistrer** le fichier au format **xls** (ou **xlsx**) dans le même répertoire.
Maintenant que nous sommes sur un fichier en format tableur, nous pouvons utiliser les fonctionnalités avancées de ce type de logiciel.

## Rechercher et remplacer: (facultatif)

Commencer par franciser le fichier en utilisant les noms des descripteurs et des [prix en français](https://fr.wikipedia.org/wiki/Prix_Nobel#Disciplines_r%C3%A9compens%C3%A9es) (Physics
-> Physique...). Pour cela utiliser la fonction Rechercher et
Remplacer(`Menu Edition> Rechercher et Remplacer`)
  
## Filtrage des données
* Selectionner toutes les colonnes du tableau

{{< img src="../images/nobels1.png" >}}

* Cliquer sur l'icône en forme d'entonnoir dans le menu du haut. Vous pouvez maintenant cliquer sur les petites flèches à côté des noms des descripteurs pour **filtrer les données** (ne sélectionner que certaines valeurs), les **trier** par ordre croissant, ou décroissant.

*Vous obtenez alors une **VUE** à partir de votre **TABLE**. C'est à dire un extrait de la table.*

**Qu 2a.** Quand a été décerné le premier prix Nobel de Littérature? Et d'économie? Combien de lauréats ont reçu un prix Nobel cette année?

**Qu 2b.** Combien de femmes ont reçu un prix Nobel? Et d'hommes?

**Qu 2c.** Quelle est la discipline dans laquelle les femmes sont les plus représentées? Le moins représentées?

> **Qu 2d.** Bilan: Quelle est la différence entre FILTRER et TRIER des données? Expliquer le rôle de chacune de ces fonctions en utilisant l'exemple de la Qu 2a. Rechercher le nom des instructions correspondante en langage SQL sur une base de données: [Lien 1: order by](https://sql.sh/cours/order-by), [Lien 2: where](https://sql.sh/cours/where)

## Nouveau tableau statistique

Nous allons maintenant créer un nouveau tableau pour rassembler des statistiques sur le genre des prix Nobel.


- Rappelez-vous que les formules commencent toujours par un signe `=`.

- Pour référencer une cellule on utilise son adresse sous la forme
  `ColonneLigne`. Exemple: `D2` pour la cellule de la colonne `D`, ligne `2`.

- On peut référencer une plage de cellule.

  Exemple: `D2:D10` pour les cellules `D2` à `D10` de la feuille.



Dans une partie libre de la feuille, créer le tableau suivant:

{{< img src="../images/tab-stats.png" >}}



### Nombre de femmes prix nobel Chimie
Dans la cellule **Chimie** -> **femme**, écrire `=` puis `NB.SI.ENS(`

La fonction `NB.SI.ENS` applique des critères aux cellules de plusieurs plages et compte le nombre de fois où tous les critères sont remplis.

$$=NB.SI.ENS(plage~critères1; critères1; plage~critères2; critères2…)$$



Un tutoriel sur la page [support.microsoft.com](https://support.microsoft.com/fr-fr/office/fonction-nb-si-ens-dda3dc6e-f74e-4aee-88bc-aa8c2a866842)

Ainsi, pour savoir combien de "femme"-s ont obtenu le prix Nobel de Chimie, il y aura 2 couples *plage critère* <-> *critère*:

* La première plage critère: sélection de la catégorie. B2:B1000 
* Le premier critère: "Chimie" (ou "Chemistry" si le document est resté en anglais)
* La deuxième plage critère: C2:C1000
* Le deuxième critère: "femme" (ou "female" si le document est resté en anglais)

- Exemple: Pour dénombrer le nombre de femmes qui ont reçu le prix nobel de Chimie:

$$=NB.SI.ENS(B2:B1000;"female";C2:C1000;"Chemistry")$$

### Compléter le tableau
Pour chacune des cases des colonnes `femme` et `homme`, saisir les formules qui donnent les nombre de *femmes* et d'*hommes* pour chaque catégorie de prix Nobel. Utiliser la fonction `=NB.SI.ENS()`

### Totaux
Dans les colonnes totaux (dernière colonne et dernière ligne), appliquer la fonction `SOMME` pour ajouter les valeurs sur une même ligne, ou sur une même colonne. [support microsoft](https://support.microsoft.com/fr-fr/office/somme-somme-fonction-043e1c7d-7726-4e80-8f32-07b23e057f89#:~:text=La%20fonction%20SUM%20ajoute%20des,des%20cellules%20A2%20%C3%A0%20A10.)

Il est aussi possible d'utiliser une formule utilisant des opérateurs mathématiques (`+, -, /, *`) sur les cellules: `= A1 + A2` par exemple, pour additionner les valeurs des cellules `A1` et `A2`. 

**Qu 3a.** Compléter les valeurs du tableau dans la feuille de reponse.

**Qu 3b.** Calculer dans une cellule de la feuille Excel, la proportion de *femmes* parmi les nobélisés (pourcentage). Donner le résultat, ainsi que la formule utilisée.

## Graphique

Sélectionner les données calculées du nouveau tableau de statistiques pour créer un histogramme résumant les données.

On peut s'aider du tutoriel suivant pour l'affichage d'un histogramme.

{{< img src="../images/graph1.png" link="https://www.youtube.com/watch?v=JNl-H6VRz6U" caption="Excel - 1 Basique - Cours Graphique" >}}

{{< img src="../images/nobels_histo.png" caption="exemple d'histogramme réalisé sur des valeurs fictives" >}}

# Base de données


1. Telecharger la base de données sous format SQL: [nobels.sql](/scripts/BDD/nobels.sql).

2. Ouvrir dans un nouvel onglet le gestionnaire de bases de données [sqliteonline.com](https://sqliteonline.com/).

3. Depuis le menu du logiciel, faire (+) dans le coin gauche et *import*. Importer alors le fichier SQL.

4. Tester alors dans l'editeur les commandes SQL correspondant aux *requêtes* que vous avez réalisées depuis le tableur. 

Voir [cours SQL](/docs/NSI/bases/page7) en ligne.

