---
Title: Format des donnees
description: donnees structurees, format de donnees standardisé, json, csv, donnees et informations, open datas
weight: 13
---









{{% badgetable %}}
| | |
|---|---|
| {{% badge color="green" icon="heart" %}}culture numer{{% /badge %}} | D1 Format des données : [Lien](../page4) |
| {{% badge color="green" icon="heart" %}}culture numer{{% /badge %}} | D2 Collecte des données personnelles : [Lien](../page5) |
| {{% badge color="red" icon="angle-double-up" %}}modelisation{{% /badge %}} | D3 Données en table [Lien](../page8) |
| {{% badge color="green" icon="heart" %}}culture numer{{% /badge %}} | D4 RGPD [Lien](page5) et [videos](page6), recherche documentaire [Lien](../page7) |
| {{% badge color="orange" icon="star" %}}competences{{% /badge %}} | TP1 Enquete de police [Lien](../page12) |
| {{% badge color="red" icon="angle-double-up" %}}modelisation{{% /badge %}} | TP2 Pommes [Lien](../page9) |
| {{% badge color="orange" icon="star" %}}competences{{% /badge %}} | TP3 Traitement de données data.gouv [Lien](../page11) |
| {{% badge color="orange" icon="star" %}}competences{{% /badge %}} | TP4 Formulaire d'[enquête](/docs/publier/page1/) et traitement [Lien](/pdf/SNT/page7.html) |
{{% /badgetable %}}

## Introduction
En informatique, tout est donné, depuis les 0 et les 1 qui décrivent l’état des transistors dans un circuit électronique, jusqu’à une vidéo, en passant par les photos, les adresses, un relevé de température ou l’âge d’une personne. Les données sont souvent rassemblées pour caractériser un objet comme l’adresse d’une personne (composée du numéro de rue, du nom de la rue, du code postal, de la ville et du pays par exemple). Lorsque les données sont ainsi rassemblées pour décrire quelque chose avec plusieurs informations, on parle de **données structurées** (voir plus loin).


{{< img src="../images/activitePostIt.png" link="/pdf/SNT/page12.html" caption="activité sur le traitement des données" >}}

1. A partir de l’image projetée, choisir une méthode pour placer les informations dans un même tableau. Quelles seront les étiquettes de colonne?
2. Lorsque l’on place ses données sur une page internet, les champs du formulaire demandent un format particulier pour les données. Etes vous capables de retrouver rapidement l’information suivante: quel évènement a pour plaignant Me Dubois? => besoin de ranger les informations dans une table pour effectuer la recherche avec une clé (étiquette de colonne)
3. Ouvrir la page de l'activité. Recopier le tableau et le compléter avec 3 étiquettes post-it ou plus. (consigne précise: Votre mission est d'extraire les informations importantes et de les organiser dans le tableau fourni ci-dessous.)

## Type de variable, cellule d’un tableur
Selon la mise en forme, le format associé est soit du texte (entre guillemets, soit un nombre (virgule pour décimal), mais cela peut être aussi une date (15/09/2023), une heure (8:30) ou une coordonnée GPS exprimée en degré minute d’arc seconde (45°30’45’’).

Dans un fichier .xls, ou csv, les données sont structurées. Dans une même colonne, les données sont dans le même format (sont du même type)

## Présentation des données
Un fichier Excel regroupe une ou plusieurs table(s)
Dans une table, les données sont mises dans des colonnes, où elles ont le meme type.
Chaque donnée est dans une cellule, référencée par ses coordonnées.

Chaque TABLE représente une COLLECTION. C’est à dire un ensemble d’objets (des lignes) qui partagent les mêmes DESCRIPTEURS. Les valeurs de ces objets ont un certain type. Chaque colonne contient des valeurs du même type.

Chaque ligne contient une *information*.


# Open datas et données structurées

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

[Lien vers le TP](../page11/)