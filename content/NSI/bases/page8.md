---
Title: TP prenoms sql
description: application du cours sql, base de donnees des prenoms
weight: 54
---



# TP1 sur la base des stations de métro
Se rendre à la page de Quentin Fortier, professeur en classes preparatoires [https://sql-exercices.github.io/](https://sql-exercices.github.io/) et choisir (à gauche), l'exercice sur le métro parisien. Celui-ci propose de travailler sur une base de données à une seule table.

La page se présente comme ceci.

{{< img src="../images/metros.png" caption="credit: fortierq Quentin Fortier" >}}

Pour chacune des questions, placer vos requêtes en bas de la page, et vérifier avec le bouton VALIDER.

# TP2 sur la table des prenoms
## Télécharger la table en format csv
Le site de l'*insee* propose une page avec les fichiers des prenoms de l'état civil: [Lien](https://www.insee.fr/fr/statistiques/7633685)

Un {{< download link="/scripts/BDD/Dpt06depuis2000.sql" hint="Dpt06depuis2000.sql" caption="fichier" >}} d'extension `.sql` a été généré à partir de ces données. Téléchargez le {{< download link="/scripts/BDD/Dpt06depuis2000.sql" hint="Dpt06depuis2000.sql" caption="ici" >}}.


## Ouverture du fichier: Deux options possibles
### Local: DB Browser for Sqlite
* Lancez votre gestionnaire de base de données (DB Browser for Sqlite). Si besoin, une version portable se trouve [ici](https://sqlitebrowser.org/dl/)

* Dans le menu: **Import**: Database from SQL file...

* Ouvrir le fichier qui se trouve dans vos Documents. 

* Le logiciel vous demande alors quel sera le nom de la base de données. Choisir: **prenoms**.

<!--
{{< img src="../images/prenom1.png" caption="import depuis sqliteonline.com" >}}

{{< img src="../images/prenom2.png" caption="import depuis db Browser for sqlite" >}}
-->

### En ligne: sqliteonline.com
gestionnaire en ligne [sqliteonline.com](https://sqliteonline.com/)


## Affichage de la table
Pour la suite, les instructions seront données pour le logiciel en local: *DB Browser for Sqlite.*

Dans la partie supérieure gauche, observez 4 onglets qui permettent de choisir entre:

* Database Structure
* Browse Data
* Edit Pragmas
* Execute SQL

> Choisir Database structure: nom de la table et des différents attributs

{{< img src="../images/sqlite_tables.png" caption="présentation des différentes tables et attributs" >}}

> Choisir Browse Data: observer le contenu e la table

{{< img src="../images/sqlite_browse.png" caption="parcourir les valeurs de la table" >}}

> Choisir Execute SQL

La fenêtre permet alors de placer une requete en langage SQLite. Le résultat dans une autre fenêtre, juste au dessous.

<!--
Aller dans l'onglet *Parcourir les données*.

On observe:

* que le nom de la table, c'est *nat2022*
* que le nom des colonnes n'est pas bien explicite

{{< img src="../images/prenom3.png" caption="Parcours des données - observer les noms de colonne et nom de la table" >}}

à l'import, on a les noms suivants:

| nom table | colonne 1 | colonne 2 | colonne 3 |
| --- | --- | --- | --- |
| nat2022 | sexe | preusuel | annais | nombre |

On va modifier ça: **Modifier** le nom de la table ainsi que celui des colonnes pour avoir les noms suivants:

| nom table | colonne 1 | colonne 2 | colonne 3 |
| --- | --- | --- | --- |
| naissances | sexe | prenom | annee | nombre |

*Rappels:*

pour **Renommer une colonne**:

```SQL
ALTER TABLE nom_table
RENAME COLUMN ancien_nom TO nouveau_nom
```

pour **Renommer la table**:

```SQL
ALTER TABLE table_name
RENAME TO new_table_name
```
-->

**Afficher** les premières lignes de la table afin de prendre connaissance des étiquettes des colonnes:

```sql
SELECT * FROM prenoms LIMIT 10;
```

Executer avec le bouton d'execution.

{{< img src="../images/sqlite_requete.png" >}}


## Travail
<!--
voir fiche [question-reponses](/pdf/NSI/bdd2_fiche_reponse_prenoms.pdf)
-->

Ecrire et tester une à une les instructions qui permettent de:

1. Afficher les dix premières lignes de la table
2. Afficher les lignes correspondant à l'année 2000. Là encore, mieux vaut ne demander que les 10 premières lignes…
3. Afficher les prénoms des garçons nés en 2000 (limiter à 50).
4. Combien de fois le prénom Nicolas a-t-il été donné en 2000 ?
5. Afficher les 10 prénoms de fille les plus donnés en 2000 rangés dans l'ordre décroissant du nombre de fois où ils ont été donnés. Utiliser les mots-clés:
`SELECT FROM WHERE ORDER BY DESC LIMIT`
6. Afficher les lignes des prénoms de garçons donnés entre 2000 et 2020 (inclus l'un et l'autre). Utiliser un AND pour tester l'encadrement des années.
7. Afficher le nombre de prénoms différents de garçons donnés depuis 2000.
`SELECT COUNT(*) FROM WHERE`
8. Afficher le nombre de naissances de garçons observées en 2020.
9. Afficher le nombre de filles et le nombre de garçons apparaissant dans la table.
`SELECT SUM(nombre) FROM GROUP BY`
10. Quel est le prénom, pour un certain sexe, en distinguant par exemple "Camille (fille)" et "Camille (garçon)", qui a été le plus donné durant une année donnée ? En quelle année ?
`SELECT FROM ORDER BY DESC LIMIT`
11. En quelle année y-a-t-il eu le plus de naissances ?
SELECT SUM(nombre) FROM GROUP BY ORDER BY DESC LIMIT
12. Quels sont les 10 prénoms les plus donnés en France au cours du XXI-ème siècle en cours?
`SELECT SUM(nombre) FROM GROUP BY ORDER BY DESC LIMIT` 

# Autres travaux pratiques SQL
## Table unique
Exercice sur les nouilles japonaises. Interface en ligne par N. Revéret sur [forge.apps.education.fr](https://exercices-bdd-aa801f.forge.apps.education.fr/32_ramens/ramens/)
## Pays, villes et langues parlées, plusieurs tables
Exercice sur le langage SQL rédigés par N. Revéret sur [forge.apps.education.fr](https://exercices-bdd-aa801f.forge.apps.education.fr/41_films/films/). Interface en ligne.

# Liens
* memento SQL sur [forge.apps.education.fr](https://exercices-bdd-aa801f.forge.apps.education.fr/memento_sql/)
* l'exercice sur les prenoms est inspiré du site [forge.apps.education.fr](https://exercices-bdd-aa801f.forge.apps.education.fr/)
* autres themes sur [forge.apps.education.fr](https://forge.apps.education.fr/gbecker/terminale-nsi/-/blob/9b29abe61b7b7aef253f99a863c8d047924b4d02/Theme2_base_de_donnees/02_langage-sql-exercices.md) (disquaire)