---
Title: BDD SQL
description: bases de donnees, sql
weight: 68
---

# Bac 2024 Amerique du Nord: Exercice 3
Cet exercice porte sur le langage SQL et les bases de données.

{{% badge icon="star" %}}sql{{% /badge %}}

Un pharmacien nouvellement installé décide de créer son propre système de gestion
des médicaments qu’il délivre à ses clients.
Pour sa base de données relationnelle, il a déjà élaboré la première relation à l’aide
des données indiquées sur les cartes vitales de ses deux premiers clients :

```
client (id_client : INT,
nom_client : VARCHAR(30),
prenom_client : VARCHAR(30), 
num_secu_sociale : VARCHAR(15))
```

{{< img src="../images/page5_medoc1.png" >}}


1. Écrire le résultat de l’exécution de la requête SQL suivante :

```sql
SELECT nom_client, prenom_client
FROM client
ORDER BY nom_client;
```

Pour écrire la relation `medicament`, il doit utiliser les informations fournies par la notice
des médicaments. En voici une ci-dessous :

{{< img src="../images/page5_medoc2.png" caption="Informations extraites de la notice du médicament Paracétamol 1 gramme CP." >}}


La relation `medicament` suivante a été obtenue à l’aide de ces notices :

```
medicament (id_medic : INT,
  nom_medic : VARCHAR(30),
  categorie : VARCHAR(20),
  conditionnement : INT,
  quantite : INT, prix : FLOAT)
```

La table des médicaments de son officine est présentée ci-dessous.

{{< img src="../images/page5_medoc3.png" >}}

2. Écrire une requête SQL permettant d’afficher les noms de tous les médicaments
dont le prix est strictement inférieur à 3 euros.
Madame Martin présente au pharmacien une nouvelle ordonnance :

{{< img src="../images/page5_medoc4.png" caption="Ordonnance de Madame Sophie Martin." >}}


Il saisit les informations de cette ordonnance dans la relation `ordonnance`, chaque médicament prescrit correspondant à un enregistrement dans la table ci-dessous.

{{< img src="../images/page5_medoc5.png" >}}

3. Ecrire une requête SQL permettant d’ajouter les informations de la carte vitale
de sa troisième cliente présentée ci-dessous :

{{< img src="../images/page5_medoc6.png" caption="Ordonnance de Madame Sophie Martin." caption="Image de la carte vitale extraite de la page wikipédia" >}}


4. Donner les attributs qui doivent être déclarés comme clés étrangères de la
relation `ordonnance` et en préciser l’utilité.
5. Indiquer, pour les lignes 7 et 8 de la table `ordonnance`, le nombre de boites prescrites.
6. Écrire la requête SQL mettant à jour la quantité du médicament Acide
ascorbique en stock dans l’officine du pharmacien suite au passage de Madame
Martin.
7. Calculer le coût total des médicaments fournis à Madame Martin (on ne
demande pas d’écrire une requête ici, mais de calculer le coût total en justifiant
le calcul).
8. Écrire la requête SQL permettant d’afficher le nom du médicament pour
l’ordonnance ayant l’`id_ordo` numéro 6.

# Bac 2022 Polynesie: Exercice 3
*Cet exercice traite du thème « base de données », et principalement du modèle
relationnel et du langage SQL.*

{{% badge icon="star" %}}sql{{% /badge %}}

L’énoncé de cet exercice peut utiliser les mots du langage SQL suivants :

`CREATE TABLE, SELECT, FROM, WHERE, JOIN ON, INSERT INTO, VALUES,
UPDATE, SET, DELETE, COUNT, DISTINCT, AND, OR, AS, ORDER BY, ASC, DESC` 

Un site web recueille des données de navigation dans une base de données afin
d'étudier les profils de ses visiteurs.

Chaque requête d'interrogation d'une page de ce site est enregistrée dans une première table dénommée **Visites** sous la forme d'un 5-uplet : `(identifiant, adresse IP, date et heure de visite, nom de la page, navigateur)`.

Le chargement de la page index.html par 192.168.1.91 le 12 juillet 1998 à 22h48 aura par exemple été enregistré de la façon suivante :

`(1534, "192.168.1.91", "1998-07-12 22:48:00", "index.html", "Internet
explorer 4.1")`.

La commande SQL ayant permis de créer cette table est la suivante:

```SQL
CREATE TABLE Visites (
  identifiant INTEGER NOT NULL UNIQUE,
  ip VARCHAR(15),
  dateheure DATETIME,
  nompage TEXT,
  navigateur TEXT
);
```


## Question 1
A.  Donner une commande d'interrogation en langage SQL permettant d'obtenir
l'ensemble des 2-uplets (adresse IP, nom de la page) de cette table.

B.  Donner une commande en langage SQL permettant d'obtenir l'ensemble des
adresses IP ayant interrogé le site, sans doublon.

C.  Donner une commande en langage SQL permettant d'obtenir la liste des
noms des pages visitées par l'adresse IP 192.168.1.91

Ce site web met en place, sur chacune de ses pages, un programme en javascript qui envoie au serveur, à intervalle régulier de 15 secondes, le temps en secondes de présence sur la page. Ces envois contiennent tous la valeur de identifiant correspondant au chargement initial de la page.

Par exemple, si le visiteur du 12 juillet 1998 est resté 65 secondes sur la page, celle-ci a envoyé au serveur les 4 doublets (1534, 15), (1534, 30), (1534, 45) et (1534, 60).

Ces données sont enregistrées dans une table nommée Pings créée avec la
commande ci-dessous :

```SQL
CREATE TABLE Pings (
  identifiant INTEGER,
  duree INTEGER
);
```

En plus de l'inscription d'une ligne dans la table **Visites**, chaque chargement d'une nouvelle page provoque l'insertion d'une ligne dans la table **Pings** comprenant l'identifiant de ce chargement et une durée de 0.

Les attributs identifiant des tables **Visites** et **Pings** partagent les mêmes
valeurs.

## Question 2
A.  De quelle table l’attribut `identifiant` est-il la clé primaire ?

B.  De quelle table l’attribut `identifiant` est-il une clé étrangère ?

C.  Par conséquent, quelles vérifications sont automatiquement effectuées par le système de gestion de base de données ?

## Question 3
Le serveur reçoit le doublet `(identifiant, duree)` suivant : `(1534, 105)`.
Écrire la commande SQL d'insertion qui permet d'ajouter cet enregistrement à la
table **Pings**.
On envisage ensuite d'optimiser la table en se contentant d'une seule ligne par
identifiant dans la table **Pings** : les valeurs de l'attribut `duree` devraient alors être mises à jour à chaque réception d'un nouveau doublet `(identifiant, duree)`.

## Question 4
A.  Écrire la requête de mise à jour permettant de fixer à 120 la valeur de l'attribut `duree` associée à l'identifiant `1534` dans la table **Pings**.

B.  Expliquer pourquoi on ne peut pas être certain que les données envoyées par
une page web, depuis le navigateur d'un client, via plusieurs requêtes formulées en javascript, arrivent au serveur dans l'ordre dans lequel elles ont été émises.

C. En déduire qu'il est préférable d'utiliser une requête d'insertion plutôt qu'une requête de mise à jour pour ajouter des données à la table **Pings**.

## Question 5
Écrire une requête SQL utilisant le mot-clef `JOIN` et une clause `WHERE`,
permettant de trouver les noms de toutes les pages qui ont été consultées plus
d'une minute par au moins un utilisateur.

# Bac 2022 metropole1: Exercice 2
*Cet exercice porte sur les bases de données.*

{{% badge icon="star" %}}sql{{% /badge %}}

On pourra utiliser les mots clés SQL suivants : `SELECT, FROM, WHERE, JOIN,
ON, INSERT, INTO, VALUES, UPDATE, SET, AND`.

Nous allons étudier une base de données traitant du cinéma dont voici le schéma
relationnel qui comporte 3 relations :

* la relation `individu`  (**`id_ind`**, `nom, prenom, naissance)
* la relation `realisation` (**`id_rea`**, `titre, annee, type`)
* la relation `emploi` (**`id_emp`**, `description, #id_ind, #id_rea`)

Les clés primaires sont **en gras** et les clés étrangères sont précédées d’un `#`.

Ainsi `emploi.id_ind` est une clé étrangère faisant référence à `individu.id_ind`.

Voici un extrait des tables individu et realisation : 

{{< img src="../images/page5_1.png" caption="1310 × 330" >}}
## Question 1
On s’intéresse ici à la récupération de données dans une relation.

a
A.  Écrire ce que renvoie la requête ci-dessous :

```SQL
SELECT nom, prenom, naissance
FROM individu
WHERE nom = 'Crog';
```

B. Fournir une requête SQL permettant de récupérer le titre et la clé primaire de chaque film dont la date de sortie est strictement supérieure à 2020.

## Question 2
Cette question traite de la modification de relations.

A.  Dire s’il faut utiliser la requête 1 ou la requête 2 proposées ci-dessous pour modifier la date de naissance de Daniel Crog. Justifier votre réponse en
expliquant pourquoi la requête refusée ne pourra pas fonctionner.

**Requête 1:**

```SQL
UPDATE individu
SET naissance = '02-03-1968'
WHERE id_ind = 688 AND nom = 'Crog' AND prenom = 'Daniel';
```
**Requête 2:**

```SQL
INSERT INTO individu
VALUES (688, 'Crog', 'Daniel', '02-03-1968'); 
```

B.  Expliquer si la relation individu peut accepter (ou pas) deux individus
portant le même nom, le même prénom et la même date de naissance.

## Question 3
Cette question porte sur la notion de clés étrangères.

A.  Recopier sur votre copie les demandes ci-dessous, dans leur intégralité, et les compléter correctement pour qu’elles ajoutent dans la relation `emploi` les rôles de Daniel Crog en tant que James Bond dans le film nommé ‘Casino
Impérial’ puis dans le film ‘Ciel tombant’.

```SQL
INSERT INTO emploi
VALUES (5400, 'Acteur(James Bond)', ... );
INSERT INTO emploi
VALUES (5401, 'Acteur(James Bond)', ... );
```

B.  On désire rajouter un nouvel emploi de Daniel Crog en tant que James Bond
dans le film 'Docteur Yes'.

Expliquer si l’on doit d’abord créer l’enregistrement du film dans la relation
realisation ou si l’on doit d’abord créer le rôle dans la relation `emploi`.

## Question 4
Cette question traite des jointures.

A.  Recopier sur votre copie la requête SQL ci-dessous, dans son intégralité, et la compléter de façon à ce qu’elle renvoie le nom de l’acteur, le titre du film et l’année de sortie du film, à partir de tous les enregistrements de la relation `emploi` pour lesquels la description de l’emploi est `'Acteur(James Bond)'`.

```SQL
SELECT ...
FROM emploi
JOIN individu ON ...
JOIN realisation ON ...
WHERE emploi.description = 'Acteur(James Bond)';
```

B.  Fournir une requête SQL permettant de trouver toutes les descriptions des
emplois de Denis Johnson (Denis est son prénom et Johnson est son nom).
On veillera à n’afficher que la description des emplois et non les films associés à ces emplois. 



