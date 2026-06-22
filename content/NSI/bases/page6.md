---
Title: TP romans sql
description: TP avec SGBD sqlitebrowser, livres, bibliotheque
weight: 57
---




# TP SQL
Nous allons créer (ou télécharger) une petite base de données à deux tables pour nous exercer aux requêtes SQL.

## Utiliser SQLite Browser
* Créer une *Nouvelle Base de données*: `bibliotheque.sqlite` (ajouter `.sqlite`)
* Editer la definition de la table selon l'image suivante


{{< img src="../images/table_brows.png" caption="table AUTEURS" >}}
* Fichier > Exporter > Exporter la base de données sous format SQL. Enregistrer le fichier avec le nom `bibliotheque.sql` (ajouter l'extension `.sql`)
* Ouvrir le fichier `bibliotheque.sql` avec un editeur de texte (*Notepad++* ou autre)
* Ajouter les instructions de creation d'une nouvelle table LIVRES de schéma:

```SQL
(id INT, titre TEXT, id_auteur INT, ann_publi INT, note INT, PRIMARY KEY (id), FOREIGN KEY (id_auteur) REFERENCES AUTEURS(id));
```

* Ajouter les entrées suivantes à chacune des tables:

```SQL
INSERT INTO AUTEURS
(id,nom,prenom,ann_naissance,langue_ecriture)
VALUES
(1,'Orwell','George',1903,'anglais'),
(2,'Herbert','Frank',1920,'anglais'),
(3,'Asimov','Isaac',1920,'anglais'),
(4,'Huxley','Aldous',1894,'anglais'),
(5,'Bradbury','Ray',1920,'anglais'),
(6,'K.Dick','Philip',1928,'anglais'),
(7,'Barjavel','René',1911,'français'),
(8,'Boulle','Pierre',1912,'français'),
(9,'Van Vogt','Alfred Elton',1912,'anglais'),
(10,'Verne','Jules',1828,'français');
```
et 

```SQL
INSERT INTO LIVRES
(id,titre,id_auteur,ann_publi,note)
VALUES
(1,'1984',1,1949,10),
(2,'Dune',2,1965,8),
(3,'Fondation',3,1951,9),
(4,'Le meilleur des mondes',4,1931,7),
(5,'Fahrenheit 451',5,1953,7),
(6,'Ubik',6,1969,9),
(7,'Chroniques martiennes',5,1950,8),
(8,'La nuit des temps',7,1968,7),
(9,'Blade Runner',6,1968,8),
(10,'Les Robots',3,1950,9),
(11,'La Planète des singes',8,1963,8),
(12,'Ravage',7,1943,8),
(13,'Le Maître du Haut Château',6,1962,8),
(14,'Le monde des Ā',9,1945,7),
(15,'La Fin de l’éternité',3,1955,8),
(16,'De la Terre à la Lune',10,1865,10);
```

* sauvegarder ;-)

## Utiliser l'application SQLite (non installée sur PC du lycée)
La ligne de commande SQLite permet d'entrer deux types de commandes :

* Les commandes spéciales pour la ligne de commande. Elles débutent toutes par un point (il ne faut pas qu'il y ait d'espace avant ni après le point pour que la commande fonctionne). Par exemple, .open, .show, .backup, .exit et toutes les autres commandes listées par .help. (voir la [documentation SQLite](https://sqlite.org/cli.html) ainsi que [Command Line Shell For SQLite](https://tool.oschina.net/uploads/apidocs/sqlite/sqlite.html)). Et la version [windows](https://apical.xyz/fiches/la_ligne_de_commande_sqlite_002/La_ligne_de_commande_SQLite)
* Les requêtes SQL, par exemple CREATE, SELECT, INSERT, UPDATE, DELETE. Chacune doit se terminer par un point-virgule.

Voici comment combiner ces deux types de commandes afin de vérifier la liste des tables de la base de données sélectionnée puis créer et afficher les enregistrements :

Pour démarrer *sqlite*, sous Windows, rechercher le fichier `sqlite.exe`

Dans la console: l'invite de commande commence alors par `sqlite>`

* Les instructions suivantes permettent d'ouvrir et executer le fichier `bibliotheque.sql`, afficher les tables, puis fermer (si besoin) l'application sqlite:

```sql
sqlite> .read bibliotheque.sql
sqlite> .tables
AUTEURS LIVRES
sqlite> .exit
```

* Pour représenter la table en *mode markdown*:

```sql
sqlite> .read bibliotheque_auteurs.sql
sqlite> .mode markdown
sqlite> select *
   ...> from LIVRES;
```

Ce qui devrait afficher:


{{< img src="../images/table_cons.png" caption="table en format markdown" >}}
**Comme vous l'avez remarqué*:

  * lorsque vous écrivez `select *`, le retour à la ligne n'execute pas le script, mais attend la fin de l'instruction, jusqu'au point virgule `;` final.
  * les requêtes et instructions SQL peuvent être écrites directement dans l'application *sqlite*, comme dans le fichier d'extension `.sql`. Il faudra alors le lire dans la console avec `.read <nom_du_fichier>`.

## Utiliser une application en ligne
* Aller sur la page{{< a link="https://sqliteonline.com/" caption="sqlonline.com" >}}
{{< img src="../images/sqlonline.png" caption="sqlonline.com" >}}
* Cliquer sur *Import*, puis choisir un fichier d'extension `.sql`, comme par exemple [bibliotheque.sql](/pdf/NSI/bibliotheque.sql)
* Utiliser alors la fenêtre *SQLite* pour tester les instructions suivantes.

# Tester quelques requêtes SQL
## INSERT ... VALUES
Ajoute une entrée

```sql
sqlite> insert into LIVRES
   ...> (id,titre,id_auteur,ann_publi,note)
   ...> VALUES
   ...> (17,'Cinq semaines en ballon',10,1862,5);
```

*Vérifier alors la modification en faisant: `SELECT * FROM LIVRES`*


## UPDATE ... WHERE
Mise à jour d'une valeur

```
sqlite> UPDATE LIVRES
   ...> SET note=6 
   ...> WHERE id=17;
```

## DELETE ... WHERE
* Supprimer une ou plusieurs occurences:

```sql
sqlite> DELETE FROM LIVRES WHERE titre='Cinq semaines en ballon';
```

* supprimer la derniere occurence:

```sql
DELETE FROM LIVRES WHERE id=(SELECT Max(id) from LIVRES);
```

**Remarques**

* La dernière requête utilise une instruction imbriquée, mise entre parenthèses de la clause `WHERE id=(SELECT ...)` 
* l’instruction DELETE FROM LIVRES permet de supprimer tous les n-uplets de la table, mais pas de remettre à zero le compteur. Pour une remise à zero du compteur, il faut aussi effacer le seul élément de la table `sqlite_sequence`, créée dans la base de donnée en même temps que la première table. 

## SELECT ... WHERE
Selectionner une partie de la table, en nommant les attributs:

```sql
sqlite> SELECT titre, ann_publi
   ...> FROM LIVRES
   ...> WHERE note=10;
```

## JOINTURE
Tester le script suivant:

```sql
sqlite> SELECT titre,id_auteur,ann_publi,nom,prenom
   ...> FROM LIVRES
   ...> INNER JOIN AUTEURS ON LIVRES.id_auteur = AUTEURS.id;
```

*Vous remarquerez que les attributs peuvent être issus des 2 tables.*

On pourra aussi ajouter une condition sur l'année de publication du livre:

```sql
sqlite> SELECT titre,id_auteur,ann_publi,nom,prenom
   ...> FROM LIVRES
   ...> INNER JOIN AUTEURS ON LIVRES.id_auteur = AUTEURS.id;
   ...> WHERE ann_publi>1950
```

## A vous de jouer
1. Afficher tous les livres, avec titre, année de parution et note, dont la note est supérieure ou égal à 8.
2. Afficher tous les livres, avec leur titre et leur année de parution, écrits par Phillip K.Dick.
3. Ajouter à la clause précédente l'instruction de classement par année de publication: `ORDER BY ann_publi`



# Ressources
* Ce TP est inspiré de celui de [David Roche, du très bon site pixees.fr](https://pixees.fr/informatiquelycee/n_site/nsi_term_bd_sql.html). Merci à lui pour le partage...
* Cours complet en SQL, avec référencement des différentes instructions: [https://sql.sh/cours](https://sql.sh/cours)

* fichier de secours [bibliotheque.sql](/pdf/NSI/bibliotheque.sql)