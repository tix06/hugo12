---
Title: repondeur telephonique
description: generer un dictionnaire de contacts et mesurer les performances de recherche
weight: 72
---

# TP – Carnet d'adresses (dictionnaires et performances)

## Fichiers fournis

- [script.py](/scripts/EP/repondeur/script.py) : le fichier à compléter. Chaque endroit à modifier est signalé par le commentaire `# A COMPLETER`.
- [donnees_contacts.py](/scripts/EP/repondeur/donnees_contacts.py) : listes de prénoms, noms, rues et villes utilisées pour générer des contacts aléatoires. **Vous n'avez pas besoin de le modifier.**

## Consignes de travail

- Telechargez et ouvrez [script.py](/scripts/EP/repondeur/script.py) dans Pyzo (ou votre éditeur habituel) en gardant [donnees_contacts.py](/scripts/EP/repondeur/donnees_contacts.py) dans le **même dossier**.
- Complétez le fichier **dans l'ordre**, section par section.
- Après chaque section, **exécutez le fichier entier** (F5 dans Pyzo, ou le bouton d'exécution). Des instructions `assert` vérifient automatiquement votre travail :
  - si rien ne s'affiche d'anormal et que vous voyez le message `Exercice N : OK`, c'est correct ;
  - si une erreur `AssertionError` apparaît, relisez l'exercice concerné et corrigez votre code.
- Ne modifiez pas les fonctions situées dans la partie *« FONCTIONS FOURNIES »* du script : elles remplacent le module `faker` (qui nécessite une connexion Internet et une installation, pas toujours possibles en salle).

---

## 1. Fabrication d'un contact

Chaque contact est un dictionnaire dont les clés seront :

| Clé | Signification |
|---|---|
| `nom` | Nom et prénom du contact |
| `tel` | N° de téléphone |
| `rue` | Adresse complète |
| `code` | Code postal |
| `ville` | Ville |
| `naissance` | Date de naissance |

### Exercice 1

Dans `script.py`, complétez le dictionnaire `contact` pour qu'il corresponde au contact suivant :

```
Margaret Costa-Royer
08 06 18 37 28
93, avenue Bruneau
13749 Perrot
```

### Exercice 2

Ajoutez une nouvelle entrée `"passwd"` dans le dictionnaire `contact`, ayant pour valeur `'s75JWikE&o'`.

---

## 2. Génération automatique d'un contact

Le fichier `script.py` fournit déjà quatre fonctions toutes prêtes, qui piochent des informations aléatoires dans `donnees_contacts.py` :

- `importer_contact()` renvoie un tuple `(nom, rue, ville, code_postal)` ;
- `genere_telephone()` renvoie un numéro de téléphone factice ;
- `genere_date_naissance()` renvoie une date de naissance factice ;
- `genere_mot_de_passe()` renvoie un mot de passe factice.

> **Remarque :** pour multiplier le nombre de noms de famille possibles, `importer_contact()` forme parfois un nom composé en accolant deux noms au hasard (comme *« Costa-Royer »* dans l'exercice 1). Cela permet de générer plusieurs dizaines de milliers de noms différents à partir d'une liste de prénoms et de noms de taille raisonnable.

### Exercice 3

Écrivez la fonction `genere_contact()` :
- elle ne prend aucun paramètre ;
- elle renvoie un dictionnaire possédant les mêmes clés que le contact de l'exercice 1, y compris `"passwd"` ;
- elle doit utiliser les quatre fonctions fournies ci-dessus pour construire ce dictionnaire.

---

## 3. Première implémentation du carnet d'adresses (liste)

Dans une première approche, le carnet d'adresses sera une **liste** de contacts, chaque contact étant un dictionnaire dont la structure a été définie précédemment.

### Exercice 4

Écrivez une fonction `genere_carnet1(n)` :
- prenant en paramètre le nombre `n` de contacts à générer ;
- renvoyant une liste de `n` contacts générés aléatoirement (utilisez `genere_contact()`) ;
- **tous les contacts du carnet doivent avoir des noms différents** (sinon la recherche par nom n'a plus de sens). Une solution simple : tant que le carnet ne contient pas encore `n` contacts, générer un nouveau contact et ne l'ajouter que si son nom n'est pas déjà présent dans le carnet.

### Exercice 5

Écrivez une fonction `est_present(nom, carnet)` :
- prenant 2 paramètres : un nom et un carnet d'adresses (liste) ;
- renvoyant `True` si le nom figure dans le carnet d'adresses, `False` sinon.

---

## 4. Mesure de performance de la recherche (liste)

Cette partie du script est **déjà écrite**, contentez-vous de l'exécuter et d'observer les temps affichés. Le module `timeit` mesure ici le temps nécessaire pour effectuer 1000 recherches, d'abord dans un carnet de 100 contacts, puis dans un carnet de 1000 contacts.

**Question 1 :** dans `script.py`, répondez par un commentaire à la question posée : comment le temps de recherche évolue-t-il quand la taille du carnet est multipliée par 10 ?

---

## 5. Seconde implémentation du carnet d'adresses (dictionnaire)

Le temps de recherche dans une liste est proportionnel à sa taille : si le carnet contient 10 fois plus de contacts, la recherche peut être jusqu'à 10 fois plus longue.

Nous allons changer d'approche et représenter le carnet d'adresses par un **dictionnaire** dont les clés sont les noms et les valeurs sont les fiches contacts (elles-mêmes des dictionnaires).

### Exercice 6

Écrivez une fonction `genere_carnet2(n)` :
- prenant en paramètre le nombre `n` de contacts à générer ;
- renvoyant un dictionnaire de `n` contacts générés aléatoirement.
- **veillez à ce qu'aucun nom ne soit généré deux fois** : si un même nom apparaissait deux fois, le second contact écraserait le premier dans le dictionnaire et vous obtiendriez un carnet de moins de `n` contacts.

---

## 6. Mesure de performance de la recherche (dictionnaire)

Cette partie du script est également déjà écrite. Elle mesure le temps de 1000 recherches, d'abord dans un carnet de 100 contacts, puis dans un carnet de 10 000 contacts (100 fois plus grand).

**Question 2 :** dans `script.py`, répondez par un commentaire : comparez l'évolution du temps de recherche dans le dictionnaire à celle observée dans la liste. Quelle structure de données est la mieux adaptée à la recherche sur les clés, et pourquoi ?

---

## Conclusion attendue

Le temps de recherche dans un dictionnaire est pratiquement indépendant du nombre d'entrées : en multipliant le nombre de contacts par 100, le temps reste quasiment identique, alors que pour une liste, ce temps est proportionnel au nombre d'éléments.

**Le dictionnaire est donc une structure de données optimisée pour la recherche sur les clés.**

---

## Licence

Ce document est adapté du TP *« Carnet d'adresses »* publié sur [levasseur.xyz](https://levasseur.xyz), sous licence [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.fr). Cette adaptation (sujet reformulé pour un fichier script à compléter, génération de contacts sans le module `faker`) est distribuée sous la même licence **CC BY-NC-SA 4.0** (Attribution – Pas d'utilisation commerciale – Partage dans les mêmes conditions).
