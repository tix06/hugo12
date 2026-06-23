---
Title: traitement des donnees en table
description: Open datas, csv, module requests, donnees en table
weight: 21
---

# Liste de dictionnaires
Les epreuves pratiques proposent de nombreux exemples de traitement de données en liste de dictionnaires. Se référer aux sujets de 2026.

# Open Datas, liste de listes
## Un exemple de données ouvertes
{{< img src="../images/page13/data.gouv.png" link="https://www.data.gouv.fr/fr/" caption="Plateforme ouverte des données publiques françaises" >}}
Le Répertoire National des Élus (RNE) a pour finalité le suivi des titulaires d’un mandat électoral. Il est renseigné et tenu à jour par les préfectures et hauts commissariats et par les services du ministère de l'intérieur, notamment sur la base des éléments fournis par les élus lors de la phase d’enregistrement des candidatures.

{{< img src="../images/page13/elus.png" caption="Données du RNE pour les conseillers municipaux - extrait en csv" >}}
Les données du RNE sont structurées par mandat. Neuf fichiers sont publiés ici :

1.{{< a link="https://www.data.gouv.fr/fr/datasets/r/d5f400de-ae3f-4966-8cb6-a85c70c6c24a" caption="les conseillers municipaux ;" >}}

2. les conseillers communautaires ;
3. les conseillers départementaux ;
4. les conseillers régionaux ;
5. les membres des assemblées des collectivités à statut particulier ;
6. les représentants au Parlement européen ;
7. les sénateurs ;
8. les députés ;
9. les maires.


En [bas de page](https://www.data.gouv.fr/fr/datasets/repertoire-national-des-elus-1/#community-reuses), vous pourrez observer les réutilisations de ces documents:

{{< img src="../images/page13/utilisation.png" link="https://www.spallian.com/2020/03/01/donnees-parite-aux-sein-des-conseils-municipaux/" caption="exemples de réutilisation des données ouvertes sur les elus municipaux" >}}
*Ouvrir les données jugées d'intérêt public, c'est encourager leur réutilisation par tout un chacun. Cela permet d'encourager la transparence démocratique, de bénéficier de services au quotidien ou de prendre des décisions plus éclairées.*

## Exploration et traitement de données 
Télécharger sur le site gouvernemental le fichier {{< a link="https://www.data.gouv.fr/fr/datasets/r/d5f400de-ae3f-4966-8cb6-a85c70c6c24a" caption="ldes élus municipaux ;" >}}, au format `.csv`

Ouvrir un nouveau notebook, ou bien un nouveau fichier dans votre IDE python (Spyder ou Pyzo). Déplacer le fichier `*.csv` dans le même dossier que le notebook/fichier python.

Lire et stocker le contenu du fichier dans une liste python que vous appelerez `table`. 

> On pourra s'aider: 
> > du dernier paragraphe de la page Python les bases > entrées / sorties pour importer le fichier csv.
> > du TP sur les algorithmes de recherche dans un dictionnaire: [voir TP ici](/docs../page14_bis/)


Une fois la liste des élus importée dans une liste python:

> Dans votre editeur python, explorer la liste table pour qu'elle affiche les informations sur la longueur, sur les premiers élus.

Si vous choisissez le **bon caractère de séparation** des données, vous devriez obtenir quelque chose d'approchant (la mise à jour est régulière, et les données peuvent différer):

```python
> len(table)
490805
> table[1]
['32', 'Gers','','','32249','Mauvezin','MASAROTTI',
 'Sylvie','F', ...]
```

*Chaque élément de `table` est constitué d'une liste, avace chaque valeur séparée par une virgule `,`

Si par contre, vous identifiez mal le caractère de séparation, vous allez obtenir quelque chose comme cela:

```python
> len(table)
1
> table[1]
['32\tGers\t\t\t32249\tMauvezin\tMASAROTTI\tSylvie\tF']
```

ou peut-être:

```python
> len(table)
1
> table[1]
['32;Gers;;;32249;Mauvezin;MASAROTTI;Sylvie;F']
```

**Question 1:** Quels sont les rangs auxquels se trouvent le numero de departement, ainsi que celui du sexe de l'élu 'H'/'F'?

> Explorer pour définir l'ordre dans lequel sont classés les élus. 

<!--
**Question 2:** Les élus du *Gers*, occupent-ils les premiers rangs? Et si oui, jusqu'à quel rang? Ecrire un script python qui recherche cette information.
-->

## Fonction recherche
> Ecrire une fonction `recherche` qui *recherche* le premier élu dans un departement donné. La fonction *recherche* aura pour seul argument la variable textuelle `dpt` correspondant au departement recherché.

Cette fonction prend les éléments du tableau un par un, en commençant par le debut, et recherche la premiere occurence (le premier élu de ce departement).

Par exemple:

```python
> recherche('06')
363891
```

**Question 2:** Pourquoi la fonction retourne t-elle un entier (par exemple 363891)?

**Question 3:** Quelle est le numero de ligne du dernier élu du departement 06 (utiliser la fonction `recherche`)?

## Fonction pariteHF
> Ecrire une fonction *pariteHF* qui compte le nombre d'élus Hommes et le nombre d'élues Femmes pour un departement donné. La fonction renvoie alors le couple de valeurs H/F.

Exemple:

```python
> score_M,score_F = pariteHF('34')
> score_M,score_F
(3143, 2646)
```

**Question 4:** Donner le script de cette fonction.

## Graphique
Représenter alors cette parité dans votre notebook sur un diagramme circulaire.

> On s'aidera du [lien suivant](https://python.doctor/page-creer-graphiques-scientifiques-python-apprendre) pour représenter des diagrammes avec *Matplolib*.

{{< img src="../images/page13/diagramme.png" caption="exemple de diagramme sur la proportion des élus H/F" >}}

## Prolongement
Rechercher si, pour l'un des departements, le ratio 'F'/'M' est supérieur à 1.

**Faire un compte rendu avec les réponses, les scripts et graphiques**. *Utiliser un editeur de texte.*

## Suggestion de projet
Utiliser une API en python avec le module `request`, et charger directement le fichier de données. Une API est une interface logicielle qui permet de se « connecter » à un service, ou un serveur.

*Exemple* issu de [realpython.com](https://realpython.com/python-api/)

```python
>>> import requests
>>> response = requests.get("https://randomuser.me/api/")
>>> response.text
'{"results":[{"gender":"female",
"name":{"title":"Ms","first":"Isobel","last":"Wang"}...'
```

Cette méthode permet de consulter la version la plus recente, mise à jour sur le serveur. On peut imaginer de nombreuses applications (météo, prix du carburant, ...)