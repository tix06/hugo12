---
Title: tp javascript 2 - hack
description: TP, transformer une page web, DOM
hidden: true
weight: 17
---

# TP(2) JS — Transformer une page web
**Première NSI — Manipulation du DOM**

## Objectifs

- Modifier dynamiquement le contenu et l'apparence d'une page HTML via la console JavaScript
- Comprendre que ces modifications sont **locales** et **temporaires**
- Prendre conscience du rôle du navigateur comme **interpréteur** côté client

---

## Matériel

- Un navigateur (Chrome ou Firefox)
- Le fichier {{< download link="/docs/NSI/javascript/page_cible.html" hint="page_cible.html" caption="page_cible.html" >}}, à ouvrir localement
- La console JavaScript : touche **F12** → onglet **Console**

---

## Rappels utiles sur la manipulation du DOM

```javascript
// Sélectionner un élément
document.getElementById('monId')
document.querySelector('#monId')
document.querySelector('.maClasse')
document.querySelectorAll('p')   // retourne une liste

// Lire / écrire du contenu
element.textContent        // texte brut
element.innerHTML          // HTML interprété
element.value              // valeur d'un champ input

// Modifier le style
element.style.color = 'red'
element.style.backgroundColor = '#000'
element.style.display = 'none'   // cache l'élément

// Modifier les attributs
element.setAttribute('src', 'nouvelle_image.jpg')

// Créer et insérer un élément
const el = document.createElement('p')
el.textContent = 'Nouveau paragraphe'
document.body.appendChild(el)

// Supprimer un élément
element.remove()
```

## Complément: boucle `for .. of` sur un objet itérable 

```javascript
const array1 = ["a", "b", "c"];

for (const element of array1) {
  console.log(element);
}

// affiche:
"a"
"b"
"c"
```


---

## Partie 1 — Prise en main (guidée)

Ouvre `page_cible.html` dans ton navigateur, puis ouvre la console (F12).

**Question 1.1**  
Lis le titre principal de la page :
```javascript
document.querySelector('h1').textContent
```
Que retourne cette instruction ?

**Question 1.2**  
Modifie ce titre pour afficher ton prénom :
```javascript
document.querySelector('h1').textContent = '...'
```

**Question 1.3**  
Change la couleur de fond de la page en bleu nuit :
```javascript
document.body.style.backgroundColor = '#0d1b2a'
```

**Question 1.4**  
Cache le paragraphe ayant l'id `#pub` :
```javascript
document.querySelector('#pub').style.display = 'none'
```

> 💡 **Observation :** Recharge la page (F5). Que se passe-t-il ? Pourquoi ?

---

## Partie 2 — Manipulation avancée (semi-guidée)

**Exercice 2.1 — Modifier tous les paragraphes**  
En utilisant `querySelectorAll`:

* récupère TOUS les paragraphes `p` dans un `array` appelé `paragraphes`
* passe le texte de tous les `<p>` en majuscules.

*Indication :* tu peux utiliser une boucle `for...of` et la méthode `.toUpperCase()`:

*Pour chaque element `p` de la liste `paragraphes`, transformer `p.textContent` en `p.textContent.toUpperCase()`*

---

**Exercice 2.2 — Ajouter un bandeau d'alerte**  
1. Crée un `<div>` en javascript:

```javascript
const bandeau = document.createElement('div')
```

2. Ajoute lui:

- du texte `"⚠️ Site en maintenance"`
- un fond rouge (`#c0392b`), texte blanc, centré

3. Insère le **en haut** de la page (avant tout autre élément)

*Indications :* 

* fait une recherche sur la méthode `prepend(), qui s'utilisera ici avec `document.body.prepend()`.
* Une méthode plus générale est d'utiliser `Node.appendChild()` qui ajoute un nœud à la fin de la liste des enfants d'un nœud parent spécifié.

---

**Exercice 2.3 — Réécrire le formulaire**  
Le formulaire de la page a l'id `#formulaire`:

```javascript
document.querySelector('#formulaire').innerHTML = '<!-- Ecrire ici les nouvelles balises -->'
```


Modifie son `innerHTML` pour y placer un nouveau formulaire avec :
- un champ texte "Pseudo"
- un champ email "Adresse mail"
- un bouton "Envoyer"

---

## Partie 3 — Défi ouvert 🚀

**Objectif :** transformer `page_cible.html` en une page qui ressemble à un site de ton choix (journal, réseau social fictif, site de jeu vidéo…).

Contraintes :
- Utiliser **au moins 6 instructions JS différentes**
- Modifier le titre, le contenu, les couleurs, et ajouter au moins **un nouvel élément**
- Prendre une **capture d'écran** de votre résultat

> 🔎 **Question de réflexion :** Le vrai site que tu as "imité" a-t-il été modifié ? Qui peut voir tes changements ?

---

## Partie 4 — Bilan et ouverture
> Recopier les questions et répondre à celles-ci dans une nouvelle page web `TP_compte_rendu.html`

Répondre aux questions suivantes dans le compte-rendu :

1. Tes modifications JavaScript ont-elles été envoyées au serveur du site ? Justifie.
2. Qui exécute le code JavaScript : le serveur ou le navigateur ?
3. Que faudrait-il faire pour que **tous les visiteurs** voient les modifications ?
4. Selon toi, à quelle couche du modèle client-serveur se situent ces échanges ?

---

*Ces questions seront le point de départ de la prochaine séquence sur le modèle client-serveur.*
