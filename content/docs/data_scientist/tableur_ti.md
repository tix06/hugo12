---
Title: tableur sur calcu TI83
---


# Utilisation de la base de données
## Ouvrir la base de données
Aller sur la page{{< a link="http://exoplanet.eu/GCM1D/" caption="Exoplanet.eu" >}}
Pour consulter la base de données de toutes les planetes observées, cliquer sur *Tous les catalogues*.

{{< img src="../images/catalogues.png" caption="accès à la base de données" >}}
Le tableau donne les caractéristiques connues pour ces planètes. Leur nombre est gigantesque. Vous allez utiliser les formules de filtre pour en selectionner quelques unes.

## Filtrer
Par exemple, si l'on cherche à étudier les seules planètes telluriques, on choisira celles dont le rayon est un peu supérieur ou un peu inférieur à celui de la Terre. 

D'après le{{< a link="https://media.afastronomie.fr/PetiteOurse/SIDERAL_PDF/outilPO%20-%20doc%20-%20tableau%20comparatif%20simplifié%20des%20planetes.pdf" caption="tableau comparatif des planètes du système solaire" >}}
$$mass:mjup = 0.00315$$

* 1/317 = 0.00315
* `mass` = masse Terre
* `mjup` = masse Jupiter
* `masse:mjup` = masse de la Terre rapporté à celle de Jupiter

On pourrait donc selectionner uniquement les planètes dont la masse (rapporté à celle de Jupiter) est comprise entre 0.001 et 0.004, soit:

$$mass{:}mjup > 0.001 ~AND ~mass{:}mjup < 0.004$$ 

> **A vous de jouer:** 

> 1. Dans la barre de formule, vous écrirez la relation qui permettra de filtrer les planètes, et conserver celles dont les masses sont comprises entre 0.001 et 0.004 fois celle de Jupiter.
> 2. Ajouter aussi un filtre sur le rayon: $$radius{:}rjup < 0.1$$

{{< img src="../images/filtre.png" caption="appliquer un filtre sur la base de données" >}}
## Loi de régréssion linéaire
### Entrer les données dans un tableau
On cherche maintenant une loi entre les grandeurs *mass* et *radius* pour ces planètes. Le modèle mathematique possible est le suivant:

$$\rho= \tfrac{mass{:}rjup}{(radius{:}rjup)^3}$$

Soit: la masse volumique relative à celle de Jupiter est égale à sa masse relative, divisée par son rayon relatif, à la puissance 3.

> Entrer les données dans un tableur:

> * Sur votre **calculatrice Ti-83**, commencer par effacer les listes: appuyer sur `2nde +` pour accéder au menu `mém`.
* Choisir `4:EffTtesListes`
* Appuyer sur le bouton `stats` puis `1:Modifier`.
* Entrer alors les données issues de la base de données: celle correspondant à *mass* dans `L1` et celles correspondant à *radius* dans `L2`
* Ajouter en dernière entrée la valeur 0 dans chacune des 2 colonnes (une planète de rayon 0 aura aussi une masse de 0...)
* Quitter alors le tableur: `2nde mode` ce qui correspond à `quitter`.
* Dans la fenêtre de calcul, saisir: `L2^3` puis touche **STO &rarr;** et `L3` pour obtenir: $$L2^3 \rightarrow L3$$

Si vous revenez sur la fenêtre d'edition du tableau, celui-ci devrait ressembler à ceci:

{{< img src="../images/Capture1.png" caption="fenêtre tableur de la Ti-83" >}}
### Afficher le nuage de points

> * Sur votre **calculatrice Ti-83**, choisir les listes de valeurs: faire `2nde f(x)`, ce qui correspond à `graph stat`. Choisir `1:Graph1...Aff` puis: 
	* `Aff`
	* Type: le nuage de points
	* XListe : `L3`
	* YListe : `L1` 

{{< img src="../images/Capture2.png" caption="selection des séries L1 et L3 pour X et Y" >}}
> * Réglage des axes: bouton `fenêtre`. Choisir:
	* Xmin=0
	* Xmax=0.001
	* Ymin=0
	* Ymax=0.005

{{< img src="../images/Capture3.png" caption="Réglage des axes" >}}
> * Appuyer alors sur le bouton `graphe` pour visualiser la distribution de points.

### Régréssion linéaire

> * Appuyer sur le bouton `stats`, puis menu `CALC`
* Choisir `4:RégLin(ax+b)`
	* Xliste: `L3`
	* Yliste: `L1` 
	* puis descendre et appuyer sur `calculer` en bas de la fenêtre

Recopier alors le coefficient obtenu pour `a`. Celui-ci représente la masse volumique relative d'une planète tellurique moyenne, rapportée à celle de Jupiter (1,3g.cm<sup>-3</sup>).

# Prolongement
On pourra faire ce même travail pour une série de planètes gazeuses. Il faudra cette fois choisir des planètes dont les masses et les rayons sont proches de ceux de Jupiter. Par exemple (vous pouvez tester d'autres combinaisons):

`mass:mjup> 0.7 and mass:mjup <1.5 AND radius:rjup>0.7` 

Choisir alors les 10 premières lignes du tableau (il devrait y en avoir plus d'une centaine...). Et faire le même travail que pour les planetes telluriques:

* effacer les listes
* remplir les listes `L1` et `L2` avec les valeurs de mass et de radius.
* Calculer les valeurs de la liste $L_3 = L_2^3$
* tracer la courbe `L1` en fonction de `L3`
* Obtenir les coefficients de la regression linéaire pour cette distribution de points.

# liens


* Les planètes telluriques et gazeuses diffèrent grandement par leur densité, comme on peut le voir sur le dossier suivant: [futura-sciences](https://www.futura-sciences.com/sciences/questions-reponses/astronomie-planete-tellurique-planete-gazeuse-differences-6462/)

* Exoplanète : première mesure de la densité d’une très jeune planète avec SPIRou: [article du CNRS.fr](https://www.cnrs.fr/fr/exoplanete-premiere-mesure-de-la-densite-dune-tres-jeune-planete-avec-spirou)
* Modeliser, simuler: [POST](/posts/sciences/modeliser/)



