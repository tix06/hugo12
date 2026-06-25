---
Title: GET POST cookies - vs SNT
description: formulaire, methode GET POST, outil reseau du dev, navigateur
hidden: true
weight: 9
---

Vous repondrez aux question sur le document: [reseau_tp_form.odt](/pdf/NSI_1/reseau_tp_form_snt.odt)

# Formulaire de données - SNT
## But de la séance
Ce TP a pour but d'illustrer la relation Client / Serveur lors de la connexion sur un site web avec **authentification**: Comment les données sont-elles **transmises**, où vont ces  données, la transmission est-elle **sûre**? 

## Partie 1: Client / Serveur
{{< img src="../images/client-server.png" link="https://developer.mozilla.org/fr/docs/Learn/Forms/Sending_and_retrieving_form_data" caption="img de MDN Sending_and_retrieving_form_data" >}}

Le schéma ci-dessus décrit la situation où un client demande une page web à un serveur.

Le client demande une page web au serveur en saisissant directement l'adresse (l'**URL**) dans la barre du navigateur.

{{< img src="../images/form_url.png" >}}

Ou bien, en cliquant sur un **lien**.

{{< img src="../images/form_lien.png" >}}

Dans une relation Client / Serveur sans identification du client, les opérations se passent dans l'ordre suivant:


1. Le client saisit l'adresse (URL) dans son navigateur. 
2. Le navigateur utilise l'URL pour envoyer la requête au serveur. 
3. Le serveur repond à la requête en retournant le code html de la page.
4. Le navigateur du client affiche la page web.

Dans de nombreux cas, le client ne peut acceder à la ressource que s'il s'identifie au préalable (site de e-commerce, banque, ENT...)

{{< img src="../images/sarenza.png" caption="un site de e-commerce" >}}

> **Qu a:** Lorsque le client doit s'authentifier sur le serveur, à l'aide d'un formulaire de connexion, d'autres étapes sont necessaires dans le processus décrit ci-dessus. Placer ces étapes dans l'ordre.

- Le serveur vérifie la bonne identité du client.
- Le client clique sur la page "s'identifier / login / compte".
- Le serveur démarre une session avec le client identifié.
- Le client envoie son identifiant et son mot de passe à l'aide du formulaire.
- Le serveur lui retourne le formulaire de connexion.
- Le client ferme la session.

### Le formulaire en ligne
Il est conseillé d'utiliser le navigateur **MOZILLA** pour la clarté des renseignements fournis par les outils réseau.

On utilisera le formulaire à la page [http://resaonline.la-bo.xyz](http://resaonline.la-bo.xyz). 

{{< img src="../images/form.png" link="http://resaonline.la-bo.xyz" caption="formulaire de connexion" >}}

**Sur la page du site**: le bandeau de navigation permet de selectionner la méthode d'envoi des données:

* méthode GET
* méthode POST
* authentification par cookie

{{< img src="../images/form_nav.png" >}}

Normalement, c'est le programmeur du site web qui choisit la méthode, pas le client. Mais ici, il s'agit d'un formulaire *pédagogique*, permettant de tester chacune des méthodes.

### Lecture d'une URL
L'URL est l'adresse qui est placée dans la *barre d'adresse* du navigateur. En cliquant sur les boutons de navigation du bandeau, GET, POST et Cookie:

> **Qu b:** L'URL est-elle la même pour chaque option choisie? Sinon, quelle extension est ajoutée à l'URL? Préciser pour chaque option de connexion choisie par le client. Compléter le tableau sur la fiche réponse.

*S'il y a plusieurs URL, c'est que le site contient 3 pages différentes pour le login. Sinon, c'est qu'il s'agit de la même page, qui est modifiée par le serveur selon les choix du client.*

Cette URL comprend le nom de domaine, et une extension qui correspond au *chemin* sur le serveur. 


## Partie 2: Utiliser les outils du navigateur
Pour la suite, vous allez utiliser la méthode d'authentification par **cookie**.

* Ouvrir la fenêtre d'*outils de développement* du navigateur. Choisir l'outil *réseau*
* Remplir et envoyer le formulaire
* Une fois parvenu à la page "espace personnel", vous allez explorer les éléments de la requête, à l'aide des outils du navigateur.

Dans la fenêtre des outils de developpement (*dev tools de Mozilla*), l'onglet **réseau** montre les différentes ressources demandées.

Dans cette liste, selectionner la page web (`result`, `result_secure` ou bien `form_cook` selon l'option choisie). On peut alors procéder à l'analyse de l'URL. 

{{< img src="../images/net3.png" caption="selectionner la page en cliquant dessus dans la liste" >}}

<!--
Cliquer sur le curseur devant le premier champs de l'en-tête:

{{< img src="../images/moz1.png" caption="inspecteur reseau sur Mozilla" >}}


*L’URL (Uniform Ressource Locator) est l'adresse qui permet de router (transporter) notre requête vers le serveur correspondant au site web, sur le réseau internet.*

-->

Le serveur distant est un site web identifié selon une combinaison unique de:

* son Adresse IP (Remote Adress)
* un Numéro de port (80 en http ou 443 en https), indiqué à la fin du Remote Adress
* le Host (nom de domaine)

Ce sont les renseignements fournis par l'en-tête (le *header*).


> 1. Retrouver tous ces renseignements dans l'en-tête (le *header*). Les recopier sur la fiche réponse.

{{< img src="../images/net2.png" cation="Remote Adress" >}}

{{< img src="../images/net1.png" caption="Host" >}}



> 2. Dans les outils réseau du navigateur, chercher l'onglet *cookie*, et lire le contenu. Comment les informations du formulaire sont-elles écrites dans le cookie? Sous une forme structurée?

{{< img src="../images/moz2.png" caption="exemple de capture d'écran de l'outil d'exploration du cookie" >}}

> 3. Recharger la page: le navigateur propose t-il de soumettre à nouveau le contenu du formulaire? Les informations du formulaire sont-elles toujours présentes dans la carte d'identité?
> 4. Dans un autre onglet du navigateur: saisir l'adresse [http://resaonline.la-bo.xyz/getcookie](http://resaonline.la-bo.xyz/getcookie). Les informations du formulaire sont-elles toujours présentes dans la carte d'identité? Pourquoi?
> 5. Saisir maintenant cette adresse dans un AUTRE navigateur. Les informations du formulaire sont-elles toujours présentes dans la carte d'identité? Pourquoi?
> 6. Rechercher le cookie grace aux options du navigateur. (Voir tuto sur cette [page](https://support.mozilla.org/fr/kb/cookies-informations-sites-enregistrent). Quels autres cookies ont été déposés lors de votre session (aujourd'hui)? Comment peut-on se debarrasser de ces cookies?

{{< img src="../images/moz3.png" >}}

> 7. *Conclure:* Les traces numériques laissées sur mon ordinateur peuvent-elles contenir des informations sur mon identité numérique?

## Partie 3: Sécurité sur le Web: http et https
Video: transfert encryptage ssl

{{< img src="../images/video_ssl.png" link="https://www.youtube.com/watch?v=WIMKeyJ60Rw" caption="Comprendre HTTPS et le chiffrement SSL TLS en animation 3D, CodeRock & Apprendre, à 0':56" >}}

**à vous de jouer:** 

Sur la page du formulaire de connexion, dans la barre de l'URL:

* Ecrire **http://** devant l'adresse: **http://** resaonline.la-bo.xyz/form_cook (*sans espace*). Soumettre le formulaire  
* Puis écrire **https://** devant l'adresse: **https://** resaonline.la-bo.xyz/form_cook.

> **Qu c:** (Utilisation du formulaire). Dans chaque cas, observer le message dans la fenêtre à propos de la **sécurité** et du **chiffrement** pour l'envoi des données. Quel est ce message? Compléter le tableau.

> **Qu d:** (Video) Quel est le scénario mettant en jeu un cyberpirate proposé dans la vidéo? Est-ce que cela change quelque chose, de naviguer en http ou bien en https?

> **Qu e:** *Conclure:* Quels conseils peut-on donner à un utilisateur qui navigue et fait des achats sur le net?

# Approfondir: 
* [MDN developer.mozilla.org](https://developer.mozilla.org/fr/docs/Learn/Forms/Sending_and_retrieving_form_data)
* [MDN securité](https://developer.mozilla.org/fr/docs/Learn/Server-side/First_steps/Website_security)

