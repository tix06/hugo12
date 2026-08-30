---
author: "Eric Tixidor"
date: 08-02-2021
linktitle: modeliser simuler
menu:
  main:
    parent: 
next: 
prev: 
title: Modèle prédictif
weight: 1
---


## Principe
Un modèle prédictif ne peut être établi qu'à partir d'une étude prealable de données. Une étude statistique permet de repérer si certains paramètres sont liés entre eux. Alors, si ces données étaient suffisamment nombreuses et précises, il est possible d'établir des lois mathematiques sur ces données. Une manière de représenter ce lien entre paramètres est d'établir une loi de regression linéaire, par exemple.

A partir de nouvelles données, on peut alors, grâce à une simulation, prédire le comportement futur  du nouvel objet. A condition que celui-ci fasse partie de la même famille d'objets que ceux qui ont permis d'établir le modèle.

## Un exemple de prédiction
Aller sur la page <a href="http://exoplanet.eu/GCM1D/" target = "blank">Exoplanet.eu</a>.

Cliquer sur le lien *online tool here* au milieu de la page de description.

La page suivante permet de simuler le comportement d'une planete dans son système stellaire. Il suffit de choisir certains paramètres comme par exemple:

* la distance de la planète à son étoile
* la courbure de sa trajectoire
* sa période de revolution
* le type d'étoile
* sa couverture oceanique
* ...

<figure>
<img src = "../images/params.png" alt="choix des paramètres de la planète">
<figcaption>Choix des paramètres de la planète</figcaption>
</figure>

La simulation demarre une fois que l'on clique sur le bouton **START**.

<figure>
<img src = "../images/modeles.png" alt="modeles predictifs">
<figcaption>Simulation du comportement de la planète</figcaption>
</figure>

Le logiciel utilise alors un modèle prédictif, établi à partir de l'observation de nombreuses autres planètes ou corps celestes, pour déterminer la temperature de surface de l'astre au cours du temps, sa trajectoire, etc...

> A tester vous même: faire un test à l'aide du simulateur.