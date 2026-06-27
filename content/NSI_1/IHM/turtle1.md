---
Title: Editeur Turtle
description: Turtle
weight: 7
---
{{< img src="../images/editeurs.png" >}}Nous allons voir 3 options pour réaliser les scripts python turtle. La syntaxe diffère légèrement selon si vous utilisez la calculatrice TI83 CE Premium Python, la tablette Android, ou bien un interpreteur en ligne.

Les 3 programmes proposés permettent de réaliser cette première figure.

{{< img src="../images/hello_world_turtle.png" >}}
# TI83 CE Premium Python
* La calculatrice doit être à jour. Il faudra ajouter le module `CE_turtle` pour pouvoir utiliser le module *python turtle*. Voir [notice d'installation](/docs/techno/pages/TI_prisenmain/)
* Dans l'App Python: démarrer un nouveau script. Ecrire et rédiger la première ligne: `from turtle import *`. Quitter le shell et revenir dans l'editeur de programme pour poursuivre l'edition. Voir [Notice turtle pour la TI83](https://resources.t3france.fr/fileadmin/user_upload/Turtle_Getting_Started_Guide_CE_Python_FR.pdf)

Le script de démarrage sur la TI83:

```python
from turtle import *
t = Turtle()
t.clear()
for i in range(4):
    t.forward(100)
    t.left(90)
t.done()
```

*Astuces:*

* On appuie alors sur la touche **Annul** pour quitter la fenêtre graphique.
* On peut augmenter la vitesse de la tortue: `t.speed(0)` 

# Tablette Android Pydroid3
* Installer l'App Pydroid3 (version gratuite)
* Utiliser la [notice suivante](/pdf/python/listes1_TP_Pydroid.pdf) pour réaliser votre premier script et prendre connaissance de l'environnement

Le script de démarrage sur la tablette android est le suivant:

```python
from turtle import *
t = Turtle()
t.clear()
t.shape("turtle")
for i in range(4):
    t.forward(100)
    t.left(90)
exitonclick()
```

# Notebook en ligne: Basthon
* Aller sur la page{{< a link="https://basthon.fr/" caption="Basthon" >}}* Il vous faudra choisir: *Notebook* à la page d'accueil
   
{{< img src="/images/basthon1.png" >}}
Le script de démarrage sur la tablette android est le suivant:

```python
from turtle import *
reset()
for i in range(4):
    forward(100)
    left(90)
done()
```



