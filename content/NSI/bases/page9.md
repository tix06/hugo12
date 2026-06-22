---
Title: TP base de libreoffice
description: TP utilisant le SGBD BASE de libreoffice, films
---

{{< img src="../images/base1.png" caption="schéma relationnel de la base de données films-realisateurs, base de libreoffice" >}}

# TP Browser SQL: Base, SQLite Browser, Access 
**Base de données sur FILMS et REALISATEURS**

## Base de Libre Office
### Démarrage
Lancer Libre Office > Base. Au demarrage:

* choisir "Créer une nouvelle base de données"
* nommer cette base de données. Par exemple `films_cultes`. L'extension placée par le logiciel est `.obd`

### Structurer et renseigner les données
Commençons par créer les 2 tables `films` et `realisateurs`.

{{< img src="../images/base2.png" caption="créer une nouvelle table" >}}

{{< img src="../images/base3.png" caption="remplir les champs nom et domaine pour chaque attribut" >}}

{{< img src="../images/base4.png" caption="1: selectionner la colonne de l'attribut id_films, 2: clic droit, choisir Primary Key" >}}


{{< img src="../images/base6.png" caption="1: sauvegarder la table, 2: renseigner le nom: films" >}}

{{< img src="../images/base7.png" caption="faire de même pour créer la table realisateurs" >}}

On va maintenant créer une *association* entre les 2 tables.

{{< img src="../images/base8.png" caption="menu Tools: choisir Relationships" >}}

{{< img src="../images/base9.png" caption="1: ajouter chacune des tables dans le canvas, 2: cliquer sur films.id_rea et le glisser sur realisateurs.id_rea" >}}

{{< img src="../images/base10.png" caption="bravo! vous avez créé l'association entre les 2 tables" >}}

La clé secondaire `films.id_rea` est maintenant liée à la clé primaire `realisateurs.id_rea`. 

Il reste maintenant à renseigner les données pour chacune des tables. Commencer par celle `realisateurs`. Car les tables sont liées par l'attribut `realisateurs.id_rea`

{{< img src="../images/base5.png" caption="1: clic droit sur la table realisateurs, 2: open" >}}


{{< img src="../images/base13.png" caption="renseigner les données" >}}

| **id_rea** | **nom** | **prenom** | **annee_naissance** |
| --- |--- | --- |--- |
| 1 | Kitano | Takeshi | 1947 |
| 2 | Burton | Tim | 1958 |
| 3 | Tarantino | Quentin | 1963 |
| 4 | Tati | Jacques | 1907 |
| 5 | Hitchcock | Alfred | 1899 |
| 6 | Almodovar | Pedro | 1949 |
| 7 | Kitamura |  Ryûhei |  1969 |

{{< img src="../images/base11.png" caption="puis ouvrir la table films" >}}

| **id_film** | **titre** | **date** | **id_rea** |
|--- |--- | --- | --- |
| 1 | Hana-bi | 1997 |  |
| 2 | Big fish | 2003 |  |
| 3 | Edward aux mains d'argent | 1990 |  |
| 4 | Sonatine | 1993 |  |
| 5 | Pulp Fiction | 1995 |  |
| 6 | Play Time | 1967 |  |
| 7 | Vertigo | 1958 |  |
| 8 | Psychose | 1960 |  |
| 9 | Parle avec elle | 2002 |  |
| 10 | Mon oncle | 1958 |  |
| 11 | Volver | 2006 |  |
| 12 |  Reservoir Dogs | 1992 |  |
| 13 |  Alive | 2003  |  |
| 14 |  Godzilla: Final Wars | 2004 |

{{< img src="../images/base12.png" caption="renseigner les données" >}}

### Requêtes sur la base de données
Les requêtes seront réalisées en mode interactif pour démarrer.

{{< img src="../images/base14.png" caption="Choisir 1. Database Queries puis 2. Design View" >}}

{{< img src="../images/base15.png" caption="Ajouter les tables films et realisateurs dans le canvas" >}}

{{< img src="../images/base16.png" caption="construire la requête comme sur l'image ci-contre" >}}

{{< img src="../images/base17.png" caption="passer en mode SQL avec le bouton (jaune) de la barre de menu" >}}

{{< img src="../images/base18.png" caption="Executer la requête SQL avec le bouton (vert)" >}}

Observer la **vue** présentée par le logiciel (tableau). Cette vue peut être obtenue avec une instruction plus simple en SQL.
Mettre les symboles `--` devant l'instruction SQL pour la mettre en commentaire.

Ajouter l'instruction SQL: `SELECT * FROM films`

Executer. Vous obtenez le même résultats...

{{< img src="../images/base19.png" caption="saisie directe d'une requête SQL" >}}

Tester une nouvelle requête en mode *Design View*

{{< img src="../images/base20.png" caption="nouvelle requête" >}}

Cette fois, on ajoute une clause sur la valeur de `id_rea`. Mais sans afficher l'attribut (Visible non coché).

Recopier la requête SQL générée. Executer. 

{{< img src="../images/base21.png" caption="nouvelle requête" >}}

Pour cette nouvelle requête en mode visuel, on selectionne des attributs des 2 tables. On applique certaines clauses. 

En mode SQL: Remarquer que la clause `"films"."id_rea" = "realisateurs"."id_rea"` s'est mise automatiquement.

Recopier cette requête SQL. 

Executer.

> Questions: Ecrire les requêtes SQL pour...

1. Afficher toute la table `films`
2. Corriger la date de parution du film *Vertigo* (se renseigner sur le net)
3. Afficher tous les attributs du-des film-s dont le réalisateur est le 1er de la table `realisateurs`
4. tous les titres des films sortis après 1970 mais avant 2002
5. le titre du film, la date de sortie le nom du realisateur pour `id_rea` egal à 2
5. tous les noms des auteurs de films qui ont sorti des films après 1960, mais pas Jacques Tati.
6. l’année de naissance du réalisateur de Reservoir Dogs ?
7. Le nombre de films du réalisateur "Hitckock"
8. Inventer une nouvelle information à partir de cette base de donnée, necessitant une jointure entre les tables.

## SQLite DBrowser
* une version portable du logiciel peut être téléchargée ici: [sqlitebrowser.org](https://sqlitebrowser.org/dl/)
* Notice:{{< a link="http://prof.math.free.fr/mgtmn/tp/bdd_pres_dbb_sqlite.pdf" caption="Consulter la notice" >}}


> Vous pouvez aussi construire les 2 tables avec SQLite DBrowser:
> * Commencer par construire la table realisateurs, puis celle films. Bien renseigner les clés primaires (PK) pour ces 2 tables, ainsi que la clé étrangère pour *films*
> * ajouter les lignes à chaque table, ici aussi, en commençant par *realisateurs*




# Solutions
Tester alors les instructions SQL suivantes... Recopier ensuite l'instruction et expliquer dans chaque cas ce qui est renvoyé:

* requête 1: `SELECT * FROM films`
* requête 3: 

```SQL
SELECT * FROM films
where ID_rea=1
```

* requête 4:

```
SELECT * FROM films
where ID_rea=1 or Date>2003
```

* requête 5: Deux possibiltés:

```SQL
select titre, date, last_name from realisateurs, films 
where films.id_rea = 2 and films.id_rea = realisateurs.id_rea
```

ou bien, en précisant la jointure avec `INNER JOIN`

```SQL
SELECT titre, date, realisateurs.last_name  FROM films
INNER JOIN realisateurs on films.id_rea = realisateurs.id_rea
where films.id_rea = 2;
```

# Compléments
La table en version sqlite se trouve ici: [films.db](/scipts/BDD/films_de_zero.db)
