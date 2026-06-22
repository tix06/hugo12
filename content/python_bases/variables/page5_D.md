+++
title= "introduction aux variables"
linkTitle = "pensée algorithmique"
description = "utiliser des variables pour mémoriser des état, pensée algorithmique"
weight = 1
+++

# Introduction: le rôle clé des variables 
Les exemples suivants montrent le rôle crucial des variables dans les algorithmes...

## Compteur de passages
Un dispositif numérique, équipé d'un capteur, compteur le nombre de passage par une porte. 


{{< img src="../images/detecteur.jpg" caption="detecteur de passage à capteur infra rouge" >}}

L'algorithme utilisé comporte 3 parties:

* initialisation de la variable
* boucle avec condition d'execution
* modification de la variable

Il utilise la fonction: `coupure_faisceau`

Et la variable: `i` nombre de passages detectés

```
i = 0
repeter indefiniment:
  {
  si coupure_faisceau_lumiere():
    {
    i = i + 1
    fin si
    }
  fin repeter
  }
```

## Point neutre Terre-Lune
Dans l’un de ses célèbres romans intitulé De la Terre à la Lune, Jules Verne (1828-1905) relate les aventures de trois héros ayant pris place à l’intérieur d’un énorme projectile qu’un gigantesque canon, baptisé Colombiad, propulse en direction de la Lune. Lors de ce périple, Jules Verne fait allusion à un point neutre, situé à une distance d = 350 000 km du centre de la Terre où les forces
gravitationnelles exercées par la Terre et la Lune sur le projectile se compensent.



{{< img src="../images/terre_lune.png" caption="point neutre sur la droite Terre-Lune" >}}

L'algorithme utilisé comporte 3 parties:

* phase d'initialisation de la variable
* boucle avec condition d'execution
* modification de la variable

Il utilise les fonctions: `F1` force de gravitation de la Terre, `F2` force de gravitation de la Lune

Et la variable: `d` distance à la surface de la Terre

```
d = 0
repeter tant que F1 (d) > F2(d):
  {
  d = d + 1
  fin repeter
  }
afficher d
```

