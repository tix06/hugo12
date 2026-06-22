---
Title: Securité informatique
hidden: true
---

# Projet 1: hacker le mot de passe
Dans ce projet, vous allez programmer un script de Hack qui va tenter d'entrer par *force brute* dans une base de donnée protégée par mot de passe.

Imaginez que vous souhaitiez entrer par le formulaire suivant vers une page necessitant un mot de passe de longueur égale à 8 caractères (l'identifiant est supposé connu):

{{< img src="../images/form.png" >}}

Vous allez écrire un script python qui va envoyer automatiquement tous les mots de passes construits par combinaisons sur les 8 caractères possibles (ascii).

## Extensions possibles
* Le mot de passe à *cracker* peut être généré de manière aléatoire au lancement du programme, ou choisi par vous-même.

Vous pouvez mesurer le temps mis pour trouver le bon mot de passe. Et répéter cette opération pour plusieurs mots de passe, jusqu'à convergence du temps mis pour le retrouver par *force brute*. 

* Vous pouvez également vous intéresser à la programmation d'un veritable formulaire d'entrée dans un site, et utiliser une architecture utilisant le module Flask vu en [classe de 1ere](/docs/NSI/HTML/page6/).

L'attaque se fera à l'aide de fonctions du module `requests` (python).

* Solutions CSS pour design du formulaire:

	* Lien vers le script html/css/bootstrap du [formulaire](/scripts/bootstrap.zip)
	* autre solution utilisant le *direct css*: [TP de 1ereNSI](/docs/NSI/CSS/page3/)

## Variante du projet: hacker le serveur microbit
Approfondir le TP a la page [MB communication radio](/docs/techno/pages/MB_radio3/).

# Projet 3: RSA
cette page est en cours de redaction. Vous pouvez suivre:

* le TP à la page [suivante (niveau Term NSI)](https://glassus.github.io/terminale_nsi/T5_Architecture_materielle/5.4_Cryptographie/cours/) 
* ou bien à la page [suivante (niveau classe prepa)](https://www.fil.univ-lille.fr/~wegrzyno/portail/PAC/Doc/TP-RSA/index.html) en attendant qu'il soit adapté ici.
