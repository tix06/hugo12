---
Title: questionnaire
description: creer un questionnaire en ligne à destination des parents d'eleves dans une ecole elementaire. Version difficile, Framasoft
weight: 20
---

# Formulaires
La réalisation d'une enquête de terrain consiste à interroger les *usagers* au moyen d'un questionnaire. 

## But et règlementation
Lors de la confection du questionnaire, posez-vous au minimum les questions suivantes:

* quel est le but du questionnaire?
* quel est le public visé?
* la collecte des informations personnelles est-elle anonyme? 
* si celle-ci n'est pas anonyme, que prevoyez-vous en regard du RGPD?
* la collecte des informations, est-elle simple?

## Questionnaire à destination des parents
Nous prendrons comme exemple le Questionnaire suivant, dont le but est d'établir un profil de la famille et des enfants scolarisés dans une école élémentaire. Ce questionnaire est adressé aux parents:

* Combien d'enfants avez vous?
* L'enfant scolarisé dans notre école, s'agit-il d'une fille/d'un garçon?
* Bénéficie t-il (elle) d'un dispositif particulier (PAP, PAI, ...)?
* Fréquente t-il (elle) l'accueil périscolaire du matin?

> Vous allez adapter ce questionnaire pour le **publier en ligne**.

Ce questionnaire est anonyme; la plupart des questions sont de type *Question à Choix Multiple*, n'autorisant qu'une seule réponse.

Ce type de questions est à privilégier pour en faciliter l'analyse.

## Framaforms
Les données relatives aux élèves ou à leurs parents sont des données sensibles qu’il faut protéger. Même si cela peut paraitre tentant d’utiliser les outils de formulaires américains tels que Microsoft et Google, il faut les éviter d’après la [CNIL](https://www.cnil.fr/fr), car non respectueuses du RGPD en raison du «privacy shield» américain.

Dans ce TP, vous allez devoir **créer un compte** sur [framaforms](https://framaforms.org/abc/fr/), une association française qui respecte le RGPD qui s’engage à ne pas vendre vos données ni celles de vos utilisateurs.

Un tutoriel pour comprendre: [docs.framasoft.org](https://docs.framasoft.org/fr/framaforms/exemple-d-utilisation.html)

## Conception du formulaire
Une fois le compte créé, aller dans l'editeur et commencer à concevoir le formulaire. 

* Mettre un titre et un commentaire à partir des informations suivantes:

**Titre du formulaire:** *Questionnaire à destination des parents*

**Description:** *Madame, Monsieur, chers parents,
Dans le cadre de l’auto-évaluation de notre école, nous vous proposons une enquête afin d'établir un profil et de répondre à vos besoins.*

*Votre participation à l’enquête est essentielle. Elle est libre et anonyme. Il vous suffit d’indiquer ce que vous pensez des propositions qui suivent.*

*Nous vous remercions à l’avance de votre participation.*

*L’équipe pédagogique* 

{{< img src="../images/form1.png" width="400" >}}

* Accès public aux résultats: Choisir *Non*.

{{< img src="../images/Q1.png" width="400" >}}

* En bas de page: Cliquer sur **Enregistrer**

* Ajouter votre première liste à puces: haut de page: *Formulaire*

{{< img src="../images/Q2.png" >}}

* Dans l'onglet *Options*, modifier les valeurs des boutons.

{{< img src="../images/Q3.png" >}}

* Pour être plus lisible, le champs de réponses peut être placé sur la même ligne que la question.

{{< img src="../images/Q4.png" >}}

* La question suivante pose un problème pour l'analyse des résultats: *Votre enfant bénéficie-t-il d'un dispositif?*. Le choix *Non* n'apparait pas. 
  * Il faudra d'abord placer une 1ere question: *Votre enfant bénéficie-t-il d'un dispositif d'accompagnement?: OUI / NON*
  * Puis la question demandant le *type de dispositif*: (PAI, PAP, UPE2A, ULIS)?
  * Enfin, il faudra lier ces 2 questions: la 2e question ne sera proposée qu'à *condition* que la réponse précédente est *OUI*. Cela demande d'ajouter un *champ conditionnel*

{{< img src="../images/Q9.png" >}}

* La reponse OUI à la première question entraine l'affichage de la 2e:

{{< img src="../images/Q5.png" caption="choix de la question 1" >}}

{{< img src="../images/Q6.png" caption="choix de la question 2" >}}

* Les questions suivantes sont regroupées dans un même tableau. Pour chaque tableau, on les regoupe dans le même paragraphe du formulaire.
{{< img src="../images/Q7.png" caption="Choisir: groupe de champs" >}}

* Puis ajouter les questions dans ce groupe de champs.

{{< img src="../images/Q8.png" >}}

* Vous pouvez alors partager ce formulaire grâce à son adresse. Voir le bouton partager depuis le tableau de bord.


# Liens
* Questionnaires préparatoires à l’évaluation d’école (documents nationaux) disponibles ci-dessous et sur l’ENT : [ac-Lille](https://ien-ronchin.etab.ac-lille.fr/?page_id=3121)
* Concevoir un questionnaire pour une etude de marché: [bpifrance-creation.fr](https://bpifrance-creation.fr/encyclopedie/letude-marche/comment-faire-son-etude-marche/realiser-questionnaire-cadre-votre-etude)
* Le RGPD appliqué aux enquêtes: [guide](https://www.plus.transformation.gouv.fr/sites/default/files/ressource/Guide%20RGPD%20appliqu%C3%A9%20aux%20enqu%C3%AAtes%20(II)_0.pdf)
* Exemple de formulaire réalisé à partir des consignes: [exemple](https://framaforms.org/questionnaire-a-destination-des-parents-1705153379)

