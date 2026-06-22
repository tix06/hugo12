---
Title: langage SQL
description: cours langage sql
weight: 53
---


# Langage SQL
SQL: structured query langage = langage de requêtes structuré est un langage informatique de dialogue avec une base de données relationnelle (un fichier qui organise les données sur une ou plusieurs tables).

Une **requête** est une question posée à une base de données. Nous allons voir comment sont écrites les requêtes de base en SQL. Une requête est la traduction d'une relation écrite en algèbre relationnelle.

L'algèbre relationnelle est un outil créé par le chercheur E. Codd (1970) pour manipuler les tables dans le modèle relationnel. Ses principales opérations sont: SELECTIONNER certaines colonnes (Projection) ou certaines lignes (selection) d'une table, mais aussi de combiner 2 tables.

Chaque opération SQL prend en entrée une ou plusieurs tables et renvoie une table.

{{< img src="/images/download.png" link="/pdf/NSI/bdd2-e.pdf" caption="version pdf" >}}



Voyons dans un premier temps les requêtes utiles pour CREER, SUPPRIMER, REMPLIR et MODIFIER la table

# Creation, modification de table
## CREATE TABLE "nom_table" (schema relation);
Créons la table:

| `Nom_eleve`	|	`Classe` |		`Math`	|		`Anglais`		|	`Info` |
|--- |--- |--- |--- |--- |
| Kevin | 209 | 16 | 17 | 18 |
|Zoe | 209| 5  | 15 | 17 |
| Toto | 210 | 4 | 6 | NULL |

```SQL
CREATE TABLE IF NOT EXISTS Table_notes (
	Nom_eleve		TEXT PRIMARY KEY,
	Classe INTEGER,
	Math		REAL,
	Anglais		REAL,
	Info		REAL);
```

CREATE TABLE va permettre d'indiquer le schéma d'une relation, avec ses **Attributs** et **Domaines**. Les types (ou domaines) les plus courants sont parmi: 

* INTEGER, entier positif ou nul
* TEXT, CHAR(n), chaine de caractères
* DATE, format de date du type  YYYY-MM-DD 
* REAL, une valeur décimale 


On peut ajouter des contraintes (`constraints`) en paramètre : PK (Primary Key), UNIQUE (dans une colonne, les valeurs doivent être uniques à chaque ligne), AUTOINCREMENT, NOT NULL (doit comprendre une valeur), DEFAULT 'Not Applicable' (la valeur mise par défaut si vide).

```SQL
CREATE TABLE etat_civil (
   id INTEGER PRIMARY KEY, 
   name TEXT UNIQUE,
   date_of_birth TEXT NOT NULL,
   date_of_death TEXT DEFAULT 'Not Applicable';)
```


## INSERT INTO "nom_table" (Attributs) VALUES (n-uplet1), (n-uplet2), ...;
On **insère** les valeurs dans la table:

```SQL
INSERT INTO "Table_notes" VALUES
("Doe", 16, 17, 18),
("Zoe", 12, 15, 17),
("Toto", 4, 6, NULL);
```

`("Doe", 16, 17, 18)` est un argument contenant les valeurs à insérer.

*Remarque:* si un enregistrement n'existe pas, il faudra mettre `NULL`

## `UPDATE <table> SET <attribut = valeur> WHERE  <attribut = valeur>`
Pour **modifier des valeurs**

```SQL
UPDATE Table_notes
SET Math = 18
WHERE Nom = "Doe";
```

## `DELETE FROM <table> WHERE <condition>`
Supprimer des lignes

```SQL
DELETE FROM Table_notes
WHERE Math <= 14;
```

## `ALTER TABLE <table> ADD COLUMN <Attribut Domaine>`
pour **modifier la table**


```SQL
ALTER TABLE Table_notes ADD COLUMN Biologie INTEGER;
```

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

## `DROP TABLE <table>`
Supprimer une table

```SQL
DROP TABLE Table_notes;
```

# Les CLAUSES SQL
Les mots-clefs SELECT, FROM, WHERE, GROUP BY, HAVING et ORDER BY sont appelés des clauses.


{{< img src="../images/resume_sql.png" caption="clauses SQL sur la tables des romans" >}}

## `SELECT <attributs> FROM nom_table` 
SELECT est la commande qui retourne la table selon les **attributs** choisis. Il s'agit d'une **Projection** comme type d'*opération relationnelle*.

*Une **projection** est un type de sélection où seulement une partie des attributs des tables choisies est retenue pour le résultat.*

FROM est la *table concernée*.

Pour avoir toutes les colonnes, faire:

```SQL
SELECT * FROM Table_notes
```

ou bien seulement certaines:

```SQL
SELECT Math, Nom_eleve AS Nom FROM Table_notes
```

On peut renommer une colonne avec l'alias AS, et choisir un nom plus pratique.

`SELECT DISTINCT` retourne les éléments de manière **unique**.

Et limiter le nombre de lignes à 10 par exemple:

```SQL
SELECT * FROM Table_notes LIMIT 10
```

## `SELECT DISTINCT <attributs> FROM nom_table` 
L'ajout du mot-clé DISTINCT, ne va retourner qu'une seule fois les lignes pour chaque valeur d'une colonne donnée. Il n'y aura pas de doublon, seule la première occurence est retournée.

## `WHERE <condition>`
La clause WHERE permet de SELECTIONNER des lignes à partir de conditions dans les requêtes, mais aussi de realiser des JOINTURES (voir plus loin)

```SQL
SELECT Nom_eleve
FROM Table_notes
WHERE Math > 14 OR Info >= 18;
```

> *Exercice*: Représenter la table `Table_notes` (En-tête et contenu de la colonne) qui sera retournée par cette requête.



## AVG SUM MIN MAX COUNT
Ce sont des fonctions d'**agregation**, qui retournent un resultat évalué sur la colonne issue de la SELECTION 

*Exemple1*: Combien d'élèves ont plus de 15 en math dans la table `Table_notes`?

```
SELECT COUNT(*) FROM Table_notes WHERE Math > 15
```

*Exemple2:* Combien de romans de l'auteur `id_auteur` =5 y-a-t-il dans la table `romans`?

```SQL
SELECT count(*) FROM romans WHERE id_auteur = 5
```

* COUNT(*) va compter le nombre de lignes pour la selection donnée
* SUM(attribut) va faire la somme pour les valeurs de l'attribut et pour la selection donnée
* AVG(attribut) calcule la moyenne
* MIN(attribut) retourne la valeur min, MAX(attribut) la vakeur max

> *Exercice:* Ecrire la requête qui calcule la moyenne de math pour tous les élèves de la table `Table_notes`

## `GROUP BY <uneTable.attribut1>`
Permet de regrouper des lignes les unes avec les autres. 

Pour regrouper des lignes d'une table selon un attribut, il faut que ces lignes aient la **même** valeur pour cet attribut.

GROUP BY s'utilise avec des **agrégats**.

*Exemple:* Quel total de notes figure dans la table `romans`pour chaque auteur?

```SQL
SELECT SUM(note) FROM romans GROUP BY id_auteur
```

> Exercice: Ecrire une requête qui calcule la moyenne des notes obtenues par écrivain sur la table Romans.

## `ORDER BY <colonne> ASC [DESC]` 
Trions les lignes par ordre croissant des notes en math:

```SQL
SELECT Nom, Math
FROM Table_notes
ORDER BY Math ASC;
```

Sinon par ordre descendant: `ORDER BY Math DESC`

> Exercice: Représenter le tableau retourné par la requête écrite en exemple.

> Exercice: Ecrire une requête qui calcule la moyenne des notes obtenues par écrivain sur la table Romans et qui classe ces auteurs par ordre de note moyenne décroissante.

*Remarque:* On peut aussi rajouter une *clause* sur le nombre de lignes retournées avec `LIMIT <nombre>` Très pratiques pour de grandes tables.

## 'GROUP BY ... HAVING`
La clause HAVING permet d'effectuer une selection sur des valeurs issues de regroupements.

Par exemple, on ne pourra pas écrire:

```sql
select count(*) from UEFA group by pays where count(*)>18
```

mais: 

```sql
select count(*) from UEFA group by pays having count(*)>18
```

## `WHERE <colonne> LIKE <motif>` et `WHERE <colonne> IN <tuple>`
### LIKE
On peut faire une recherche dans une table selon certains motifs. Pour cela, on utilise `WHERE ... LIKE <suivi de caractères spéciaux>`.

Caractères spéciaux:

* le caractère `%` représente 0, 1 ou plus de caractères
	* `%s` permet d'obtenir toutes chaines qui finissent par s, mais aussi le caractère unique s.
* le caractère `_` représente un caractère unique
	* `ro_e` permet d'obtenir `robe` ou bien `rose`

> Exercice: Dans la relation `Eleves` de schéma `((prenom, TEXT), (nom, TEXT), (nais, DATE), (rue, TEXT), (numero, INTEGER), (CP, INTEGER), (ville, TEXT), (email, TEXT)):

> 1. Définir une requête qui permet d'obtenir tous les élèves nés en 2002
2. Définir une requête qui permet d'obtenir tous les élèves habitant dans le département des Alpes Maritimes.
3. Définir une requête qui permet d'obtenir tous les élèves ayant un compte e-mail chez l'opérateur *laposte* (du type *pseudo@laposte.net*)

### IN
Pour faire une recherche dans une table selon une liste de critères, on utilise le mot clé `IN`
On peut par exemple rechercher les élèves qui habitent Nice, Saint-Laurent ou Cagnes-sur-mer dans la table `Eleves`:

```SQL
SELECT nom, prenom
FROM Eleves
WHERE ville IN ('Nice', 'Saint-laurent', 'Cagnes-sur-mer')
```

*Remarque:* Cette syntaxe peut être ajoutée à l'opérateur `NOT`, ce qui fait `NOT IN`.

On peut avoir besoin d'extraire un groupe de lettres du texte. On utilise alors la fonction `substr`. Les paramètres attendus sont:

* nom de l'attribut
* rang du premier caractere (commence à 1)
* rang du dernier caractere.

*Exemple: Recherche des élèves dont les noms commencent par 'a', 'b' ou 'c':*

```SQL
SELECT nom, prenom
FROM Eleves
WHERE substr(nom, 1, 1) IN ('a', 'b', 'c')
```

> Exercice: 

> Ecrire une requête sur la table *Eleves* qui retourne les noms des élèves dont la famille habite dans les départements ('06', '83', '05')

## Jointure
Pour eviter les redondances, on a vu qu'il était préférable de répartir les données sur plusieurs tables, chaque table modélisant UNE seule entité.

La jointure permet de mettre en relation plusieurs tables, par l’intermédiaire des liens qui existent en particuler entre la **clé primaire** de l’une et la **clé étrangère** de l’autre.
La jointure est une opération de sélection car elle permet de ne retenir que les enregistrements pour lesquels la valeur de la **clé primaire** d’une table correspond à la valeur de la **clé étrangère** d’une autre table.


{{< img src="../images/jointure.png" caption="exemple de jointure entre 2 tables" >}}

Pour joindre 2 tables complètes:

* **1ere méthode**:

```SQL
SELECT *
FROM orders
JOIN customers
  ON orders.customer_id = customers.customer_id;
```

à la 4e ligne : on declare comment les 2 tables sont combinées : on veut faire correspondre la colonne `ìd_customers`de la table orders avec celle `ìd_customers`de la table customers.

Comme le nom d'une colonne va se retrouver dans de nombreuses tables, on utilisera la syntaxe : `table_name.column_name`

* **2e méthode**:

```SQL
SELECT *
FROM orders, customers
WHERE orders.customer_id = customers.customer_id;
```

