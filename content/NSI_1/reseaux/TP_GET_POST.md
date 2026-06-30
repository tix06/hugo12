---
Title: TP GET POST cookies
description: formulaire, methode GET POST, outil reseau du dev, navigateur
weight: 10
---

Vous repondrez aux question sur le document: [reseau_tp_form.odt](/pdf/NSI_1/reseau_tp_form.odt)

# Formulaire de données - 1ere NSI
## But de la séance
Ce TP a pour but d'illustrer ce qui arrive quand un utilisateur soumet un formulaire: où les données vont-elles et comment les gère-t-on une fois à destination? Nous examinerons aussi quelques problèmes de sécurité associés à l'envoi des données d'un formulaire.

{{< img src="../images/client-server.png" link="https://developer.mozilla.org/fr/docs/Learn/Forms/Sending_and_retrieving_form_data" caption="img de MDN Sending_and_retrieving_form_data" >}}

## Le formulaire en ligne
Il est conseillé d'utiliser le navigateur **MOZILLA** pour la clarté des renseignements fournis par les outils réseau.

On utilisera le formulaire à la page [http://resaonline.la-bo.xyz](http://resaonline.la-bo.xyz). 

{{< img src="../images/form.png" link="http://resaonline.la-bo.xyz" caption="formulaire de connexion" >}}

Le bandeau de navigation permet de selectionner la méthode d'envoi des données:

* méthode GET
* méthode POST
* authentification par cookie

Vous allez utiliser chacune des 3 méthodes. La procédure sera la même dans les 3 cas:

* Ouvrir la fenêtre d'*outils de développement* du navigateur. Choisir l'outil *réseau*
* Remplir et envoyer le formulaire
* Une fois parvenu à la page "espace personnel", vous allez explorer les éléments de la requête.

Dans la fenêtre de *dev tools*, l'outil réseau montre les différentes requêtes et ressources demandées. Dans cette liste, selectionner la page web (resaonline.la-bo.xyz). On peut alors procéder à l'analyse de l'URL. Cliquer sur le curseur devant GET.

{{< img src="../images/moz1.png" caption="inspecteur reseau sur Mozilla" >}}

*L’URL permet de router notre requête vers le serveur correspondant au site web sur le réseau.*

Un **site Web est identifié** selon une combinaison unique de:

* son Adresse IP
* un Numéro de port
* le Host header (equivalent au nom de domaine)

## Méthode GET
1. Dans la barre d'URL du navigateur. Recopier l'URL de la page demandée. Repérer les 3 sous parties: (se documenter: [openclassroom](https://openclassrooms.com/fr/courses/918836-concevez-votre-site-web-avec-php-et-mysql/912799-ecoutez-la-requete-de-vos-utilisateurs-grace-aux-url), ou bien [wikipedia](https://en.wikipedia.org/wiki/Query_string))
	* le nom de domaine
	* le chemin
	* les paramètres query
2. la connexion vers le site, se fait-elle selon le protocole *http* ou bien *https*? Comment le voit-on? Peut-on modifier le protocole directement dans la barre d'adresse, en ecrivant `http://` ou bien `https://` avant le nom de domaine `resaonline.la-bo.xyz`
3. Dans la fenêtre *réseau* du *dev tools*: Repérer les informations du *header (en-tête)* pour cette requête (client): 
	* méthode (vous devez lire en principe: GET)
	* la version HTTP (1.1? autre?)
	* L'identité du site Web serveur: voir plus haut (IP, Host header)
	* le chemin vers la ressource sur le serveur (*path*)
	* les *paramètres query* (Query String Parameters), s'il y en a. 
4. Repérer les informations de la *reponse* à cette requête
	* **code de statut** (200 OK?)
	* **Referrer**: URL de la ressource à partir de laquelle la demande est faite (c’est-à-dire à partir de laquelle le lien a été créé)
	* **Content-Type**: informations sur le contenu du document chargé (txt, html, js, css, ...?)
	* **User-Agent**: navigateur client

5. Recharger la page: le navigateur propose t-il de soumettre à nouveau le contenu du formulaire? Les informations du formulaire sont-elles toujours présentes dans la carte d'identité?
6. Dans l'historique du navigateur: le lien consulté contient-il les Query String Parameters?
7. Ecrire directement, dans la barre d'adresse une requête vers ce serveur en choisissant vous-même vos Query Parameters. Le serveur repond-il à votre requête?

## Méthode POST
Répondre aux même questions *(qu 1 à 6 de la méthode GET)*.

## Méthode avec authentification par cookie
1. Dans les outils réseau du navigateur, chercher l'onglet *cookie*, et lire le contenu. Faire une copie d'écran dans votre document réponse. Comment les informations du formulaire sont-elles écrites dans le cookie? Sous une forme structurée?

{{< img src="../images/moz2.png" caption="exemple de capture d'écran de l'outil d'exploration du cookie" >}}

2. Recharger la page: le navigateur propose t-il de soumettre à nouveau le contenu du formulaire? Les informations du formulaire sont-elles toujours présentes dans la carte d'identité?
3. Dans un autre onglet du navigateur: saisir l'adresse [http://resaonline.la-bo.xyz/getcookie](http://resaonline.la-bo.xyz/getcookie). Les informations du formulaire sont-elles toujours présentes dans la carte d'identité?
4. Saisir maintenant cette adresse dans un AUTRE navigateur. Les informations du formulaire sont-elles toujours présentes dans la carte d'identité?

5. Rechercher le cookie grace aux options du navigateur. (Voir tuto sur cette [page](https://support.mozilla.org/fr/kb/cookies-informations-sites-enregistrent). Quels autres cookies ont été déposés lors de votre session (aujourd'hui)? Comment peut-on se debarrasser de ces cookies?

{{< img src="../images/moz3.png" >}}

6. *Conclure:* Les traces numériques laissées sur mon ordinateur peuvent-elles contenir des informations sur mon identité numérique?

## Sécurité sur le Web
Video: transfert encryptage ssl

{{< img src="../images/video_ssl.png" link="https://www.youtube.com/watch?v=WIMKeyJ60Rw" caption="Code Rock & Apprendre" >}}


*Questions*

1. Quel est le scénario mettant en jeu un cyberpirate proposé dans cette vidéo?
2. Est-ce que cela change quelque chose, de naviguer en http ou bien en https?
3. parmi les éléments suivants, quels sont ceux qui sont cryptés lors d'une communication en *https*: (lire les discussions sur [https://www.ssl.com/faqs/what-is-https/](https://www.ssl.com/faqs/what-is-https/) ou bien [https://stackoverflow.com/questions](https://stackoverflow.com/questions/323200/is-a-https-query-string-secure))

	* Domain name
	* Request URL (which web page was requested by the client)
	* Website content
	* Query parameters
	* Headers
	* Cookies

4. Si votre échange avec le serveur est en *https*. Est-ce une bonne idée d'échanger des informations personnelles par la méthode GET si le site internet ne propose que la méthode GET? Pourquoi?
5. Conclure: Quels conseils peut-on donner à un utilisateur qui navigue et fait des achats sur le net?

# Liens
* Cette page est largement inspirée de [MDN developer.mozilla.org](https://developer.mozilla.org/fr/docs/Learn/Forms/Sending_and_retrieving_form_data)
* Approfondir: [MDN securité](https://developer.mozilla.org/fr/docs/Learn/Server-side/First_steps/Website_security)
* page sur les requetes http sur le blog du professeur [maximilienandile](https://maximilienandile.github.io/2016/09/30/Comprendre-les-headers-d-une-requete-HTTP/)
