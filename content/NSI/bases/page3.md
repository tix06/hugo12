---
Title : SGBD
description: gestion des requetes, problèmes d'acces concurents
hidden: true
weight: 54
---


# Système de gestion de base de données relationnelles
## Deux problématiques complémentaires
Une base de donnée est necessaire pour stocker de manière permanente des données, mais aussi pour partager ces données.

**La structuration des données:** Une base de données est une représentation tabulaire de ces données. Les tables respectent des contraintes sur leur contenu. Il existe des liens entre tables qui doivent obéir à certaines règles et satisfaire certaines proprietés. La théorie sous-jacente, la *normalisation*, a été développée pour s’assurer que l’on construit un schéma correct.

Il faudra organiser ces données et utiliser un langage spécifique pour acceder à ces données: le **langage de requêtes**.



## BDD et SGBD

**Définition:** une base de données est une collection de données, constituant un ensemble d’informations *structurées*, mémorisées sur un support permanent, et qui peut être partagée entre plusieurs services, serveurs, utilisateurs. (grâce à un SGBD).

> **Question:** Mais alors, qu'est ce qui différencie la base de donnée d'un simple fichier stocké sur serveur?

> *Réponse:* l'utilisation d'un simple fichier (par exemple de type tableur) va entrainer:

> * *une certaine lourdeur lors de l'accès aux données*,
> * *un manque de sécurité,*
> * *une absence de contrôle de concurence d'accès.*

Ces problèmes amènent à utiliser un SGBD...

**Définition:** Le **Système de Gestion de Bases de Données (SGBD)** est un logiciel qui a pour rôle de gérer les informations stockées dans une base de données, et leur accès. 



{{< img src="../images/SGBD.jpg" caption="rôle d'un SGBD" >}}
Il existe des SGBD gratuites, et payantes. Ces logiciels ont pour rôle: 

* de gérer la lecture et l'ecriture ou les modifications des informations contenues dans la base de données.
* de gérer les autorisations d'accès à la base de données. (certains utilisateurs peuvent lire, d'autres peuvent lire/ecrire)
* d'assurer la maintenance des différentes copies des bases de données (par mesure de securité, la base de données est reproduite à plusieurs endroits)
* de gérer les accès concurents: plusieurs personnes peuvent avoir besoin d'accéder aux informations et modifier des informations en même temps.

L'utilisation de SGBD est généralisé dès qu'il faut pouvoir gérer des données de grande quantité, et permettre un accès plus simple et sûr à ces données.

## Description des termes utilisés
### DML = SQL
**DML** signifie data manipulation langage. Il s'agit du langage SQL.

Exemple d'instructions:

* Sélection de données dans une table :

```sql
SELECT nom, prenom, classe FROM eleves;
```

* Insertion de données dans une table :

```sql
INSERT INTO eleves (nom, prenom)
VALUES ('Dupont', 'Matthieu');
```

* Suppression de données dans une table :

```sql
DELETE FROM eleves
WHERE prenom = 'Paul' and nom = 'Durand';
```

* Mise à jour de données dans une table :

```sql
UPDATE eleves
SET prenom = 'Henry'
WHERE nom = 'Leroy';
```

Cette partie du cours sera developpée en TP [ici](/docs/NSI/bases/page6/)

### Schema d'une BDD
Le terme « schéma de base de données » fait référence à la représentation visuelle d'une base de données, à un ensemble de règles qui régissent une base de données.

On parle aussi de sous-schéma pour l'ensemble des objets appartenant à un utilisateur particulier.

Cette partie du cours sera developpée [ici](/docs/NSI/bases/page1/)

# Problèmes d'accès concurents
## Exemple de la perte de mise à jour
{{< img src="../images/acces_img1.png" caption="Problème de la perte de mise à jour du tuple T par la transaction A" >}}

Les transaction A et B accèdent au même tuple T ayant la même valeur respectivement à t1 et t2. Ils modifient chacun la valeur de T. Les modifications effectuées par A seront perdues puisqu'elle avait lu T avant sa modification par B.

{{< img src="../images/acces_img2.png" caption="Doucle crédit d'un compte bancaire C" >}}

Dans cet exemple le compte bancaire vaut 1010 à la fin des deux transactions à la place de 1110.

## Solution
Une solution générale à la gestion de la concurrence est une technique très simple appelée verrouillage.

Poser un verrou sur un objet (typiquement un tuple) par une transaction signifie rendre cet objet inaccessible aux autres transactions.

Lorsqu'une transaction se termine (COMMIT ou ROLLBACK) elle libère tous les verrous qu'elle a posé.

## Autres problèmes pouvant survenir
L'inter-blocage est le phénomène qui apparaît quand deux transactions (ou plus, mais généralement deux) se bloquent mutuellement par des verrous posés sur les données. Ces verrous empêchent chacune des transactions de se terminer et donc de libérer les verrous qui bloquent l'autre transaction. Un processus d'attente sans fin s'enclenche alors.

## Documents issus de...
[stph.scenari-community.org](https://stph.scenari-community.org/bdd/0/co/traUC031.html)


