---
Title: questionnaire
description: creer un questionnaire en ligne à destination des parents d'eleves dans une ecole elementaire. Framasoft
weight: 20
---

# Formulaires
La réalisation d'une enquête de terrain consiste à interroger les *usagers* au moyen d'un [questionnaire](/pdf/SNT/C26_Enquete_questionnaire_SNT.pdf). 

## But et règlementation
Lors de la confection du questionnaire, posez-vous au minimum les questions suivantes:

* quel est le but du questionnaire?
* quel est le public visé?
* la collecte des informations personnelles est-elle anonyme? 
* si celle-ci n'est pas anonyme, que prevoyez-vous en regard du RGPD?
* la collecte des informations, est-elle simple?

## Tuto: réaliser un questionnaire en ligne
Nous prendrons comme exemple le Questionnaire suivant, dont le but est d'établir un profil de la famille et des enfants scolarisés dans une école élémentaire. Ce questionnaire est adressé aux parents:

* Combien d'enfants avez vous?
* L'enfant scolarisé dans notre école, s'agit-il d'une fille/d'un garçon?
* Bénéficie t-il (elle) d'un dispositif particulier: Oui/Non?
  * Si Oui, quel est ce dispositif (PAP, PAI, ...)?
* Fréquente t-il (elle) l'accueil périscolaire du matin? (jamais, parfois, toujours). Fréquente t-il (elle) l'accueil périscolaire du soir? (jamais, parfois, toujours)

> Vous allez adapter ce questionnaire pour le **publier en ligne**.

Ce questionnaire est anonyme; la plupart des questions sont de type *Question à Choix Multiple*, n'autorisant qu'une seule réponse.

Ce type de questions est à privilégier pour en faciliter l'analyse.

### Liberaforms
Les données relatives aux élèves ou à leurs parents sont des données sensibles qu’il faut protéger. Même si cela peut paraitre tentant d’utiliser les outils de formulaires américains tels que Microsoft et Google, il faut les éviter d’après la [CNIL](https://www.cnil.fr/fr), car non respectueuses du RGPD en raison du «privacy shield» américain.

Dans ce TP, vous allez devoir **créer un compte** sur [Liberaforms](https://my.liberaforms.org/user/new), une association française qui respecte le RGPD qui s’engage à ne pas vendre vos données ni celles de vos utilisateurs.

Une fois le compte créé, et l'adresse mail validée, vous pourrez DIRECTEMENT aller à la page LOGIN:

#### [Login](https://my.liberaforms.org/user/login)


### Conception du formulaire
Une fois le compte créé, aller dans l'editeur et créer un nouveau formulaire (*create new)*.

Le tuto proposé ici est celui de *framaforms*, un projet en cours d'abandon. Il vous faudra adapter les screens pour réaliser votre formulaire sur [Liberaforms](https://my.liberaforms.org)

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

{{< img src="../images/Q2.png" width="400" >}}

* Dans l'onglet *Options*, modifier les valeurs des boutons.

{{< img src="../images/Q3.png" width="400">}}

* Pour être plus lisible, le champs de réponses peut être placé sur la même ligne que la question.

{{< img src="../images/Q4.png" width="400" >}}

> Pour la question suivante: *Votre enfant bénéficie-t-il d'un dispositif?*

* Il faudra d'abord placer une 1ere question: *Votre enfant bénéficie-t-il d'un dispositif d'accompagnement?: OUI / NON*
* Puis la question demandant le *type de dispositif*: (PAI, PAP, UPE2A, ULIS)?
* Enfin, il faudra lier ces 2 questions: la 2e question ne sera proposée qu'à *condition* que la réponse précédente est *OUI*. Cela demande d'ajouter un *champ conditionnel*

{{< img src="../images/Q9.png" width="400" >}}

* La reponse OUI à la première question entraine l'affichage de la 2e:

{{< img src="../images/Q5.png" caption="choix de la question 1" width="400" >}}

{{< img src="../images/Q6.png" caption="choix de la question 2" width="400" >}}

* Les questions suivantes sont regroupées dans un même tableau. Pour chaque tableau, on les regoupe dans le même paragraphe du formulaire.
{{< img src="../images/Q7.png" caption="Choisir: groupe de champs" width="400" >}}

* Puis ajouter les questions dans ce groupe de champs.

{{< img src="../images/Q8.png" width="400" >}}

* Vous pouvez alors partager ce formulaire grâce à son adresse. Voir le bouton partager depuis le tableau de bord.

## Votre enquête
Vous avez travaillé sur la conception d'un [questionnaire d'enquête](/pdf/SNT/C26_Enquete_questionnaire_SNT.pdf) au cours d'une séance précédente.

1. Utiliser ce travail pour créer votre propre questionnaire.

2. Générer une adresse pour le publier à partir de votre tableau de bord:

> Pour distribuer votre questionnaire, il faudra revenir sur votre tableau de bord, cliquer sur *my forms* (mes formulaires), choisir le formulaire dans la liste, et, parmi les *Options*, valider à la première ligne: *Public => True*. L'adresse URL (ligne suivante) est alors active, et c'est celle-ci qui permet de le publier.

{{< img src="../images/option_public.png" width="400" >}}


3. Générer un QR-code à partir de cette adresse. *Regardez plus bas dans votre fenêtre d'option: Public URL in a QR*. Vous pouvez directement télécharger votre QR-code!
4. Placer le QR-code, le nom du sujet, celui des enquêteurs, le nombre de questions, ainsi qu'une illustration sur un document (Word) à rendre au professeur:


{{< img src="../images/enquete.png" width="400" >}}


# Liens
* Questionnaires préparatoires à l’évaluation d’école (documents nationaux) disponibles ci-dessous et sur l’ENT : [ac-Lille](https://ien-ronchin.etab.ac-lille.fr/?page_id=3121)
* Concevoir un questionnaire pour une etude de marché: [bpifrance-creation.fr](https://bpifrance-creation.fr/encyclopedie/letude-marche/comment-faire-son-etude-marche/realiser-questionnaire-cadre-votre-etude)
* Le RGPD appliqué aux enquêtes: [guide](https://www.plus.transformation.gouv.fr/sites/default/files/ressource/Guide%20RGPD%20appliqu%C3%A9%20aux%20enqu%C3%AAtes%20(II)_0.pdf)

