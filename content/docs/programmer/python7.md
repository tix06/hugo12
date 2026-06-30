---
Title: de scratch à python
description: programmer une fonction python avec des blocs scratch puis recopier le programme python généré
weight: 18
---

# TP1: de scratch à python
Aller sur l'interface de programmation python du site{{< a link="https://fr.vittascience.com/python/?mode=mixed&console=bottom" caption="Vittascience" >}}
## Partie 1: Premier programme
### BUT: 
créer un programme qui demande à l'utilisateur son nom, et lui affiche un message de bienvenue.
### VARIABLES:
le programme utilise les variables:

* `nom`, de type texte. Contient le nom renseigné par l'utilisateur
* `debut`, de type texte. Contient le mot: "Bonjour "
* `message`, de type texte, contient `debut` + `nom`

On rappelle qu'une variable, c'est un nom qui fait référence à une valeur stockée dans un espace de la mémoire. *Exemple:*

{{< img src="../images/memoire0.png" caption="Le nom de variable " >}}
### ECRIRE LE PROGRAMME:
Dans la fenêtre *SCRATCH*, on a un seul bloc de code:

{{< img src="../images/scratch0.png" >}}
* Dans la rubrique AFFICHAGE:
selectionner et glisser l'instruction: *demander un texte à l'utilisateur*.

{{< img src="../images/scratch1.png" >}}
Comme cette instruction n'est pas complète, elle ne peut pas constituer un bloc de code. Il faut ajouter une affectation.

* Dans la rubrique VARIABLE: cliquer sur *Créer une variable*. Nommer celle-ci *nom*

{{< img src="../images/scratch2.png" >}}
* Rubrique VARIABLES: selectionner et glisser: *Affecter à `nom` la valeur `" "`*. <br>Puis mettre l'instruction *demander un texte à l'utilisateur*, et coller les 2 blocs de code.

{{< img src="../images/scratch3.png" >}}
* Rubrique VARIABLES: Créer une nouvelle variable `debut`. Selectionner et glisser: *Affecter à `debut` la valeur `" "`*. <br>Ecrire `"Bonjour "`à la place de `" "`.

{{< img src="../images/scratch4.png" >}}
* Rubrique VARIABLES: créer une nouvelle variable `message`.

* Rubrique MATH: choisir le premier élément, celui qui permet une addition 

{{< img src="../images/scratch5.png" >}}
A l'aide des variables `debut` et `nom`, vous allez construire l'instruction complète: *Affecter à `message` la valeur `debut + nom`*

Vous trouverez les éléments `debut` et `nom` dans la rubrique VARIABLES:

{{< img src="../images/scratch9.png" >}}
Compléter alors l'instruction pour obtenir:

{{< img src="../images/scratch7.png" >}}
* Mettre à la suite les blocs de code pour former le programme:

{{< img src="../images/scratch8.png" >}}
* Mettez vous maintenant dans la peau de l'utilisateur: Executer le programme (bouton du haut `>`) Et repondre à la question dans le *shell*, sous la fenêtre d'edition.

> Sur **votre cahier**, recopier le script python correspondant. Et répondre aux questions:

1. Quelle instruction en python permet de demander à l'utilisateur d'entrer une valeur ou un texte?
2. Quelle instruction python permet d'afficher :
  * un texte? 
  * le contenu d'une variable?
3. Quelle instruction en python permet d'affecter le texte "bonjour" à la variable "debut"?



## Partie 2: programmer une fonction
### But: remplacer les entrées *demander à* et sortie *afficher* par des paramètres de fonction

### Ecrire le programme
* Supprimer le premier bloc du programme précédent (*Affecter à `nom` la valeur demander...*)
* Rubrique FONCTIONS: Choisir le 2e bloc, *Définir `nom_de_la_fonction`* avec l'option *retour*.
  * modifier le `nom_de_la_fonction`: mettre `salutation` comme nouveau nom
  * Bouton (+): ajouter le paramètre `nom`

{{< img src="../images/scratch10.png" >}}
Votre fonction est vide et ne contient pas encore d'instruction.

{{< img src="../images/scratch11.png" >}}
* Mettre le bloc du programme précédent dans la fonction:

{{< img src="../images/scratch12.png" >}}
* Supprimer la dernière ligne *afficher `message`*.
* Dans l'espace vide après *retour* : mettre la variable `message` pour que celle-ci s'affiche lorsque l'on appelle la fonction:

{{< img src="../images/scratch13.png" >}}
* Executer le programme (bouton du haut >)<br>En apparence, il ne se passe rien, mais vous avez quand même chargé la fonction en mémoire.
* Dans le shell (partie inférieure de la fenêtre), après les chevrons `>>>`, saisir l'instruction qui va appeler votre fonction: <br>

```python
>>> salutation("votre nom")
```

*Modifier `votre nom` par votre veritable nom...*

{{< img src="../images/scratch14.png" >}}

> Sur **votre cahier**, recopier le script python correspondant. Et répondre aux questions: Dans le script python: ...




1. Quelle partie du programme associe votre nom à la variable `nom`?
2. Quelle partie du programme affiche le contenu du message?
3. Comment sont mises les instructions du bloc de code dans la fonction?
3. Comment faut-il faire pour appeler la fonction et déclencher son execution?
4. Quel est l'avantage d'utiliser une fonction plutôt que le script de la partie 1?

## Utiliser la calculatrice TI-83 Premium CE edition Python
* *S'il vous reste du temps, recopiez ce programme dans l'environnement python de la calculatrice.* Executez le.

{{< img src="../images/ti_codes.png" >}}



