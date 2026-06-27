---
Title: format des donnees
description: donnees structurees, format de donnees standardisé, json, csv, donnees et informations, open datas
weight: 13
---

# Open datas

{{< img src="../images/sitecookie.png" link="https://youtu.be/pnrc6ZaYrwg" caption="video du site cookie-connecté" >}}
> L'open data (ou données ouvertes) est l'ouverture via le Web de données collectées par des organismes publics (ou entreprises), et dont la diffusion est considerée comme d'interêt général.

Quelques exemples:

* horaires transports publics
* état des lignes (métro, autobus...)
* prévisions météorologiques
* prix des carburants
* ...

Il y a des conditions à respecter pour la mise à disposision de ces données. Une donnée doit être de nature:

* ouverte
* primaire
* libre de droit

# Organisation des données
* Une **collection de données** peut être ordonnée sous forme de liste, ou d'une table.

La façon de *structurer les données* influe fortement sur les opérations de traitement : il est par exemple bien plus efficace de rechercher une donnée dans une collection toujours ordonnée, mais y insérer une information est plus coûteux.


* **Donnée :** représentation d'une information au sein d'un système informatique.

* **Métadonnée :** donnée servant à définir ou décrire une autre donnée, pour permettre sa manipulation.

* **Une base de données** regroupe plusieurs collections de données reliées entre elles.

* **Descripteur :** mot ou un groupe de mots choisi pour caractériser les informations contenues dans un document et pour faciliter les recherches.

* Une **collection** regroupe des objets partageant les mêmes descripteurs (par exemple, la collection des contacts d’un carnet d’adresses). La structure de table permet de présenter une collection : les objets en ligne, les descripteurs en colonne et les données à l’intersection. Les données sont alors dites structurées.

* Une **information** est issu du croisement de plusieurs données. On donne un nouveau sens à ces données.

# Format des données
L'OPen Datas exige que les données doivent être au format EXPLOITABLE, et non proprietaire.

Souvent, on va trouver les format csv, json et XML pour les fichiers.

**csv**:

```
nom, prenom, age
Dupont, François, 17
Darcis, Pauline, 16
```

**json**:

```
{
	{
		"nom": "Dupont",
		"prenom": "François",
		"age": 17
	}
	{
		"nom": "Darcis",
		"prenom": "Pauline",
		"age": 16		
	}
}
```

**XML**

```
<membre>
	<nom>Dupont</nom>
	<prenom>Francois</prenom>
```

{{< a link="https://www.data.gouv.fr/fr/" caption="" >}}{{< img src="../images/data.gouv.png" link="https://www.data.gouv.fr/fr/" caption="Plateforme ouverte des données publiques françaises" >}}

Le Répertoire National des Élus (RNE) a pour finalité le suivi des titulaires d’un mandat électoral. Il est renseigné et tenu à jour par les préfectures et hauts commissariats et par les services du ministère de l'intérieur, notamment sur la base des éléments fournis par les élus lors de la phase d’enregistrement des candidatures.

{{< img src="../images/elus.png" caption="Données du RNE pour les conseillers municipaux - extrait en csv" >}}
Les [données du RNE](https://www.data.gouv.fr/fr/datasets/repertoire-national-des-elus-1/) sont structurées par mandat. Neuf fichiers sont publiés ici :

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

{{< img src="../images/utilisation.png" link="https://www.spallian.com/2020/03/01/donnees-parite-aux-sein-des-conseils-municipaux/" caption="exemples de réutilisation des données ouvertes sur les elus municipaux" >}}
On voit ici comment des *données numériques* sont transformées en *informations*.

> Ouvrir les données jugées d'intérêt public, c'est encourager leur réutilisation par tout un chacun. Cela permet d'encourager la transparence démocratique, de bénéficier de services au quotidien ou de prendre des décisions plus éclairées.