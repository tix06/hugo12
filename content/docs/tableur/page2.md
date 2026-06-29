---
Title: graphiques tableur
---

# Partie 1: Traitement de données avec un tableur
Lors de la [seance précédente](/docs/competences/Form/page1), vous avez réalisé un questionnaire en ligne. L'interface de [framaforms](https://framaforms.org/abc/fr/) permet de visualiser les réponses, et d'établir des statistiques. 

Mais, les réponses étant accessibles dans un format standard, le fichier de données peut également être ouvert avec un logiciel tableur.

## Soumission et import des résultats du questionnaire
A l'aide du lien de partage sur votre tableau de bord sur [framaforms.org](https://framaforms.org/abc/fr/), répondez à votre questionnaire.
Répéter l'opération au moins 2 fois. Puis, depuis votre tableau de bord, choisissez le téléchargement en format *csv*.

Choisir *virgule* (`,`) comme séparateur. 

{{< img src="../images/graph2.png" >}}

Dans *Composants d'export inclus*, choisir les informations à importer. Ne pas choisir celles relatives à l'identité des parents questionnés (formulaire anonyme).

{{< img src="../images/graph3.png" >}}

**Télécharger** votre fichier.

**Question a:** Quelle est l'extension du fichier? Avec quel logiciel (editeur texte) peut on *ouvrir et visualiser* les données? Donner au moins 2 exemples à partir des logiciels installés sur votre ordinateur.

**Question b:** Comment sont organisées les données dans le fichier? Décrire le format des données.

Pour la suite de la séance, nous allons prendre le fichier suivant, [resultats.csv](../datas/resultats.csv) pour analyse.

Vous allez réaliser un premier travail de mise en forme des données avant leur représentation graphique.

## Mise en forme des données sous Excel
- Télécharger le ficher, [resultats.csv](../datas/resultats.csv), et l'ouvrir avec Excel (*ou bien LibreOffice Calc*) comme vu dans le TP sur le [format des données](/docs/SNT_2nde/pages/pages_donnees/page5/).

- Enregistrer le fichier au format `xls` dans le même répertoire. *Attention, Sans cette manipulation, `csv -> xls`, vous risquez de perdre vos travaux sur ce fichier.*

Maintenant que nous sommes sur un fichier tableur d'extension `xls`, nous pouvons utiliser les fonctionnalités avancées de ce type de logiciel.

**Question c:** Combien de réponses au formulaire sont présentées dans le tableau?

**Question d:** Combien de questions comporte le formulaire?

### Utiliser la fonction nb.si
Pour compter le nombre de "Oui" dans une colonne, utiliser la fonction NB.SI

* Pour compter le nombre d'élèves qui fréquentent la cantine: Ecrire sous la colonne *Cantine*:

$$=NB.SI(plagedonnees;"Oui")$$

{{< img src="../images/graph4.png" caption="selection de la plage de données (en pointillés bleus) après avoir écrit =NB.SI(" >}}

Un tutoriel sur la page [support.microsoft.com](https://support.microsoft.com/fr-fr/office/fonction-nb-si-e0de10c6-f885-4e71-abb4-1f464816df34)

* Plage données correspond alors à C1:C50 si la colonne C est celle de *cantine* (Et que le tableau contient 50 lignes)
* On peut aussi, de la même manière, compter le nombre de "Non". 

**Question e:** Quelle formule Excel donne le nombre de "Oui" pour la colonne *cantine*? Quelle formule donne le nombre de "Non"?

### Utiliser la fonction nb.si.ens
La fonction NB.SI.ENS applique les critères aux cellules de plusieurs plages et compte le nombre de fois où tous les critères sont remplis.

$$NB.SI.ENS(plage~critères1; critères1; plage~critères2; critères2…)$$


Un tutoriel sur la page [support.microsoft.com](https://support.microsoft.com/fr-fr/office/fonction-nb-si-ens-dda3dc6e-f74e-4aee-88bc-aa8c2a866842)

Ainsi, pour savoir combien d'élèves de "CP" déjeunent à la cantine, il y aura 2 couples *plage critère* <-> *critère*:

* La première plage critère: sélection de la classe. B1:B50 si la colonne B correspond à la classe. Et que 50 lignes sont renseignées.
* Le premier critère: "CP"
* La deuxième plage critère: C1:C50
* Le deuxième critère: "Oui"

**Question f:** Quelle est alors la formule utilisée dans la cellule du tableur?

# Partie 2: Etude statistique
## Tableau statistique à 2 entrées
Cette deuxième partie demande une nouvelle présentation des données.

Vous allez créer 2 nouvelles tables à partir des résultats bruts:

* Une table donnant les effectifs cantine, suivi périscolaire:

{{< img src="../images/graph5.png" >}}

* Une table donnant une information sur la qualité d'accueil

{{< img src="../images/graph6.png" >}}

Les valeurs sont indicatives. Celles affichées dans chacune de vos tables doivent être calculées à partir du fichier .csv fourni, à l'aide des formules nb.si et nb.si.ens vues dans la partie 1.

**Completer la fiche reponse:** [tableau](/pdf/competences/formulaire.pdf)

## Graphiques, histogrammes
Il est conseillé de suivre le tutoriel suivant pour l'affichage des graphiques.

{{< img src="../images/graph1.png" link="https://www.youtube.com/watch?v=JNl-H6VRz6U" caption="Excel - 1 Basique - Cours Graphique" >}}

Obtenir les graphiques suivants (*les valeurs ont été modifiées pour le tracé et ne correspondent pas au tableau fourni*):

{{< img src="../images/excel1.png" caption="graphique 1" >}}

{{< img src="../images/excel2.png" caption="graphique 2" >}}

> Lequel de ces graphiques répond à la question:
* A. Quelle est la distribution de reponses des élèves de CP à propos de la qualité de la cantine?
* B. Quelle distribution en age ou classe des élèves repond favorablement à la question sur la qualité de la cantine?

> Etablir un diagnostic à propos de cette enquête. (max 5 lignes)