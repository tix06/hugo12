---
Title: shifumi
weight: 31
---

# Jeu du Shifumi
Le pierre-feuille-ciseaux, chifoumi, pierre-papier-ciseaux ou encore roche-papier-ciseaux est un jeu dans lequel chaque joueur forme simultanément une parmi plusieurs armes symbolisées par la forme de la main et dont les rapports d'efficacité suivent un cycle : la pierre (aussi appelée « caillou » ou « roche ») battant les ciseaux, qui battent la feuille (ou « papier »), qui elle-même bat la pierre. Si les armes choisies sont les mêmes, il y a égalité. [wikipedia](https://fr.wikipedia.org/wiki/Pierre-feuille-ciseaux)

{{< img src="../images/regles_shifumi.jpg" width="400" link="https://www.jesuisanimateur.fr/petits-jeux/jeux-express/pierre-feuille-ciseaux" caption="cliquer pour consulter les règles du jeu" >}}

## Programmer un jeu à 2 joueurs
Pour programmer le choix de l'ordinateur: On utilisera la fonction `randint` du module `random`. Tester le script suivant pour comprendre son fonctionnement:

```python
from random import randint
for i in range(10):
    print(randint(0,2))
```

On utilisera le code numerique suivant:

{{< img src="../images/code_shifumi.png" width="400" caption="pierre = 0, ..." >}}

1. Stocker le choix de l'ordinateur dans la variable `j1`
2. Demander au joueur son choix (0: pierre, 1:feuille, 2: ciseaux). Transformer la valeur en un entier et la stocker dans `j2`
3. Evaluer le vainqueur, ou, préciser s'il s'agit d'un match nul, à l'aide d'une structure conditionnelle
4. Afficher un message (vainqueur, nul, defaite)
5. Ajouter un score sur N parties jouées.

**Astuce**

On pourra utiliser à bon escient la fonction *modulo* `%`, en remarquant:

`j2` gagne si la valeur de `j2` est egale à `j1+1`, et même plus précisemment `(j1+1)%2`. Vérifiez le à l'aide d'un schéma.

## Prolongement
*Joueur 1 et joueur 2 = ordinateur*

Dans le cadre d'un mini-projet, il serait intéressant de faire jouer l'ordinateur contre lui-même, et relever, sur plusieurs séries de N parties, le nombre de victoires du joueur 1. Utiliser une liste python. Et tracer un [histogramme](/python_bases/boucles/page2/#tracer-un-histogramme).


