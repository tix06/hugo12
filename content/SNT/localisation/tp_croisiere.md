---
Title: TP croisiere
---

# TP croisiere autour du monde
## Objectif de l'activité
Placer des marqueurs sur une carte à partir de coordonnées GPS pour reconstituer le parcours d'une croisière autour du monde.

{{< img src="../images/croisiere.jpg" caption="Crédit photo moofushi/Adobe Stock" >}}


## Openstreetmap
Utilisez l'outil uMap disponible à l'adresse suivante : [https://umap.openstreetmap.fr/fr/](https://umap.openstreetmap.fr/fr/)

Un [tuto de l'academie d'Amiens](https://blogs.ac-amiens.fr/tuicsoissonnais/public/TNP_SPIP_documents/utilisation_umap.pdf) détaille l'utilisation de *umap*.

Au cours de la séance, vous allez:

* Créer une nouvelle carte
* Importer les données de localisation depuis un fichier *csv* géocodé (voir paragraphe suivant)
* Personnaliser et partager la carte.

Notez que si vous souhaitez sauvegarder votre carte, il faudra d'abord créer un compte.. voir [tuto](https://blogs.ac-amiens.fr/tuicsoissonnais/public/TNP_SPIP_documents/utilisation_umap.pdf) à la page 2.

## Créer un fichier CSV Géocodé
Coordonnées GPS des escales
Les coordonnées doivent être codées de la manière suivante: 43.2965,5.3698 (sans espace et sans les caractères °N,S,E,O)

```
Marseille : 43.2965° N, 5.3698° E
étape 2: 41.3851° N, 2.1734° E
étape 3 : 38.7169° N, -9.1399° W
étape 4 : 40.7128° N, -74.0060° W
étape 5 : -22.9068° S, -43.1729° W
étape 6 : -33.9249° S, 18.4241° E
étape 7 : 19.0760° N, 72.8777° E
étape 8 : 1.3521° N, 103.8198° E
étape 9 : -33.8688° S, 151.2093° E
Retour à Marseille : 43.2965° N, 5.3698° E
```



### Editer le fichier
A l'aide d'un editeur de texte (Notepad++): 
* remplir le fichier à l'aide des informations plus haut. La premiere ligne sera reservée à l'etiquette des colonnes. Chaque étape sera écrite sur une seule ligne dans le document (même si la description est longue).

{{< img src="../images/etape.png" >}}

* Ajouter les informations manquantes: le **nom** et la **description** des lieux pour chacune des étapes:
	* Pour retrouver le **nom** des villes, placer les **coordonnées** dans le champs de recherche de umap (attention au format numérique, qui doit être en degrés décimaux, sans préciser °N,S,E,O). *Voir image ci-dessous.*
	* pour la **description**, vous pouvez peut être copier coller une ou deux phrases trouvées sur le site [wikipedia](https://fr.wikipedia.org/wiki/Wikip%C3%A9dia:Accueil_principal)...

{{< img src="../images/loupe.png" caption="utiliser l'outil recherche du logiciel umap" >}}

### Importer les données dans umap
A l'aide de l'icone pour *importer* les données, charger votre fichier *csv*.

{{< img src="../images/import.png" link="/scripts/SNT/etapes.csv" >}}

fichier de secours: [etapes.csv](/scripts/SNT/etapes.csv)

## Personnaliser l'affichage des etiquettes et des pop-up
Vous pouvez maintenant:

> * **personnaliser vos marqueurs**: en mode edition, cliquer sur le marqueur (crayon).
Vous pouvez alors choisir une nouvelle icône, et sa transparence.

{{< img src="../images/edit.png" link="https://blogs.ac-amiens.fr/tuicsoissonnais/public/TNP_SPIP_documents/utilisation_umap.pdf" caption="voir tuto detaillé à la page 5" >}}

> * **ajouter** l'affichage permanent (ou en cas de survol) d'une etiquette avec le nom du marqueur: *menu de droite > Propriétés > Options d'interaction par defaut*.

> * **ajouter** l'affichage d'une [infobulle](https://wiki.cartocite.fr/doku.php?id=umap:5_-_je_cree_des_infobulles_multimedia) en cas de clic sur le marqueur. Eventuellement, ajouter une image dans l'infobulle.



> * *(facultatif)* Ajouter la distance et la durée estimée entre 2 étapes. S'aider du *distance-calculator* du site [bednblue.fr](https://www.bednblue.fr/sailing-distance-calculator)

# Partager votre carte
* Si vous avez créé un compte: sauvegarder la carte
* Modifier les permissions avec l'outil clé du menu de droite:

{{< img src="../images/cle.png" caption="modification des permissions" >}}

Choisir: **Qui peut voir** => *Quiconque a le lien*


* copier l'URL (celle dans la barre du navigateur). Et partager cette adresse en collant dans votre document word ou libre Office
* coller aussi une copie d'ecran, c'est plus sûr...

Bonne navigation 🚢 !

